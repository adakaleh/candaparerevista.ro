---
title: "Introducere în Unreal Engine 4 (III)"
subtitle: "Partea III: Introducere în Blueprints - personajele"
type: post
date: 2018-11-17T00:00:03
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

description: "În seria de jocuri Half-Life, personajul principal avea un costum menit să îl protejeze de diverse pericole. Costumul avea o proprietate specială: îl punea pe jucător să aibă grijă de o variabilă numită „HP”. Noi vom implementa o astfel de variabilă, a cărei valoare poate fi interpretată de jucător printr-o cifră afișată pe ecran."

resources:
  - src:
    name: "card-cover-image"

  - src: images/ue4-cover.jpg
    name: "cover-image"
---

>Acest articol e al treilea dintr-o serie de 5 articole. Găsiți aici celelalte părți:

>[Partea I: Introducere. Epic Games Launcher](/posts/2018/11/atelier-introducere-unreal-engine-i-mahri726)

>[Partea II: Introducere în Blueprints - nivelul de joc](/posts/2018/11/atelier-introducere-unreal-engine-ii-mahri726)

>[Partea IV: Grafică și Audio](/posts/2018/11/atelier-introducere-unreal-engine-iv-mahri726)

>[Partea V: Împachetarea finală și resurse suplimentare](/posts/2018/11/atelier-introducere-unreal-engine-v-mahri726)

## Cum să efectuăm o scădere fatală?

_În seria de jocuri Half-Life, personajul principal, Gordon Freeman, avea un costum menit să îl protejeze de diverse pericole: radiații, acid, electricitate sau extratereștri. Costumul avea o proprietate specială: îl punea pe jucător să aibă grijă de o variabilă numită „HP”. Când atingea pragul 0, Gordon murea. Desigur, conceptul de **Hit Points** a apărut mult mai devreme, când jocuri tabletop precum **Dungeons and Dragons** își făceau debutul. Noi vom implementa o astfel de variabilă, a cărei valoare poate fi interpretată de jucător printr-o cifră afișată pe ecran. Inițial, aceasta va scădea atunci când jucătorul apasă o tastă._

Pentru a crea variabila, vom deschide blueprint-ul **FirstPersonCharacter**, iar în panelul **My Blueprint** apăsați butonul verde **Add New**, apoi selectați din meniu **Variable**. Vom numi variabila _„Sănătate”_.

{{< figure  src="gallery_5_hp/zxD3qww.jpg" >}}

Lângă numele variabilei, puteți observa o culoare. Dacă apăsați culoarea respectivă, veți putea schimba tipul variabilei. O vom schimba în `Integer`. Ţineți apăsat click stânga pe ea, apoi o trageți într-un loc liber în grafic; va apărea un meniu cu două opțiuni, din care selectați **Get**. Apăsați butonul **Compile**, iar dacă nodul ei este selectat, în **Details Panel** veți vedea sub tabul **Default Value** că are valoarea 0. Schimbați valoarea la 10. Pentru a o face să scadă, în primul rând adăugați un nod eveniment, cum ar fi cel pentru tasta **G**, care inițiază impulsul. De la nodul variabilei **Sănătate** vom trage un fir de date, scriem „–” în bara de căutare și selectăm „**integer** – **integer”**. În mod normal, ar trebui ca valoarea nodului din dreptul pinului al doilea să fie 1.

Din tabul **My Blueprint** vom trage din nou variabila în grafic, dar de data aceasta vom selecta din meniu **Set** în loc de **Get**. Urmează să conectăm firul de execuție de la nodul **G** la nodul **Set** și firul de date de la rezultatul scăderii în pinul acestuia. Ca să vedem scăderea pe ecran, vom trage de la pinul de execuție al nodului **Set** un fir și vom adaugă **Print String**. De la pinul turcoaz al nodului **Set**, vom trage un fir de date la pinul roz al nodului **Print String**. Motorul grafic va adăuga automat un nod care să convertească variabila de tip integer în variabilă de tip string (șir de caractere). Vom compila și vom testa. De fiecare dată când apăsăm G, variabila **Sănătate** ar trebui să scadă cu 1.

