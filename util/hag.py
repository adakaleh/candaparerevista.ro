#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HAG (Highlights Aggregator) e un mic helper pentru a agrega continutul din articolele Retrospectiva Saptamanii.
Scriptul citeste toate articolele de tip Retrospectiva pentru un an intreg si aduna toate liniile
dintr-o anumita sectiune (ex. Stiri) intr-un singur fisier.

In mod implicit, scriptul citeste cel mai recent an pentru sectiunea Stiri, dar poate primi argumente pentru alti ani
si alte sectiuni (sau subsectiuni, ex: Lansari jocuri).

-------------------
# TODO
-------------------
* Accepta sectiune si an ca parametri
* Accepta subsectiuni si ignora separator
* Curatare cod nefolosit + refactoring
* Adaugare la fisier istorie existent si actualizare data la cea mai recenta data
* Documentatie + usage
* De generat cuprins cu id-uri potrivite si impartit pe luni
* Fix metoda diacritice
* Procesare yaml cu librarie python
"""

import os
import sys
import io
import time
import re
import yaml


OUTPUT_FILE = "rezultat_agregare_retrospective"

DEFAULT_UNKNOWN_TEXT = "<span style='background-color:red'>PROBLEM</span>"

HIGHLIGHTS_DIR_PATH = os.path.join("..", "content", "highlights")
SECTIUNE_DEFAULT = "știri"
INDEX_MD = "index.md"

### --------- SCRIPTUL INCEPE AICI --------- ###

def read_retro_dirs(sectiune_cautata, sub_sectiune_cautata=None):

    def get_current_year(list_of_dirs):
        return next(curr_year for curr_year in reversed(list_of_dirs) if curr_year.isnumeric())
        # return "2018"

    def is_weekly_highlights_dir(dir_name):
        # ignoram directoarele care nu-s retrospective (nu sunt
        # intr-un director care incepe cu numar,
        # respectiv copertile sau retrospectivele speciale)
        retro_dir = os.path.split(dir_name)[1]
        return retro_dir[0].isnumeric()

    lista_bucati_saptamanale = {}

    lista_directoare = os.listdir(HIGHLIGHTS_DIR_PATH)
    current_year = get_current_year(lista_directoare)

    # for year_dir in os.listdir(highlights_base_path):

    print("---------------------------------")
    print ("## ", current_year, sectiune_cautata, sub_sectiune_cautata)
    print("---------------------------------")
    year_dir_path = os.path.join(HIGHLIGHTS_DIR_PATH, current_year)

    # walk year dir
    for root, dirs, files in os.walk(year_dir_path):

        # retro_dir = os.path.split(root)[1]
        if is_weekly_highlights_dir(root):
            for f in files:
                if f == INDEX_MD:
                    # citeste fisier
                    # TODO citeste sectiune ca parametru si inlocuieste diacritice
                    linii_sectiune = citeste_fisier(root, current_year, sectiune_cautata, sub_sectiune_cautata)

                    if (linii_sectiune):
                        lista_bucati_saptamanale.update(linii_sectiune)

    return lista_bucati_saptamanale

def citeste_fisier(root_dir, retro_year, sectiune_cautata, sub_sectiune_cautata=None):
    """
    Cauta in fiecare fisier sectiunea dorita si returneaza un dict
    de forma {titlu_saptamana: [linii_sectiune]}
    """

    file_path = os.path.join(root_dir, INDEX_MD)
    print("(reading file ", file_path, ")")

    fisier = open(file_path, "r", encoding="utf-8")
    linii_fisier = fisier.readlines()
    titlu_saptamana = DEFAULT_UNKNOWN_TEXT
    linii_sectiune = []
    gasit_sectiune = False      # heading 2 ##
    gasit_sub_sectiune = False  # heading 3 ###

    def is_hugo_markdown_title(line):
        return line.startswith("title: ")

    def is_section_title(line):
        return line.startswith("## ")

    def is_sub_section_title(line):
        return line.startswith("### ")

    # TODO de folosit sau sters
    def is_separator(line):
        return line.startswith("---")

    def get_link_relref():
        f_root = os.path.join("..", "content")
        url = root_dir.replace(f_root, "", 1)
        return "{{<relref \"%s\">}}" % url

    # citim toate liniile din fisier; cand gasim sectiunea cautata, punem liniile in lista de returnat
    for line in linii_fisier:
        # print("checking linie | ", is_section_title(line.strip()), " | ", line)

        if is_hugo_markdown_title(line):

            # TODO replace with regex
            titlu_saptamana = line.lstrip('title: "Retrospectiva săptămânii ').rstrip().rstrip(' ' + retro_year + '"')

        # pana acum n-am gasit sectiunea cautata; acum am gasit o sectiune - verificam daca e cea dorita
        elif not gasit_sectiune and is_section_title(line):
            # if sectiune_cautata in line.lower():
            if clean_diacritice(sectiune_cautata) in clean_diacritice(line):
                gasit_sectiune = True

        # am gasit sectiunea cautata; acum citim liniile din sectiune pana la urmatoarea sectiune
        elif gasit_sectiune and not is_section_title(line):
            # daca nu cautam o anume subsectiune, luam toate liniile din sectiune
            if not sub_sectiune_cautata:
                linii_sectiune.append(line.rstrip())

            else:
                # pana acum n-am gasit subsectiunea cautata; acum am gasit o subsectiune - verificam daca e cea dorita
                if not gasit_sub_sectiune and is_sub_section_title(line):
                    if clean_diacritice(sub_sectiune_cautata) in clean_diacritice(line):
                        gasit_sub_sectiune = True

                # am gasit subsectiunea cautata; acum citim liniile pana la urmatoarea subsectiune
                elif gasit_sub_sectiune and not is_sub_section_title(line):
                    linii_sectiune.append(line.rstrip())

                # daca anterior am gasit subsectiunea cautata si acum am ajuns la alta sectiune,
                # inseamna ca am epuizat subsectiunea dorita, putem incheia bucla
                elif gasit_sub_sectiune and is_sub_section_title(line):
                    break

        # daca anterior am gasit sectiunea cautata si acum am ajuns la alta sectiune,
        # inseamna ca am epuizat sectiunea dorita, putem incheia bucla
        elif gasit_sectiune and is_section_title(line):
            break

        # cazul in care n-am gasit sectiunea dorita si suntem la o linie oarecare
        else:
            continue

    fisier.close()
    if (linii_sectiune):
        # daca am gasit linii pentru aceasta sectiune, inseram si titlul (saptamana) in prima pozitie
        # cu link catre articolul original din care am cules liniile
        link_articol_original = make_markdown_url(titlu_saptamana, get_link_relref())
        linii_sectiune.insert(0, "\n## %s" % link_articol_original)
        return {titlu_saptamana: linii_sectiune}
    else:
        pass

def scrie_fisier(lista_bucati_saptamanale, nume_sectiune):
    """
    Scrie un fisier cu toate liniile din sectiunea cautata, pornind de la
    un dict de sectiuni (sau subsectiuni) de forma {titlu_saptamana: [linii_sectiune]}
    """
    filename = "{base_filename}_{sectiune}.txt".format(
        base_filename=OUTPUT_FILE,
        sectiune=nume_sectiune)
    markdown_file = io.open(filename, mode='w', encoding='utf-8')

    # scrie cuprins
    cuprins_cu_links = genereaza_cuprins(lista_bucati_saptamanale.keys())
    markdown_file.write(cuprins_cu_links)
    markdown_file.write("\n\n")

    # scrie bucatile de sectiuni
    for weekly_piece in lista_bucati_saptamanale.values():
        markdown_file.write("\n".join(weekly_piece))

    markdown_file.close()

def genereaza_cuprins(lista_titluri):
    lista_links = [make_markdown_url(titlu, make_html_id(titlu)) for titlu in lista_titluri]
    # TODO de impartit pe luni
    return " | ".join(lista_links)


### --------- UTILS --------- ###

def make_markdown_url(url_text, url_link):
    return "[%s](%s)" % (url_text, url_link)

def make_html_id(text):
    # TODO fix sa includa id-ul generat dupa procesarea relref din titlul saptamanii
    clean_id = re.sub('[^(a-z)(A-Z)(0-9)._-]', '-', text)
    clean_id = re.sub('-+', '-', clean_id)
    return "#%s" % clean_id

def clean_diacritice(cuvant):
    """
    Sterge diacritice si returnează cuvantul in lowercase
    """
    # TODO make this proper
    cleaned_s = re.sub('[ș,ş]', 's', cuvant.lower())
    cleaned_t = re.sub('[ţ, ț]', 't', cleaned_s)
    cleaned_a = re.sub('[ă]', 'a', cleaned_t)
    clean_result = cleaned_a
    return clean_result

### --------- MAIN --------- ###
if __name__ == "__main__":


    args = sys.argv[1:]

    # TODO foloseste argumente - sectiune si an
    # python hag.py [sectiune] [an]

    start_time = float(time.time())

    # read highlights years
    # TODO fix - include sectiune si subsectiune din argumente
    sectiune_cautata = SECTIUNE_DEFAULT
    # sectiune_cautata = "anun"
    lista_finala_bucati = read_retro_dirs(sectiune_cautata)
    # lista_finala_bucati = read_retro_dirs("anun", "lansate")

    # scrie_fisier("\n".join(lista_finala_bucati))
    scrie_fisier(lista_finala_bucati, clean_diacritice(sectiune_cautata))

    end_time = float(time.time())
    print("TERMINAT de scris in %s sec." % round(end_time - start_time, 2))