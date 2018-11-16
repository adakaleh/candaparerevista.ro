---
title: "Introducere în Unreal Engine 4 (II)"
subtitle: "Partea II: Introducere în Blueprints - nivelul de joc"
type: post
date: 2018-11-17
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

description: "Un joc video, spre deosebire de un film, este interactiv. Pentru a realiza mecanicile unui joc în Unreal Engine 4, se poate face programarea cu ajutorul limbajului C++, Blueprints sau amândouă. Blueprints, spre deosebire de C++, este un sistem de scripting vizual. Aceasta înseamnă că dezvoltatorul jocului, în loc să scrie linii de cod într-un document, creează un grafic format din mai multe noduri."

resources:
  - src:
    name: "card-cover-image"

  - src: images/ue4-cover.jpg
    name: "cover-image"
---

>Acest articol e al doilea dintr-o serie de 5 articole. Găsiți aici celelalte părți:

>[Partea I: Introducere. Epic Games Launcher](/posts/2018/11/atelier-introducere-unreal-engine-i-mahri726)

>[Partea III: Introducere în Blueprints - personajele](/posts/2018/11/atelier-introducere-unreal-engine-iii-mahri726)

>[Partea IV: Grafică și Audio](/posts/2018/11/atelier-introducere-unreal-engine-iv-mahri726)

>[Partea V: Împachetarea finală și resurse suplimentare](/posts/2018/11/atelier-introducere-unreal-engine-v-mahri726)

<br>

Un joc video, spre deosebire de un film, este interactiv. Pentru a realiza mecanicile unui joc în Unreal Engine 4, se poate face programarea cu ajutorul limbajului C++, Blueprints sau amândouă. Blueprints, spre deosebire de C++, este un sistem de scripting vizual. Aceasta înseamnă că dezvoltatorul jocului, în loc să scrie linii de cod într-un document, creează un grafic format din mai multe noduri.

Fiecare nod îndeplinește o anumită funcție. Nodurile sunt legate între ele prin fire de execuție. În momentul în care un nod generează un impuls (de exemplu, un nod l-ar putea genera atunci când jucătorul apasă o tastă), acesta se propagă la nodul următor printr-un fir de execuție, de la stânga la dreapta. Când primește impulsul, al doilea nod își activează funcția. Dacă există un al treilea nod conectat la al doilea printr-un fir de execuție, acesta va primi la rândul lui impulsul, după ce îl primește al doilea.

Pentru a putea înțelege mai bine cum funcționează Blueprints-urile, vom încerca să scriptam o lumină care se stinge atunci când detectează jucătorul într-o regiune și se aprinde la loc când pleacă de acolo.

---

În primul rând, din panel-ul **Modes**, vom selecta tabul basic, apoi vom ține apăsat click stânga pe **box trigger** și o vom trage în nivel. O vom scala mai mare, ca să fie mai ușor să detectăm personajul nostru. Asigurați-vă că aveți cutia selectată, apăsați pe butonul **Blueprints** din toolbar, apoi **Open Level Blueprint**. Ţineți apăsat click stânga să selectați cele două noduri existente (**Event BeginPlay** și **Event Tick**), apoi apăsați tasta **Delete**, ca să le ștergeți. Momentan nu avem nevoie de ele.

Apăsați **click dreapta** pe grilă, și va apărea o bară de căutare. Aveți grijă ca bifa **Context sensitive** să fie activată. Dacă nu găsiți un anumit nod, puteți dezactiva bifa. În bara de căutare, scrieți _„Event Overlap”_, apoi selectați **Add On Actor BeginOverlap**. Nodul acesta face următorul lucru: când detectează că jucătorul intră în/se ciocnește de cutie, generează un impuls. În general, nodurile care generează impulsuri se numesc **Events** (evenimente) și sunt de culoare roșie. Deoarece cutia era selectată când am pus nodul, Unreal Engine 4 a detectat automat că ne referim la ea, drept urmare, în cadrul denumirii nodului apare în paranteză numele obiectului selectat.