Acum, vom vrea ca atunci când variabila ajunge la valoarea 0, personajul să moară. O modalitate simplă pentru a produce moartea personajului este ca nivelul să se reîncarce. Pentru asta, vom deschide din nou blueprint-ul personajului și vom trage un fir de date de la pinul nodului **Set**, vom căuta „=” și vom selecta „**integer <= integer”**. Noul nod face comparația dintre valoarea variabilei noastre și o altă variabilă, apoi oferă ca rezultat informație de tip `Boolean`, adică spune dacă primul număr este mai mic sau egal cu al doilea sau nu.

Această informație ne va fi utilă pentru a putea opri impulsul, dacă condiția se adeverește. Pentru aceasta, vom trage un fir de execuție de la nodul **Print String**, apoi vom adăuga nodul **Branch**. Acesta este al patrulea tip de nod despre care vă vorbesc în acest atelier, aparținând categoriei **Flow Control**.

Vom conecta pinul nodului comparator la pinul **Condition** al acestui nod. De la pinul de execuție **True** vom adăuga nodul **Get Current Level Name** apoi, legat de acesta, **Open Level**. Următoarele lucruri pe care le vom face vor fi să conectăm firul de la pinul **Return Value** la **Level Name** să compilăm și să testăm.

## UMG

_Acum, că am scriptat un sistem care să scadă sănătatea personajului, jucătorul ar trebui să vadă acest efect. **Print String** se folosește doar pentru teste, nu pentru jocuri finale, deci va trebui să afișăm punctele de viață așa cum trebuie. Pentru asta, vom folosi editorul de interfață (UI) inclus în Unreal Engine 4 numit Unreal Motion Graphics sau UMG. UMG ne permite să punem butoane, meniuri, bare de viață sau alte elemente 2D care îi pot oferi informații jucătorului despre starea jocului._

Pentru a începe să folosim UMG, trebuie mai întâi să creăm un plan pentru un widget. Un widget este ca un fel de pânză, pe care putem aranja elementele de interfață. Pentru a crea un plan de widget, dați click dreapta în **Content Browser**, mergeți în categoria **UI/User Interface** (s-ar putea să fie nevoie să dați scroll ca să o vedeți, mai ales dacă folosiți versiuni mai vechi ale motorului) și selectați **Widget Blueprint**. O putem numi _„Interfață”_. Dacă dați două click-uri pe aceasta se va deschide UMG.

UMG are două tab-uri, **Designer** și **Graph**. În **Designer** puteți aranja elementele de interfață iar în **Graph** le scriptați. Pentru a afișa punctele de viață, va trebui să tragem din panelul **Palette** categoria **Common**, elementul **Text**. Cu textul selectat, vom observa că putem face niște setări în **Details panel**. Sub **Content** vom schimba conținutul textului în „+”, vom seta mărimea fontului 50 apoi vom scala căsuța în care este situat acesta astfel încât să cuprindă doar plusul.

Un lucru important în UMG este ancorarea elementelor. Ancorarea se face din meniul **Anchors**. Dacă selectați opțiunea potrivită, textul se va vedea în aceiași locație indiferent de rezoluția ecranului. Este bine să puneți ancora în colțul unde se află textul.

Lângă plusul nostru vom adăuga încă un element de tip text, pe care îl vom numi _XX_. Numele acesta este pus doar provizoriu, pentru a putea aranja textul mai bine. În timpul rulării jocului, va fi înlocuit de cifrele corespunzătoare variabilei **Sănătate**. Este bine ca bifa **Is Variable** să fie activată astfel încât textul să poate fi accesat de alte noduri, precum cele de schimbare a vizibilității. Următorul pas este să apăsăm butonul **Bind** de lângă **Text** (din categoria **Content**) și să selectăm **Create binding**. Motorul grafic va crea o funcție (**GetText_0**) și va deschide o fereastră astfel încât să o putem edita.

Din interiorul funcției, putem accesa variabila **Sănătate** aflată în blueprint-ul personajului în două moduri: fie folosim nodurile **Get all actors of class** și **Get** așa cum am făcut anterior în cazul bombelor, sau putem folosi nodurile **Get Player Character** și **Cast To FirstPersonCharacter**.

