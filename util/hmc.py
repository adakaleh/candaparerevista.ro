#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HMC (Highlights Magazine Convert) e un mic helper pentru a genera continutul pentru articolul Revistele Lunii. Scriptul citeste un csv cu datele necesare:
(header: nume_revista, tara_revista, site_revista, link_revista_curenta, img_coperta_full, luna_curenta, editie_curenta, thumbnail)
si genereaza echivalentul markdown.

-------------------
Folosire
-------------------
# TODO

-------------------
# TODO
-------------------

# TODO de adaugat
# generare linkuri rapide / cuprins
# afisare site oficial doar daca linkul editiei e catre alt site sau nu exista
## mentiune editii normale+abonati

# TODO corecturi manuale
## fix level cehia + level turcia
## mentiune wireframe link download
## fix site edge
"""

import sys
import codecs
import csv
import time

### --------- CLASE SI CONSTANTE --------- ###

# is_debug = True

INPUT_FILE_DEFAULT = "input_reviste_csv.txt" # if not is_debug else "test_input_links.txt"
OUTPUT_FILE = "rezultat_reviste_markdown.txt" # if not is_debug else "test_rezultat_final_markdown.txt"
EMPTY = "n/a"

class Revista(object):
    '''
    Transforma fiecare rand din fisierul csv, care e un dict de forma (header->value),
    intr-un obiect care are drept atribute cheile din dict (headerele din csv)

    '''
    def __init__(self, dict_obj):
        self.nume = dict_obj.get('nume_revista', EMPTY)
        self.tara = dict_obj.get('tara_revista', EMPTY)
        self.site_revista = dict_obj.get('site_revista', EMPTY)
        self.link_revista_curenta = dict_obj.get('link_revista_curenta', EMPTY)
        self.img_link_full = dict_obj.get('img_coperta_full', EMPTY)
        self.luna_curenta = dict_obj.get('luna_curenta', EMPTY)
        self.editie_curenta = dict_obj.get('editie_curenta', EMPTY)
        self.img_thumbnail = dict_obj.get('thumbnail', EMPTY)

        # Metoda generica, cu headere necunoscute dinainte
        # (thx https: // github.com / alon710 / DictToObj / blob / master / dict_to_obj / __init__.py)
        # for k, v in dict_obj.items():
        #     if isinstance(v, (list, tuple)):
        #         setattr(self, k, [DictToObj(x) if isinstance(x, dict) else x for x in v])
        #     else:
        #         setattr(self, k, DictToObj(v) if isinstance(v, dict) else v)

    def __str__(self):
        return "{nume}, luna: {luna}, editie: {editie}".format(
            nume=self.nume,
            luna=self.luna_curenta,
            editie=self.editie_curenta
        )

    def get_nume_tara(self):
        return "%s (%s)" % (self.nume, self.tara)

    def are_editie(self):
        return self.luna_curenta != EMPTY or self.editie_curenta != EMPTY

    def get_title_markdown(self):
        # Textul linkului va fi ori luna, ori numarul editiei
        if self.luna_curenta != EMPTY:
            # Daca avem luna si numarul editiei, numarul va fi trecut la sfarsit in paranteza
            editie = " (#%s)" % self.editie_curenta if self.editie_curenta != EMPTY else ""
            if self.link_revista_curenta != EMPTY:
                return "[{luna}]({link}){editie}".format(
                    luna=self.luna_curenta.capitalize(),
                    link=self.link_revista_curenta,
                    editie=editie)
            else:
                return "{luna}{editie}".format(
                    luna=self.luna_curenta.capitalize(),
                    editie=editie)

        else:
            if self.link_revista_curenta != EMPTY:
                return "[#{editie}]({link})".format(
                    editie=self.editie_curenta,
                    link=self.link_revista_curenta)
            else:
                return "#{editie}".format(
                    editie=self.editie_curenta)

    def get_shortcode_markdown(self):
        def make_markdown(thumb, link):
            return "\t\"images/{thumbnail}|{link}|\"".format(
                thumbnail=thumb,
                link=link)

        # Pentru editiile care au mai multe variante (ex: coperta pentru abonati),
        # trebuie sa facem split si sa construim mai multe linkuri
        if ";" in self.img_link_full and ";" in self.img_thumbnail:
            links = self.img_link_full.split(";")
            thumbs = self.img_thumbnail.split(";")
            zipped_list = list(zip(thumbs, links))
            list_of_markdowns = (make_markdown(linie[0], linie[1]) for linie in zipped_list)
            return "\n".join(list_of_markdowns)

        # Altfel, pentru editiile cu o singura coperta, facem un link simplu
        else:
            return make_markdown(self.img_thumbnail, self.img_link_full)

    def get_site_markdown(self):
        if self.site_revista != EMPTY:
            return "[Site {nume}]({link})".format(
                nume=self.nume,
                link=self.site_revista)
        else:
            return ""

### --------- SCRIPTUL INCEPE AICI --------- ###
def citeste_fisier(fisier_csv):
    '''
    Citeste csv-ul si transforma fiecare rand din fisier, care e un dict de
    forma (header->value), intr-un obiect de tip Revista care are drept
    atribute cheile din dict (headerele csv-ului)
    '''
    # lista_linkuri = open(fisier_csv, "r")

    print("reading %s" % fisier_csv)

    fisier = open(fisier_csv, "r")
    csv_reader = csv.DictReader(fisier, delimiter='\t')
    lista_reviste = {}
    for row in csv_reader:
        # print("============")
        # print(row)
        revista_curenta = Revista(row)
        if revista_curenta.are_editie():
            # print("lista_reviste = ", lista_reviste)
            # print("revista_curenta = ", revista_curenta)
            revista_curenta_din_lista = lista_reviste.get(revista_curenta.get_nume_tara(), [])
            # print("revista_curenta_din_lista = ", revista_curenta_din_lista)
            revista_curenta_din_lista.append(revista_curenta)
            lista_reviste[revista_curenta.get_nume_tara()] = revista_curenta_din_lista
            # print("revista_curenta_din_lista dupa append = ", revista_curenta.nume, "size = ", len(lista_reviste.get(revista_curenta.nume, [])))
            # print(revista_curenta.nume, " -> ", revista_curenta.site_revista)
    # print("total: ", len(lista_reviste), " reviste")
    return lista_reviste

def make_articol(lista_reviste):
    '''
    Primeste lista de obiecte tip 'Revista', o proceseaza pe fiecare in parte,
    si genereaza stringul final markdown pentru includere in articol
    '''
    lista_reviste_markdown = []
    print(lista_reviste)
    # itereaza reviste
    for revista in lista_reviste.values():
        print("iterating revista: {}".format(revista.nume))
        try:
            revista_curenta_markdown = proceseaza_revista(revista)
        except Exception as e:
            print("problema la revista {}: {}".format(str(revista), e))
        lista_reviste_markdown.append(revista_curenta_markdown)

    # scrie fisier
    scrie_fisier("\n".join(lista_reviste_markdown))

def proceseaza_revista(lista_editii):

    return "## %s\n" \
           "### %s\n" \
           "{{< figure-multi-ext\n%s\n>}}\n\n" \
           "%s\n" \
         % (
            lista_editii[0].get_nume_tara(),
            " | ".join(r.get_title_markdown() for r in lista_editii),
            "\n".join(r.get_shortcode_markdown() for r in lista_editii),
            lista_editii[0].get_site_markdown())

def print_sumar_reviste(lista_reviste):
    for k, v in lista_reviste.items():
        print(k, ":", len(v))
        for r in v:
            print("\t", r)

def scrie_fisier(reviste_markdown):
    markdown_file = codecs.open(OUTPUT_FILE, 'w', "utf-8")
    markdown_file.write(reviste_markdown)
    markdown_file.close()

### --------- MAIN --------- ###

if __name__ == "__main__":
    # try:
    args = sys.argv[1:]
    fisier = args[0] if (len(args) == 1) else INPUT_FILE_DEFAULT

    start_time = time.time()

    lista_reviste = citeste_fisier(fisier)
    print("------------------------------------------------")
    print_sumar_reviste(lista_reviste)
    print("------------------------------------------------")
    make_articol(lista_reviste)
    end_time = time.time()
    print("TERMINAT de scris in %d sec." % round(end_time - start_time, 2))
# except IOError as ioerr:
#     print("Eroare IO: fisierul cu linkuri nu exista (err: %s" % ioerr)

# except Exception as e:
#    print("Ceva n-a mers bine: %s." % e)
#    exit(1)