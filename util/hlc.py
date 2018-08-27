#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HLC (Highlights Link Convert) e un mic helper pentru a genera continutul pentru articolul Retrospectiva Saptamanii. Scriptul citeste o listă de linkuri
si genereaza echivalentul markdown, folosind fie numele site-ului, fie pe cel al articolului pentru textul linkului, in functie de sectiune, iar pentru
paginile magazinelor de jocuri incearca sa citeasca si pretul jocului (si il converteste in echivalentul euro, pentru consistenta).

-------------------
Exemple
-------------------
1. Pentru stirea:
"* World of Warcraft (jocul de bază și extensiile) va fi gratuit pentru abonati. https://www.gamesindustry.biz/articles/2018-07-18-blizzard-makes-wow-base-game-and-expansions-free-to-subscribers "

va fi generata linia:
"* World of Warcraft (jocul de bază și extensiile) va fi gratuit pentru abonati. ([GamesIndustry.biz](https://www.gamesindustry.biz/articles/2018-07-18-blizzard-makes-wow-base-game-and-expansions-free-to-subscribers))"

2. Pentru articolul:
"* https://www.pcgamer.com/game-remakes-shouldnt-be-afraid-to-change-the-classics/"

va fi generata linia:
"* [Game remakes shouldn’t be afraid to change the classics](https://www.pcgamer.com/game-remakes-shouldnt-be-afraid-to-change-the-classics/) (PC Gamer)

-------------------
Folosire
-------------------
In mod implicit, scriptul cauta linkuri intr-un fisier 'input_links.txt'. Alternativ, i se poate da un alt fisier ca argument:

python hlc.py [cale-fisier-linkuri.txt]

-------------------
Extra info
-------------------
Testat cu Python 3, dar ar trebui sa mearga si in Python 2 (eventual cu unele mici modificari)

Scriptul trateaza sectiunile in mod diferit, astfel incat rezultatul difera:
- la stiri va fi lasat textul stirii normal ca string simplu, iar la sfarsit numele site-ului cu link catre stirea originala
- la articole titlul articolului va fi linkul, iar la sfarsitul liniei va fi trecut numele site-ului in paranteza, ca string simplu
- articolele Made in Ro vor fi tratate precum stirile
- articolele despre lansari/anunturi sunt tratate precum stirile
- la articolele cu linkuri catre magazine de jocuri, linkurile vor fi inlocuite inline cu link markdown catre pagina respectiva,
  iar pentru jocuri va fi trecut si pretul in euro in paranteza

-------------------
TODO
-------------------
Features:
- (DONE) tratament diferentiat pentru fiecare sectiune (stirile au link pe numele site-ului, la sfarsit)
- (DONE) dictionar site-uri pentru numele site-urilor
- (DONE) linkuri multiple in aceeasi linie
- (DONE) de adaugat detectie pret jocuri din store pages pentru sectiunea pentru Oferte jocuri
- de tratat raspuns not OK la requests cand citim un url
- de mutat ca web script in candaparerevista.ro/utils/ si apelat printr-un formular html
  sau de adaugat args parser daca il folosim local