Hai să facem un mic test, să vedem dacă nodul nostru chiar funcționează. În cadrul nodului, veți observa mai multe săgeți, una albă, și două albastre. Acestea se numesc _pin_-uri. Din cea albă putem trage un singur fir de execuție. țineți apăsat click stânga pe săgeată, apoi trageți firul de execuție spre dreapta. Când eliberați mouse-ul, va apărea din nou bara de căutare. Scrieți în bară _„Print string”_. Selectați opțiunea ca să generați nodul. Unde scrie **In string**, puteți înlocui _„Hello”_ cu ce propoziție vreți.

De fiecare dată când schimbați ceva la grafic, este foarte important să apăsați butonul **Compile** din toolbar. Când apare cu un V verde, înseamnă că graficul vostru e pregătit să fie interpretat de joc.

Închideți fereastra, astfel încât să vedeți nivelul, apoi apăsați **Play**. Dacă butonul Play nu e vizibil, în toolbar există un simbol cu două săgeți spre dreapta. Apăsați-l. Veți vedea că în momentul în care personajul intră în locul unde e cutia, apare mesajul vostru în colțul ecranului.

**Felicitări! Ați realizat primul vostru script cu Blueprints.**

Acum să adăugăm lumina. În panel-ul **Modes** accesați tab-ul **Lights** și trageți în nivel **Point Light**. Cu lumina selectată, deschideți **Level Blueprint**, dați click dreapta în zona graficului, apoi selectați **Create a reference to point light**. Veți vedea că apare un mic nod albastru cu același nume ca și lumina noastră.

{{< figure-multi
    "gallery_1_introducere/1-OcE59CC.jpg||intro_1"
    "gallery_1_introducere/2-jFg3XXm.jpg||intro_2"
    "gallery_1_introducere/3-dml8WEs.jpg||intro_3"
    "gallery_1_introducere/4-KLm1cLv.jpg||intro_4"
    "gallery_1_introducere/5-ftf1OhH.jpg||intro_5"
>}}

Acest nod este reprezentativ pentru lumină, iar efectele exercitate de alte noduri asupra acestuia o vor influența direct.

Până acum, în graficul nostru există 3 tipuri de noduri:

* **Event node** (ex: OnActorBeginOverlap). După cum am mai spus, nodurile _eveniment_ generează impulsuri, în cazul acestui nod, când jucătorul intră în perimetrul cutiei.

* **Function node** (ex: Print String). Nodurile _funcție_ determină o anumită acțiune specifică. Îndeplinesc o funcție. În cazul nostru, când impulsul intră în nodul funcție **Print String  ** se activează un cod din interiorul motorului grafic care afișează pe ecran un anumit text.

* **Variable node** (ex: Point Light). Nodurile de tip _variabilă_ reprezintă o variabilă. Ce este o variabilă? Este o valoare care se poate schimba. Să vă dau un exemplu: Ana ar putea fi o fată care are 3 mere puse pe o masă. Vine fratele ei cu o foaie de hârtie și un creion, începe să îi numere merele Anei, apoi notează pe foaie: `mere = 3`. În cazul acesta, 3 este o variabilă de tip număr întreg iar „mere” este numele variabilei. Dacă îl întreabă cineva pe frate „Câte mere are Ana pe masă?”, acel cineva se referă la variabila numită „mere”. Desigur, Ana poate pune mai multe pe masă, deci numărul lor se poate schimbă. De aici vine numele de „variabilă”.

Variabilele pot fi de mai multe tipuri. `Integer` sau `Int` reprezintă un număr întreg, iar `Float` un număr fracționar, cum ar fi „3,2”. Variabilele pot de asemenea să exprime o condiție (Da sau Nu). Acestea sunt de tip `Boolean`.

