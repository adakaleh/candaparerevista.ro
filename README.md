Codul sursă pentru site-ul [candaparerevista.ro](https://candaparerevista.ro)

# Instalare

# [...] TODO mai mult conținut

# Conţinut

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