{{< figure  src="gallery_6_umg/1-i0gel2d.jpg" >}}

Nodul **Cast To FirstPersonCharacter** are rolul de a face o verificare. Dacă blueprintul **FirstPersonCharacter** este chiar personajul controlat de jucător (**Player Character**), atunci acesta poate fi accesat. De asemenea, atunci când e activat, nodul poate trimite impulsuri prin pin-ul **Exec** dacă premisa este adevărată, sau prin **Cast Failed** dacă e falsă iar **FirstPersonCharacter** nu reprezintă personajul controlat de jucător.

Apropo, pentru a comenta anumite noduri, le selectați și apăsați tasta `C`. Când dezvoltați un joc, este bine să comentați ce ați făcut, ca mai târziu să vă aduceți aminte mai repede mecanismele pe care le-ați creat.

Acum că avem planul pus la punct, vom crea widgetul. Pentru aceasta, vom deschide blueprintul **FirstPersonCharacter**, și vom crea nodul **Event BeginPlay**. Vom adăuga nodul **Create Widget**, vom selecta din meniu **Interfață**. Următorul nod pe care îl vom mai adăuga este **Add To Viewport**. Acest nod va afișa widgetul pe ecran. Ultimele lucruri pe care le vom mai face în legătură cu interfața este să conectăm pinul **Return Value** la **Target**, să eliminăm nodul **Print String**, că nu mai avem nevoie de el (apoi refacem conexiunile, desigur), să compilăm și să testăm. Viața ar trebui să scadă de fiecare dată când apăsăm tasta **G**.

{{< figure  src="gallery_6_umg/2-KOkuC9z.jpg" >}}

## Kamikaze făr' de cap

_Headless Kamikaze… unul dintre cei mai interesanți monștri din Serious Sam. Urlă, fuge spre tine și te aruncă în aer. Deoarece mecanicile acestui tip de inamic nu sunt foarte dificil de programat, le vom putea implementa în jocul nostru._

Pentru a recrea acest tip de inamic, vom  importa un personaj deja existent în alt template și îl vom modifica asfel încât să aibă inteligență artificială (AI).

Pentru început, vom salva proiectul curent selectând din meniul `File > Save All` apoi vom selecta din nou `File > New Project`. Vom selecta ca template **Third Person**, aflat în tabul **Blueprint**. Selectați **No starter content** ca să ocupe mai puțin spațiu, apoi apăsați butonul **Create Project**. Acum, editorul va reporni. În **Content Browser**, vom naviga în folderul `Content > ThirdPersonBP > Blueprints`. Vom apăsa click dreapta pe **ThirdPerson Character**, apoi selectăm din meniu **Asset Actions** apoi **Migrate**. La noua fereastră dăm OK, apoi navigăm la folderul **Content** din proiectul anterior.

De obicei atunci când creați un proiect nou, dacă nu ați specificat altă locație, ar trebui să se regăsească în `Documents > Unreal Projects`. Vom selecta folderul **Content** al proiectului anterior, apoi vom da OK. Următorul pas este să deschidem proiectul la care lucram inițial și să continuăm cu programarea. În folderul **Content** vom regăsi folderul **ThirdPersonBP**. Îl deschidem, iar în Blueprints vom găsi **ThirdPerson Character**. În interiorul blueprintului, vom șterge toate nodurile ce se află incluse în comentarii cu excepția celor care se află sub comentariul **Movement Input**.

Următorul pas este să compilăm și să închidem fereastra. Prima dată vom face AI-ul să se miște aleatoriu în nivel, apoi îl vom face să ne urmărească când ne vede. Pentru asta, vom adaugă în nivel din **Modes Panel** elementul **Nav Modifier Volume** și îl vom scala ca să cuprindă tot nivelul. Dacă apăsați tasta **P**, veți observa că podeaua se înverzește. Zona marcată cu verde reprezintă locul pe unde monstrul poate merge. Acum, deschideți din nou planul **ThirdPersonCharacter** și încercați să construiți graficul din imaginea de mai jos:

{{< figure  src="gallery_7_kamikaze/f4BTLwF.jpg" >}}

