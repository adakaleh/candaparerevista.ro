---
title: "Introducere în Unreal Engine 4 (II)"
subtitle: "Partea II: Introducere în Blueprints"
type: post
date: 2018-08-08
authors: mahri726
draft: true
categories:
    - Atelier
    - GameDev
tags:
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

>Acest articol e partea a doua dintr-o serie de 4 articole. Găsiți aici celelalte articole:

>* Partea I: Introducere. Epic Games Launcher
>* Partea III: Grafică și Audio
>* Partea IV: Resurse Suplimentare și Extra


Un joc video, spre deosebire de un film, este interactiv. Pentru a realiza mecanicile unui joc în Unreal Engine 4, se poate face programarea cu ajutorul limbajului C++, Blueprints sau amândouă. Blueprints, spre deosebire de C++, este un sistem de scripting vizual. Aceasta înseamnă că dezvoltatorul jocului, în loc să scrie linii de cod într-un document, creează un grafic format din mai multe noduri.

Fiecare nod îndeplinește o anumită funcție. Nodurile sunt legate între ele prin fire de execuție. În momentul în care un nod generează un impuls (de exemplu, un nod l-ar putea genera atunci când jucătorul apasă o tastă), acesta se propagă la nodul următor printr-un fir de execuție, de la stânga la dreapta. Când primește impulsul, al doilea nod își activează funcția. Dacă există un al treilea nod conectat la al doilea printr-un fir de execuție, acesta va primi la rândul lui impulsul, după ce îl primește al doilea.

Pentru a putea înțelege mai bine cum funcționează Blueprints-urile, vom încerca să scriptam o lumină care se stinge atunci când detectează jucătorul într-o regiune și se aprinde la loc când pleacă de acolo.

În primul rând, din panel-ul Modes, vom selecta tabul basic, apoi vom ține apăsat click stânga pe box trigger și o vom trage în nivel. O vom scala mai mare, ca să fie mai ușor să detectăm personajul nostru. Asigurați-vă că aveți cutia selectată, apăsați pe butonul Blueprints din toolbar, apoi Open Level Blueprint. Ţineți apăsat click stânga să selectați cele două noduri existente (Event BeginPlay și Event Tick), apoi apăsați tasta Delete, ca să le ștergeți. Momentan nu avem nevoie de ele.

Apăsați click dreapta pe grilă, și va apărea o bară de căutare. Aveți grijă ca bifa Context sensitive să fie activată. Dacă nu găsiți un anumit nod, puteți dezactiva bifa. În bara de căutare, scrieți „Event Overlap”, apoi selectați Add On Actor BeginOverlap. Nodul acesta face următorul lucru: când detectează că jucătorul intră în/se ciocnește de cutie, generează un impuls. În general, nodurile care generează impulsuri se numesc Events (evenimente) și sunt de culoare roșie. Deoarece cutia era selectată când am pus nodul, Unreal Engine 4 a detectat automat că ne referim la ea, drept urmare, în cadrul denumirii nodului apare în paranteză numele obiectului selectat.

Hai să facem un mic test, să vedem dacă nodul nostru chiar funcționează. În cadrul nodului, veți observa mai multe săgeți, una albă, și două albastre. Acestea se numesc pin-uri. Din cea albă putem trage un singur fir de execuție. țineți apăsat click stânga pe săgeată, apoi trageți firul de execuție spre dreapta. Când eliberați mouse-ul, va apărea din nou bara de căutare. Scrieți în bară „Print string”. Selectați opțiunea ca să generați nodul. Unde scrie In string, puteți înlocui „Hello” cu ce propoziție vreți.

De fiecare dată când schimbați ceva la grafic, este foarte important să apăsați butonul Compile din toolbar. Când apare cu un V verde, înseamnă că graficul vostru e pregătit să fie interpretat de joc.

Închideți fereastra, astfel încât să vedeți nivelul, apoi apăsați Play. Dacă butonul Play nu e vizibil, în toolbar există un simbol cu două săgeți spre dreapta. Apăsați-l. Veți vedea că în momentul în care personajul intră în locul unde e cutia, apare mesajul vostru în colțul ecranului.

Felicitări! Ați realizat primul vostru script cu Blueprints.



Acum să adăugăm lumina. În panel-ul Modes accesați tab-ul Lights și trageți în nivel Point Light. Cu lumina selectată, deschideți Level Blueprint, dați click dreapta în zona graficului, apoi selectați Create a reference to point light. Veți vedea că apare un mic nod albastru cu același nume ca și lumina noastră.

Acest nod este reprezentativ pentru lumină, iar efectele exercitate de alte noduri asupra acestuia o vor influența direct.



Până acum, în graficul nostru există 3 tipuri de noduri:

* Event node (ex: OnActorBeginOverlap)

