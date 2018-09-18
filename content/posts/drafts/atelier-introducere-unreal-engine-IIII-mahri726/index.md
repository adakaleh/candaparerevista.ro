---
title: "Introducere în Unreal Engine 4 (IV)"
subtitle: "Partea IV: Resurse suplimentare și download proiect"
type: post
date: 2018-08-08
authors: mahri726
draft: true
categories:
    - Atelier
tags:
    - GameDev
    - Unreal Engine

sursa:
   link: https://forum.candaparerevista.ro/viewtopic.php?f=77&t=1290
   text: Articolele Comunității / Nivelul 2 Community Edition - Numărul 2
   data: 2017-02-24

linkForum: https://forum.candaparerevista.ro/viewtopic.php?f=77&t=1290

resources:
  - src:
    name: "card-cover-image"

  - src: images/ue4-cover.jpg
    name: "cover-image"
---

{{% aside %}}
## TODO
* De adăugat linkuri către celelalte articole.
* De formatat text şi adăugat linkuri.
* De adăugat download proiect.
{{% /aside %}}

>Acest articol e ultimul dintr-o serie de 4 articole. Găsiți aici celelalte părți:

>* Partea I: Introducere. Epic Games Launcher
>* Partea II: Introducere în Blueprints
>* Partea III: Grafică și Audio


## Extra 1: Tutoriale și resurse

La final, vă voi vorbi despre tutoriale și resurse pe care le puteți accesa. În cazul tutorialelor, există unele oficiale, făcute chiar de Epic Games. Căutați pe YouTube Massive UE4 Tutorial Playlist. De asemenea, cei de la Epic au și tutoriale care îți explică cum să faci un tip de joc de la 0. Le puteți găsi aici: docs.unrealengine.com/latest/INT/Videos/. Alte surse de informare la care puteți apela sunt forumurile oficiale Unreal Engine și Unreal Engine AnswerHub. Resurse gratuite sunt și în tabul Learn al lansatorului. Vă recomand ca la un moment dat să creați proiectul Content Examples. Este ca un muzeu interactiv.În cazul vectorilor, am găsit un blog care îi explică mai pe larg: Wolfire Blog | Linear algebra for game developers.

Am găsit și un site cu sfaturi de level design: World of Level Design. Acolo sunt informații destul de utile. Vă recomand să citiți How to Plan Level Designs and Game Environments in 11 Steps.

După cum observați în articol, puteți dezvolta jocuri video și fără a folosi calculatorul. Pentru a vă putea crea propriile modele, este bine să știți să desenați ca să puteți face concepte. Am găsit un site cu tutoriale care te învață desen de la 0, numit drawabox.com. După ce parcurgeți tutorialele de acolo și decideți să faceți artă digitală, puteți intra pe ctrlpaint.com. În secțiunea Free Video Library găsiți foarte multe tutoriale gratuite.

Legat de animație, cei de la Extra Credits, în clipul So You Want To Be an Animator, recomandă cartea The Animator’s Survival Kit. Nu știu cât de bună ar fi.

Ca programe, pe lângă Unreal Engine 4, puteți folosi Blender pentru modelare 3D și Krita ori Gimp pentru texturi și desen 2D.

O sursă de animații și personaje gratuite este mixamo.com. Nu știu cât timp vor rămâne gratuite, deci este bine le descărcați cât mai repede. Mixamo au dezvoltat și un program numit Fuse, care vă permite să vă creați un personaj ca într-un MMORPG (cu ajutorul sliderelor), apoi să-l exportați în UE4.

Pentru muzică, puteți folosi Reaper gratuit timp de 3 luni de zile sau puteți opta pentru opțiunea de mai sus. Un alt soft gratuit este Audacity.


## Extra 2: Forumul e în joc

Unreal Engine 4 conține un plugin numit Web Browser, ce se poate activa din Edit>Plugins. Pluginul acesta vă permite să puneți ferestre de browser în joc cu care jucătorii pot interacționa. De asemenea, titlul paginii poate fi folosit de engine pentru a genera diverse evenimente, cum ar fi deschiderea unei uși secrete ce duce la easter eggs. Cum fiecare thread și pagină din forumul Nivelul2 are un titlu, vă dați seama de posibilități.

Eu am făcut un script prin care, atunci când detectează că jucătorul intră pe pagina Surse și resurse pentru proiecte | Proiect personal - Forum Nivelul 2, motorul grafic citeşte titlul paginii și îl compară cu o variabilă de tip text. Pentu a putea interacționa cu forumul, am activat pluginul, am creat un Widget Blueprint în care l-am pus, apoi, în blueprintul personajului am adăugat componenta Widget Interaction Component. Aceasta componentă trebuie legată de armă, pentru a se roti împreună cu personajul. Pentru asta, țineți apăsat click stânga pe aceasta, apoi o trageti deasupra componentei Sphere sau FP_Gun. Puteti activa si bifa Show Debug din Details Panel, ca să vă dați seama cum să îi aranjați poziția și unghiul pentru precizie. Am mai creat încă un Actor Blueprint al cărui singur rol este să dețină componenta Widget, astfel încât forumul să apară în nivel. Mai jos sunt cele două grafice.

Ca idee, s-ar putea realiza un concurs pe forum, la care participă două sau mai multe echipe care creează fiecare un Forum Adventure Game. Aceste jocuri ar putea fi formate dintr-o serie de camere, iar progresul dintr-o cameră în alta se realizează doar dacă un anumit thread din forum este accesat. Camerele pot conține și indicii.

Concursul ar avea două etape: în prima etapă, o echipă încearcă să parcurgă jocul echipei adverse, încercând să îl rezolve. Dacă membrii unei echipe vizitează mai des forumul, au mai multe șanse de câștig. Câteva persoane neutre vor fi desemnate Hint Givers. Aceștia vor ști toate secretele. Când o echipă cere un hint, aceasta va fi descalificată cu un punct, iar echipa cu cele mai puține descalificări câștigă. În a două etapă, membrii forumului votează care joc pare mai interesant. Cine are mai multe voturi câștigă. ■