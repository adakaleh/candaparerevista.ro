---
title: "Introducere în Unreal Engine 4 (IV)"
subtitle: "Partea IV: Grafică și Audio"
type: post
date: 2018-11-17T00:00:04
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
description: "Acum, că am terminat partea de programare, putem să ne ocupăm de aspectul jocului. Fiecare obiect din Unreal Engine 4 are la bază un material. Acest material influențează modul în care acesta este vizualizat. Materialele pot avea texturi diferite și grade de reflexie diferită. Noi vom face câteva materiale metalice și câteva materiale care să strălucească."

resources:
  - src:
    name: "card-cover-image"

  - src: images/ue4-cover.jpg
    name: "cover-image"
---
>Acest articol e al patrulea dintr-o serie de 5 articole. Găsiți aici celelalte părți:

>[Partea I: Introducere. Epic Games Launcher](/posts/2018/11/atelier-introducere-unreal-engine-i-mahri726)

>[Partea II: Introducere în Blueprints - nivelul de joc](/posts/2018/11/atelier-introducere-unreal-engine-ii-mahri726)

>[Partea III: Introducere în Blueprints - personajele](/posts/2018/11/atelier-introducere-unreal-engine-iii-mahri726)

>[Partea V: Împachetarea finală și resurse suplimentare](/posts/2018/11/atelier-introducere-unreal-engine-v-mahri726)

<br>

Acum, că am terminat partea de programare, putem să ne ocupăm de aspectul jocului.

## Materiale

_Fiecare obiect din Unreal Engine 4 are la bază un material. Acest material influențează modul în care acesta este vizualizat. Materialele pot avea texturi diferite și grade de reflexie diferită. Noi vom face câteva materiale metalice și câteva materiale care să strălucească._

Pentru a crea un material, apăsați click dreapta în **Content Browser** și selectați **New Material**. După ce îl creați, îi puteți da o denumire. Eu l-am denumit _„metal 1”_. Dacă dați două clickuri pe material, se va deschide **Material Editor**. În centrul ecranului, veți vedea un nod cu mai multe pinuri de intrare. Fiecare pin are un rol în definirea aspectului materialului. Le voi enumera pe cele mai importante:

#### Base Colour

Base colour reprezintă culoarea materialului. Aceasta poate fi și o textură, adică o imagine. Cum poate o imagine să determine aspectul unui material? Pentru a înțelege, voi explica procesul prin care un model 3D poate fi creat.

Modelele 3D se realizează în aplicații speciale precum Maya sau Blender. Un model este alcătuit din puncte numite vertecși, uniți între ei de linii/margini (edges). Minim 3 linii formează o față, numită și poligon. Un ansamblu de fețe formează un model 3D, numit și _„mesh”_.

Cum se texturează un model? Imaginați-vă un cub de hârtie, pe care vreți să îl pictați. Luați o cariocă și îi desenați marginile pe care vreți să le tăiați. După aceea, cu un cutter, le tăiați, astfel încât să întindeți cubul desfăcut pe o masă. Fiind pe o suprafață plană, este foarte ușor să îl pictați. După aceea, îl asamblați la loc și lipiți tăieturile cu scotch.

În procesul de texturare a unui model 3D, marginile marcate pentru tăiat se numesc F sau cusături. După ce se marchează, urmează despachetarea (_unwrapping_). Dacă în spațiul 3D, obiectul se poate mișca pe 3 axe, X,Y și Z, pe „masa 2D” există doar două axe numite U și V.

Feţele obiectului despachetat se vor vedea pe „masă”. Acestea vor fi exportate către un program de pictură digitală, cum ar fi Adobe Photoshop, Gimp sau Krita. Artiștii pictează fețele despăturite, rezultatul fiind o textură care se va „mula” pe modelul 3D.

Cu greutate, am făcut o „poză” capului Elementalului din **Elemental Demo**, ca să vedeți că e făcut din triunghiuri. Când importați un model 3D, Unreal Engine 4 împarte poligoanele în triunghiuri, deoarece sunt mai ușor de interpretat de placa grafică.

{{< figure-multi
    "gallery_materiale/fV4H9Xa.jpg|| "
    "gallery_materiale/EHMif6M.jpg|| "
>}}

<iframe width="560" height="315" src="https://www.youtube.com/embed/dD9CPqSKjTU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

(Apropo, puteți folosi în jocurile voastre orice se află în secțiunile **Learn** și **Marketplace**, cu condiția să nu le exportați către alte motoare grafice.)

#### Metallic

Acest parametru determină dacă obiectul este metalic sau nu.

#### Specular

La fel ca roughness, dar doar pentru obiecte nemetalice. Nu prea se folosește.

#### Roughness

Ce este o oglindă? Este o sticlă care are la suprafață un strat de argint. Față de un obiect mat, oglinda are foarte puține asperități, drept urmare reflexia luminii este foarte bună. În cazul unui obiect mat, atunci când razele de lumină întâlnesc o suprafață aspră cu denivelări, se împrăștie în toate direcțiile. Parametrul **Roughness** determină gradul de reflexie al materialului.

#### Emmisive Colour

Se folosește pentru a face obiectele să strălucească.

#### Normal

O hartă a normalelor, **normal map** este o textură specială folosită pentru a produce denivelări la nivelul suprafeței obiectelor, fără a modifica geometria lor. Fiecare pixel din hartă are o anumită culoare, care se traduce într-o anumită înălțime a pixelului respectiv raportat la suprafață.

