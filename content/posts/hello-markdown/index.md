---
title: A Plain Markdown Post
type: post
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
linkuriExterne:
  res-toml-yaml:
    text: Deep dive into TOML, JSON and YAML
    link: https://gohugohq.com/howto/toml-json-yaml-comparison/
    desc: O scurtă comparaţie între formatele folosite de Hugo pentru front-matter.
  templating-help:
    text: Hugo Translator
    link: https://regisphilibert.com/blog/2017/04/hugo-go-template-translator-explained-understanding/
    desc: Un mic ajutor pentru a înţelege mai bine cum se foloseşte Go în template-urile Hugo, având şi comparaţii cu PHP sau JavaScript.
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

Looks good?