După cum am mai spus, nodurile eveniment generează impulsuri, în cazul acestui nod, când jucătorul intră în perimetrul cutiei.

* Function node (ex: Print String)

Nodurile funcție determină o anumită acțiune specifică. Îndeplinesc o funcție. În cazul nostru, când impulsul intră în nodul funcție Print String  se activează un cod din interiorul motorului grafic care afișează pe ecran un anumit text.

* Variable node (ex: Point Light)

Nodurile de tip variabilă reprezintă o variabilă. Ce este o variabilă? Este o valoare care se poate schimba. Să vă dau un exemplu: Ana ar putea fi o fată care are 3 mere puse pe o masă. Vine fratele ei cu o foaie de hârtie și un creion, începe să îi numere merele Anei, apoi notează pe foaie: mere=3. În cazul acesta, 3 este o variabilă de tip număr întreg iar „mere” este numele variabilei. Dacă îl întreabă cineva pe frate „Câte mere are Ana pe masă?”, acel cineva se referă la variabila numită „mere”. Desigur, Ana poate pune mai multe pe masă, deci numărul lor se poate schimbă. De aici vine numele de „variabilă”.

Variabilele pot fi de mai multe tipuri. Integer sau Int reprezintă un număr întreg, iar Float un număr fracționar, cum ar fi 3,2. Variabilele pot de asemenea să exprime o condiție (Da sau Nu). Acestea sunt de tip Boolean.

În Unreal Engine 4, orice obiect care poate fi plasat într-un nivel, fie model 3D, fie lumină poartă denumirea de Actor. În graficul nostru, Point Light este un nod care reprezintă o variabilă de tip Actor.



Revenind la dezvoltarea graficului, vom trage un fir de la nodul Point Light, vom căuta Set Visibility (Light Component) și vom aranja nodurile ca să încapă mai bine. Un Actor poate fi alcătuit din mai multe componente. Light component este o variabilă de tip Actor Component, pe care editorul ne-a adăugat-o automat, deoarece a prevăzut ce vrem să facem. Această componentă emite lumina.

Observați că firul legat de nodul Light Component nu este alb, ci colorat. De asemenea, este mai subțire decât firele de execuție. Acest tip de fir se numește „data wire” sau fir de date. Spre deosebire de firele de execuție, prin firele de date nu circulă impulsuri. Dacă firele de execuție au rolul de a determina un nod să își activeze funcția, firele de date au rolul de a transporta informația de la un nod la altul. În cazul nostru, de la actorul Point Light (o lampă) se preia informația legată de Light Component, care este sursa luminii (cum ar fi un bec). Informația ajunge la nodul Set Visibility, la pin-ul Target, adică unde trebuie să ajungă informațiile despre obiectul țintă. Totuși, este o problemă: Atâta vreme cât nodul Set Visibility nu este conectat la un fir de execuție, impulsul nu va ajunge niciodată la el, drept urmare nu se va activa. Vom conecta pin-ul Exec de la Print String la nodul Set Visibility. Apăsați butonul Compile și închideți fereastra. Apăsați butonul Play și testați.



------

Cum se deschide o ușă blocată ?

Multe tutoriale de Blueprints pentru începători explică cum să deschizi o ușă. Noi o vom face țăndări. Ușa noastră va fi făcută dintr-un metal cu o grosime considerabilă, drept urmare, ne va trebui explozibil. Pe lângă ușa în sine, vom face țăndări și alte obiecte, astfel încât să putem vorbi despre aranjamente (Arrays).

------



Mai întâi, hai să facem ușa casabilă. În content browser, navigați în Content>Starter Content>Architecture, apoi dați click stânga pe Wall_500x500, apoi selectați Create Destructible Mesh. Se va deschide o nouă fereastră. Mișcați-vă în viewport, astfel încât să vedeți partea luminată a zidului. În panel-ul din stânga, sub categoria Voronoi, aveți posibilitatea să setați în câte bucăți să se spargă ușa (Cell Site Count). Eu am setat 30 de bucăți. Apăsați butonul Fracture Mesh și folosiți slider-ul Explode Amount ca să le previzualizați. Asigurați-vă că bifa Enable inpact damage este deselectată și închideți fereastra. Observați că în Content Browser avem un nou obiect, Wall_500x500_DM. DM vine de la „destructible mesh”. Va reprezenta ușa noastră. Selectați-o, și trageți-o în nivel, în continuarea peretelui central. O puteți scala, ca să nu fie găuri între pereți și ușă.

Acum, hai să facem explozibilul. La începutul articolului, am spus că Blueprints reprezintă un sistem de scripting vizual, specific pentru Unreal Engine 4. Pe lângă această semnificație, denumirea de „Blueprint” se referă și la o clasă. Ce este o clasă? Este o noțiune care a apărut acum zeci de ani, odată cu introducerea unui tip de programare numit Object Oriented Programming.

