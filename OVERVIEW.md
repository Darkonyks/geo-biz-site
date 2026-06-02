# GeoBiz — Pregled web sajta (OVERVIEW)

> Završni dokument analize projekta. Generisano na osnovu kompletnog pregleda izvornog koda.
> Datum analize: 2026-06-02

---

## 1. Opis projekta

**GeoBiz** je statički, prezentacioni (marketinški) web sajt IT kompanije
**GeoBiz** iz Sremske Mitrovice (Srbija). Sajt predstavlja usluge kompanije iz
oblasti informacionih tehnologija, IT konsaltinga, bezbednosti i sopstvenih
softverskih proizvoda.

- **Jezik sadržaja:** srpski (latinica)
- **Tip:** statički sajt (HTML/CSS/JS) + jedna PHP skripta za kontakt formu
- **Osnova:** komercijalni Bootstrap šablon **"HeroBiz"** od [BootstrapMade](https://bootstrapmade.com/)
- **Domen / produkcija:** `geo-biz.com` (referencirano u kodu, npr. podrška i email)
- **Kontakt:** office@geo-biz.com · +381 60 345 32 93 · Mirna 1, 22000 Sremska Mitrovica

---

## 2. Tehnološki stack

| Sloj | Tehnologija |
|------|-------------|
| Markup | HTML5 (statičke stranice) |
| Stilizacija | CSS3, **Bootstrap 5**, prilagođeni `main.css` (~64 KB) |
| Tema/varijable | CSS varijable sa više šema boja (`variables-*.css`) |
| JavaScript | Vanilla JS (`main.js`), prilagođeni `contact-form.js` (fetch/AJAX) |
| Animacije | **AOS** (Animate On Scroll) |
| Slajderi | **Swiper** (klijenti, obuke/testimonijali) |
| Lightbox / galerija | **GLightbox** |
| Filtriranje portfolija | **Isotope** |
| Ikonice | **Bootstrap Icons** |
| Fontovi | Google Fonts (Open Sans, Poppins, Source Sans Pro) |
| Backend (kontakt) | **PHP + PHPMailer 6.9** (slanje emaila preko SMTP-a) |
| Zavisnosti | **Composer** (`composer.json` / `composer.lock`) |
| Analitika | **Google Analytics** (gtag.js, `G-N2G2KRPLFM`) |
| Mape | Google Maps embed (iframe) |

---

## 3. Struktura projekta

```
GeoBiz sajt/
├── index.html                  # Glavna (home) stranica — sve sekcije
├── inner-page.html             # Šablonska "inner" stranica (placeholder)
├── contact.html                # Zasebna kontakt stranica (još sa template tekstom)
│
├── usluge/                     # IT USLUGE (6 stranica)
│   ├── odrzavanje-racunara.html
│   ├── mreze.html
│   ├── odrzavanje-servera.html
│   ├── data-storage.html
│   ├── web-designe.html
│   └── razvoj-aplikacija.html
│
├── it-konsulting/              # IT KONSALTING (ISO standardi)
│   ├── bezbednost-informacija.html      (ISO 27001)
│   ├── kontinuitet-poslovanja.html      (ISO 22301)
│   ├── upravljanje-rizicima.html        (ISO 31000)
│   └── upravljanje-it-uslugama.html     (ISO/IEC 20000-1)
│
├── bezbednost/
│   └── testiranje-bezbednosti.html      # Testiranje bezbednosti IT sistema
│
├── programi/                   # Sopstveni softverski proizvodi
│   ├── geobiz.html
│   └── inner-page.html
│
├── pages/                      # Demo/šablonske stranice iz teme (blog, portfolio…)
│   ├── blog.html, blog-details.html
│   ├── index-2.html, index-3.html, index-4.html
│   ├── portfolio-details.html
│   └── template.html
│
├── forms/                      # Backend kontakt forme
│   ├── contact.php             # Aktivna PHP skripta (PHPMailer SMTP)
│   ├── contact-form.php
│   └── Readme.txt
│
├── assets/
│   ├── css/                    # main.css, style.css, variables*.css (šeme boja)
│   ├── js/                     # main.js, main-1.js, contact-form.js
│   ├── img/                    # Slike (usluge, klijenti, obuke, portfolio, logo…)
│   ├── scss/                   # SCSS izvori teme
│   └── vendor/                 # Bootstrap, AOS, Swiper, GLightbox, Isotope, PHPMailer
│
├── vendor/                     # Composer zavisnosti (PHPMailer)
├── composer.json / .lock
├── .gitignore / .gitattributes (Git LFS za *.zip)
│
├── geo-biz-sajt.git/           # ⚠ Ugnježdeni bare Git repo (artefakt git-filter-repo)
├── GeoBiz sajt.zip             # ⚠ ~905 MB arhiva u radnom direktorijumu
└── Struktura sajta.docx        # Dokument sa planiranom strukturom sajta
```

> Ukupno tracked fajlova u Gitu: **468**.

---

## 4. Sadržaj i sekcije (glavna stranica `index.html`)

Glavna stranica je *single-page* sa sledećim sekcijama (povezane preko sidra `#`):

1. **Header / Navigacija** — fiksni meni sa dropdown-ovima: Početna, O nama,
   Usluge, IT Konsalting, Bezbednost, Programi, Obuke, Kontakt + dugme „Podrška".
2. **Hero** — animirani uvod „Dobro došli u GeoBiz — Vaš IT oslonac u digitalnom svetu".
3. **O nama** — tabovi: **Misija / Vrednosti / Vizija**.
4. **Klijenti** — Swiper slajder logotipa (Cosun, Lidea, Geodigit, ISOQAR, Lautec…).
5. **Usluge** — 6 kartica (računari, serveri, data storage, mreže, web dizajn, razvoj aplikacija).
6. **Call To Action** — poziv na besplatne konsultacije.
7. **Bezbednost (onfocus)** — testiranje bezbednosti IT sistema.
8. **IT Konsalting (features)** — tabovi za 4 ISO standarda.
9. **Obuke** — Swiper slajder sa 7 tipova obuka (info-bezbednost, phishing, mobilni uređaji…).
10. **Kontakt** — info + forma (`forms/contact.php`) + Google Maps.
11. **Footer** — kontakt, korisni linkovi, usluge, logo.

### Proizvodi (Programi)
U meniju se navode 4 proizvoda: **GeoBiz** (geodetske firme), **GeoDent**
(zubarske ordinacije), **GeoMedik** (klinike/bolnice), **GeoErp** (poslovni softver).
Trenutno svi linkovi vode na isti `inner-page.html` (placeholder).

### Kontakt forma — tok rada
`contact-form.js` presreće submit, šalje `fetch` POST na `forms/contact.php`,
koja preko **PHPMailer + SMTP** (`host107.dwhost.net:587`, STARTTLS) šalje mejl
na `office@geo-biz.com` i vraća JSON odgovor; rezultat se prikazuje kroz `alert()`.

---

## 5. Stanje Git repozitorijuma

- Aktivna grana: **`programi`**; glavna grana: **`master`**.
- Grane: `main`, `master`, `programi`, `origin/darko-fix`.
- Skorija istorija ukazuje na čišćenje velikog ZIP fajla iz istorije pomoću
  **git-filter-repo** (`brisanje zip fajlova iz git istorije`, `Delete GeoBiz sajt.zip`).
- `.gitattributes` konfiguriše **Git LFS** za `*.zip`; `.gitignore` sada ignoriše arhive.

---

## 6. Uočeni problemi i preporuke

### 🔴 Kritično

1. **Nerazrešeni Git merge konflikti u produkcijskom fajlu.**
   `programi/geobiz.html` sadrži **24** markera (`<<<<<<<`, `=======`, `>>>>>>>`).
   Stranica je polomljena (dupli sadržaj, neispravna struktura).
   → *Razrešiti konflikt i očistiti markere.*

2. **Tajna (SMTP lozinka) u izvornom kodu.**
   `forms/contact.php` sadrži hardkodovan email i **lozinku u plaintextu**
   (`$smtp_password = '...'`), koja je verovatno i u Git istoriji.
   → *Hitno promeniti lozinku, prebaciti kredencijale u environment varijable /
   konfiguraciju van repozitorijuma, ukloniti iz istorije.*

3. **Ugnježdeni Git repozitorijum u radnom stablu.**
   Direktorijum `geo-biz-sajt.git/` (bare repo + `git-filter-repo.py`) je
   delom commit-ovan (~30 fajlova tracked) — artefakt rewrite operacije.
   → *Ukloniti iz radnog stabla i iz praćenja.*

### 🟠 Važno

4. **Nekonzistentne relativne putanje u `index.html`.**
   Stranica je u rootu, ali referencira CSS i `main.js` preko `../assets/...`
   (izlazi iznad roota), dok skripte koriste `assets/vendor/...`. Zavisno od
   načina serviranja, stilovi/JS mogu da se ne učitaju.
   → *Uskladiti sve putanje na konzistentne (root-relativne ili relativne).*

5. **Velika arhiva u repozitorijumu.** `GeoBiz sajt.zip` (~905 MB) i dalje
   postoji na disku u radnom direktorijumu.
   → *Ukloniti sa diska; držati van VCS-a.*

### 🟡 Manje / kvalitet i SEO

6. **Prazni meta opisi i ključne reči** na svim stranicama (`<meta description/keywords>` prazni) — loše za SEO.
7. **Šablonski (default) naslovi** — npr. `inner-page.html` ima naslov *„Inner Page - HeroBiz Bootstrap Template"*.
8. **`contact.html` još sadrži placeholder tekst** — „Your Address Here", „Your Phone Number", engleski naslovi.
9. **Duplirani linkovi u footeru** (npr. „Održavanje servera" i „Data storage" se ponavljaju sa različitim putanjama, neke pogrešne).
10. **Demo stranice iz teme** (`pages/blog*`, `index-2/3/4`, `portfolio-details`) — neiskorišćene, mogu se ukloniti radi čistoće.
11. **Pomešani jezici u UI-ju** kontakt forme (placeholderi „Your Name", „Send Message", poruka „Your message has been sent") naspram srpskog ostatka sajta.
12. **Korišćenje `alert()`** za poruke forme — bolje inline UI poruke koje već postoje u markup-u (`.sent-message`, `.error-message`).

---

## 7. Sažetak

GeoBiz je čist statički prezentacioni sajt baziran na Bootstrap „HeroBiz" temi,
sa dobro organizovanom strukturom usluga, IT konsaltinga (ISO standardi),
bezbednosti, obuka i sopstvenih proizvoda. Funkcionalno jezgro je marketinški
sadržaj + kontakt forma (PHP/PHPMailer).

Pre objave/produkcije prioritetno treba: **(1)** razrešiti merge konflikte u
`programi/geobiz.html`, **(2)** ukloniti i rotirati SMTP lozinku iz koda,
**(3)** počistiti repozitorijum (ugnježdeni `.git`, ZIP), i **(4)** uskladiti
putanje resursa. Sekundarno: SEO meta podaci, lokalizacija forme i uklanjanje
neiskorišćenih demo stranica.
```