În Unreal Engine 4, orice obiect care poate fi plasat într-un nivel, fie model 3D, fie lumină poartă denumirea de Actor. În graficul nostru, **Point Light** este un nod care reprezintă o variabilă de tip `Actor`.

Revenind la dezvoltarea graficului, vom trage un fir de la nodul **Point Light**, vom căuta **Set Visibility (Light Component)** și vom aranja nodurile ca să încapă mai bine. Un **Actor** poate fi alcătuit din mai multe componente. **Light component** este o variabilă de tip `Actor Component`, pe care editorul ne-a adăugat-o automat, deoarece a prevăzut ce vrem să facem. Această componentă emite lumina.

{{< figure  src="gallery_2_introducere/KLm1cLv.jpg" >}}

Observați că firul legat de nodul **Light Component** nu este alb, ci colorat. De asemenea, este mai subțire decât firele de execuție. Acest tip de fir se numește „data wire” sau fir de date. Spre deosebire de firele de execuție, prin firele de date nu circulă impulsuri. Dacă firele de execuție au rolul de a determina un nod să își activeze funcția, firele de date au rolul de a transporta informația de la un nod la altul. În cazul nostru, de la actorul **Point Light** (o lampă) se preia informația legată de **Light Component**, care este sursa luminii (cum ar fi un bec). Informația ajunge la nodul **Set Visibility**, la pin-ul **Target**, adică unde trebuie să ajungă informațiile despre obiectul țintă. Totuși, este o problemă: Atâta vreme cât nodul **Set Visibility** nu este conectat la un fir de execuție, impulsul nu va ajunge niciodată la el, drept urmare nu se va activa. Vom conecta pin-ul **Exec** de la **Print String** la nodul **Set Visibility**. Apăsați butonul **Compile** și închideți fereastra. Apăsați butonul **Play** și testați.

## Cum se deschide o ușă blocată?

_Multe tutoriale de Blueprints pentru începători explică cum să deschizi o ușă. Noi o vom face țăndări. Ușa noastră va fi făcută dintr-un metal cu o grosime considerabilă, drept urmare, ne va trebui explozibil. Pe lângă ușa în sine, vom face țăndări și alte obiecte, astfel încât să putem vorbi despre aranjamente (Arrays)._

Mai întâi, hai să facem ușa casabilă. În content browser, navigați în `Content > Starter Content > Architecture`, apoi dați **click stânga** pe **Wall_500x500**, apoi selectați **Create Destructible Mesh**. Se va deschide o nouă fereastră. Mișcați-vă în viewport, astfel încât să vedeți partea luminată a zidului. În panel-ul din stânga, sub categoria **Voronoi**, aveți posibilitatea să setați în câte bucăți să se spargă ușa (**Cell Site Count**). Eu am setat 30 de bucăți. Apăsați butonul **Fracture Mesh** și folosiți slider-ul **Explode Amount** ca să le previzualizați. Asigurați-vă că bifa **Enable inpact damage** este deselectată și închideți fereastra. Observați că în **Content Browser** avem un nou obiect, **Wall_500x500_DM**. **DM** vine de la „destructible mesh”. Va reprezenta ușa noastră. Selectați-o, și trageți-o în nivel, în continuarea peretelui central. O puteți scala, ca să nu fie găuri între pereți și ușă.

Acum, hai să facem explozibilul. La începutul articolului, am spus că Blueprints reprezintă un sistem de scripting vizual, specific pentru Unreal Engine 4. Pe lângă această semnificație, denumirea de „Blueprint” se referă și la o clasă. Ce este o clasă? Este o noțiune care a apărut acum zeci de ani, odată cu introducerea unui tip de programare numit Object Oriented Programming.

O clasă este un șablon, plan sau set de instrucțiuni care pot duce la crearea unui tip de obiect. Să vă dau un exemplu: un ceasornicar întemeiază o făbricuță de ceasuri și face un plan (_blueprint_) pentru un nou model de ceas, _Nivelul 2_. Toate ceasurile construite de fabrică vor funcționa la fel și se vor numi la fel deoarece au fost construite după același plan. De asemenea, planul pentru construcția ceasului definește și o categorie, în care s-ar încadra toate ceasurile numite Nivelul 2, construite după planul respectiv.