O clasă este un șablon, plan sau set de instrucțiuni care pot duce la crearea unui tip de obiect. Să vă dau un exemplu: un ceasornicar întemeiază o făbricuță de ceasuri și face un plan (blueprint) pentru un nou model de ceas, Nivelul 2. Toate ceasurile construite de fabrică vor funcționa la fel și se vor numi la fel deoarece au fost construite după același plan. De asemenea, planul pentru construcția ceasului definește și o categorie, în care s-ar încadra toate ceasurile numite Nivelul 2, construite după planul respectiv.

În Unreal Engine 4, poți să creezi astfel de planuri în Content Browser. În momentul în care tragi un plan din Content Browser în nivel, se crează un obiect care are specificațiile stabilite în plan. Dacă mai tragi încă unul, se crează un al doilea obiect, identic cu primul, deoarece este bazat pe același plan/face parte din aceeaşi clasă. Dacă modifici planul, toate obiectele din joc bazate pe acesta se vor schimba automat, ca să reflecte instrucțiunile sale.

Pentru a face explozibilul, va trebui să creăm un Actor Blueprint. În Content Browser, apăsați pe folderul Content, apoi selectați New Folder. Îl vom denumi „MyAssets”. Un „asset” reprezintă un model 3D, o textură, o animație, o melodie, un sunet etc, cu alte cuvinte materiile prime pentru dezvoltarea unui joc video.

Vom deschide noul folder, apoi selectăm (sub categoria Create Basic Asset) Blueprint Class. Va apărea un meniu cu tipuri de blueprints, din care vom alege Actor Blueprint. Vom denumi noul Blueprint „TNT”, apoi îl vom deschide, cu dublu click.

În noua fereastră avem mai multe ferestre. În mijloc avem viewport-ul, care ne arată forma obiectului. În colțul din stânga sus, avem panel-ul Components. După cum ați văzut când am stins lumina, un actor poate avea mai multe componente. Același lucru se aplică și în cazul Actor Blueprints. Mai jos, avem un panel din care putem accesa diferite grafice. În panel-ul Components selectați Add Component, apoi căutați și adăugați Radial Force. Deasupra viewport-ului, sunt 3 tab-uri: Viewport, Construction Script și Event Graph.

Deschideți tabul Event Graph și trageți Radial Force din panel-ul Components în acest grafic. De la noul nod Radial Force vom trage un fir de date, apoi vom căuta și adăuga Fire Impulse. De la nodul Event Begin Play, deja existent în grafic, dar inactiv, vom trage un fir de execuție și vom crea un nou nod, Delay. Acesta va induce o întârziere a impulsului. Apoi, vom conecta nodul Delay cu nodul Fire Impulse. Nodul Event Begin Play trimite un impuls când începe jocul. Nodul Fire Impulse are rolul de a activa o forță fizică, cum ar fi „radial force”. Cu alte cuvinte, dă foc explozibilului.

Vom selecta Radial Force în panel-ul Components. În panel-ul Details avem trei variabile: sub categoria Force, „force strength” iar sub categoria Destructible, „destructible damage”, iar sub categoria Impulse, „impulse strength”.

Vom seta destructible damage la 5, force strength la 10 și impulse strength la 100. Puteți schimba aceste valori precum și poziția bombei pentru diferite efecte.

Dacă vreți să vedeți un efect vizual al exploziei, atunci vom adăuga Particle System în panel-ul Components. Îl vom selecta, astfel încât în Details Panel să apară informații despre el, apoi, din meniul Template, selectăm P_Explosion. Vom trage Particle System din Components în grafic, apoi de la el vom trage un fir de date legat de un nou nod, Activate. De la nodul Fire Impulse, vom trage un fir de execuție la nodul Activate. Vom compila TNT-ul nostru, închidem fereastra, apoi îl vom trage în nivel, chiar lângă ușă. Apăsați butonul Play pentru a vedea efectul.





------

Control de la distanță

Până acum, am făcut explozibilul să se detoneze imediat ce începe jocul. Nu este cea mai bună soluție, deoarece jucătorul ar trebui să aibă control asupra momentului detonării acestuia. Cineva spunea că unul dintre cele mai importante elemente care diferențiază un joc bun de unul mediocru este numărul de alegeri pe care le poate face jucătorul. Cred că dacă gradul de interactivitate este redus, atunci este nevoie de elemente compensatorii, cum ar fi povestea. Romanele vizuale precum Fate: Stay Night folosesc din plin acest element compensator.

