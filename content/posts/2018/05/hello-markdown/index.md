---
title: A Plain Markdown Post
subtitle: A post subtitle
type: post
draft: true
author: car-lvl
date: '2017-02-14'
categories:
  - Example
  - Hugo
tags:
  - blogdown
  - markdown
  - sample
  - altul
  - inca-unul
  - ultimul
sursa:
  text: blogul autorului
  link: https://github.com/eueung/hugo-casper-two
licenta: default
disclaimerReviewCopy: default
download:
  versiune-text:
    text: Text version
    link: download/markdown.txt
    desc: Versiunea .txt a acestui fişier markdown.
linkuriExterne:
  res-toml-yaml:
    text: Deep dive into TOML, JSON and YAML
    link: https://gohugohq.com/howto/toml-json-yaml-comparison/
    desc: O scurtă comparaţie între formatele folosite de Hugo pentru front-matter.
  templating-help:
    text: Hugo Translator
    link: https://regisphilibert.com/blog/2017/04/hugo-go-template-translator-explained-understanding/
    desc: Un mic ajutor pentru a înţelege mai bine cum se foloseşte Go în template-urile Hugo, având şi comparaţii cu PHP sau JavaScript.
disableGallery: false
classicGallery: false
infoBox:
  data: '2017-02-14'
  gen: [Bătaie cu catane]
  producator: FromSoftware
  autor: Johnny Hidetaka
  platforme: [PC , XBOX]
  reviews:
    metacritic: https://www.metacritic.com/game/pc/sekiro-shadows-die-twice
    opencritic: https://opencritic.com/game/6629/devil-may-cry-5
  cumpara:
    - [Steam, https://store.steampowered.com/app/951440/Volcanoids/]
    - [GOG, https://www.gog.com/game/katana_zero]
casetaTehnica:
  nota: 6.8
  verdict: "Nașpa."
  concluzie: "Nu recomand. Deloc. Decît dacă aflați despre un val de comentarii pozitive online la adresa acestui titlu, apărut după eventuala rezolvare a numeroaselor probleme care îl grevează. Și dacă producătorii și distribuitorii se pocăiesc. Public. Cu umilință."
  alternativa:
    nume: "Seria Total War"
    descriere: "La noi în țară, titlurile din seria Total War anterioare Rome II se vînd la prețuri foarte mici. Este vorba de jocuri care merită toată atenția noastră de pasionați, realizate mult mai bine decît Rome II. Ele sînt alternativa. Și își fac toți banii, cu vîrf și îndesat."
    imagine: gallery/1.jpg
    link: https://store.steampowered.com/app/4760/Rome_Total_War__Collection/

  plusuri:
    - "împărțirea administrativ-teritorială"
    - "armatele"

  minusuri:
    - "buguri numeroase, AI slab"
    - "sistem de agenți dezechilibrat"
    - "strategie stufoasă, neimersivă și nerealistă"
    - "consum mare de resurse"
linkForum: https://forum.candaparerevista.ro/viewtopic.php?f=28&p=77237
resources :
  - src: "images/car-cover.png"
    name: "cover-image"
    
  - src: "images/car-cover.png"
    name: "card-cover-image"
---

# Sample Text

## Second-level header

### Third-level header

#### Fourth-level header

A paragraph (with a footnote):

**Lorem ipsum** <!--more-->dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore _magna aliqua_. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.^[I'm sure you are bored by the text here.]

A blockquote (a gray bar at the left and lightgray background):

> Quisque mattis volutpat lorem vitae feugiat. Praesent porta est quis porta imperdiet. Aenean porta, mi non cursus volutpat, mi est mollis libero, id suscipit orci urna a augue. In fringilla euismod lacus, vitae tristique massa ultricies vitae. Mauris accumsan ligula tristique, viverra nulla sed, porta sapien. Vestibulum facilisis nec nisl blandit convallis. Maecenas venenatis porta malesuada. Ut ac erat tortor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nulla sodales quam sit amet tincidunt egestas. In et turpis at orci vestibulum ullamcorper. Aliquam sed ante libero. Sed hendrerit arcu lacus.

Info-box intern:

{{< info-box
  data="2016"
  gen="Bătaie cu catane"
  producator="My Man"
  platforme="PC,XBOX"
  cumpara="Steam,https://store.steampowered.com/app/951440/Volcanoids/|GOG,https://www.gog.com/game/katana_zero"
  opencritic="https://opencritic.com/game/6629/devil-may-cry-5"
  metacritic="https://www.metacritic.com/game/pc/sekiro-shadows-die-twice"
>}}

Some code (with a drop-shadow effect):

```js
(function() {
  var quotes = document.getElementsByTagName('blockquote'), i, quote;
  for (i = 0; i < quotes.length; i++) {
    quote = quotes[i];
    var n = quote.children.length;
    if (n === 0) continue;
    var el = quote.children[n - 1];
    if (!el || el.nodeName !== 'P') continue;
    // right-align a quote footer if it starts with ---
    if (/^—/.test(el.textContent)) el.style.textAlign = 'right';
  }
})();
```

A table (centered by default):

| Sepal.Length| Sepal.Width| Petal.Length| Petal.Width|Species |
|------------:|-----------:|------------:|-----------:|:-------|
|          5.1|         3.5|          1.4|         0.2|setosa  |
|          4.9|         3.0|          1.4|         0.2|setosa  |
|          4.7|         3.2|          1.3|         0.2|setosa  |
|          4.6|         3.1|          1.5|         0.2|setosa  |
|          5.0|         3.6|          1.4|         0.2|setosa  |
|          5.4|         3.9|          1.7|         0.4|setosa  |

An image (automatically centered when it is appropriate):

![Happy Elmo](https://slides.yihui.name/gif/happy-elmo.gif)


Imagine cu caption:

{{< figure  src="gallery/1.jpg" caption="Caption imagine aici dedesubt" >}}

Galerie de imagini cu caption (merg oricâte, dar ar trebui să ne limităm la 2):

{{< figure-multi
    "gallery/1.jpg|Lorem ipsum caption1 dolor sit amet, consectetur adipiscing elit"
    "gallery/2.jpg|Lorem ipsum caption2|altdescription2"
    "gallery/3.jpg|Caption 3|altdescription3"
    "gallery/4.jpg|Caption4"
    "gallery-2/5.jpg||altdescription5"
>}}

Looks good?

Quisque mattis volutpat lorem vitae feugiat. Praesent porta est quis porta imperdiet. Aenean porta, mi non cursus volutpat, mi est mollis libero, id suscipit orci urna a augue. In fringilla euismod lacus, vitae tristique massa ultricies vitae. Mauris accumsan ligula tristique, viverra nulla sed, porta sapien. Vestibulum facilisis nec nisl blandit convallis. Maecenas venenatis porta malesuada. Ut ac erat tortor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nulla sodales quam sit amet tincidunt egestas. In et turpis at orci vestibulum ullamcorper. Aliquam sed ante libero. Sed hendrerit arcu lacus.

Galerie cu toate imaginile dintr-un director:

{{< gallery "gallery" "titlu optional galerie cu caption"
      "1.jpg|Caption 1.jpg"
      "3.jpg|Caption 3.jpg"
>}}

Quisque mattis volutpat lorem vitae feugiat. Praesent porta est quis porta imperdiet. Aenean porta, mi non cursus volutpat, mi est mollis libero, id suscipit orci urna a augue. In fringilla euismod lacus, vitae tristique massa ultricies vitae. Mauris accumsan ligula tristique, viverra nulla sed, porta sapien. Vestibulum facilisis nec nisl blandit convallis. Maecenas venenatis porta malesuada. Ut ac erat tortor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nulla sodales quam sit amet tincidunt egestas. In et turpis at orci vestibulum ullamcorper. Aliquam sed ante libero. Sed hendrerit arcu lacus.

Sau din alt director:

{{< gallery "gallery-2" ""
    "5.jpg|Caption 5.jpg"
>}}