În Unreal Engine 4, poți să creezi astfel de planuri în **Content Browser**. În momentul în care tragi un plan din **Content Browser** în nivel, se crează un obiect care are specificațiile stabilite în plan. Dacă mai tragi încă unul, se crează un al doilea obiect, identic cu primul, deoarece este bazat pe același plan/face parte din aceeaşi clasă. Dacă modifici planul, toate obiectele din joc bazate pe acesta se vor schimba automat, ca să reflecte instrucțiunile sale.

Pentru a face explozibilul, va trebui să creăm un **Actor Blueprint**. În **Content Browser**, apăsați pe folderul **Content**, apoi selectați **New Folder.** Îl vom denumi _„MyAssets”_. Un „asset” reprezintă un model 3D, o textură, o animație, o melodie, un sunet etc, cu alte cuvinte materiile prime pentru dezvoltarea unui joc video.

Vom deschide noul folder, apoi selectăm (sub categoria Create Basic Asset) **Blueprint Class**. Va apărea un meniu cu tipuri de _blueprints_, din care vom alege **Actor Blueprint**. Vom denumi noul Blueprint _„TNT”_, apoi îl vom deschide, cu dublu click.

{{< figure-multi
    "gallery_3_control_distanta/1-M4Bdz4m.jpg||control_1"
    "gallery_3_control_distanta/2-xuqdLN8.jpg||control_2"
>}}

În noua fereastră avem mai multe ferestre. În mijloc avem _viewport_-ul, care ne arată forma obiectului. În colțul din stânga sus, avem panel-ul **Components**. După cum ați văzut când am stins lumina, un actor poate avea mai multe componente. Același lucru se aplică și în cazul **Actor Blueprints**. Mai jos, avem un panel din care putem accesa diferite grafice. În panel-ul **Components** selectați **Add Component**, apoi căutați și adăugați **Radial Force**. Deasupra viewport-ului, sunt 3 tab-uri: **Viewport**, **Construction Script** și **Event Graph**.

Deschideți tabul **Event Graph** și trageți **Radial Force** din panel-ul **Components** în acest grafic. De la noul nod **Radial Force** vom trage un fir de date, apoi vom căuta și adăuga **Fire Impulse**. De la nodul **Event Begin Play**, deja existent în grafic, dar inactiv, vom trage un fir de execuție și vom crea un nou nod, **Delay**. Acesta va induce o întârziere a impulsului. Apoi, vom conecta nodul **Delay** cu nodul **Fire Impulse**. Nodul **Event Begin Play** trimite un impuls când începe jocul. Nodul **Fire Impulse** are rolul de a activa o forță fizică, cum ar fi „radial force”. Cu alte cuvinte, dă foc explozibilului.

Vom selecta **Radial Force** în panel-ul **Components**. În panel-ul **Details** avem trei variabile: sub categoria **Force**, „force strength” iar sub categoria **Destructible**, „destructible damage”, iar sub categoria **Impulse**, „impulse strength”.

Vom seta **destructible damage** la 5, **force strength** la 10 și **impulse strength** la 100. Puteți schimba aceste valori precum și poziția bombei pentru diferite efecte.

Dacă vreți să vedeți un efect vizual al exploziei, atunci vom adăuga **Particle System** în panel-ul **Components**. Îl vom selecta, astfel încât în **Details Panel** să apară informații despre el, apoi, din meniul **Template**, selectăm **P_Explosion**. Vom trage **Particle System** din **Components** în grafic, apoi de la el vom trage un fir de date legat de un nou nod, **Activate**. De la nodul **Fire Impulse**, vom trage un fir de execuție la nodul **Activate**. Vom compila TNT-ul nostru, închidem fereastra, apoi îl vom trage în nivel, chiar lângă ușă. Apăsați butonul **Play** pentru a vedea efectul.