Pentru jocul nostru, va trebui ca impulsul să ajungă de la jucător la explozibil. Pentru asta, vom proceda în felul următor: vom deschide blueprint-ul TNT, și vom șterge nodul Event Begin Play. Vom adăuga nodul Custom Event, îl vom redenumi Detonează, apoi îl vom lega la nodul Delay. Vom compila, apoi vom închide fereastra.

------



În Content Browser, deschideți folderul FirstPersonBP, apoi Blueprints, apoi blueprint-ul First Person Character. Deoarece am pornit dezvoltarea jocului de la un șablon, avem inclus un blueprint de personaj, gândit pentru shootere first person. În Event Graph vom găsi un loc liber apoi vom caută F Keyboard și vom crea nodul „F”. Nodul acesta generează un impuls când apăsați tasta F. Este important ca nodurile care necesită o acțiune din partea jucătorului, cum ar fi apăsarea unei taste, să se afle în blueprint-ul personajului pe care îl controlăm, altfel nu vor funcționa.

Acum, din blueprint-ul personajului va trebui să accesăm bomba din nivel. Pentru a face asta, de la pin-ul Pressed din cadrul nodului F vom trage un fir de execuție și vom crea nodul Get all actors of class. Pentru a înțelege mai bine cum funcționează acest nod, voi face o referire la modul în care Unreal Engine 4 redenumește obiectele pe care le plasezi în nivel. În momentul în care tragem același obiect din Content Browser de mai multe ori în nivel, editorul redenumeste fiecare copie a acestuia (instanța) cu ajutorul numerelor. De exemplu, când am început dezvoltarea jocului am plasat Shape_Cube de câteva ori în nivel pentru a defini pereții încăperii. În World Outliner se poate vedea denumirea fiecărei copii: Shape_Cube, Shape_Cube2 și așa mai departe. Nodul Get All Actors of Class îi spune motorului grafic să caute toți actorii/toate obiectele din nivel bazate pe un anumit blueprint și să le adauge unui aranjament. Un aranjament (Array) este o colecție de obiecte sau variabile care sunt puse într-o anumită ordine. Această ordine este dictată de un număr numit index.

Apăsați butonul Select Class din cadrul nodului apoi căutați și selectați blueprintul TNT. Din toate obiectele acestea trebuie să accesăm bomba noastră. Trageți un fir de date de la Out Actors din cadrul nodului, apoi căutați și adăugați nodul Get.

Nodul Get ne va ajuta să accesăm toate informațiile legate de un obiect, folosind indexul pentru a-l identifica. Bomba de lângă ușă este plasată prima, deci va avea indexul 0. De la nodul Get, vom trage un fir de execuție și vom căuta și adăuga evenimentul pe care l-am creat anterior în planul bombei, Detonează, acum transformat într-o funcție care trimite impulsul la alt blueprint. Vom conecta firul de execuție de la Get All actors of class la Detonează, apoi vom compila și închide fereastra. După ce apăsăm Play, apăsând tasta F, zidul ar trebui să se distrugă. Totuși, este o problemă. Imediat ce apăsăm butonul Play, efectul de particule al bombei se activează.

Pentru a rezolva această problemă, vom deschide blueprintul TNT (pentru a-l accesa mai rapid, selectați Edit TNT din World Outliner), vom selecta Particle System din tabul Components, iar în Details Panel deselectam bifa Auto Activate, sub categoria Activation. Compilăm, închidem fereastra și testăm.



-------

Hai să detonăm scaune și mese

Până acum, am făcut o bombă și am detonat o ușă. Acum este timpul pentru aranjamente.

-------



Pentru început, vom crea mai multe obiecte destructibile, în același mod cum am procedat și cu ușa. Puteți să alegeți ce vreți din Content Browser. Eu propun „SM_CHAIR”, respectiv „SM_Table Round”. Vom face din amândouă obiecte destructibile și le vom adăuga în nivel de mai multe ori. Eu am pus 3 scaune și 3 mese.

Lângă fiecare obiect, vom adăuga câte o bombă. Dacă apăsăm Play, desigur, se va sparge ușa. Dacă deschidem blueprint-ul personajului nostru (FirstPersonCharacter), schimbăm indexul de la nodul Get de la 0 la 1 și compilăm, în timpul jocului, când apăsăm F, se va distruge obiectul în dreptul căruia se află al doilea TNT pus în nivel.

Dar cum să detonăm toate obiectele? În cazul acesta, deschidem blueprint-ul FirstPersonCharacter, ștergem nodul Get, apoi rupem firul care îl leagă de nodul Detonează cu Alt-Click dreapta. De la pin-ul Out Actors tragem un fir de date și căutăm nodul ForEachLoop. Următorul pas este să conectăm firele cum vedeți în imaginea alăturată.