Nodul **Prima Buclă** este un **Custom Event**. Anterior, am folosit astfel de noduri pentru a trimite impulsul dintr-un blueprint în altul. Dacă punem eventul și funcția în același grafic, impulsul care intră în funcție va ieși prin eveniment, deci vom crea un fel de buclă. Ce face nodul **Random Unit Vector**? Pentru a înțelege, voi explica cum interpretează Unreal Engine 4 vectorii.

Un vector este un segment de dreaptă care are o anumită direcție, lungime și sens. Fiind un segment, este situat între două puncte. Primul ar putea fi originea. Acest punct este folosit ca reper pentru calcularea poziției tuturor obiectelor. Pentru a defini un vector, este nevoie de al doilea punct. Din tabul **My Blueprint**, dacă adăugăm o nouă variabilă și îi schimbăm tipul în `Vector`, după ce compilăm vom observa că în **Details Panel**, sub **Default Value**, variabila are trei valori: X, Y și Z. Aceste valori se numesc coordonate, iar fiecare literă reprezintă numele unei axe. Dacă schimbăm valoarea Z la 1, atunci vom defini un vector cu lungimea de o unitate, perpendicular pe podea, cu sensul de jos în sus. Putem vizualiza un vector ori sub formă de săgeată, ori pur și simplu ca un punct în spațiu.

Nodul **Random Unit Vector** creează un punct în spațiu la întâmplare. Nodul **Get Random Point in Navigable Radius** proiectează punctul pe zona navigabilă (Podeaua verde) și în jurul acestei proiecții face un cerc. Cercul va avea o anumită rază. Eu am setat-o la 5000, ca să ocupe tot nivelul. În aria cercului, nodul va selecta încă un punct la întâmplare, iar informația legată de locația acestuia va fi trimisă la nodul **AI Move To**. După ce AI-ul ajunge la destinație, va aștepta o secundă și ciclul se reia. Nodul **Event BeginPlay** are rolul să trimită un prim impuls în sistem când începe jocul.

Acum, că inamicul se deplasează aleatoriu în nivel, va trebui să urmărească jucătorul atunci când îl vede. Pentru a-l putea vedea, vom adăuga o componentă la **ThirdPerson Character** numită **Pawn Sensing**. Dacă este selectată, vom vedea în **Details Panel** mai multe variabile. Cele mai importante sunt **Sight Radius**, pentru distanță maximă de la care te vede și **Peripheral Vision**, pentru unghiul maxim al vizibilității sale. **Sensing Interval** se referă la intervalul de timp dintre verificările sale, atunci când decide dacă te-a văzut sau nu. Dacă apăsați tabul **Viewport**, puteți vedea o reprezentare grafică a acestor distanțe și unghiuri. Momentan, lăsăm variabilele așa cum sunt.

Întorcându-ne la tabul **Event Graph**, cu componentă **Pawn Sensing** încă selectată vom adăuga nodul **OnSeePawn**. Acest nod va genera impulsuri atunci când monstrul vă vede, din 0.5 în 0.5 secunde sau la ce valoare ați setat **Sensing Interval**. Acum, recreați graficul următor:

{{< figure  src="gallery_7_kamikaze/DHlFVfP.jpg" >}}

Acum, după ce compilați și apăsați **Play**, inamicul vă va urmări imediat ce vă va vedea, dar odată ce ajunge lângă voi, nu vă va face nimic. Pentru a-l face să rănească personajul, vom deschide blueprintul **FirstPersonCharacter** și vom adăuga un nod **Custom Event**, pe care îl vom numi **Scade sănătatea**.

Dacă vom compila, când selectăm nodul, vom observa în **Details Panel** o categorie numită **Inputs** și un plus. Când ducem cursorul deasupra acestuia, va apărea butonul **New Parameter**. Îl apăsăm și vom schimba tipul parametrului în `Integer`. În căsuța de text vom redenumi parametrul în **Cu cât?** și compilăm din nou.

Vom șterge nodul eveniment **G** și vom conecta pinul de execuție de la **Scade Sănătatea** la **Set sănătate** și pinul **Cu cât?** la nodul –, așa cum vedeți în _Figura 1_.