- de handluit terminatiile de linie / rstrip
- de ignorat url-urile deja formatate pentru markdown (ex:  [text](http://url.com))
- de testat si fixat ce ar mai trebui pentru a merge integral si in Python 2
- (PARTIAL) de adaugat un indicator de progres pentru linii procesate + scriere; Update: de adaugat space padding la linia de progress si un nume pentru sectiune
- de mutat majoritatea metodelor de tipul "parseaza_nume" in Sectiuni, unde le e locul

Bugs/issues:
- la unele site-uri sunt probleme cu identficarea numelui pe Open Graph (ex: pcgamer) - detecteaza
  prea mult / nu detecteaza sfarsitul (edit: s-ar putea sa fi rezolvat, mai trebuie teste)
- nu detecteaza categoria Stiri cand e scrisa cu diacritice (dar la Romania merge ok)

Alte observatii:
- cautarea de text in paginile html nu e foarte robusta si o sa mai dea rateuri - se face cu cautari pe string cu regex;
  ideal ar trebui folosita o librarie html care sa parseze DOM-ul (vezi BeautifulSoup), dar pentru scopurile noastre nu se justifica deocamdata
- unele magazine de jocuri folosesc JS in proportie mai mare sau mai mica pentru generarea paginilor, asa incat unele
  informatii nu vor fi disponibile in raspunsul html (ex: pretul la jocurile Humble, sau orice de pe Fanatical)
"""

import sys
import requests
import re
import codecs
import time

### --------- CLASE SI CONSTANTE --------- ###

is_debug = False

INPUT_FILE_DEFAULT = "input_links.txt" if not is_debug else "test_input_links.txt"
OUTPUT_FILE = "rezultat_final_markdown.txt" if not is_debug else "test_rezultat_final_markdown.txt"

DEFAULT_UNKNOWN_TEXT = "<span style='background-color:red'>PROBLEM</span>"

SITEURI_CUNOSCUTE = {
    'idlethumbs': 'Idle Thumbs',    'pcgamer': 'PC Gamer',          'rockpapershotgun': 'RPS',
    'gamasutra': 'Gamasutra',       'unwinnable': 'Unwinnable',     'eurogamer': 'Eurogamer',
    'wired': 'Wired',               'kotaku': 'Kotaku',             'destructoid': 'Destructoid',
    'vg247': 'VG247',               'waypoint.vice': 'Waypoint',    'gameinformer': 'Games Informer',
    'arstechnica': 'Ars Technica',  'gamereactor': 'Gamereactor',   'gamesindustry': 'GamesIndustry.biz',
    'vgchartz': 'VGChartz',         'theverge': 'The Verge',        'pcgamesn': 'PCGamesN',
    'techpowerup': 'TechPowerUp',   'variety': 'Variety',           'massivelyop': 'Massively OP',
    'rpgcodex': 'RPG Codex',        'videogamer': 'VideoGamer',     'steamcommunity': 'Steam Community',
    'gog.com': 'gog.com',           'steampowered.com': 'Steam',    'humblebundle.com/store': 'Humble Store',
    'gamesradar': 'GamesRadar+',    'venturebeat': 'VentureBeat',   'humblebundle': 'Humble Bundle',
    'avclub': 'A.V. Club',          'tedium': 'Tedium',             'hardcoregamer': 'Hardcore Gamer',
    'polygon': 'Polygon',           'guardian': 'The Guardian',     'engadget': 'Engadget',
    'shacknews': 'Shacknews',       'dotesports': 'Dot Esports',    'pcgamesinsider': 'PCGamesInsider.biz'
    'techraptor': 'TechRaptor',     'phoronix': 'Phoronix',         'wccftech': 'Wccf tech',
    'bloomberg': 'Bloomberg',       'medium.com':'Medium',          'filfre.net': 'The Digital Antiquarian',
    'usgamer': 'USgamer',           'gematsu': 'Gematsu',
}

MAGAZINE = {
    "steam"     : "store.steampowered.com",
    "gog"       : "gog.com",
    "humble"    : "humblebundle.com", # aici pretul e generat cu js, nu poate fi citit din html
    "fanatical" : "fanatical.com",  # fanatical au tot site-ul generat cu js, nu putem citi mai nimic
    "gmg"       : "greenmangaming",
    "origin"    : "origin.com"
}

EXCH_GBP_EUR = 1.1

class RawLine(object):
    """
    Reprezinta o linie simpla, neprelucrata, ce contine doar textul brut
    """

    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def __str__(self):
        return ("type(%s), values(%s)" % (type(self), self.text.rstrip() if (self.text) else "<empty>"))


class Sectiune(RawLine):
    """
    O linie despre care stim ca contine numele unei sectiuni un header de nivel 2 ("## ')
    """

    def __init__(self, text):
        RawLine.__init__(self, text)
        # lista liniilor care apartin acestei sectiuni
        self.linii = []

    def is_different_type_than(self, other_section):
        return type(self) != type(other_section)

    def adauga_linie(self, linie_noua):
        self.linii.append(linie_noua)

    def get_linii_formatate_pentru_output(self):
        """
        Alcatuieste o lista noua cu textul fiecarei linii formatat pentru output markdown
        """
        return (linie.get_text() for linie in self.linii)

    def make_markdown_link(self, link):
        pass

    def __str__(self):
        return ("type(%s) \n\tvalues(%d elements: %s)" % (type(self), len(self.linii), self.linii))


class SectiuneStire(Sectiune):

    def get_linii_formatate_pentru_output(self):
        """
        Citeste fiecare linie din lista si formateaza linkurile in format markdown, daca exista
        Exemplu: ' * Corp stire. ( [nume site](link articol) ) '
        """
        lista_formatata = []

        for linie in self.linii:
            if (linie.are_linkuri()):
                url_incepe     = linie.get_links()[0].start
                lista_sites = ", ".join([self.make_markdown_link(link) for link in linie.get_links()])
                text_rescris = linie.text[:url_incepe] + "(" + lista_sites + ")"
                lista_formatata.append(text_rescris)
            else:
                lista_formatata.append(linie.get_text().rstrip())
        return lista_formatata

    def make_markdown_link(self, link):
        return "[%s](%s)" % (link.nume_site, link.url)


class SectiuneArticole(Sectiune):

    def adauga_linie(self, linie_noua):
        self.linii.append(linie_noua)

    def get_linii_formatate_pentru_output(self):
        """
        Citeste fiecare linie din lista si formateaza linkurile in format markdown, daca exista
        Exemplu: '* [nume articol](link articol). (nume site)'
        """
        lista_formatata = []

        for linie in self.linii:
            if (linie.are_linkuri()):
                url_incepe     = linie.get_links()[0].start
                lista_articole = ", ".join([self.make_markdown_link(link) for link in linie.get_links()])
                text_rescris = linie.text[:url_incepe] + lista_articole
                lista_formatata.append(text_rescris)
            else:
                lista_formatata.append(linie.get_text().rstrip())
        return lista_formatata

    def make_markdown_link(self, link):
        return "[%s](%s) (%s) " % (link.text, link.url, link.nume_site)


class SectiuneRomania(Sectiune):
    # nu avem nevoie deocamdata de clasa asta, folosim tot SectiuneStire
    pass


class SectiuneAnunturiLansari(Sectiune):
    pass


class SectiuneOferte(Sectiune):

    def adauga_linie(self, linie_noua):
        self.linii.append(linie_noua)

    def get_linii_formatate_pentru_output(self):
        """
        Citeste fiecare linie din lista si formateaza linkurile in format markdown, daca exista
        Exemplu: '* [nume joc](link store page) (pret)'
        """
        lista_formatata = []

        for linie in self.linii:
            if (linie.are_linkuri()):
                text_rescris = linie.get_text()
                for link in linie.get_links():
                    text_rescris = text_rescris.replace(link.url, self.make_markdown_link(link))
                lista_formatata.append(text_rescris)
            else:
                lista_formatata.append(linie.get_text().rstrip())
        return lista_formatata

    def make_markdown_link(self, link):
        # pentru pagina promotiei, afisam doar numele promotiei
        if link.is_promo_page:
            return "[%s](%s)" % (link.text, link.url)
        # altfel afisam numele jocului cu pretul
        else:
            return "[%s](%s) (%s) " % (self.curata_caractere_nume_joc(link.text), link.url, link.pret_joc)


    # TODO poate de inlocuit cu reduce() sau ceva echivalent
    def curata_caractere_nume_joc(self, text):
        bad_strings = ["®", "™"]
        tmp_text = text
        for bad in bad_strings:
            tmp_text = tmp_text.replace(bad, "")

        return tmp_text


class SectiuneRecomandare(Sectiune):
    pass


class LinieNormala(RawLine):
    """
    O line prelucrata, care apartine unei sectiuni, si care poate contine unul sau mai multe linkuri.
    """

    def __init__(self, text):
        RawLine.__init__(self, text)
        self.lista_linkuri = []

    def are_linkuri(self):
        return len(self.lista_linkuri) > 0

    def get_links(self):
        return self.lista_linkuri


class LinkInLinie(object):
    """
    Reprezinta un link care se poate gasi intr-o linie. Pe langa URL,
    acest link are si valori pentru pozitia de start si de sfarsit in
    linia respectiva, precum si numele site-ului si (in functie de sectiune)
    si al articolului.
    Cand se exporta o linie, aceste valori sunt folosite pentru a genera
    linkul in format markdown, ex:  "[text](http://url.com)"
    """

    USE_SITE_NAME, USE_TEXT, USE_GAME_NAME_PRICE = range(3) # un fel de enum

    def __init__(self, url, start, end):
        self.url = url
        self.start = start
        self.end = end
        self.text = DEFAULT_UNKNOWN_TEXT
        self.nume_site = DEFAULT_UNKNOWN_TEXT

        # astea sunt folosite doar pentru linkurile de la store pages,
        # poate ar trebui mutate intr-o subclasa (TODO)
        self.is_promo_page = False
        self.pret_joc = DEFAULT_UNKNOWN_TEXT

    def __str__(self):
        return "Link: url(%s) (%d - %d), text(%s), site(%s), is_promo(%s), pret(%s)" % \
               (self.url, self.start, self.end, self.text, self.nume_site, self.is_promo_page, self.pret_joc)


### --------- SCRIPTUL INCEPE AICI --------- ###

def execute(linii_fisier):
    """
    Metoda principala de lucru: primeste liniile din fisier, pe care
    le itereaza si prelucreaza pe rand, salvand rezultatul intr-o lista.
    La sfarsit, scrie liniile procesate din lista intr-un fisier txt
    ce poate fi copiat direct in fisierul markdown.
    """

    # lista cu sectiunile si liniile procesate, ce vor fi salvate in
    # fisierul de output pentru a fi apoi copiate in articolul din Hugo
    document_parsat = []

    sectiune_curenta = None

    # iteram si tratam fiecare linie in parte, apoi le adaugam in lista de mai sus
    for index, linie_curenta in enumerate(linii_fisier):
        # try:
            rezultat_parsare = parseaza_linie(linie_curenta, sectiune_curenta, index)

            # track progress
            nume_sectiune = type(sectiune_curenta).__name__[len("Sectiune"):]
            print("%d/%d (%s)" % (index + 1, len(linii_fisier), nume_sectiune), end='\r')

            # daca am parsat o sectiune, verificam daca e diferita de sectiunea curenta, caz in care
            # o setam pe aceasta ca noua sectiune curenta si o adaugam la lista
            if isinstance(rezultat_parsare, Sectiune):
                if (rezultat_parsare.is_different_type_than(sectiune_curenta)):
                    sectiune_curenta = rezultat_parsare
                    document_parsat.append(rezultat_parsare)

            # am primit inapoi o linie ce nu tine de nicio sectiune
            else:
                document_parsat.append(rezultat_parsare)

        # except Exception as e:
        #     print("EROARE parsare la linia %d: %s" % (index, e))

    # scrie rezultat in fisier
    print()
    print("Scrie fisier...")
    if is_debug:
        # afiseaza_fisier(document_parsat)
        scrie_fisier(document_parsat)
    else:
        scrie_fisier(document_parsat)


def parseaza_linie(linie_bruta, sectiune_curenta, index = -1):

    # verifica daca avem Sectiune (heading 2)
    if linie_bruta[0:3] == "## ":
        sect = get_sectiune(linie_bruta)
        return sect

    # altfel inseamna ca avem o Linie

    # daca linia nu apartine unei sectiuni (sectiune_curenta == None),
    # nu ne intereseaza si o returnam ca atare, neprelucrata
    if not (sectiune_curenta):
        return RawLine(linie_bruta)

    linie_parsata = LinieNormala(linie_bruta)

    # gaseste_url_in(linie_parsata)
    completeaza_urls(linie_parsata.get_text(), linie_parsata.get_links())

    # completam nume site si text linkuri
    for link in linie_parsata.lista_linkuri:
        url = link.url

        if is_debug:
            print("--------------------")
            print("sending request to url %s" % url)

        try:
            http_result = requests.get(url)
            http_result.encoding = 'utf-8'
        except Exception as e:
            print("Eroare la url(%s): %s" % (url, e))
            continue

        # TODO de tratat raspuns not OK la requests
        if not is_status_ok(http_result):
            print("url %s | status %s" % (url, http_result.status_code))

        # completeaza nume site
        link.nume_site = parseaza_nume_site(url, http_result.text)

        # completeaza text link
        # TODO de tratat properly aici
        if isinstance(sectiune_curenta, SectiuneArticole):
            titlu_articol = parseaza_titlu_articol(url, http_result.text)
            link.text = titlu_articol

        elif isinstance(sectiune_curenta, SectiuneOferte):
            link.is_promo_page = check_if_promo_page(url)

            if (link.is_promo_page):
                link.text = parseaza_nume_promo(url, http_result.text)
            else:
                link.text = parseaza_nume_joc(url, http_result.text)
                link.pret_joc = parseaza_pret_joc(url, http_result.text)

        if is_debug:
            print("link parsat = %s" % link)

    # adaugam linia parsata in lista de linii a sectiunii curente
    sectiune_curenta.adauga_linie(linie_parsata)

    if is_debug:
        print("index %d, adaugat in SECT %s LINIA %s" % (index, type(sectiune_curenta.get_text()), linie_parsata.get_text().rstrip()))

    return sectiune_curenta


def gaseste_terminator_char_pos(text, start_pos):
    url_terminator_chars = [",", ";", " ", "|", "\n"]

    # cauta toate caracterele de sfarsit in linia de text si returneaza pozitia
    # pentru fiecare caracter care nu a fost gasit se returneaza -1, asa ca dupa aceea le filtram
    terminator_chars_in_text = [text[start_pos:].find(char) for char in url_terminator_chars]
    filtered_pos = list(filter(lambda n: n >= 0, terminator_chars_in_text))

    # daca am gasit mai mult de un terminator char in linie, cel cu pozitia cea mai mica va fi ales
    if len(filtered_pos) > 0:
        return start_pos + min(filtered_pos)
    # daca nu am gasit un terminator, end va fi sfarsitul liniei
    else:
        return len(text)


def completeaza_urls(text, lista_linkuri):
    """
    Citeste o linie bruta si cauta recursiv toate linkurile. De fiecare data cand
    gaseste unul, va adauga in lista un obiect Link, folosind url-ul, pozitia de start
    si pozitia de sfarsit, apoi cauta urmatorul link in restul textului
    """
    if not (len(text) > 9): # adica len("http://a.a")
        return

    # gaseste inceput url
    start = text.find("http")

    if (start > -1):
        # gaseste sfarsit URL
        end = gaseste_terminator_char_pos(text, start)

        url = text[start:end]

        lista_linkuri.append(LinkInLinie(url=url, start=start, end=end))

        # cauta recursiv in restul textului
        return completeaza_urls(text[end:], lista_linkuri)

    return


def get_sectiune(linie):
    titlu_sectiune = linie[3:].lower()

    def titlu_contine(*args):
        for arg in args:
            if arg in titlu_sectiune:
                return True
        return False

    if (titlu_contine('stiri', 'știri')):
        return SectiuneStire(linie)
    elif (titlu_contine('articole')):
        return SectiuneArticole(linie)
    elif (titlu_contine('romania', 'românia')):
        # return SectiuneRomania(linie)
        # formatul e acelasi deocamdata, nu e nevoie sa folosim o clasa diferita
        return SectiuneStire(linie)
    elif (titlu_contine('anunturi', 'anunţuri')):
        # return SectiuneAnunturiLansari(linie)
        # formatul e acelasi deocamdata, nu e nevoie sa folosim o clasa diferita
        return SectiuneStire(linie)
    elif (titlu_contine('oferte')):
        return SectiuneOferte(linie)
    elif (titlu_contine('recomandare')):
        return SectiuneRecomandare(linie)

    # n-ar trebui sa ajungem aici
    else:
        return Sectiune(linie)


def parseaza_titlu_articol(url, text):
    titluri = get_regex_og_title().findall(text)

    if not (len(titluri) > 0):
        # daca nu am gasit titlu Open Graph, cautam titlul normal
        titluri = get_regex_html_title().findall(text)

        if not (len(titluri) > 0):
            titluri = [DEFAULT_UNKNOWN_TEXT]

    try:
        titlu = titluri[0]
        return titlu
    except:
        print("EROARE cautare titlu in url %s, TITLURI = %s\n" % (url, titluri))


def parseaza_nume_site(url, text):

    # cauta nume site in site-urile cunoscute
    nume_site_cunoscut = check_string_for_dict_key(url, SITEURI_CUNOSCUTE.items())
    if (nume_site_cunoscut):
        return nume_site_cunoscut

    # altfel incercam sa cautam numele in tag-ul Open Graph
    else:
        pattern_og = re.compile("\"og:site_name\" content=\" *(.*?)\" *\/>",re.DOTALL|re.M)
        titluri = pattern_og.findall(text[0:2000])

        if (len(titluri)>0):
            titlu = titluri[0]
            return titlu
        else:
            return DEFAULT_UNKNOWN_TEXT


def check_if_promo_page(url):
    if MAGAZINE['steam'] in url:
        # return "sale" in url
        return "/app/" not in url

    elif MAGAZINE['gog'] in url:
        return "/promo/" in url

    elif MAGAZINE['humble'] in url:
        return "/store/promo/" in url

    elif MAGAZINE['gmg'] in url:
        return "/games/" not in url

    else:
        return False


def parseaza_nume_promo(url, text):

    def get_search_pattern():
        if MAGAZINE['steam'] in url:
            if "/search/" in url:
                # paginile bazate pe search nu au titlul in <title>
                return get_regex_css_class("pageheader")
            else:
                return get_regex_html_title()

        elif MAGAZINE['gog'] in url:
            return get_regex_css_class("header__title")

        elif MAGAZINE['humble'] in url:
            return get_regex_og_title()

        elif MAGAZINE['gmg'] in url:
            return get_regex_html_title()

        else:
            return None

    def curata_nume_if_necessary(nume):
        if MAGAZINE['humble'] in url:
            bad_suffix = "| Humble Store"
            if nume.endswith(bad_suffix):
                nume = nume[:-len(bad_suffix)]
        return nume.strip()

    nume_promo = search_regex(text, get_search_pattern())

    return curata_nume_if_necessary(nume_promo)


def parseaza_nume_joc(url, text):

    def get_search_pattern():
        if MAGAZINE['steam'] in url:
            return get_regex_css_class("apphub_AppName")
        elif MAGAZINE['gog'] in url:
            return get_regex_css_class("header__title")
        elif MAGAZINE['humble'] in url:
            return get_regex_og_title()
        elif MAGAZINE['gmg'] in url:
            return get_regex_html_title()
        else:
            return None

    def curata_nume_if_necessary(nume):
        if MAGAZINE['humble'] in url:
            bad_prefix = "Buy "
            bad_suffix = " from the Humble Store"
            if nume.startswith(bad_prefix):
                nume = nume[4:]
            if nume.endswith(bad_suffix):
                nume = nume[:-len(bad_suffix)]

        elif MAGAZINE['gmg'] in url:
            bad_suffix = "| PC - Steam | Game Keys"
            if nume.endswith(bad_suffix):
                nume = nume[:-len(bad_suffix)]

        return nume.strip()

    nume_joc = search_regex(text, get_search_pattern())
    return curata_nume_if_necessary(nume_joc)


def parseaza_pret_joc(url, text):

    def get_start_pos():
        start_pos = 0
        # in functie de site, s-ar putea sa fie nevoie sa incepem cautarea de la alta pozitie, nu de la inceput

        if MAGAZINE['steam'] in url:
            start_pos = text.find("game_area_purchase_game_wrapper")

        elif MAGAZINE['gog'] in url:
            # la gog avem clasa "_price" si la pretul vechi si la pretul nou,
            # de aceea trebuie sa vedem intai de unde incepe pretul nou
            first_start = text.find("module module--buy")
            if (first_start >= 0):
                start_pos = first_start + text[first_start:].find("buy-price__new")

        elif MAGAZINE['gmg'] in url:
            start_pos = text.find('<p class="current-price">')

        return start_pos if start_pos >= 0 else 0

    def get_search_pattern():
        if MAGAZINE['steam'] in url:
            return get_regex_css_class("discount_final_price")
        elif MAGAZINE['gog'] in url:
            return get_regex_css_class("_price")
        elif MAGAZINE['humble'] in url:
            # pretul e generat pe loc cu js, nu exista in html
            pass
        elif MAGAZINE['gmg'] in url:
            return re.compile("amount=\"product.price\">(.*?) ?<",re.DOTALL|re.M)
        else:
            return None

    def curata_pret_if_necessary(pret):
        if MAGAZINE['gog'] in url:
            return (pret + "€").replace(".", ",")
        elif MAGAZINE['gmg'] in url:
            pret_cifre = pret.replace("&#163;", "").strip()
            try:
                pret_eur = float(pret_cifre) * EXCH_GBP_EUR
                return "aprox. " + ("%.2f€" % pret_eur).replace(".", ",")
            except:
                return pret_cifre
        return pret.strip()

    pret = search_regex(text[get_start_pos():], get_search_pattern())

    return curata_pret_if_necessary(pret)


### --------- HELPERS --------- ###

def search_regex(text, search_pattern):
    if search_pattern:
        search_result = search_pattern.findall(text)
        if search_result and len(search_result)>0:
            return search_result[0].strip()

    return DEFAULT_UNKNOWN_TEXT


def check_string_for_dict_key(haystack_string, needles_dict):
    for needle_key, needle_value in needles_dict:
        if needle_key not in haystack_string:
            continue
        else:
            return needle_value

    return 0


def get_regex_og_title():
    # pattern preluat si adaptat de aici: https://ubuntuforums.org/showthread.php?t=1215158
    return re.compile("\"og:title\" content=\" ?(.*?)\" ?\/?>",re.DOTALL|re.M)


def get_regex_html_title():
    return re.compile("<title>(.*?)<\/title>",re.DOTALL|re.M)


def get_regex_css_class(css_class_name):
    pattern_string = "\"%s.*?\">(.*?)<\/" % css_class_name
    return re.compile(pattern_string,re.DOTALL|re.M)


def is_status_ok(response):
    return response.status_code == requests.codes.ok


def citeste_fisier(fisier_linkuri):
    # lista_linkuri = open(fisier_linkuri, "r")
    lista_linkuri = codecs.open(fisier_linkuri, 'r', "utf-8")
    return lista_linkuri.readlines()


def afiseaza_fisier(document_parsat):
    """
    E doar pentru debug, dar poate fi adaptat sa afiseze continutul direct
    pentru copy-paste in Hugo, sa nu mai salvam separat intr-un fisier
    """
    for index, sect in enumerate(document_parsat):
        # afisam sectiunea, respectiv eventuala linie care nu apartine unei sectiuni
        print("%d | %s" % (index, sect.get_text()))

        # o sectiune cuprinde o lista de linii, le afisam acum
        if isinstance(sect, Sectiune):
            for linie in sect.get_linii_formatate_pentru_output():
                try:
                    print("%d | %s" % (index, linie.rstrip())) #TODO scoate newline la sursa, nu aici
                except Exception as e:
                    print("EROARE la linia %s: %s" % (linie, e))


def scrie_fisier(document_parsat):
    links_file = codecs.open(OUTPUT_FILE, 'w', "utf-8")
    for sect in document_parsat:
        # scriem sectiunea, respectiv eventuala linie care nu apartine unei sectiuni
        links_file.write("%s\n" % sect.get_text())

        # o sectiune cuprinde o lista de linii, le scriem acum
        if isinstance(sect, Sectiune):
            for linie in sect.get_linii_formatate_pentru_output():
                try:
                    links_file.write("%s\n" % linie.rstrip()) #TODO scoate newline la sursa, nu aici
                except Exception as e:
                    print("EROARE la linia %s: %s" % (linie, e))

    links_file.close()


### --------- MAIN --------- ###

if __name__ == "__main__":
    # try:
        args = sys.argv[1:]
        if (len(args) == 1):
            linii_fisier = citeste_fisier(args[0])

        else:
            linii_fisier = citeste_fisier(INPUT_FILE_DEFAULT)

        start_time = time.time()
        execute(linii_fisier)
        end_time = time.time()
        print("TERMINAT de scris in %d sec." % round(end_time - start_time, 2))
    # except IOError as ioerr:
    #     print("Eroare IO: fisierul cu linkuri nu exista (err: %s" % ioerr)

    # except Exception as e:
    #    print("Ceva n-a mers bine: %s." % e)
    #    exit(1)