Ce reprezintă nodul For Each Loop ? Este al patrulea tip de nod despre care vom vorbi în aceast atelier, aflat în categoria Flow Control. Nodurile din această categorie se folosesc pentru a opri sau dirija impulsurile. Vă voi explica graficul alăturat, deoarece, pentru a înțelege mai bine cum funcționează nodul, trebuie privită imaginea de ansamblu.

La început, apăsăm tasta F. Aceasta trimite un impuls la nodul Get All Actors of Class, care caută toate obiectele cu numele „TNT” existente în nivel și le pune într-un aranjament. Informațiile legate de elementele aranjamentului sunt transmise la nodul For Each Loop printr-un fir de date. În momentul în care un impuls ajunge la nodul For Each Loop, acesta accesează informația despre primul element din aranjament și trimite un impuls prin pin-ul Loop Body. După aceea, accesează informația despre al doilea element din aranjament, și trimite încă un impuls prin același pin. După ce accesează informația despre ultimul element din aranjament și trimite impulsul prin pin, nodul mai trimite un ultim impuls, însă de dată această prin pinul Completed. De remarcat este faptul că atunci când nodul accesează informația despre un element din aranjament, această informație devine disponibilă pentru alte noduri pentru un scurt timp, prin pin-ul Array Element.

Această informație poate fi folosită pentru a activa diverse mecanisme, direct în interiorul elementul respectiv. Deoarece sunt copii, în fiecare bombă există un Custom Event Node, nodul Detonează. În cadrul nodului-funcție Detonează din blueprint-ul personajului nostru, putem observa pin-ul Target. Prin acest pin, nodul poate afla la ce obiect să trimită impulsul. Cum pinul Loop Body din cadrul nodului For Each Loop tot va trimite impulsuri până când nu vor mai fi elemente în array la care să nu trimită, toate bombele le vor primi, drept urmare toate se vor detona.



------

Cum să efectuăm o scădere fatală?

În seria de jocuri Half-Life, personajul principal, Gordon Freeman, avea un costum menit să îl protejeze de diverse pericole: radiații, acid, electricitate sau extratereștri. Costumul avea o proprietate specială: îl punea pe jucător să aibă grijă de o variabilă numită „HP”. Când atingea pragul 0, Gordon murea.

Desigur, conceptul de Hit Points a apărut mult mai devreme, când jocuri tabletop precum Dungeons and Dragons își făceau debutul. Noi vom implementa o astfel de variabilă, a cărei valoare poate fi interpretată de jucător printr-o cifră afișată pe ecran. Inițial, aceasta va scădea atunci când jucătorul apasă o tastă.

------

Pentru a crea variabila, vom deschide blueprint-ul FirstPersonCharacter, iar în panelul My Blueprint apăsați butonul verde Add New, apoi selectați din meniu Variable. Vom numi variabila „Sănătate”.

Lângă numele variabilei, puteți observa o culoare. Dacă apăsați culoarea respectivă, veți putea schimba tipul variabilei. O vom schimba în Integer. Ţineți apăsat click stânga pe ea, apoi o trageți într-un loc liber în grafic; va apărea un meniu cu două opțiuni, din care selectați Get. Apăsați butonul Compile, iar dacă nodul ei este selectat, în Details Panel veți vedea sub tabul Default Value că are valoarea 0. Schimbați valoarea la 10. Pentru a o face să scadă, în primul rând adăugați un nod eveniment, cum ar fi cel pentru tasta G, care inițiază impulsul. De la nodul variabilei Sănătate vom trage un fir de date, scriem „–” în bara de căutare și selectăm „integer–integer”. În mod normal, ar trebui ca valoarea nodului din dreptul pinului al doilea să fie 1.

Din tabul My Blueprint vom trage din nou variabila în grafic, dar de data aceasta vom selecta din meniu Set în loc de Get. Urmează să conectăm firul de execuție de la nodul G la nodul Set și firul de date de la rezultatul scăderii în pinul acestuia. Ca să vedem scăderea pe ecran, vom trage de la pinul de execuție al nodului Set un fir și vom adaugă Print String. De la pinul turcoaz al nodului Set, vom trage un fir de date la pinul roz al nodului Print String. Motorul grafic va adăuga automat un nod care să convertească variabila de tip integer în variabilă de tip string (șir de caractere). Vom compila și vom testa. De fiecare dată când apăsăm G, variabila Sănătate ar trebui să scadă cu 1.

Acum, vom vrea ca atunci când variabila ajunge la valoarea 0, personajul să moară. O modalitate simplă pentru a produce moartea personajului este ca nivelul să se reîncarce. Pentru asta, vom deschide din nou blueprint-ul personajului și vom trage un fir de date de la pinul nodului Set, vom căuta „=” și vom selecta „integer <= integer”. Noul nod face comparația dintre valoarea variabilei noastre și o altă variabilă, apoi oferă ca rezultat informație de tip Boolean, adică spune dacă primul număr este mai mic sau egal cu al doilea sau nu.