Următorul pas este să compilăm și să deschidem blueprintul **ThirdPerson Character** și să adăugăm o componentă, **Sphere Collision**. În tabul **Viewport** o vom scala așa cum vedeți în imagine, apoi în **Event Graph** vom recrea graficul din _Figura 2_, format din 3 noduri.

{{< figure-multi
    "gallery_7_kamikaze/1-J10nXhs.jpg|Figura 1|"
    "gallery_7_kamikaze/2-EdS1nSr.jpg|Figura 2|"
>}}

Acum, de fiecare dată când inamicul ajunge lângă noi, va scădea un punct de sănătate. Deoarece nodului **Scade Sănătatea** i-am adăugat pinul **Cu cât?**, vom putea la final să duplicăm blueprintul inamicului și să schimbăm foarte ușor periculozitatea sa.

{{< figure  src="gallery_7_kamikaze/3-c5XYrfA.jpg" >}}

Următoarele lucruri pe care le vom mai face legat de programarea AI-ului este să îl facem să explodeze și să dispară atunci când ajunge lângă jucător. Pentru explozie, vom crea un **Actor Blueprint** la care vom adăuga ca și componentă același efect de particule pe care l-am adăugat la **TNT**, însă nu umblăm la bifa **Auto Activate**. Următorul pas este să schimbăm graficul din blueprintul **ThirdPerson Character** cum vedeți mai jos:

{{< figure  src="gallery_7_kamikaze/vrDYYro.jpg" >}}

În final, îl vom face să dispară atunci când este lovit, și, de asemenea, vom crea și un spawner (vezi pasul următor). Pentru a-l face să dispară la atac, vom deschide blueprintul **FirstPerson Projectile**. Acolo, vom trage nodul **Event Hit** mai în stânga, ca să facem loc, apoi vom modifica graficul în felul următor:

{{< figure  src="gallery_7_kamikaze/RFShV5P.jpg" >}}

Dacă vreți, puteți adăuga și scor într-un mod asemănător cum am făcut cu variabila **Sănătate**. Dacă veți vrea ca scorul să persiste între niveluri, există un tip de plan pe care îl puteți folosi numit **Game Instance Blueprint**.

Pentru a crea un spawner, vom face un nou **Actor Blueprint** și vom face o buclă cu un **Custom Event**, un nod de delay și funcția evenimentului. Vom folosi nodul **Spawn AIFrom Class** pentru a genera inamici. Puteți să setați delay-ul la 0,5 secunde.

{{< figure  src="gallery_7_kamikaze/vieV5Pe.jpg" >}}

Acum, vom deschide blueprintul **First Person Character** și vom folosi nodurile **Get All actors of Class** și **For Each Loop** pentru a accesa funcția eventului din toate spawnerele din nivel.

Ultimul lucru pe care îl vom face în legătură cu spawnerul este să setăm navmesh-ul (zona verde) să detecteze monștrii generați în timpul jocului. Pentru asta, navigați în meniurile `Edit > Project Setings > Navigation Mesh` și schimbați **Runtime Generation** din **Static** în **Dynamic**.

Când începeți jocul, cum apăsați **F**, se sparge și zidul, pornește și hoarda. Eu am mai făcut o ultimă modificare la blueprint-ul **ThirdPerson Character**: pinul **On Fail** de la nodul **AI move to** de jos l-am conectat la pinul de intrare de la nodul **AI move to** de sus, astfel încât, dacă unii monștri nu te mai văd, se vor deplasa aleatoriu.

Desigur, AI-ul pe care l-am construit acum este unul rudimentar. Pentru AI-urile mai complexe, se folosesc grafice speciale numite **Behaviour Trees** (vezi exemplul de mai jos). Dacă vreți să aflați mai mult, puteți găsi resurse de informare în ultimul articol din serie. ■

{{< figure-multi
    "gallery_7_kamikaze/DoneBehaviorTree.jpg|Exemplu Behaviour Trees 1|"
    "gallery_7_kamikaze/connectedTasks.jpg|Exemplu Behaviour Trees 2|"
>}}