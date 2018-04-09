## Pre-release - alpha
### General
* [x] Favicon
* [x] Evidențiere categorie (ex: "[Review]") în card/articol

### Mobile
* [x] Fix mobile css

### Prima pagină
* [x] Featured/pinned posts (categorie nouă)

### Navbar
* [x] De scos linkuri FB şi GH
* [x] De mutat buton Forum în dreapta

### Articole
* [x] Linkuri suplimentare articol
* [x] Suport subtitluri
* [x] Improve carduri read next-prev


## Beta release
### General
* [ ] Logo
* [x] Tagline

### Pagina articol
* [x] De adăugat info data originală a articolului în caseta tehnică 
* [ ] De adăugat info licenţă în caseta tehnică 

### Conţinut
#### Articole
* [ ] Selecţie şi formatare primul set de articole

#### Autori
* [ ] Pagini autori

#### Site
* [ ] Pagina Despre

### Pagina single
* [ ] Fix margins

### Navbar
* [ ] Buton Forum mai proeminent

### Cod
* [x] Embed fonturi
* [x] De scos request-uri 3rd party (img, css, js)
* [ ] Optimizare fonturi (de scos fonturi nefolosite, unicode ranges) - ?


## v1.0 release
### General
* [ ] De stabilit categorii fixe
* [x] Sidebar/Footbar cu noutăți comunitate

### Blog comunitate
* [x] Fix layout flex vertical (~~justify~~ flex-grow) 
* [ ] Îmbunătăţiri layout
* [ ] Link pe card

### Pagina articol
* [x] De căutat font nou serif
* [x] De rearanjat layout titlu - subtitlu - data - autor - categorii

### Pagini taguri/categorii
* [ ] ~~De testat înălțime header cu multe categorii / taguri~~
* [ ] De unit tags şi categorii într-o singură categorie, cu un singur nav link

### Mobile
* [ ] Fix layout carduri prev/next
* [ ] Test

### Conţinut 

#### Articole
* [ ] Licența materiale din `/content/posts`
* [ ] Casetă tehnică joc si suport nota ?

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

### Cod
* [ ] De eliminat `singleViewStyle = "casper"` din config, condiţiile din cod `{{if ne .Site.Params.singleViewStyle "casper"}}` şi layout-urile aferente, că nu ne trebuie
* [ ] De văzut unde sunt folosite parţialele `meta-twitter` şi `meta-facebook` şi eliminat
* [ ] De elimimat citirea variabilei `.Params.image`, pe care nu o mai folosim după ce am introdus page resources

### Functionalitati suplimentare
* [ ] Header pagina autor (vezi https://github.com/eueung/hugo-casper-two/issues/3) 
* [ ] Galerie de imagini
* [ ] RSS fix/improv. (?)
* [ ] Search
* [ ] Arhivă toate posturile
* [ ] Dark theme