Harta normalelor este foarte utilă, deoarece poți adăuga multe detalii minuscule cum ar fi scoarța unui copac, fără să le modelezi.

<br><br>

Pentru a construi materialul, vom căuta nodul **Constant**. Acest nod va avea o anumită valoare, pe care o putem modifica din **Details Panel**. O vom schimba în 1, și vom conecta nodul la pinul **Metallic**. Vom mai face încă un nod **Constant**, îl lăsăm la 0 și îl conectăm la pinul **Roughness**.

Acum, vom adăuga nodul **Constant 3 Vector**, vom da dublu click pe el și îi vom schimba culoarea în gri deschis. Urmează să apăsăm butonul **Apply** și așteptăm ca materialul să se compileze.

Acum, materialul ar trebui să fie ca oglinda. Vom închide fereastra, apoi tragem materialul din **Content Browser** deasupra pereților și așteptăm să se compileze shaderele.

(Am observat că dacă apăsați **Ctrl+Shift+Esc** se deschide **Task Manager** și compilarea e mai rapidă.)

Problema este că pereții devin complet negri când le adăugăm materialul. Pentru a rezolva această problemă, vom căuta în **Modes Panel** elementul **Box Reflection Capture** și îl vom adăuga în nivel de mai multe ori, astfel încât îi acopere pe toți. Acum, vom căuta în **Content Browser** materialul **M_Tech_Hex_Tile_Pulse** și îl vom adăuga la podea.

Următorul pas este să adăugăm materialul metalic și la ușă. Dacă o selectați, veți vedea în **Details Panel** că puteți să îi dați un al doilea material, pentru crăpături. Îl puteți alege pe același.

Acum, putem face inamicii să strălucească. Pentru asta, creați un material și recreați graficul alăturat:

{{< figure  src="gallery_materiale/6YUlx5I.jpg" >}}

Apoi deschideți tabul **Viewport** din blueprintul **ThirdPerson Character**, selectați-l și schimbați materialele din **Details Panel** cu noul material creat. Voi aplica același tratament și la pușcă, și la bila lansată de aceasta.

Ca jocul să arate mai interesant, am selectat cerul apoi am bifat **Actor hidden in game**.

## Sunet și muzică

_Un joc video nu poate fi considerat complet fără sunet. Unul dintre elementele foarte importante pentru pentru atmosferă este muzica. Deoarece pe calculatorul nou nu am instalat niciun program de făcut muzică, m-am gândit să apelez la o soluție web, ca să termin tema jocului cât mai rapid. Aşa am descoperit Soundtrap. Fiind un program web, este mult mai limitat decât programele instalate pe care le foloseam de obicei. Totuși, a fost util. Când Unreal Engine 4 va ajunge la versiunea 4.16, sistemul audio va fi complet schimbat. Deoarece va putea sintetiza și sunete, în unele cazuri, utilizarea programelor externe nu va mai fi necesară._

{{< figure  src="gallery_materiale/993E3bV.jpg" >}}

O melodie are două componente principale: linia melodică și armonia, adică acorduri. Când compui pentru un joc video, poți porni de la o serie de acorduri, apoi adaugi deasupra linia melodică.

În cazul acestei melodii, armonia este alcătuită dintr-un singur acord, _Mi minor_ sub formă arpegiată, adică fiecare notă este apăsată separat, nu împreună.

Unele jocuri au un sistem muzical dinamic, muzica schimbându-se în funcție de acțiunile jucătorului, tranziția fiind atât de lină încât acesta nici nu poate să observe.

Există un video pe YouTube legat de **Squadron 42**, campania singleplayer pentru **Star Citizen**, în care se vorbește tocmai despre un astfel de sistem. Să sperăm că în Unreal Engine 4.16 acest lucru va fi mult mai ușor de realizat.

Unreal Engine 4, în varianta 4.15, poate importa sunete WAV de 16 biți. Pentu a adăuga în proiect un sunet sau o melodie, îl trageți de pe Desktop în **Content Browser**. După import, este recomandat să fie transformat în **Sound Cue**. Ca să faceți asta, dați click dreapta pe sunet și alegeți **Create Cue**. Dacă deschideți acest _cue_, se va deschide un grafic, în care puteți să aplicați diverse efecte audio sunetului.

De asemenea, puteți schimba și volumul acestuia. De îndată ce sunetul a fost transformat în _cue_, acesta poate fi folosit în orice blueprint cu ajutorul nodului **Play Sound 2D**. Pentru a putea rula o melodie nelimitat, acest nod trebuie pus între un **Custom Event** și funcția acestuia. Nodul **Delay** va trebui să aibă exact atâtea secunde cât are melodia, în cazul meu 72 de secunde.

Pentru zgomotul făcut de bombe, am descărcat _Cannon1.wav_ de pe freesound.org. De acolo puteți descărca multe sunete gratuite aflate în domeniul public.

După ce i-am creat un _cue_, va trebui să adăugăm și **Attenuation** în **Content Browser**. Acest asset este folosit pentru a stabili de la ce distanță se vor auzi zgomotele exploziilor, precum și intensitatea acestora în funcție de distanță. Acum, vom deschide _cue_-ul, iar în **Details Panel** vom schimba **Attenuation Settings** în **New Sound Attenuation**, assetul pe care tocmai l-am creat.

Următorul pas este să deschidem blueprintul **TNT** și să adăugăm, după nodul **Activate**, **Play sound at location** legat de **Get actor location**. Ultimul pas este să selectăm _cue_-ul nostru din lista nodului și să compilăm. ■


