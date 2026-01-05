📄 Moj Web CV (Životopis)
Ovo je moj lični Web CV, hostan besplatno putem GitHub Pages. Dizajniran je da bude brz, responzivan (prilagođen mobitelima) i jednostavan za održavanje. Projekt koristi jednu index.html datoteku koja sadrži svu strukturu, stilove (putem Tailwind CSS-a) i logiku.
✨ Ključne Funkcionalnosti
🌓 Dark Mode / Light Mode: Automatski detektuje postavke sistema, ali ima i ručni prekidač.
📱 Potpuno Responzivan: Izgleda odlično na desktopu, tabletu i mobitelu.
⚡ Brze Performanse: Koristi Tailwind CSS putem CDN-a i minimalan JavaScript.
🎨 Animacije: Glatke "fade-in" animacije pri skrolanju i animirane trake vještina (skill bars).
🖨️ PDF Export: Dugme za printanje ili spremanje stranice kao PDF.
🚀 Kako pokrenuti projekt lokalno
Klonirajte repozitorij: https://github.com/budxxx/github.io.git



Uđite u folder:
cd moj-web-cv


Otvorite index.html u bilo kojem pregledniku (Chrome, Firefox, Edge).
🛠️ Prilagođavanje (Kako izmijeniti podatke)
Sve informacije se nalaze unutar index.html datoteke. Da biste promijenili podatke, otvorite datoteku u uređivaču teksta (npr. VS Code ili Notepad) i potražite sljedeće sekcije:
Lični podaci: Potražite <h1> tag na početku za ime i titulu.
Iskustvo (Experience): Sekcija <section id="experience">. Kopirajte <div class="card ..."> blok da dodate novi posao.
Vještine (Skills): Sekcija <section id="skills">. Promijenite data-width="85%" da ažurirate nivo znanja.
Linkovi: U <section id="contact"> promijenite href="#" u vaše prave linkove za LinkedIn, GitHub itd.
🌐 Tehnologije
HTML5: Semantička struktura.
Tailwind CSS (CDN): Za stiliziranje bez potrebe za kompajliranjem CSS-a.
Font Awesome: Za ikonice.
Vanilla JavaScript: Za logiku tamnog načina rada i animacije.
📄 Licenca
Ovaj projekt je licenciran pod MIT Licencom - pogledajte LICENSE datoteku za detalje.