## Control de la distanță

_Până acum, am făcut explozibilul să se detoneze imediat ce începe jocul. Nu este cea mai bună soluție, deoarece jucătorul ar trebui să aibă control asupra momentului detonării acestuia. Cineva spunea că unul dintre cele mai importante elemente care diferențiază un joc bun de unul mediocru este numărul de alegeri pe care le poate face jucătorul. Cred că dacă gradul de interactivitate este redus, atunci este nevoie de elemente compensatorii, cum ar fi povestea. Romanele vizuale precum **Fate: Stay Night** folosesc din plin acest element compensator._

Pentru jocul nostru, va trebui ca impulsul să ajungă de la jucător la explozibil. Pentru asta, vom proceda în felul următor: vom deschide blueprint-ul **TNT**, și vom șterge nodul **Event Begin Play**. Vom adăuga nodul **Custom Event**, îl vom redenumi **Detonează**, apoi îl vom lega la nodul **Delay**. Vom compila, apoi vom închide fereastra.

În **Content Browser**, deschideți folderul **FirstPersonBP**, apoi **Blueprints**, apoi blueprint-ul **First Person Character**. Deoarece am pornit dezvoltarea jocului de la un șablon, avem inclus un blueprint de personaj, gândit pentru shootere first person. În **Event Graph** vom găsi un loc liber apoi vom căuta **F Keyboard** și vom crea nodul „F”. Nodul acesta generează un impuls când apăsați tasta `F`. Este important ca nodurile care necesită o acțiune din partea jucătorului, cum ar fi apăsarea unei taste, să se afle în blueprint-ul personajului pe care îl controlăm, altfel nu vor funcționa.

Acum, din blueprint-ul personajului va trebui să accesăm bomba din nivel. Pentru a face asta, de la pin-ul **Pressed** din cadrul nodului **F** vom trage un fir de execuție și vom crea nodul **Get all actors of class**. Pentru a înțelege mai bine cum funcționează acest nod, voi face o referire la modul în care Unreal Engine 4 redenumește obiectele pe care le plasezi în nivel. În momentul în care tragem același obiect din **Content Browser** de mai multe ori în nivel, editorul redenumeste fiecare copie a acestuia (instanța) cu ajutorul numerelor. De exemplu, când am început dezvoltarea jocului am plasat **Shape_Cube** de câteva ori în nivel pentru a defini pereții încăperii. În **World Outliner** se poate vedea denumirea fiecărei copii: **Shape_Cube**, **Shape_Cube2** și așa mai departe. Nodul **Get All Actors of Class** îi spune motorului grafic să caute toți actorii/toate obiectele din nivel bazate pe un anumit blueprint și să le adauge unui aranjament. Un aranjament (Array) este o colecție de obiecte sau variabile care sunt puse într-o anumită ordine. Această ordine este dictată de un număr numit index.

Apăsați butonul **Select Class** din cadrul nodului apoi căutați și selectați blueprintul **TNT**. Din toate obiectele acestea trebuie să accesăm bomba noastră. Trageți un fir de date de la **Out Actors** din cadrul nodului, apoi căutați și adăugați nodul **Get**.

Nodul **Get** ne va ajuta să accesăm toate informațiile legate de un obiect, folosind indexul pentru a-l identifica. Bomba de lângă ușă este plasată prima, deci va avea indexul 0. De la nodul **Get**, vom trage un fir de execuție și vom căuta și adăuga evenimentul pe care l-am creat anterior în planul bombei, **Detonează**, acum transformat într-o funcție care trimite impulsul la alt blueprint. Vom conecta firul de execuție de la **Get All actors of class** la **Detonează**, apoi vom compila și închide fereastra. După ce apăsăm **Play**, apăsând tasta **F**, zidul ar trebui să se distrugă. Totuși, este o problemă. Imediat ce apăsăm butonul **Play**, efectul de particule al bombei se activează.