Această informație ne va fi utilă pentru a putea opri impulsul, dacă condiția se adeverește. Pentru aceasta, vom trage un fir de execuție de la nodul Print String, apoi vom adăuga nodul Branch. Acesta este al patrulea tip de nod despre care vă vorbesc în acest atelier, aparținând categoriei Flow Control.

Vom conecta pinul nodului comparator la pinul Condition al acestui nod. De la pinul de execuție True vom adăuga nodul Get Current Level Name apoi, legat de acesta, Open Level. Următoarele lucruri pe care le vom face vor fi să conectăm firul de la pinul Return Value la Level Name să compilăm și să testăm.



------

UMG

Acum, că am scriptat un sistem care să scadă sănătatea personajului, jucătorul ar trebui să vadă acest efect. Print String se folosește doar pentru teste, nu pentru jocuri finale, deci va trebui să afișăm punctele de viață așa cum trebuie. Pentru asta, vom folosi editorul de interfață (UI) inclus în Unreal Engine 4 numit Unreal Motion Graphics sau UMG. UMG ne permite să punem butoane, meniuri, bare de viață sau alte elemente 2D care îi pot oferi informații jucătorului despre starea jocului.

-------



Pentru a începe să folosim UMG, trebuie mai întâi să creăm un plan pentru un widget. Un widget este ca un fel de pânză, pe care putem aranja elementele de interfață. Pentru a crea un plan de widget, dați click dreapta în Content Browser, mergeți în categoria UI/User Interface (s-ar putea să fie nevoie să dați scroll ca să o vedeți, mai ales dacă folosiți versiuni mai vechi ale motorului) și selectați Widget Blueprint. O putem numi „Interfață”. Dacă dați două click-uri pe aceasta se va deschide UMG.

UMG are două tab-uri, Designer și Graph. În Designer puteți aranja elementele de interfață iar în Graph le scriptați. Pentru a afișa punctele de viață, va trebui să tragem din panelul Palette categoria Common, elementul Text. Cu textul selectat, vom observa că putem face niște setări în Details panel. Sub Content vom schimba conținutul textului în „+”, vom seta mărimea fontului 50 apoi vom scala căsuța în care este situat acesta astfel încât să cuprindă doar plusul.

Un lucru important în UMG este ancorarea elementelor. Ancorarea se face din meniul Anchors. Dacă selectați opțiunea potrivită, textul se va vedea în aceiași locație indiferent de rezoluția ecranului. Este bine să puneți ancora în colțul unde se află textul.

Lângă plusul nostru vom adăuga încă un element de tip text, pe care îl vom numi XX. Numele acesta este pus doar provizoriu, pentru a putea aranja textul mai bine. În timpul rulării jocului, va fi înlocuit de cifrele corespunzătoare variabilei Sănătate. Este bine ca bifa Is Variable să fie activată astfel încât textul să poate fi accesat de alte noduri, precum cele de schimbare a vizibilității. Următorul pas este să apăsăm butonul Bind de lângă Text (din categoria Content) și să selectăm Create binding. Motorul grafic va crea o funcție (GetText_0) și va deschide o fereastră astfel încât să o putem edita.

Din interiorul funcției, putem accesa variabila Sănătate aflată în blueprint-ul personajului în două moduri: fie folosim nodurile Get all actors of class și Get așa cum am făcut anterior în cazul bombelor, sau putem folosi nodurile Get Player Character și Cast To FirstPersonCharacter.

Nodul Cast To FirstPersonCharacter are rolul de a face o verificare. Dacă blueprintul FirstPersonCharacter este chiar personajul controlat de jucător (Player Character), atunci acesta poate fi accesat. De asemenea, atunci când e activat, nodul poate trimite impulsuri prin pin-ul Exec dacă premisa este adevărată, sau prin Cast Failed dacă e falsă iar FirstPersonCharacter nu reprezintă personajul controlat de jucător.

Apropo, pentru a comenta anumite noduri, le selectați și apăsați tasta C. Când dezvoltați un joc, este bine să comentați ce ați făcut, ca mai târziu să vă aduceți aminte mai repede mecanismele pe care le-ați creat.

Acum că avem planul pus la punct, vom crea widgetul. Pentru aceasta, vom deschide blueprintul FirstPersonCharacter, și vom crea nodul Event BeginPlay. Vom adăuga nodul Create Widget, vom selecta din meniu Interfață. Următorul nod pe care îl vom mai adăuga este Add To Viewport. Acest nod va afișa widgetul pe ecran. Ultimele lucruri pe care le vom mai face în legătură cu interfața este să conectăm pinul Return Value la Target, să eliminăm nodul Print String, că nu mai avem nevoie de el (apoi refacem conexiunile, desigur), să compilăm și să testăm. Viața ar trebui să scadă de fiecare dată când apăsăm tasta G.



