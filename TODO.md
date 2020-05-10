## Next releases
### General
* [ ] De stabilit categorii fixe
* [ ] Logo - improve
* [x] Buton Forum mai proeminent
* [ ] Pagină credits, cu link în footer - Hugo, Casper, font, imagine fundal etc.

### Prima pagină
* [ ] De testat și modificat pentru cazurile cu autor/avatar lipsă sau default
* [ ] Link autor pentru posturile cu autor default (car-lvl) duc doar către pagina de autori (vezi post-list.html)

### Pagina articol
* [ ] Fix/improve layout imagini
* [ ] Aside cu float left/width 50%

### Blog comunitate
* [x] Modificare post list să nu apară niciodată primul (cardul mare)

### Mobile
* [x] Fix layout carduri prev/next
* [ ] Test

### Cod
* [ ] De eliminat `singleViewStyle = "casper"` din config, condiţiile din cod `{{if ne .Site.Params.singleViewStyle "casper"}}` şi layout-urile aferente, că nu ne trebuie
* [ ] De testat si modificat daca e cazul parţialul `meta-twitter`; de modificat parţialul `meta-facebook` să setăm, dacă se poate, `og:image:width` şi `og:image:height` (vezi https://developers.facebook.com/docs/sharing/best-practices/#precaching)
* [ ] De schimbat utilizarea `.Params.image`, pe care nu o mai folosim după ce am introdus page resources - de folosit pe post de override cand nu vrem sa folosim resources (ex: pentru GIF-uri); asta e comportamentul acum pentru cover, dar trebuie un parametru asemanator si pentru card thumb
* [ ] De îmbunătățit citirea avatarului pentru autori, să găsească automat fișierul de tip imagine cu același nume ca al fișierului autorului, astfel încât să nu mai fie nevoie de scrierea explicită a avatarului ca variabilă în fișierul yml
* [ ] De folosit page resources pentru download
* [ ] Optimizare fonturi (de scos fonturi nefolosite, unicode ranges) - ?
* [x] De corectat paginație (navigation.html) - lista de page numbers nu ține cont de numărul total de pagini, trebuie clamp

### Documentatie
* [ ] Info contribuitori git / site map
* [ ] Update readme

### Functionalitati suplimentare
* [x] Header pagina autor (vezi https://github.com/eueung/hugo-casper-two/issues/3)
* [x] Galerie de imagini
* [x] RSS limită
* [ ] RSS improv: adăugare categorie la titlu sau RSS-uri separate
* [ ] Search
* [ ] Arhivă toate posturile
* [ ] Dark theme

### Conţinut
#### Autori
* [ ] Suplimentat caseta autorului cu date contact, dacă există

#### Documentaţie
* [ ] Pagină-exemplu cu formatare
* [x] Pagină Contribuitori

#### Secţiuni suplimentare
* [ ] Proiectele comunităţii
* [ ] Istoric Level / Arhiva reviste