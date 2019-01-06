Codul sursă pentru site-ul [candaparerevista.ro](https://candaparerevista.ro)

# Instalare

Clonează repo-ul și rulează hugo ca să generezi site-ul. Fișierele site-ului vor fi puse în folderul „public”.

Site-ul nu este compatibil cu ultimele versiuni Hugo. Versiunea [0.42.2](https://github.com/gohugoio/hugo/releases/tag/v0.42.2) e ultima care generează site-ul cum trebuie.

# Conţinut

## Articole
Se pot introduce articole în corpul altui articol folosind parțialul `include-post.html`, folosind sintaxa:

~~~
text articol aici

{{< include-post "nume-unic-director-articol" "imagine/optionala.jpg" >}}

text articol aici
~~~

Numele directorului este echivalentul slug-ului, respectiv ultima parte a URL-ului:

`https://candaparerevista.ro/posts/2018/10/nume-unic-director-articol/`

Parțialul caută numele în toate paginile site-ului, și îi introduce conținutul în articolul-părinte, afișând și numele autorului cu link către articolul sursă.

Imaginea este opțională. Dacă este dată, trebuie folosită calea relativă la articolul-părinte **în care** introducem articolul. Dacă lipsește, va fi căutată imaginea de copertă ("cover-image") din resursele articolului-copil (cel inclus).

Atenție:
* dacă articolul-copil conține imagini cu cale relativă, acele imagini nu vor fi afișate în articolul părinte.
* în caz de eroare, trebuie verificat dacă numele directorului e scris corect și dacă pagina nu are setat `draft: true`, caz în care nu are cum să o găsească.

### Ascundere articole de pe home page
Pentru a omite unele articole din lista de posturi afișate pe home page, se poate seta un parametru suplimentar în front matter:

`hideOnHome: true`

Când acest parametru e setat, articolul nu va fi inclus în lista de articole de pe home (indiferent de numărul de pagini), dar va apărea în celelalte secțiuni alte site-ului, cum ar fi pagina de articole sau pagina autorului.

Acest parametru e util atunci când publicăm un articol în categoria "Recomandare" în același timp cu publicarea Retrospectivei Săptămânii în care includem articolul respectiv (folosind parțialul `include-post` de mai sus) la "Recomandarea Săptămânii". În felul ăsta, evităm să avem două articole consecutive cu același conținut (și poate și aceeași imagine pe card).

## Imagini
Pentru a introduce imagini în articole, există 4 variante:

#### Varianta simplă
Fiecare imagine se introduce separat folosind sintaxa normală de markdown și va ocupa întreaga lățime a articolului:
~~~
text articol aici

![un titlu pentru imagine](sursa/imaginii.jpg)

text articol aici
~~~

#### Varianta simplă cu comentariu
Fiecare imagine se introduce separat folosind shortcode-ul built-in `figure` și va ocupa întreaga lățime a articolului:
~~~
text articol aici

{{< figure  src="sursa/imaginii.jpg" caption="Comentariu ce va fi afișat sub imagine" >}}

text articol aici
~~~

#### Varianta imagini multiple cu comentariu opţional
Se foloseşte un shortcode custom `figure-multi`. Fiecare imagine trebuie trecută pe un rând separat, iar sursa imaginii, comentariul şi (opţional) descrierea "alt" vor fi separate de `|`, ca în exemplul de mai jos. Imaginile vor fi afişate câte 2 sau 3 pe un rând, *cu înalţime fixă de 300 px* şi laţime variabilă în funcţie de numărul lor şi de lăţimea ferestrei. De asemenea, fiecare imagine are ataşat şi un link către imaginea la rezoluţia originală.      

~~~
text articol aici

{{< figure-multi
    "sursa/imaginii-1.jpg|Comentariu ce va fi afișat sub imaginea 1|Descriere opţională pentru imaginea 1"
    "sursa/imaginii-2.jpg|Comentariu ce va fi afișat sub imaginea 2"
    "sursa/imaginii-3.jpg|Comentariu ce va fi afișat sub imaginea 3|Descriere opţională pentru imaginea 2"
    "sursa/imaginii-4.jpg|Comentariu ce va fi afișat sub imaginea 4"
    "sursa/imaginii-5.jpg||Descrierea e obligatorie dacă lipseşte comentariul"
>}}

text articol aici
~~~

#### Varianta imagini multiple, cu comentariu opţional, imaginea locala nu este cropata si are link catre imaginea originala
Se foloseşte un shortcode custom `figure-multi-ext`. Fiecare imagine trebuie trecută pe un rând separat, iar sursa imaginii locale, sursa originlă, comentariul opțional și descrierea opțională "alt" vor fi separate de `|`, ca în exemplul de mai jos. Imaginile vor fi afişate pe cât posibil la dimensiunea reală, fără să fie cropate sau restrânse în alt fel. De asemenea, fiecare imagine are ataşat şi un link către sursa originală a imaginii.
~~~
text articol aici
{{< figure-multi-ext
    "sursa/imagine-locala-1.jpg|https://link.sursa.originala.a.imaginii-1|Comentariu opţional ce va fi afișat sub imaginea 1|Descriere opţională pentru imaginea 1"
    "sursa/imagine-locala-2.jpg|https://link.sursa.originala.a.imaginii-2|Comentariu opţional ce va fi afișat sub imaginea 2|Descriere opţională pentru imaginea 2"
>}}
text articol aici
~~~

## Aside
Pentru a introduce o casetă de text separată de corpul articolului, trebuie folosit parţialul `aside`, astfel:
* ` {{< aside >}} text aici {{< /aside >}} `
* ` {{% aside %}} text aici {{% /aside %}} `
cu deosebirea că a doua variantă procesează şi conţinutul markdown, ca de exemplu ` ## Header ` sau ` **bold** `

# Cod

[...] TODO mai mult conținut

## Conţinutul postat
Articolele trebuie ţinute într-un director propriu, în directorul `content`, cu un fișier `index.md` obligatoriu ce conține front matter și articolul, plus directoare opţionale pentru conţinut adiţional (imagini, ataşamente), care vor fi folosite în articol. Împreună formează un Page Bundle, cu următoarea structură:

~~~
content/
├── nume-articol/
│   ├── images/
│   │   ├── image-1.jpg
│   │   ├── image-2.jpg
│   ├── gallery/
│   │   ├── image-1.jpg
│   │   ├── image-2.jpg
│   │   ├── image-3.jpg
│   │   ├── image-4.jpg
│   ├── index.md
~~~

Unde:
* `nume-articol` - va deveni parte din url-ul articolului (slug): `https://candaparerevista.ro/posts/nume-articol/`
* directoarele sunt opţionale şi păstrează resursele ce vor fi folosite în articol cu linkuri relative; exemplu inserare imagine: `![](images/image-1.jpg)`
* directorul `gallery` conține imaginile ce vor fi prezentate ca o galerie la sfârșitul articolului;
* `index.md` - numele fişierului ce conţine front matter şi corpul articolului.

### Cover image
Imaginea principală (cover), care va apărea pe card şi la începutul articolului, poate fi specificată în front matter prin două metode:
  * metoda clasică, cu referire directă: `image: images/image-1.jpg`
  * folosind Page Resources, sub variabila `resources`. Aceasta va fi citită în cod astfel: `.Resources.GetMatch "cover-image"`.
~~~
  resources :
    - src: "images/image-1.jpg"
      name: "cover-image"
~~~
Dacă lipsește, pe carduri va fi afișată o imagine aleasă la întâmplare din setul de imagini default, iar în articol nu va fi afișat nimic.

### Redimensionare imagini
Toate imaginile recunoscute ca page resources (aflate într-un bundle cu structura de mai sus) pot fi citite separat, iar imaginile pot fi și redimensionate astfel:
~~~
# citire toate imaginile
{{ range .Resources.ByType "image" }}
# redimensionare proportionala la latimea de 200 px
{{ $resizedImage := .Resize "200x" }} 
~~~

Dimensiunile pentru redimensionare sunt stabilite la nivel de site și stocate în `config.toml`:
~~~
  firstCardThumbSize = "x500"
  cardThumbSize = "x350"
~~~

### Informații suplimentare
Hugo Page Bundles: https://gohugo.io/content-management/page-bundles
Hugo Page Resources: https://gohugo.io/content-management/page-resources/
Hugo Image Processing: https://gohugo.io/content-management/image-processing/

[...] TODO mai mult conținut

# Credits
* Hugo static site generator: [website](https://gohugo.io/) | [github](https://github.com/gohugoio/hugo)
* Casper Two Hugo Theme: [github](https://github.com/eueung/hugo-casper-two)
* Merriweather font: [github](https://github.com/EbenSorkin/Merriweather)
* Merriweather Sans font: [github](https://github.com/EbenSorkin/Merriweather-Sans)