----

Kamikaze făr’ de cap

Headless Kamikaze… unul dintre cei mai interesanți monștri din Serious Sam. Urlă, fuge spre tine și te aruncă în aer. Deoarece mecanicile acestui tip de inamic nu sunt foarte dificil de programat, le vom putea implementa în jocul nostru.

-----

Pentru a recrea acest tip de inamic, vom  importa un personaj deja existent în alt template și îl vom modifica asfel încât să aibă inteligență artificială (AI).

Pentru început, vom salva proiectul curent selectând din meniul File > Save All apoi vom selecta din nou File > New Project. Vom selecta ca template Third Person, aflat în tabul Blueprint. Selectați No starter content ca să ocupe mai puțin spațiu, apoi apăsați butonul Create Project. Acum, editorul va reporni. În Content Browser, vom naviga în folderul Content>ThirdPersonBP>Blueprints. Vom apăsa click dreapta pe ThirdPerson Character, apoi selectăm din meniu Asset Actions apoi Migrate. La noua fereastră dăm OK, apoi navigăm la folderul Content din proiectul anterior.

De obicei atunci când creați un proiect nou, dacă nu ați specificat altă locație, ar trebui să se regăsească în Documents>Unreal Projects. Vom selecta folderul Content al proiectului anterior, apoi vom da OK. Următorul pas este să deschidem proiectul la care lucram inițial și să continuăm cu programarea. În folderul Content vom regăsi folderul ThirdPersonBP. Îl deschidem, iar în Blueprints vom găsi ThirdPerson Character. În interiorul blueprintului, vom șterge toate nodurile ce se află incluse în comentarii cu excepția celor care se află sub comentariul Movement Input.

Următorul pas este să compilăm și să închidem fereastra. Prima dată vom face AI-ul să se miște aleatoriu în nivel, apoi îl vom face să ne urmărească când ne vede. Pentru asta, vom adaugă în nivel din Modes Panel elementul Nav Modifier Volume și îl vom scala ca să cuprindă tot nivelul. Dacă apăsați tasta P, veți observa că podeaua se înverzește. Zona marcată cu verde reprezintă locul pe unde monstrul poate merge. Acum, deschideți din nou planul ThirdPersonCharacter și încercați să construiți graficul din imaginea de mai jos:



Nodul Prima Buclă este un Custom Event. Anterior, am folosit astfel de noduri pentru a trimite impulsul dintr-un blueprint în altul. Dacă punem eventul și funcția în același grafic, impulsul care intră în funcție va ieși prin eveniment, deci vom crea un fel de buclă. Ce face nodul Random Unit Vector ? Pentru a înțelege, voi explica cum interpretează Unreal Engine 4 vectorii.

Un vector este un segment de dreaptă care are o anumită direcție, lungime și sens. Fiind un segment, este situat între două puncte. Primul ar putea fi originea. Acest punct este folosit ca reper pentru calcularea poziției tuturor obiectelor. Pentru a defini un vector, este nevoie de al doilea punct. Din tabul My Blueprint, dacă adăugăm o nouă variabilă și îi schimbăm tipul în Vector, după ce compilăm vom observa că în Details Panel, sub Default Value, variabila are trei valori: X, Y și Z. Aceste valori se numesc coordonate, iar fiecare literă reprezintă numele unei axe. Dacă schimbăm valoarea Z la 1, atunci vom defini un vector cu lungimea de o unitate, perpendicular pe podea, cu sensul de jos în sus. Putem vizualiza un vector ori sub formă de săgeată, ori pur și simplu ca un punct în spațiu.

Nodul Random Unit Vector creează un punct în spațiu la întâmplare. Nodul Get Random Point in Navigable Radius proiectează punctul pe zona navigabilă (Podeaua verde) și în jurul acestei proiecții face un cerc. Cercul va avea o anumită rază. Eu am setat-o la 5000, ca să ocupe tot nivelul. În aria cercului, nodul va selecta încă un punct la întâmplare, iar informația legată de locația acestuia va fi trimisă la nodul AI Move To. După ce AI-ul ajunge la destinație, va aștepta o secundă și ciclul se reia. Nodul Event BeginPlay are rolul să trimită un prim impuls în sistem când începe jocul.