Pentru a rezolva această problemă, vom deschide blueprintul TNT (pentru a-l accesa mai rapid, selectați **Edit TNT** din **World Outliner**), vom selecta **Particle System** din tabul **Components**, iar în **Details Panel** deselectam bifa **Auto Activate**, sub categoria **Activation**. Compilăm, închidem fereastra și testăm.

## Hai să detonăm scaune și mese

_Până acum, am făcut o bombă și am detonat o ușă. Acum este timpul pentru aranjamente._

Pentru început, vom crea mai multe obiecte destructibile, în același mod cum am procedat și cu ușa. Puteți să alegeți ce vreți din **Content Browser**. Eu propun „**SM_CHAIR**”, respectiv „**SM_Table Round**”. Vom face din amândouă obiecte destructibile și le vom adăuga în nivel de mai multe ori. Eu am pus 3 scaune și 3 mese.

Lângă fiecare obiect, vom adăuga câte o bombă. Dacă apăsăm **Play**, desigur, se va sparge ușa. Dacă deschidem blueprint-ul personajului nostru (**FirstPersonCharacter**), schimbăm indexul de la nodul **Get** de la 0 la 1 și compilăm, în timpul jocului, când apăsăm **F**, se va distruge obiectul în dreptul căruia se află al doilea **TNT** pus în nivel.

Dar cum să detonăm toate obiectele? În cazul acesta, deschidem blueprint-ul **FirstPersonCharacter**, ștergem nodul **Get**, apoi rupem firul care îl leagă de nodul **Detonează** cu **Alt** - **Click dreapta**. De la pin-ul **Out Actors** tragem un fir de date și căutăm nodul **ForEachLoop**. Următorul pas este să conectăm firele cum vedeți în imaginea de mai jos.

{{< figure-multi
    "gallery_4_detonare/D84c4Qh.jpg||detonare_1"
    "gallery_4_detonare/F6bcraB.jpg||detonare_2"
>}}

Ce reprezintă nodul **For Each Loop**? Este al patrulea tip de nod despre care vom vorbi în aceast atelier, aflat în categoria **Flow Control**. Nodurile din această categorie se folosesc pentru a opri sau dirija impulsurile. Vă voi explica graficul alăturat, deoarece, pentru a înțelege mai bine cum funcționează nodul, trebuie privită imaginea de ansamblu.

La început, apăsăm tasta **F**. Aceasta trimite un impuls la nodul **Get All Actors of Class**, care caută toate obiectele cu numele „TNT” existente în nivel și le pune într-un aranjament. Informațiile legate de elementele aranjamentului sunt transmise la nodul **For Each Loop** printr-un fir de date. În momentul în care un impuls ajunge la nodul **For Each Loop**, acesta accesează informația despre primul element din aranjament și trimite un impuls prin pin-ul **Loop Body**. După aceea, accesează informația despre al doilea element din aranjament, și trimite încă un impuls prin același pin. După ce accesează informația despre ultimul element din aranjament și trimite impulsul prin pin, nodul mai trimite un ultim impuls, însă de dată această prin pinul **Completed**. De remarcat este faptul că atunci când nodul accesează informația despre un element din aranjament, această informație devine disponibilă pentru alte noduri pentru un scurt timp, prin pin-ul **Array Element**.

Această informație poate fi folosită pentru a activa diverse mecanisme, direct în interiorul elementul respectiv. Deoarece sunt copii, în fiecare bombă există un **Custom Event Node**, nodul **Detonează**. În cadrul nodului-funcție **Detonează** din blueprint-ul personajului nostru, putem observa pin-ul **Target**. Prin acest pin, nodul poate afla la ce obiect să trimită impulsul. Cum pinul **Loop Body** din cadrul nodului **For Each Loop** tot va trimite impulsuri până când nu vor mai fi elemente în array la care să nu trimită, toate bombele le vor primi, drept urmare toate se vor detona. ■