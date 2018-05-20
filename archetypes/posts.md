---

# (OBLIGATORIU)
title: Titlul Noului Articol

# (OBLIGATORIU)
type: post

# (optional) Subtitlul Articolului
subtitle: 

# (OBLIGATORIU) data publicării de forma `2018-02-10` sau `2018-02-10T17:38:18+02:00`
date: {{ .Date }}

# (OBLIGATORIU, aproape) aici se trece numele fisierului ce contine
# detaliile autorului (un fişier .yml în `data/authors`).
# Exemplu: pentru fişierul de autor `data/authors/someone-name.yml`
# se va completa `authors: someone-name`
# Daca autorul explicit lipseşte, autorul va fi cel default, adica site-ul
authors: 

# (optional) listă de forma `categories: ["cat1", "cat2", "cat3"]`
# sau
# `categories:`
# `  - cat1`
# `  - cat2`
categories: 

# (optional) listă de forma `tags: ["tag1", "tag2", "tag3"]`
# sau
# `tags:`
# `  - tag1`
# `  - tag2`
tags: 

# (optional) textul care va apărea pe card; dacă lipsește, va fi 
# înlocuit cu primele cuvinte din articol
description: 

# (opțional) tipul de licență atribuit articolelor de tipul 'post'
# trebuie să corespundă unui fișier din directorul `licenses` 
# ca în exemplul: `mit` pentru fișierul `LICENSE-mit.md`;
# dacă lipsește, va fi afișată licența `default`
licenta: 

# (optional) link către site-ul unde a fost publicat prima dată articolul,
# dacă e cazul, unde `text` e numele linkului (ex: "Blogul autorului")
# iar `data` este data originală de publicare, în format `YYYY-MM-DD`
sursa:
   link:
   text: 
   data:

# (optional) diverse linkuri suplimentare, relevante pentru articol
# trebuie sa fie o structura de tipul
# `linkuriExterne:`
# `  website-1:`
# `    text: textul ce va apărea ca link`
# `    link: https://url.ul/sitului`
# `    desc: O scurtă descriere a site-ului`
linkuriExterne:
 
# (optional) link către postul deschis pe forum pentru articol 
# pentru comentarii și discuții
linkForum: 


# (optional, recomandat) calea către imaginea articolului, relativ la directorul articolului:
# - pentru card, va fi căutată una dintre cele două imagini, în ordina de mai jos, sau, 
#   dacă lipsește, va fi înlocuită cu o imagine generică;
# - pentru imaginea principală a articolului, va fi căutată doar imaginea "cover-image"
# Se completează doar src astfel: `src: "images/coperta.jpg"`
resources:
  - src: 
    name: "card-cover-image"

  - src: 
    name: "cover-image"

---

_(conținutul tău aici)_