Acum, că inamicul se deplasează aleatoriu în nivel, va trebui să urmărească jucătorul atunci când îl vede. Pentru a-l putea vedea, vom adăuga o componentă la ThirdPerson Character numită Pawn Sensing. Dacă este selectată, vom vedea în Details Panel mai multe variabile. Cele mai importante sunt Sight Radius, pentru distanță maximă de la care te vede și Peripheral Vision, pentru unghiul maxim al vizibilității sale. Sensing Interval se referă la intervalul de timp dintre verificările sale, atunci când decide dacă te-a văzut sau nu. Dacă apăsați tabul Viewport, puteți vedea o reprezentare grafică a acestor distanțe și unghiuri. Momentan, lăsăm variabilele așa cum sunt.

Întorcându-ne la tabul Event Graph, cu componentă Pawn Sensing încă selectată vom adăuga nodul OnSeePawn. Acest nod va genera impulsuri atunci când monstrul vă vede, din 0.5 în 0.5 secunde sau la ce valoare ați setat Sensing Interval. Acum, recreați graficul următor:



IMG



Acum, după ce compilați și apăsați Play, inamicul vă va urmări imediat ce vă va vedea, dar odată ce ajunge lângă voi, nu vă va face nimic. Pentru a-l face să rănească personajul, vom deschide blueprintul FirstPersonCharacter și vom adăuga un nod Custom Event, pe care îl vom numi Scade sănătatea.

Dacă vom compila, când selectăm nodul, vom observa în Details Panel o categorie numită Inputs și un plus. Când ducem cursorul deasupra acestuia, va apărea butonul New Parameter. Îl apăsăm și vom schimba tipul parametrului în Integer. În căsuța de text vom redenumi parametrul în Cu cât? și compilăm din nou.

Vom șterge nodul eveniment G și vom conecta pinul de execuție de la Scade Sănătatea la Set sănătate și pinul Cu cât? la nodul –, așa cum vedeți în imaginea 1.

Următorul pas este să compilăm și să deschidem blueprintul ThirdPerson Character și să adăugăm o componentă, Sphere Collision. În tabul Viewport o vom scala așa cum vedeți în imagine, apoi în Event Graph vom recrea graficul din imaginea 2, format din 3 noduri.

Acum, de fiecare dată când inamicul ajunge lângă noi, va scădea un punct de sănătate. Deoarece nodului Scade Sănătatea i-am adăugat pinul Cu cât?, vom putea la final să duplicăm blueprintul inamicului și să schimbăm foarte ușor periculozitatea sa.



Următoarele lucruri pe care le vom mai face legat de programarea AI-ului este să îl facem să explodeze și să dispară atunci când ajunge lângă jucător. Pentru explozie, vom crea un Actor Blueprint la care vom adăuga ca și componentă același efect de particule pe care l-am adăugat la TNT, însă nu umblăm la bifa Auto Activate. Următorul pas este să schimbăm graficul din blueprintul ThirdPerson Character cum vedeți mai jos:



IMG



În final, îl vom face să dispară atunci când este lovit, și, de asemenea, vom crea și un spawner (vezi pasul următor). Pentru a-l face să dispară la atac, vom deschide blueprintul FirstPerson Projectile. Acolo, vom trage nodul Event Hit mai în stânga, ca să facem loc, apoi vom modifica graficul în felul următor:



IMG



Dacă vreți, puteți adăuga și scor într-un mod asemănător cum am făcut cu variabila Sănătate. Dacă veți vrea ca scorul să persiste între niveluri, există un tip de plan pe care îl puteți folosi numit Game Instance Blueprint.



Pentru a crea un spawner, vom face un nou Actor Blueprint și vom face o buclă cu un Custom Event, un nod de delay și funcția evenimentului. Vom folosi nodul Spawn AIFrom Class pentru a genera inamici. Puteți să setați delay-ul la 0,5 secunde.

Acum, vom deschide blueprintul First Person Character și vom folosi nodurile Get All actors of Class și For Each Loop pentru a accesa funcția eventului din toate spawnerele din nivel.

Ultimul lucru pe care îl vom face în legătură cu spawnerul este să setăm navmesh-ul (zona verde) să detecteze monștrii generați în timpul jocului. Pentru asta, navigați în meniurile Edit>Project Setings>Navigation Mesh și schimbați Runtime Generation din Static în Dynamic.

Când începeți jocul, cum apăsați F, se sparge și zidul, pornește și hoarda. Eu am mai făcut o ultimă modificare la blueprint-ul ThirdPerson Character: pinul On Fail de la nodul AI move to de jos l-am conectat la pinul de intrare de la nodul AI move to de sus, astfel încât, dacă unii monștri nu te mai văd, se vor deplasa aleatoriu.



Desigur, AI-ul pe care l-am construit acum este unul rudimentar. Pentru AI-urile mai complexe, se folosesc grafice speciale numite Behaviour Trees (vezi exemplul de mai jos). Dacă vreți să aflați mai mult, puteți găsi resurse de informare în ultimul articol. ■