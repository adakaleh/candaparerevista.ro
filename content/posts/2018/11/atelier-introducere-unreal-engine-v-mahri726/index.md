---
title: "Introducere în Unreal Engine 4 (V)"
subtitle: "Partea V: Împachetarea finală și resurse suplimentare"
type: post
date: 2018-11-17T00:00:05
authors: mahri726
categories:
    - Atelier
tags:
    - GameDev
    - Unreal Engine

sursa:
   link: https://forum.candaparerevista.ro/viewtopic.php?f=77&t=1469
   text: Articolele Comunității / Nivelul 2 Community Edition - Numărul 2
   data: 2017-02-24

linkForum: https://forum.candaparerevista.ro/viewtopic.php?f=77&t=1469

description: "După ce am terminat dezvoltarea jocului, îl putem împacheta într-un fișier executabil, însă, înainte de asta trebuie să facem câteva modificări. Iar la final vă voi vorbi despre tutoriale și resurse pe care le puteți accesa."

download:
  proiect-1:
    text: Download proiect
    link: https://www.dropbox.com/s/o5gvy0cadxp9zok/Atelier%20UE4%20-%20Nivelul2ShooterBlank.rar?dl=0
    desc: sursa 1 (Dropbox, arhivă)
  proiect-2:
    text: Download proiect
    link: https://1drv.ms/u/s!AoQ2nQcYxvxag2SXtis49ep59hMr
    desc: (OneDrive, arhivă)
  proiect-3:
    text: Download proiect
    link: https://1drv.ms/f/s!AoQ2nQcYxvxabXQmmQJD2koHcN4
    desc: (OneDrive, nearhivat)

resources:
  - src:
    name: "card-cover-image"

  - src: images/ue4-cover.jpg
    name: "cover-image"
---
>Acest articol e ultimul dintr-o serie de 5 articole. Găsiți aici celelalte părți:

>[Partea I: Introducere. Epic Games Launcher](/posts/2018/11/atelier-introducere-unreal-engine-i-mahri726)

>[Partea II: Introducere în Blueprints - nivelul de joc](/posts/2018/11/atelier-introducere-unreal-engine-ii-mahri726)

>[Partea III: Introducere în Blueprints - personajele](/posts/2018/11/atelier-introducere-unreal-engine-iii-mahri726)

>[Partea IV: Grafică și Audio](/posts/2018/11/atelier-introducere-unreal-engine-iv-mahri726)

## Împachetarea finală

_Acum, că am terminat dezvoltarea jocului, îl putem împacheta într-un fișier executabil, însă, înainte de asta trebuie să facem câteva modificări._

În primul rând, este nevoie de o modalitate de a închide jocul. Pentru asta, vom deschide **FirstPerson Character** și vom adaugă nodul **Escape**. Legat de el va fi nodul **Execute Console Command**. Unde scrie **Command**, scrieți _„quit”_.

Este bine ca jucătorul să poată schimba rezoluția în timpul jocului. Pentru asta, vom adăuga tasta evenimentul **1** și vom lega de el un nod cu comanda `r.setRes 1920x1080f`.

Dacă în loc de `f` punem `w`, când se va executa nodul jocul va apărea în fereastră, în loc de full screen. Pentru tasta **2**, am aplicat aceeași comandă pentru rezoluția `640x480`. Compilați și închideți graficul.

Pentru a testa jocul în altă fereastră, apăsați cele două săgeți din toolbar, selectați `Active play mode > New Editor Window` (`PIE`). Acum puteți testa nodurile consolă. Mai este o problemă: când porniți jocul, apare cursorul și trebuie să dați click ca să puteți controla personajul.

Pentru a o rezolva, vom deschide din nou **FirstPerson Blueprint** și vom lega la nodul **Add to Viewport**, **Set Input Mode Game Only**. La pinul liber al acestui nod, vom adăuga **Get Player Controller** și vom compila.

Acum, mergeți la `Edit > Project Settings > Packaging` și selectați la opțiunea **Build Configuration**, **Shipping**. Dacă nu e activată, activați bifele **Use Pak File** și **Include Prerequisites**. „Prerequisites” reprezintă de fapt Visual C++ 2015, un limbaj de programare ce trebuie instalat înainte ca jocul să ruleze. Majoritatea jocurilor includ kitul de instalare C++ chiar în installerul jocului. Bifa **Include Prerequisites** face ca atunci când executabilul jocului este rulat, detectează automat dacă C++ este instalat. Dacă nu, îi pornește installerul.

Un lucru important de care trebuie să țineți cont înainte de împachetare este **list of maps to include in a packaged build**. Dacă nu adăugați aici toate hărțile din joc, editorul va împacheta tot, chiar și modelele nefolosite. Interesul este ca mărimea jocului să fie cât este necesar. Dacă selectați sub categoria **Platforms** opțiunea **Windows**, puteți să îi puneți un icon jocului.

Ultimii pași sunt să închideți fereastra, și să mergeți la `File > Package Project > Windows > Windows` (`32-bit`) sau `Windows` (`64-bit`). Împachetarea inițială poate să dureze câteva ore, însă împachetările ulterioare vor dura în jur de 10 minute.

