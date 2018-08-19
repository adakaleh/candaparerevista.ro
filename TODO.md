## Beta release
### General

* [x] Tagline

### Pagina articol
* [x] De adăugat info data originală a articolului în caseta tehnică 

### Conţinut
#### Articole
* [x] Selecţie şi formatare primul set de articole

#### Autori
* [x] Pagini autori

#### Site
* [x] Pagina Despre

### Pagina single
* [x] Fix margins



### Cod
* [x] Embed fonturi
* [x] De scos request-uri 3rd party (img, css, js)
* [ ] Optimizare fonturi (de scos fonturi nefolosite, unicode ranges) - ?


## v1.0 release
### General
* [ ] De stabilit categorii fixe
* [x] Sidebar/Footbar cu noutăți comunitate
* [ ] Logo - improve

### Navbar
* [ ] Buton Forum mai proeminent (?)

### Blog comunitate
* [x] Fix layout flex vertical (~~justify~~ flex-grow)
* [x] Font sans serif
* [x] Eliminare info autor
* [ ] Îmbunătăţiri layout
* [ ] Link pe card

### Pagina articol
* [x] De căutat font nou serif
* [x] De rearanjat layout titlu - subtitlu - data - autor - categorii

### Pagini taguri/categorii
* [ ] ~~De testat înălțime header cu multe categorii / taguri~~
* [x] De unit tags şi categorii într-o singură categorie, cu un singur nav link

### Mobile
* [ ] Fix layout carduri prev/next
* [ ] Test

### Conţinut 

#### Articole
* [x] Licența materiale din `/content/posts`
* [x] Casetă tehnică joc si suport nota ?
* [x] Suport pentru aside (casete cu text adiţional)

#### Autori
* [ ] Suplimentat caseta autorului cu date contact, dacă există

#### Documentaţie
* [ ] Pagină-exemplu cu formatare
* [ ] Pagină Contribuitori

#### Secţiuni suplimentare
* [ ] Proiectele comunităţii
* [ ] Istoric Level / Arhiva reviste

### Cod
* [ ] Documentaţie-Readme
* [ ] CI
* [x] Page Bundles / Resources + image resize


## Next releases
### Prima pagină
* [ ] De testat și modificat pentru cazurile cu autor/avatar lipsă sau default
* [ ] Link autor pentru posturile cu autor default (car-lvl) duc doar către pagina de autori (vezi post-list.html)

### Pagina articol
* [ ] Fix/improve layout imagini
* [ ] Aside cu float left/width 50%

### Cod
* [ ] De eliminat `singleViewStyle = "casper"` din config, condiţiile din cod `{{if ne .Site.Params.singleViewStyle "casper"}}` şi layout-urile aferente, că nu ne trebuie
* [ ] De testat si modificat daca e cazul parţialul `meta-twitter`; de modificat parţialul `meta-facebook` să setăm, dacă se poate, `og:image:width` şi `og:image:height` (vezi https://developers.facebook.com/docs/sharing/best-practices/#precaching)
* [ ] De schimbat utilizarea `.Params.image`, pe care nu o mai folosim după ce am introdus page resources - de folosit pe post de override cand nu vrem sa folosim resources (ex: pentru GIF-uri); asta e comportamentul acum pentru cover, dar trebuie un parametru asemanator si pentru card thumb
* [ ] De îmbunătățit citirea avatarului pentru autori, să găsească automat fișierul de tip imagine cu același nume ca al fișierului autorului, astfel încât să nu mai fie nevoie de scrierea explicită a avatarului ca variabilă în fișierul yml
* [ ] De folosit page resources pentru download

### Functionalitati suplimentare
* [x] Header pagina autor (vezi https://github.com/eueung/hugo-casper-two/issues/3)
* [ ] Galerie de imagini
* [x] RSS limită
* [ ] RSS improv: adăugare categorie la titlu sau RSS-uri separate
* [ ] Search
* [ ] Arhivă toate posturile
* [ ] Dark theme
