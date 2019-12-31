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

# (optional) se specifica daca vrem sa afisam o imagine mai mare pentru coperta
# articolului; trebuie specificata si o imagine la resurse (vezi mai jos) pentru
# a avea efect
featured: true

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

# (optional) daca este prezent, cu valoarea `true`, postul nu va fi
# inclus in lista de articole de pe home page
hideOnHome:

# (optional) daca este prezent, cu valoarea `true`, postul nu va
# avea descriere (excerpt) pe card, chiar daca e completat
# atributul 'description' de mai jos
hideDescription:

# (optional) daca este prezent, cu valoarea `true`, postul nu va
# avea imagine pe card, nici macar pe cea default care este aleasa
# in cazul in care nu e definita o imagine proprie
hideImage:

# (optional) o valoare css pentru culoarea de fundal; poate fi un string
# de tip `rgba(223, 205, 106, 0.15)` sau culoarea in hex '#dfcd6a' 
cardColor: 

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

# (optional) un text în caz că articolul necesită un disclaimer
# (ex: "Articol scris în baza unei copii de review de la producător”)
# valorile pot fi `default` (caz în care va fi folosit textul predefinit
# în config.toml) sau orice alt text, dacă trebuie să fie customizat.
disclaimerReviewCopy:

# (optional) diverse resurse pentru download, relevante pentru articol
# trebuie sa fie o structura de tipul
# `download:`
# `  resursa-1:` # acest nume nu e relevant, nu e folosit
# `    text: textul ce va apărea ca link pentru download`
# `    link: download/resursa.pdf`  # link relativ catre resursa
# `    desc: O scurtă descriere a resursei ce poate fi descărcată`
download:

# (optional) daca e prezent si e true, nu va mai fi afisata 
# galeria la sfarsitul articolului
disableGallery:

# (optional) daca disableGallery nu e true, iar acest parametru
# e prezent si este true, atunci galeria de la sfarsit va fi 
# afisata in modul vechi (doar thumbs, fara fotorama)
classicGallery:

# (optional) informatii tehnice minime despre joc sau carte
# dintre parametrii care pot fi dati, doar `data` este obligatoriu
# vezi exemplu in [postarea exemplu](/content/posts/2018/05/hello-markdown/index.md).
# `  data: # un string oarecare, nu trebuie să fie în format dată`
# `  producator: # numele producătorului (pentru jocuri)`
# `  autor: # numele autorului (pentru cărți)`
# `  platforme: # o lista în format "[PC , XBOX]"`
# `  reviews: # linkuri catre paginile de metacritic si/sau opencritic`
# `    metacritic: https://www.link.url`
# `    opencritic: https://www.link.url`
# `  cumpara: # o lista de array-uri cu nume si link, exemplu:` 
# `    - [Steam, https://store.steampowered.com/app/951440/Volcanoids/]`
infoBox:

# (optional) caseta-concluzie cu nota, plusuri, minusuri, alternativa;
# vezi exemplu in [postarea exemplu](/content/posts/2018/05/hello-markdown/index.md).
casetaTehnica:

# (optional) diverse linkuri suplimentare, relevante pentru articol
# trebuie sa fie o structura de tipul
# `linkuriExterne:`
# `  website-1:`  # acest nume nu e relevant, nu e folosit
# `    text: textul ce va apărea ca link`
# `    link: https://url.ul/sitului`
# `    desc: O scurtă descriere a site-ului`
linkuriExterne:
 
# (optional) link către postul deschis pe forum pentru articol 
# pentru comentarii și discuții
linkForum: 


# (optional, recomandat) calea către imaginea articolului, relativ la directorul articolului:
# - pentru card, va fi căutată una dintre cele două imagini (card sau cover), în ordinea de mai jos, sau,
#   dacă lipsește, va fi înlocuită cu o imagine generică;
# - pentru imaginea principală a articolului, va fi căutată imaginea "feature-image" apoi "cover-image"
# Se completează doar src astfel: `src: "images/coperta.jpg"`
resources:
  - src: 
    name: "card-cover-image"

  - src: 
    name: "cover-image"

  - src:
    name: "feature-image"
---

_(conținutul tău aici)_