Asta a fost tot. Aici aveţi şi linkul pentru a [descărca proiectul](https://www.dropbox.com/s/o5gvy0cadxp9zok/Atelier%20UE4%20-%20Nivelul2ShooterBlank.rar?dl=0) din acest articol (alte linkuri sunt în caseta de la sfârșitul articolului).

Sper că v-a plăcut şi aţi găsit informaţii interesante. Dacă aveţi întrebări, vă aştept pe forum.

## Extra 1: Tutoriale și resurse

La final, vă voi vorbi despre tutoriale și resurse pe care le puteți accesa. În cazul tutorialelor, există unele oficiale, făcute chiar de Epic Games. Căutați pe YouTube Massive UE4 Tutorial Playlist. De asemenea, cei de la Epic au și tutoriale care îți explică cum să faci un tip de joc de la 0. Le puteți găsi [aici](docs.unrealengine.com/latest/INT/Videos/). Alte surse de informare la care puteți apela sunt forumurile oficiale [Unreal Engine](https://forums.unrealengine.com/) și [Unreal Engine AnswerHub](https://answers.unrealengine.com/index.html). Resurse gratuite sunt și în tabul Learn al lansatorului. Vă recomand ca la un moment dat să creați proiectul Content Examples. Este ca un muzeu interactiv.În cazul vectorilor, am găsit un blog care îi explică mai pe larg: [Wolfire Blog | Linear algebra for game developers](http://blog.wolfire.com/2009/07/linear-algebra-for-game-developers-part-1/).

Am găsit și un site cu sfaturi de level design: [World of Level Design](https://www.worldofleveldesign.com/). Acolo sunt informații destul de utile. Vă recomand să citiți [How to Plan Level Designs and Game Environments in 11 Steps](https://www.worldofleveldesign.com/categories/level_design_tutorials/how-to-plan-level-designs-game-environments-workflow.php).

După cum observați în această serie de articole, puteți dezvolta jocuri video și fără a folosi calculatorul. Pentru a vă putea crea propriile modele, este bine să știți să desenați ca să puteți face concepte. Am găsit un site cu tutoriale care te învață desen de la 0, numit [drawabox.com](http://drawabox.com/). După ce parcurgeți tutorialele de acolo și decideți să faceți artă digitală, puteți intra pe [ctrlpaint.com](https://www.ctrlpaint.com/). În secțiunea [Free Video Library](https://www.ctrlpaint.com/library/) găsiți foarte multe tutoriale gratuite.

Legat de animație, cei de la Extra Credits, în clipul [So You Want To Be an Animator](https://www.youtube.com/watch?v=YQGaoj7jnBg), recomandă cartea [The Animator's Survival Kit](https://www.amazon.com/gp/product/086547897X). Nu știu cât de bună ar fi.

Ca programe, pe lângă Unreal Engine 4, puteți folosi [Blender](https://www.blender.org/) pentru modelare 3D și [Krita](https://krita.org/en/) ori [GIMP](https://www.gimp.org/) pentru texturi și desen 2D.

O sursă de animații și personaje gratuite este [mixamo.com](https://www.mixamo.com/). Nu știu cât timp vor rămâne gratuite, deci este bine le descărcați cât mai repede. Mixamo au dezvoltat și un program numit [Fuse](https://www.mixamo.com/fuse/1.3/eol), care vă permite să vă creați un personaj ca într-un MMORPG (cu ajutorul sliderelor), apoi să-l exportați în UE4.

Pentru muzică, puteți folosi [REAPER](https://www.reaper.fm/) gratuit timp de 3 luni de zile sau puteți opta pentru opțiunea de mai sus. Un alt soft gratuit este [Audacity](https://www.audacityteam.org/).

## Extra 2: Forumul e în joc

Unreal Engine 4 conține un plugin numit **Web Browser**, ce se poate activa din `Edit > Plugins`. Pluginul acesta vă permite să puneți ferestre de browser în joc cu care jucătorii pot interacționa. De asemenea, titlul paginii poate fi folosit de engine pentru a genera diverse evenimente, cum ar fi deschiderea unei uși secrete ce duce la easter eggs. Cum fiecare thread și pagină din forum are un titlu, vă dați seama de posibilități.

Eu am făcut un script prin care, atunci când detectează că jucătorul intră pe pagina `Surse și resurse pentru proiecte | Proiect personal - Forum`, motorul grafic citeşte titlul paginii și îl compară cu o variabilă de tip text. Pentu a putea interacționa cu forumul, am activat pluginul, am creat un **Widget Blueprint** în care l-am pus, apoi, în blueprintul personajului am adăugat componenta **Widget Interaction Component**. Aceasta componentă trebuie legată de armă, pentru a se roti împreună cu personajul. Pentru asta, țineți apăsat **click stânga** pe aceasta, apoi o trageti deasupra componentei **Sphere** sau **FP_Gun**. Puteti activa si bifa **Show Debug** din **Details Panel**, ca să vă dați seama cum să îi aranjați poziția și unghiul pentru precizie. Am mai creat încă un **Actor Blueprint** al cărui singur rol este să dețină componenta **Widget**, astfel încât forumul să apară în nivel. Mai jos sunt cele două grafice.

{{< figure-multi
    "gallery_1/1.Xgmrsqy.jpg|| "
    "gallery_1/2.H4mVhF2.jpg|| "
>}}

Ca idee, s-ar putea realiza un concurs pe forum, la care participă două sau mai multe echipe care creează fiecare un **Forum Adventure Game**. Aceste jocuri ar putea fi formate dintr-o serie de camere, iar progresul dintr-o cameră în alta se realizează doar dacă un anumit thread din forum este accesat. Camerele pot conține și indicii.

Concursul ar avea două etape: în prima etapă, o echipă încearcă să parcurgă jocul echipei adverse, încercând să îl rezolve. Dacă membrii unei echipe vizitează mai des forumul, au mai multe șanse de câștig. Câteva persoane neutre vor fi desemnate _Hint Givers_. Aceștia vor ști toate secretele. Când o echipă cere un hint, aceasta va fi descalificată cu un punct, iar echipa cu cele mai puține descalificări câștigă. În a două etapă, membrii forumului votează care joc pare mai interesant. Cine are mai multe voturi câștigă. ■