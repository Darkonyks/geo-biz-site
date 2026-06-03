# -*- coding: utf-8 -*-
"""Prevodi SR -> EN/RU/DE. Kljuc = SR tekst (jedna linija; generator hvata i preloman tekst),
vrednost = prevod. Brend "GeoBiz/GeoDent/GeoMedik/GeoErp" se ne prevodi."""

# =========================== ENGLISH ===========================
EN = {
    # --- Navigacija / header ---
    "Početna": "Home",
    "O nama": "About us",
    "Usluge": "Services",
    "Održavanje računara": "Computer maintenance",
    "Projektovanje i izvođenje mrežne infrastrukturea": "Network infrastructure design & deployment",
    "Projektovanje i izvođenje mrežne infrastrukture": "Network infrastructure design & deployment",
    "Održavanje servera i virtuelizacija": "Server maintenance & virtualization",
    "Data storage": "Data storage",
    "WEB dizajn": "Web design",
    "WEB designe": "Web design",
    "Razvoj aplikacija i baza podataka": "Application & database development",
    "IT Konsalting": "IT consulting",
    "Bezbednost informacija": "Information security",
    "Kontinuitet poslovanja": "Business continuity",
    "Upravljanje rizicima": "Risk management",
    "Upravljanje IT uslugama": "IT service management",
    "Bezbednost": "Security",
    "Testiranje bezbednosti IT sistema": "IT systems security testing",
    "Programi": "Software",
    "GeoBiz - za Geodetske firme": "GeoBiz - for surveying companies",
    "GeoDent - za Zubarske ordinacije": "GeoDent - for dental offices",
    "GeoMedik - za klinike i bolnice": "GeoMedik - for clinics and hospitals",
    "GeoErp - Poslovni softver": "GeoErp - Business software",
    "Obuke": "Training",
    "OBUKE": "TRAINING",
    "Kontakt": "Contact",
    "Podrška": "Support",

    # --- Footer ---
    "Korisni linkovi": "Useful links",
    "Sremska Mitrovica, Srbija": "Sremska Mitrovica, Serbia",
    "Sremska Mitrovica, Srbija": "Sremska Mitrovica, Serbia",

    # --- Hero ---
    "Dobro došli u": "Welcome to",
    "Vaš IT oslonac u digitalnom svetu": "Your IT support in the digital world",

    # --- About / tabovi ---
    "Misija": "Mission",
    "Vrednosti": "Values",
    "Vizija": "Vision",
    "Omogućiti klijentima da ostvare svoje poslovne ciljeve kroz inovativna IT rešenja i usluge.":
        "To enable clients to achieve their business goals through innovative IT solutions and services.",
    "Pružiti visokokvalitetne IT usluge koje unapređuju produktivnost i efikasnost klijenata.":
        "To deliver high-quality IT services that improve our clients' productivity and efficiency.",
    "Želimo da postanemo partneri klijenata u njihovom digitalnom transformacijskom putovanju kroz prilagođena IT rešenja.":
        "We want to become our clients' partners on their digital transformation journey through tailored IT solutions.",
    "Težimo da izgradimo pouzdanu reputaciju kao lider u industriji koji pruža pouzdane i sigurne IT usluge.":
        "We strive to build a trusted reputation as an industry leader providing reliable and secure IT services.",
    "Doprineti društvenoj i ekonomskoj dobrobiti kroz inovacije u tehnologiji i pravedno poslovanje.":
        "To contribute to social and economic well-being through technological innovation and fair business.",
    "Kvaliteta: Posvećenost pružanju visokokvalitetnih proizvoda i usluga koji nadmašuju očekivanja klijenata":
        "Quality: A commitment to providing high-quality products and services that exceed client expectations",
    "Inovacija: Stalna težnja za razvojem novih ideja, tehnologija i pristupa kako bi se unapredila konkurentnost i donele nove vrednosti klijentima.":
        "Innovation: A constant drive to develop new ideas, technologies and approaches to improve competitiveness and bring new value to clients.",
    "Integriteta: Poštovanje etičkih standarda, iskrenost, transparentnost i odgovornost u svim poslovnim aktivnostima.":
        "Integrity: Respect for ethical standards, honesty, transparency and accountability in all business activities.",
    "Partnerstva: Izgradnja dugoročnih partnerskih odnosa s klijentima, saradnicima i zajednicom kako bi se postigla obostrana korist i podržao održivi rast.":
        "Partnership: Building long-term partnerships with clients, associates and the community to achieve mutual benefit and support sustainable growth.",
    "Klijentski fokus: Stavljanje klijenata u središte svih aktivnosti, slušanje njihovih potreba i prilagođavanje rešenja kako bi se osigurala njihova potpuna satisfakcija.":
        "Client focus: Placing clients at the center of all activities, listening to their needs and adapting solutions to ensure their complete satisfaction.",
    "Društvena odgovornost: Posvećenost doprinosu društvenoj zajednici kroz održive prakse, podršku zajednici i društveno korporativno delovanje.":
        "Social responsibility: A commitment to the community through sustainable practices, community support and corporate social action.",
    "Postati regionalni lider u pružanju inovativnih IT usluga koje podstiču digitalnu transformaciju u svim industrijama":
        "To become a regional leader in providing innovative IT services that drive digital transformation across all industries",
    "Stvoriti tehnološki ekosistem koji omogućuje beskonačne mogućnosti za klijente i unapređuje kvalitet života ljudi":
        "To create a technological ecosystem that opens up endless possibilities for clients and improves people's quality of life",
    "Biti prepoznat kao najpouzdaniji i najkreativniji partner za digitalne potrebe klijenata, stvarajući dugoročne i održive poslovne odnose.":
        "To be recognized as the most reliable and creative partner for clients' digital needs, building long-term and sustainable business relationships.",
    "Transformisati način na koji se koristi tehnologija, stvarajući intuitivna, sigurna i pristupačna rešenja koja svakodnevno olakšavaju život ljudima.":
        "To transform the way technology is used by creating intuitive, secure and accessible solutions that make people's everyday lives easier.",
    "Izgraditi kulturu inovacije i saradnje koja podstiče talentovane pojedince da ostvare svoj puni potencijal i donose revolucionarne ideje na tržište.":
        "To build a culture of innovation and collaboration that empowers talented individuals to reach their full potential and bring revolutionary ideas to market.",

    # --- Services sekcija ---
    "Pružamo kompletnu uslugu u oblasti IT. Sve na jednom mestu!":
        "We provide complete IT services. Everything in one place!",
    "Održavanje i servis računara": "Computer maintenance and repair",
    "Vaš pouzdan partner za besprekorno digitalno iskustvo.": "Your reliable partner for a flawless digital experience.",
    "Održavanje Servera i Virtualizacija": "Server maintenance and virtualization",
    "Optimizacija Vaše Poslovne Infrastrukture": "Optimization of your business infrastructure",
    "Čuvanje i bezbednost vaših podataka su naš prioritet": "Storing and securing your data is our priority",
    "Temelj vašeg digitalnog uspeha i bezbednog rada": "The foundation of your digital success and secure operations",
    "VEB Dizajn - Dizajniranje i razvoj veb sajtova": "Web design - designing and developing websites",
    "Moderna Veb rešenja su postala jedan od ključnih faktora za uspešno poslovanje":
        "Modern web solutions have become one of the key factors for successful business",
    "Desktop ili veb aplikacije, vaš ključ za digitalni napredak.":
        "Desktop or web applications - your key to digital progress.",

    # --- CTA ---
    "Sve što je potrebno za pouzdano, sigurno i savremeno poslovanje!":
        "Everything you need for reliable, secure and modern operations!",
    "Ukoliko smatrate da je potrebno da stručno lice proveri vašu IT infrastrukturu, ili da da predlog unapređenja vašeg IT sistem, pozovite nas na besplatne konsultacije!":
        "If you feel an expert should review your IT infrastructure or suggest improvements to your IT system, call us for a free consultation!",
    "Zakažite sastanak": "Schedule a meeting",

    # --- On Focus / Testiranje bezbednosti ---
    "Testiranje bezbednosti": "Security testing",
    "Zaštita vaše digitalne imovine": "Protecting your digital assets",
    "Pružamo testiranje sigurnosti IT sistema kako bismo identifikovali potencijalne ranjivosti i osigurali da vaša digitalna imovina bude zaštićena od napada i pretnji.":
        "We provide IT systems security testing to identify potential vulnerabilities and ensure your digital assets are protected from attacks and threats.",
    "Vršimo ispitivanja i analizu sistema kako bi identifikovali ranjivosti u vašem IT okruženju, uključujući mrežne sisteme, aplikacije, baze podataka i infrastrukturu.":
        "We test and analyze systems to identify vulnerabilities in your IT environment, including networks, applications, databases and infrastructure.",
    "Naš cilj je osigurati da vaši IT sistemi budu otporni na napade, sigurni od neovlašćenog pristupa i pouzdani u zaštiti vaših osetljivih informacija.":
        "Our goal is to ensure your IT systems are resilient to attacks, safe from unauthorized access and reliable in protecting your sensitive information.",
    "Kontaktirajte nas": "Contact us",

    # --- Consulting tabovi ---
    "Vaša zaštita u digitalnom svetu": "Your protection in the digital world",
    "Implementiramo i održavamo bezbednosne standarde prema ISO 27001 standardu":
        "We implement and maintain security standards according to the ISO 27001 standard",
    "Osiguravamo da su informacije naših klijenata budu zaštićene od svih mogućih prijetnji,":
        "We ensure our clients' information is protected from all possible threats,",
    "Implementiramo stroge kontrole pristupa, enkripciju podataka, redovne sigurnosne provere i obuke osoblja":
        "We implement strict access controls, data encryption, regular security audits and staff training",
    "Pročitajte više": "Read more",
    "Vaša sigurnost u svakoj situaciji": "Your security in any situation",
    "Implementiramo zahteve kontinuiteta poslovanja prema ISO 22301 standardu":
        "We implement business continuity requirements according to the ISO 22301 standard",
    "ISO 22301 je međunarodni standard koji definiše zahteve za upravljanje kontinuitetom poslovanja, uključujući planiranje, implementaciju, održavanje i unapređenje sistema kontinuiteta poslovanja":
        "ISO 22301 is an international standard that defines requirements for business continuity management, including planning, implementation, maintenance and improvement of the business continuity system",
    "Identifikujemo ključne procese, resurse i rizike i razvijamo strategije za njihovo očuvanje i obnovu.":
        "We identify key processes, resources and risks and develop strategies for their preservation and recovery.",
    "Kroz implementaciju strogo planiranje infrastrukture, redovne vežbe i testiranja, kontinuirano praćenje i poboljšavanje, osiguravamo da naši klijenti budu spremni suočiti se s izazovima i očuvati kontinuitet poslovanja u svakoj situaciji.":
        "Through rigorous infrastructure planning, regular drills and testing, and continuous monitoring and improvement, we ensure our clients are ready to face challenges and maintain business continuity in any situation.",
    "Vaša zaštita od neizvesnosti": "Your protection against uncertainty",
    "Implementiramo zahteve upravljanja rizicima prema ISO 31000 standardu":
        "We implement risk management requirements according to the ISO 31000 standard",
    "ISO 31000 je međunarodni standard koji pruža okvir za upravljanje rizicima u organizaciji, uključujući identifikaciju, procenu, upravljanje i praćenje rizika":
        "ISO 31000 is an international standard that provides a framework for risk management in an organization, including risk identification, assessment, treatment and monitoring",
    "pomažemo našim klijentima da prepoznaju potencijalne prijetnje, identifikuju ranjive tačke i razviju strategije za minimiziranje i upravljanje rizicima.":
        "we help our clients recognize potential threats, identify weak points and develop strategies to minimize and manage risks.",
    "Informacione tehnologije – upravljanje uslugama": "Information technology - service management",
    "vaš partnera za implementaciju ISO/IEC 20000-1 standarda": "your partner for implementing the ISO/IEC 20000-1 standard",
    "Naša usluga konsultacija za implementaciju ISO/IEC 20000-1 osmišljena je kako bismo vam pomogli da vaša organizacija postigne izvrsnost u upravljanju IT uslugama":
        "Our consulting service for ISO/IEC 20000-1 implementation is designed to help your organization achieve excellence in IT service management",
    "Sa našim iskusnim timom stručnjaka, pružamo sveobuhvatnu podršku u procesu implementacije ovog važnog standarda":
        "With our experienced team of experts, we provide comprehensive support throughout the implementation of this important standard",
    "Naše usluge uključuju procenu trenutnog stanja, izradu plana implementacije, obuku zaposlenih, razvoj dokumentacije, kao i podršku tokom sertifikacije":
        "Our services include current-state assessment, implementation planning, employee training, documentation development, and support during certification",

    # --- Obuke (testimonials) ---
    "Osnove informacione bezbednosti": "Information security fundamentals",
    "Ova obuka pruža osnovna znanja o konceptima informacione bezbednosti, uključujući prepoznavanje pretnji, identifikaciju ranjivosti, i osnove zaštite podataka.":
        "This training provides basic knowledge of information security concepts, including threat recognition, vulnerability identification, and data protection fundamentals.",
    "Phishing simulacije": "Phishing simulations",
    "Phishing napadi predstavljaju veliku pretnju organizacijama. Kroz simulacije phishing napada, zaposleni mogu naučiti kako da prepoznaju sumnjive e-mail-ove ili linkove i kako da se zaštite od njih.":
        "Phishing attacks are a major threat to organizations. Through phishing simulations, employees learn how to recognize suspicious emails or links and how to protect themselves.",
    "Bezbedno korišćenje Interneta i društvenih mreža": "Safe use of the Internet and social networks",
    "Ova obuka fokusira se na pravilno korišćenje interneta i društvenih mreža kako bi se smanjio rizik od deljenja ličnih ili osetljivih informacija":
        "This training focuses on the proper use of the Internet and social networks to reduce the risk of sharing personal or sensitive information",
    "Sigurno rukovanje podacima": "Secure data handling",
    "Zaposleni treba da budu svesni kako pravilno rukovati osetljivim podacima, kao što su lični podaci klijenata ili poslovne tajne. Obuka o sigurnom rukovanju podacima obuhvata pravilno skladištenje, deljenje i brisanje podataka.":
        "Employees should know how to properly handle sensitive data such as client personal data or business secrets. Secure data handling training covers proper storage, sharing and deletion of data.",
    "Zaštita mobilnih uređaja": "Mobile device protection",
    "S obzirom na sve veću upotrebu mobilnih uređaja u poslovnom okruženju, važno je da zaposleni budu obučeni o bezbednosnim merama koje treba preduzeti kako bi zaštitili podatke na svojim mobilnim uređajima.":
        "Given the growing use of mobile devices in the workplace, it is important that employees are trained on the security measures needed to protect the data on their mobile devices.",
    "Politike informacione bezbednosti": "Information security policies",
    "Zaposleni treba da budu upoznati sa internim politikama i procedurama informacione bezbednosti organizacije, uključujući pravila za kreiranje i čuvanje jakih lozinki, upotrebu VPN-a, i pristup osetljivim informacijama.":
        "Employees should be familiar with the organization's internal information security policies and procedures, including rules for creating and storing strong passwords, using a VPN, and accessing sensitive information.",
    "Redovno ažuriranje znanja": "Regular knowledge updates",
    "Informaciona bezbednost je dinamično polje, pa je redovno ažuriranje znanja od suštinskog značaja. Organizacije treba da obezbede kontinuirane obuke i informacije o novim pretnjama i najboljim praksama u oblasti informacione bezbednosti.":
        "Information security is a dynamic field, so regularly updating knowledge is essential. Organizations should provide continuous training and information about new threats and best practices in information security.",

    # --- Contact ---
    "Naš tim stručnjaka će rado odgovoriti i na najteže izazove":
        "Our team of experts will gladly take on even the toughest challenges",
    "Adresa:": "Address:",
    "Email:": "Email:",
    "Mobilni:": "Mobile:",
    "Telefon:": "Phone:",
    "Vaše ime": "Your name",
    "Vaš email": "Your email",
    "Naslov": "Subject",
    "Poruka": "Message",
    "Učitavanje": "Loading",
    "Vaša poruka je poslata. Hvala!": "Your message has been sent. Thank you!",
    "Pošalji poruku": "Send message",
}

# =========================== RUSSIAN ===========================
RU = {
    "Početna": "Главная",
    "O nama": "О нас",
    "Usluge": "Услуги",
    "Održavanje računara": "Обслуживание компьютеров",
    "Projektovanje i izvođenje mrežne infrastrukturea": "Проектирование и развёртывание сетевой инфраструктуры",
    "Projektovanje i izvođenje mrežne infrastrukture": "Проектирование и развёртывание сетевой инфраструктуры",
    "Održavanje servera i virtuelizacija": "Обслуживание серверов и виртуализация",
    "Data storage": "Хранение данных",
    "WEB dizajn": "Веб-дизайн",
    "WEB designe": "Веб-дизайн",
    "Razvoj aplikacija i baza podataka": "Разработка приложений и баз данных",
    "IT Konsalting": "ИТ-консалтинг",
    "Bezbednost informacija": "Информационная безопасность",
    "Kontinuitet poslovanja": "Непрерывность бизнеса",
    "Upravljanje rizicima": "Управление рисками",
    "Upravljanje IT uslugama": "Управление ИТ-услугами",
    "Bezbednost": "Безопасность",
    "Testiranje bezbednosti IT sistema": "Тестирование безопасности ИТ-систем",
    "Programi": "Программы",
    "GeoBiz - za Geodetske firme": "GeoBiz — для геодезических компаний",
    "GeoDent - za Zubarske ordinacije": "GeoDent — для стоматологий",
    "GeoMedik - za klinike i bolnice": "GeoMedik — для клиник и больниц",
    "GeoErp - Poslovni softver": "GeoErp — Бизнес-ПО",
    "Obuke": "Обучение",
    "OBUKE": "ОБУЧЕНИЕ",
    "Kontakt": "Контакт",
    "Podrška": "Поддержка",

    "Korisni linkovi": "Полезные ссылки",
    "Sremska Mitrovica, Srbija": "Сремска-Митровица, Сербия",

    "Dobro došli u": "Добро пожаловать в",
    "Vaš IT oslonac u digitalnom svetu": "Ваша ИТ-опора в цифровом мире",

    "Misija": "Миссия",
    "Vrednosti": "Ценности",
    "Vizija": "Видение",
    "Omogućiti klijentima da ostvare svoje poslovne ciljeve kroz inovativna IT rešenja i usluge.":
        "Помогать клиентам достигать бизнес-целей с помощью инновационных ИТ-решений и услуг.",
    "Pružiti visokokvalitetne IT usluge koje unapređuju produktivnost i efikasnost klijenata.":
        "Предоставлять высококачественные ИТ-услуги, повышающие продуктивность и эффективность клиентов.",
    "Želimo da postanemo partneri klijenata u njihovom digitalnom transformacijskom putovanju kroz prilagođena IT rešenja.":
        "Мы хотим стать партнёрами клиентов на пути цифровой трансформации с помощью индивидуальных ИТ-решений.",
    "Težimo da izgradimo pouzdanu reputaciju kao lider u industriji koji pruža pouzdane i sigurne IT usluge.":
        "Мы стремимся завоевать репутацию надёжного лидера отрасли, предоставляющего надёжные и безопасные ИТ-услуги.",
    "Doprineti društvenoj i ekonomskoj dobrobiti kroz inovacije u tehnologiji i pravedno poslovanje.":
        "Вносить вклад в социальное и экономическое благополучие через технологические инновации и честный бизнес.",
    "Kvaliteta: Posvećenost pružanju visokokvalitetnih proizvoda i usluga koji nadmašuju očekivanja klijenata":
        "Качество: приверженность предоставлению высококачественных продуктов и услуг, превосходящих ожидания клиентов",
    "Inovacija: Stalna težnja za razvojem novih ideja, tehnologija i pristupa kako bi se unapredila konkurentnost i donele nove vrednosti klijentima.":
        "Инновации: постоянное стремление развивать новые идеи, технологии и подходы для повышения конкурентоспособности и создания новой ценности для клиентов.",
    "Integriteta: Poštovanje etičkih standarda, iskrenost, transparentnost i odgovornost u svim poslovnim aktivnostima.":
        "Честность: соблюдение этических стандартов, искренность, прозрачность и ответственность во всей деятельности.",
    "Partnerstva: Izgradnja dugoročnih partnerskih odnosa s klijentima, saradnicima i zajednicom kako bi se postigla obostrana korist i podržao održivi rast.":
        "Партнёрство: построение долгосрочных партнёрских отношений с клиентами, коллегами и сообществом ради взаимной выгоды и устойчивого роста.",
    "Klijentski fokus: Stavljanje klijenata u središte svih aktivnosti, slušanje njihovih potreba i prilagođavanje rešenja kako bi se osigurala njihova potpuna satisfakcija.":
        "Ориентация на клиента: клиент в центре всей деятельности, внимание к его потребностям и адаптация решений для полного удовлетворения.",
    "Društvena odgovornost: Posvećenost doprinosu društvenoj zajednici kroz održive prakse, podršku zajednici i društveno korporativno delovanje.":
        "Социальная ответственность: вклад в общество через устойчивые практики, поддержку сообщества и корпоративную социальную деятельность.",
    "Postati regionalni lider u pružanju inovativnih IT usluga koje podstiču digitalnu transformaciju u svim industrijama":
        "Стать региональным лидером в предоставлении инновационных ИТ-услуг, способствующих цифровой трансформации во всех отраслях",
    "Stvoriti tehnološki ekosistem koji omogućuje beskonačne mogućnosti za klijente i unapređuje kvalitet života ljudi":
        "Создать технологическую экосистему, открывающую безграничные возможности для клиентов и повышающую качество жизни людей",
    "Biti prepoznat kao najpouzdaniji i najkreativniji partner za digitalne potrebe klijenata, stvarajući dugoročne i održive poslovne odnose.":
        "Быть признанными самым надёжным и креативным партнёром по цифровым потребностям клиентов, строя долгосрочные и устойчивые отношения.",
    "Transformisati način na koji se koristi tehnologija, stvarajući intuitivna, sigurna i pristupačna rešenja koja svakodnevno olakšavaju život ljudima.":
        "Изменить то, как используется технология, создавая интуитивные, безопасные и доступные решения, облегчающие повседневную жизнь людей.",
    "Izgraditi kulturu inovacije i saradnje koja podstiče talentovane pojedince da ostvare svoj puni potencijal i donose revolucionarne ideje na tržište.":
        "Построить культуру инноваций и сотрудничества, которая помогает талантливым людям раскрыть потенциал и выводить на рынок революционные идеи.",

    "Pružamo kompletnu uslugu u oblasti IT. Sve na jednom mestu!":
        "Мы предоставляем полный спектр ИТ-услуг. Всё в одном месте!",
    "Održavanje i servis računara": "Обслуживание и ремонт компьютеров",
    "Vaš pouzdan partner za besprekorno digitalno iskustvo.": "Ваш надёжный партнёр для безупречной цифровой работы.",
    "Održavanje Servera i Virtualizacija": "Обслуживание серверов и виртуализация",
    "Optimizacija Vaše Poslovne Infrastrukture": "Оптимизация вашей бизнес-инфраструктуры",
    "Čuvanje i bezbednost vaših podataka su naš prioritet": "Хранение и безопасность ваших данных — наш приоритет",
    "Temelj vašeg digitalnog uspeha i bezbednog rada": "Основа вашего цифрового успеха и безопасной работы",
    "VEB Dizajn - Dizajniranje i razvoj veb sajtova": "Веб-дизайн — проектирование и разработка сайтов",
    "Moderna Veb rešenja su postala jedan od ključnih faktora za uspešno poslovanje":
        "Современные веб-решения стали одним из ключевых факторов успешного бизнеса",
    "Desktop ili veb aplikacije, vaš ključ za digitalni napredak.":
        "Десктопные или веб-приложения — ваш ключ к цифровому развитию.",

    "Sve što je potrebno za pouzdano, sigurno i savremeno poslovanje!":
        "Всё необходимое для надёжной, безопасной и современной работы!",
    "Ukoliko smatrate da je potrebno da stručno lice proveri vašu IT infrastrukturu, ili da da predlog unapređenja vašeg IT sistem, pozovite nas na besplatne konsultacije!":
        "Если вы считаете, что специалисту стоит проверить вашу ИТ-инфраструктуру или предложить улучшения, позвоните нам на бесплатную консультацию!",
    "Zakažite sastanak": "Назначить встречу",

    "Testiranje bezbednosti": "Тестирование безопасности",
    "Zaštita vaše digitalne imovine": "Защита ваших цифровых активов",
    "Pružamo testiranje sigurnosti IT sistema kako bismo identifikovali potencijalne ranjivosti i osigurali da vaša digitalna imovina bude zaštićena od napada i pretnji.":
        "Мы проводим тестирование безопасности ИТ-систем, чтобы выявить потенциальные уязвимости и обеспечить защиту ваших цифровых активов от атак и угроз.",
    "Vršimo ispitivanja i analizu sistema kako bi identifikovali ranjivosti u vašem IT okruženju, uključujući mrežne sisteme, aplikacije, baze podataka i infrastrukturu.":
        "Мы проверяем и анализируем системы, чтобы выявить уязвимости в вашей ИТ-среде, включая сети, приложения, базы данных и инфраструктуру.",
    "Naš cilj je osigurati da vaši IT sistemi budu otporni na napade, sigurni od neovlašćenog pristupa i pouzdani u zaštiti vaših osetljivih informacija.":
        "Наша цель — обеспечить устойчивость ваших ИТ-систем к атакам, защиту от несанкционированного доступа и надёжную защиту конфиденциальной информации.",
    "Kontaktirajte nas": "Свяжитесь с нами",

    "Vaša zaštita u digitalnom svetu": "Ваша защита в цифровом мире",
    "Implementiramo i održavamo bezbednosne standarde prema ISO 27001 standardu":
        "Мы внедряем и поддерживаем стандарты безопасности по ISO 27001",
    "Osiguravamo da su informacije naših klijenata budu zaštićene od svih mogućih prijetnji,":
        "Мы обеспечиваем защиту информации клиентов от всех возможных угроз,",
    "Implementiramo stroge kontrole pristupa, enkripciju podataka, redovne sigurnosne provere i obuke osoblja":
        "Мы внедряем строгий контроль доступа, шифрование данных, регулярные проверки безопасности и обучение персонала",
    "Pročitajte više": "Подробнее",
    "Vaša sigurnost u svakoj situaciji": "Ваша безопасность в любой ситуации",
    "Implementiramo zahteve kontinuiteta poslovanja prema ISO 22301 standardu":
        "Мы внедряем требования непрерывности бизнеса по стандарту ISO 22301",
    "ISO 22301 je međunarodni standard koji definiše zahteve za upravljanje kontinuitetom poslovanja, uključujući planiranje, implementaciju, održavanje i unapređenje sistema kontinuiteta poslovanja":
        "ISO 22301 — международный стандарт, определяющий требования к управлению непрерывностью бизнеса, включая планирование, внедрение, поддержку и улучшение системы непрерывности",
    "Identifikujemo ključne procese, resurse i rizike i razvijamo strategije za njihovo očuvanje i obnovu.":
        "Мы определяем ключевые процессы, ресурсы и риски и разрабатываем стратегии их сохранения и восстановления.",
    "Kroz implementaciju strogo planiranje infrastrukture, redovne vežbe i testiranja, kontinuirano praćenje i poboljšavanje, osiguravamo da naši klijenti budu spremni suočiti se s izazovima i očuvati kontinuitet poslovanja u svakoj situaciji.":
        "Благодаря тщательному планированию инфраструктуры, регулярным учениям и тестированию, постоянному мониторингу и улучшению мы обеспечиваем готовность клиентов к вызовам и непрерывность бизнеса в любой ситуации.",
    "Vaša zaštita od neizvesnosti": "Ваша защита от неопределённости",
    "Implementiramo zahteve upravljanja rizicima prema ISO 31000 standardu":
        "Мы внедряем требования управления рисками по стандарту ISO 31000",
    "ISO 31000 je međunarodni standard koji pruža okvir za upravljanje rizicima u organizaciji, uključujući identifikaciju, procenu, upravljanje i praćenje rizika":
        "ISO 31000 — международный стандарт, предоставляющий основу для управления рисками в организации, включая идентификацию, оценку, обработку и мониторинг рисков",
    "pomažemo našim klijentima da prepoznaju potencijalne prijetnje, identifikuju ranjive tačke i razviju strategije za minimiziranje i upravljanje rizicima.":
        "мы помогаем клиентам распознавать потенциальные угрозы, выявлять слабые места и разрабатывать стратегии минимизации и управления рисками.",
    "Informacione tehnologije – upravljanje uslugama": "Информационные технологии — управление услугами",
    "vaš partnera za implementaciju ISO/IEC 20000-1 standarda": "ваш партнёр по внедрению стандарта ISO/IEC 20000-1",
    "Naša usluga konsultacija za implementaciju ISO/IEC 20000-1 osmišljena je kako bismo vam pomogli da vaša organizacija postigne izvrsnost u upravljanju IT uslugama":
        "Наша консультационная услуга по внедрению ISO/IEC 20000-1 призвана помочь вашей организации достичь совершенства в управлении ИТ-услугами",
    "Sa našim iskusnim timom stručnjaka, pružamo sveobuhvatnu podršku u procesu implementacije ovog važnog standarda":
        "С нашей опытной командой специалистов мы предоставляем всестороннюю поддержку при внедрении этого важного стандарта",
    "Naše usluge uključuju procenu trenutnog stanja, izradu plana implementacije, obuku zaposlenih, razvoj dokumentacije, kao i podršku tokom sertifikacije":
        "Наши услуги включают оценку текущего состояния, разработку плана внедрения, обучение сотрудников, подготовку документации и поддержку при сертификации",

    "Osnove informacione bezbednosti": "Основы информационной безопасности",
    "Ova obuka pruža osnovna znanja o konceptima informacione bezbednosti, uključujući prepoznavanje pretnji, identifikaciju ranjivosti, i osnove zaštite podataka.":
        "Это обучение даёт базовые знания о концепциях информационной безопасности, включая распознавание угроз, выявление уязвимостей и основы защиты данных.",
    "Phishing simulacije": "Фишинг-симуляции",
    "Phishing napadi predstavljaju veliku pretnju organizacijama. Kroz simulacije phishing napada, zaposleni mogu naučiti kako da prepoznaju sumnjive e-mail-ove ili linkove i kako da se zaštite od njih.":
        "Фишинговые атаки — серьёзная угроза для организаций. С помощью фишинг-симуляций сотрудники учатся распознавать подозрительные письма и ссылки и защищаться от них.",
    "Bezbedno korišćenje Interneta i društvenih mreža": "Безопасное использование Интернета и соцсетей",
    "Ova obuka fokusira se na pravilno korišćenje interneta i društvenih mreža kako bi se smanjio rizik od deljenja ličnih ili osetljivih informacija":
        "Это обучение посвящено правильному использованию Интернета и социальных сетей для снижения риска раскрытия личной или конфиденциальной информации",
    "Sigurno rukovanje podacima": "Безопасная работа с данными",
    "Zaposleni treba da budu svesni kako pravilno rukovati osetljivim podacima, kao što su lični podaci klijenata ili poslovne tajne. Obuka o sigurnom rukovanju podacima obuhvata pravilno skladištenje, deljenje i brisanje podataka.":
        "Сотрудники должны уметь правильно обращаться с конфиденциальными данными, такими как персональные данные клиентов или коммерческая тайна. Обучение охватывает правильное хранение, передачу и удаление данных.",
    "Zaštita mobilnih uređaja": "Защита мобильных устройств",
    "S obzirom na sve veću upotrebu mobilnih uređaja u poslovnom okruženju, važno je da zaposleni budu obučeni o bezbednosnim merama koje treba preduzeti kako bi zaštitili podatke na svojim mobilnim uređajima.":
        "Учитывая растущее использование мобильных устройств в работе, важно обучать сотрудников мерам безопасности для защиты данных на их устройствах.",
    "Politike informacione bezbednosti": "Политики информационной безопасности",
    "Zaposleni treba da budu upoznati sa internim politikama i procedurama informacione bezbednosti organizacije, uključujući pravila za kreiranje i čuvanje jakih lozinki, upotrebu VPN-a, i pristup osetljivim informacijama.":
        "Сотрудники должны знать внутренние политики и процедуры информационной безопасности организации, включая правила создания и хранения надёжных паролей, использование VPN и доступ к конфиденциальной информации.",
    "Redovno ažuriranje znanja": "Регулярное обновление знаний",
    "Informaciona bezbednost je dinamično polje, pa je redovno ažuriranje znanja od suštinskog značaja. Organizacije treba da obezbede kontinuirane obuke i informacije o novim pretnjama i najboljim praksama u oblasti informacione bezbednosti.":
        "Информационная безопасность — динамичная область, поэтому регулярное обновление знаний крайне важно. Организациям следует обеспечивать непрерывное обучение и информирование о новых угрозах и лучших практиках.",

    "Naš tim stručnjaka će rado odgovoriti i na najteže izazove":
        "Наша команда экспертов с радостью примет даже самые сложные вызовы",
    "Adresa:": "Адрес:",
    "Email:": "Эл. почта:",
    "Mobilni:": "Мобильный:",
    "Telefon:": "Телефон:",
    "Vaše ime": "Ваше имя",
    "Vaš email": "Ваш email",
    "Naslov": "Тема",
    "Poruka": "Сообщение",
    "Učitavanje": "Загрузка",
    "Vaša poruka je poslata. Hvala!": "Ваше сообщение отправлено. Спасибо!",
    "Pošalji poruku": "Отправить сообщение",
}

# =========================== GERMAN ===========================
DE = {
    "Početna": "Startseite",
    "O nama": "Über uns",
    "Usluge": "Leistungen",
    "Održavanje računara": "Computerwartung",
    "Projektovanje i izvođenje mrežne infrastrukturea": "Planung und Aufbau der Netzwerkinfrastruktur",
    "Projektovanje i izvođenje mrežne infrastrukture": "Planung und Aufbau der Netzwerkinfrastruktur",
    "Održavanje servera i virtuelizacija": "Serverwartung & Virtualisierung",
    "Data storage": "Datenspeicherung",
    "WEB dizajn": "Webdesign",
    "WEB designe": "Webdesign",
    "Razvoj aplikacija i baza podataka": "Anwendungs- und Datenbankentwicklung",
    "IT Konsalting": "IT-Beratung",
    "Bezbednost informacija": "Informationssicherheit",
    "Kontinuitet poslovanja": "Geschäftskontinuität",
    "Upravljanje rizicima": "Risikomanagement",
    "Upravljanje IT uslugama": "IT-Service-Management",
    "Bezbednost": "Sicherheit",
    "Testiranje bezbednosti IT sistema": "Sicherheitstests von IT-Systemen",
    "Programi": "Software",
    "GeoBiz - za Geodetske firme": "GeoBiz – für Vermessungsfirmen",
    "GeoDent - za Zubarske ordinacije": "GeoDent – für Zahnarztpraxen",
    "GeoMedik - za klinike i bolnice": "GeoMedik – für Kliniken und Krankenhäuser",
    "GeoErp - Poslovni softver": "GeoErp – Unternehmenssoftware",
    "Obuke": "Schulungen",
    "OBUKE": "SCHULUNGEN",
    "Kontakt": "Kontakt",
    "Podrška": "Support",

    "Korisni linkovi": "Nützliche Links",
    "Sremska Mitrovica, Srbija": "Sremska Mitrovica, Serbien",

    "Dobro došli u": "Willkommen bei",
    "Vaš IT oslonac u digitalnom svetu": "Ihre IT-Stütze in der digitalen Welt",

    "Misija": "Mission",
    "Vrednosti": "Werte",
    "Vizija": "Vision",
    "Omogućiti klijentima da ostvare svoje poslovne ciljeve kroz inovativna IT rešenja i usluge.":
        "Kunden befähigen, ihre Geschäftsziele durch innovative IT-Lösungen und -Dienstleistungen zu erreichen.",
    "Pružiti visokokvalitetne IT usluge koje unapređuju produktivnost i efikasnost klijenata.":
        "Hochwertige IT-Dienstleistungen bieten, die Produktivität und Effizienz der Kunden steigern.",
    "Želimo da postanemo partneri klijenata u njihovom digitalnom transformacijskom putovanju kroz prilagođena IT rešenja.":
        "Wir möchten Partner unserer Kunden auf ihrem Weg der digitalen Transformation durch maßgeschneiderte IT-Lösungen werden.",
    "Težimo da izgradimo pouzdanu reputaciju kao lider u industriji koji pruža pouzdane i sigurne IT usluge.":
        "Wir streben einen vertrauenswürdigen Ruf als Branchenführer für zuverlässige und sichere IT-Dienste an.",
    "Doprineti društvenoj i ekonomskoj dobrobiti kroz inovacije u tehnologiji i pravedno poslovanje.":
        "Zum sozialen und wirtschaftlichen Wohl durch technologische Innovation und faires Geschäft beitragen.",
    "Kvaliteta: Posvećenost pružanju visokokvalitetnih proizvoda i usluga koji nadmašuju očekivanja klijenata":
        "Qualität: Engagement für hochwertige Produkte und Dienstleistungen, die die Erwartungen der Kunden übertreffen",
    "Inovacija: Stalna težnja za razvojem novih ideja, tehnologija i pristupa kako bi se unapredila konkurentnost i donele nove vrednosti klijentima.":
        "Innovation: Das ständige Bestreben, neue Ideen, Technologien und Ansätze zu entwickeln, um die Wettbewerbsfähigkeit zu steigern und Kunden neuen Mehrwert zu bieten.",
    "Integriteta: Poštovanje etičkih standarda, iskrenost, transparentnost i odgovornost u svim poslovnim aktivnostima.":
        "Integrität: Einhaltung ethischer Standards, Ehrlichkeit, Transparenz und Verantwortung in allen Geschäftsaktivitäten.",
    "Partnerstva: Izgradnja dugoročnih partnerskih odnosa s klijentima, saradnicima i zajednicom kako bi se postigla obostrana korist i podržao održivi rast.":
        "Partnerschaft: Aufbau langfristiger Partnerschaften mit Kunden, Partnern und der Gemeinschaft für gegenseitigen Nutzen und nachhaltiges Wachstum.",
    "Klijentski fokus: Stavljanje klijenata u središte svih aktivnosti, slušanje njihovih potreba i prilagođavanje rešenja kako bi se osigurala njihova potpuna satisfakcija.":
        "Kundenfokus: Den Kunden in den Mittelpunkt aller Aktivitäten stellen, seine Bedürfnisse anhören und Lösungen anpassen, um volle Zufriedenheit zu gewährleisten.",
    "Društvena odgovornost: Posvećenost doprinosu društvenoj zajednici kroz održive prakse, podršku zajednici i društveno korporativno delovanje.":
        "Soziale Verantwortung: Engagement für die Gemeinschaft durch nachhaltige Praktiken, Unterstützung der Gemeinschaft und gesellschaftliches Handeln.",
    "Postati regionalni lider u pružanju inovativnih IT usluga koje podstiču digitalnu transformaciju u svim industrijama":
        "Regionaler Marktführer für innovative IT-Dienste werden, die die digitale Transformation in allen Branchen vorantreiben",
    "Stvoriti tehnološki ekosistem koji omogućuje beskonačne mogućnosti za klijente i unapređuje kvalitet života ljudi":
        "Ein technologisches Ökosystem schaffen, das Kunden unendliche Möglichkeiten eröffnet und die Lebensqualität der Menschen verbessert",
    "Biti prepoznat kao najpouzdaniji i najkreativniji partner za digitalne potrebe klijenata, stvarajući dugoročne i održive poslovne odnose.":
        "Als zuverlässigster und kreativster Partner für die digitalen Bedürfnisse der Kunden anerkannt werden und langfristige, nachhaltige Beziehungen aufbauen.",
    "Transformisati način na koji se koristi tehnologija, stvarajući intuitivna, sigurna i pristupačna rešenja koja svakodnevno olakšavaju život ljudima.":
        "Die Art und Weise verändern, wie Technologie genutzt wird, durch intuitive, sichere und zugängliche Lösungen, die den Alltag der Menschen erleichtern.",
    "Izgraditi kulturu inovacije i saradnje koja podstiče talentovane pojedince da ostvare svoj puni potencijal i donose revolucionarne ideje na tržište.":
        "Eine Kultur der Innovation und Zusammenarbeit aufbauen, die talentierte Menschen ermutigt, ihr volles Potenzial auszuschöpfen und revolutionäre Ideen auf den Markt zu bringen.",

    "Pružamo kompletnu uslugu u oblasti IT. Sve na jednom mestu!":
        "Wir bieten umfassende IT-Dienstleistungen. Alles an einem Ort!",
    "Održavanje i servis računara": "Wartung und Reparatur von Computern",
    "Vaš pouzdan partner za besprekorno digitalno iskustvo.": "Ihr zuverlässiger Partner für ein reibungsloses digitales Erlebnis.",
    "Održavanje Servera i Virtualizacija": "Serverwartung und Virtualisierung",
    "Optimizacija Vaše Poslovne Infrastrukture": "Optimierung Ihrer Geschäftsinfrastruktur",
    "Čuvanje i bezbednost vaših podataka su naš prioritet": "Die Speicherung und Sicherheit Ihrer Daten hat für uns Priorität",
    "Temelj vašeg digitalnog uspeha i bezbednog rada": "Die Grundlage Ihres digitalen Erfolgs und sicheren Betriebs",
    "VEB Dizajn - Dizajniranje i razvoj veb sajtova": "Webdesign – Gestaltung und Entwicklung von Websites",
    "Moderna Veb rešenja su postala jedan od ključnih faktora za uspešno poslovanje":
        "Moderne Web-Lösungen sind zu einem Schlüsselfaktor für erfolgreiches Geschäft geworden",
    "Desktop ili veb aplikacije, vaš ključ za digitalni napredak.":
        "Desktop- oder Web-Anwendungen – Ihr Schlüssel zum digitalen Fortschritt.",

    "Sve što je potrebno za pouzdano, sigurno i savremeno poslovanje!":
        "Alles, was Sie für einen zuverlässigen, sicheren und modernen Betrieb brauchen!",
    "Ukoliko smatrate da je potrebno da stručno lice proveri vašu IT infrastrukturu, ili da da predlog unapređenja vašeg IT sistem, pozovite nas na besplatne konsultacije!":
        "Wenn ein Experte Ihre IT-Infrastruktur prüfen oder Verbesserungen vorschlagen soll, rufen Sie uns für eine kostenlose Beratung an!",
    "Zakažite sastanak": "Termin vereinbaren",

    "Testiranje bezbednosti": "Sicherheitstests",
    "Zaštita vaše digitalne imovine": "Schutz Ihrer digitalen Werte",
    "Pružamo testiranje sigurnosti IT sistema kako bismo identifikovali potencijalne ranjivosti i osigurali da vaša digitalna imovina bude zaštićena od napada i pretnji.":
        "Wir führen Sicherheitstests von IT-Systemen durch, um potenzielle Schwachstellen zu erkennen und Ihre digitalen Werte vor Angriffen und Bedrohungen zu schützen.",
    "Vršimo ispitivanja i analizu sistema kako bi identifikovali ranjivosti u vašem IT okruženju, uključujući mrežne sisteme, aplikacije, baze podataka i infrastrukturu.":
        "Wir testen und analysieren Systeme, um Schwachstellen in Ihrer IT-Umgebung zu erkennen – einschließlich Netzwerke, Anwendungen, Datenbanken und Infrastruktur.",
    "Naš cilj je osigurati da vaši IT sistemi budu otporni na napade, sigurni od neovlašćenog pristupa i pouzdani u zaštiti vaših osetljivih informacija.":
        "Unser Ziel ist es, Ihre IT-Systeme widerstandsfähig gegen Angriffe, sicher vor unbefugtem Zugriff und zuverlässig beim Schutz Ihrer sensiblen Daten zu machen.",
    "Kontaktirajte nas": "Kontaktieren Sie uns",

    "Vaša zaštita u digitalnom svetu": "Ihr Schutz in der digitalen Welt",
    "Implementiramo i održavamo bezbednosne standarde prema ISO 27001 standardu":
        "Wir implementieren und pflegen Sicherheitsstandards gemäß ISO 27001",
    "Osiguravamo da su informacije naših klijenata budu zaštićene od svih mogućih prijetnji,":
        "Wir stellen sicher, dass die Informationen unserer Kunden vor allen möglichen Bedrohungen geschützt sind,",
    "Implementiramo stroge kontrole pristupa, enkripciju podataka, redovne sigurnosne provere i obuke osoblja":
        "Wir implementieren strenge Zugriffskontrollen, Datenverschlüsselung, regelmäßige Sicherheitsprüfungen und Mitarbeiterschulungen",
    "Pročitajte više": "Mehr lesen",
    "Vaša sigurnost u svakoj situaciji": "Ihre Sicherheit in jeder Situation",
    "Implementiramo zahteve kontinuiteta poslovanja prema ISO 22301 standardu":
        "Wir implementieren Anforderungen an die Geschäftskontinuität gemäß ISO 22301",
    "ISO 22301 je međunarodni standard koji definiše zahteve za upravljanje kontinuitetom poslovanja, uključujući planiranje, implementaciju, održavanje i unapređenje sistema kontinuiteta poslovanja":
        "ISO 22301 ist ein internationaler Standard, der Anforderungen an das Business-Continuity-Management definiert, einschließlich Planung, Implementierung, Pflege und Verbesserung des Systems",
    "Identifikujemo ključne procese, resurse i rizike i razvijamo strategije za njihovo očuvanje i obnovu.":
        "Wir identifizieren Schlüsselprozesse, Ressourcen und Risiken und entwickeln Strategien zu deren Erhalt und Wiederherstellung.",
    "Kroz implementaciju strogo planiranje infrastrukture, redovne vežbe i testiranja, kontinuirano praćenje i poboljšavanje, osiguravamo da naši klijenti budu spremni suočiti se s izazovima i očuvati kontinuitet poslovanja u svakoj situaciji.":
        "Durch sorgfältige Infrastrukturplanung, regelmäßige Übungen und Tests sowie kontinuierliche Überwachung und Verbesserung stellen wir sicher, dass unsere Kunden auf Herausforderungen vorbereitet sind und die Geschäftskontinuität in jeder Situation wahren.",
    "Vaša zaštita od neizvesnosti": "Ihr Schutz vor Unsicherheit",
    "Implementiramo zahteve upravljanja rizicima prema ISO 31000 standardu":
        "Wir implementieren Anforderungen an das Risikomanagement gemäß ISO 31000",
    "ISO 31000 je međunarodni standard koji pruža okvir za upravljanje rizicima u organizaciji, uključujući identifikaciju, procenu, upravljanje i praćenje rizika":
        "ISO 31000 ist ein internationaler Standard, der einen Rahmen für das Risikomanagement in einer Organisation bietet, einschließlich Identifikation, Bewertung, Behandlung und Überwachung von Risiken",
    "pomažemo našim klijentima da prepoznaju potencijalne prijetnje, identifikuju ranjive tačke i razviju strategije za minimiziranje i upravljanje rizicima.":
        "wir helfen unseren Kunden, potenzielle Bedrohungen zu erkennen, Schwachstellen zu identifizieren und Strategien zur Minimierung und Steuerung von Risiken zu entwickeln.",
    "Informacione tehnologije – upravljanje uslugama": "Informationstechnologie – Service-Management",
    "vaš partnera za implementaciju ISO/IEC 20000-1 standarda": "Ihr Partner für die Implementierung des Standards ISO/IEC 20000-1",
    "Naša usluga konsultacija za implementaciju ISO/IEC 20000-1 osmišljena je kako bismo vam pomogli da vaša organizacija postigne izvrsnost u upravljanju IT uslugama":
        "Unser Beratungsservice zur Implementierung von ISO/IEC 20000-1 hilft Ihrer Organisation, Exzellenz im IT-Service-Management zu erreichen",
    "Sa našim iskusnim timom stručnjaka, pružamo sveobuhvatnu podršku u procesu implementacije ovog važnog standarda":
        "Mit unserem erfahrenen Expertenteam bieten wir umfassende Unterstützung bei der Implementierung dieses wichtigen Standards",
    "Naše usluge uključuju procenu trenutnog stanja, izradu plana implementacije, obuku zaposlenih, razvoj dokumentacije, kao i podršku tokom sertifikacije":
        "Unsere Leistungen umfassen die Ist-Analyse, die Erstellung eines Implementierungsplans, Mitarbeiterschulungen, die Dokumentationserstellung sowie Unterstützung während der Zertifizierung",

    "Osnove informacione bezbednosti": "Grundlagen der Informationssicherheit",
    "Ova obuka pruža osnovna znanja o konceptima informacione bezbednosti, uključujući prepoznavanje pretnji, identifikaciju ranjivosti, i osnove zaštite podataka.":
        "Diese Schulung vermittelt Grundkenntnisse der Informationssicherheit, einschließlich Bedrohungserkennung, Schwachstellenidentifikation und Grundlagen des Datenschutzes.",
    "Phishing simulacije": "Phishing-Simulationen",
    "Phishing napadi predstavljaju veliku pretnju organizacijama. Kroz simulacije phishing napada, zaposleni mogu naučiti kako da prepoznaju sumnjive e-mail-ove ili linkove i kako da se zaštite od njih.":
        "Phishing-Angriffe sind eine große Bedrohung für Organisationen. Durch Phishing-Simulationen lernen Mitarbeiter, verdächtige E-Mails oder Links zu erkennen und sich davor zu schützen.",
    "Bezbedno korišćenje Interneta i društvenih mreža": "Sichere Nutzung von Internet und sozialen Netzwerken",
    "Ova obuka fokusira se na pravilno korišćenje interneta i društvenih mreža kako bi se smanjio rizik od deljenja ličnih ili osetljivih informacija":
        "Diese Schulung konzentriert sich auf die richtige Nutzung von Internet und sozialen Netzwerken, um das Risiko der Weitergabe persönlicher oder sensibler Informationen zu verringern",
    "Sigurno rukovanje podacima": "Sicherer Umgang mit Daten",
    "Zaposleni treba da budu svesni kako pravilno rukovati osetljivim podacima, kao što su lični podaci klijenata ili poslovne tajne. Obuka o sigurnom rukovanju podacima obuhvata pravilno skladištenje, deljenje i brisanje podataka.":
        "Mitarbeiter sollten wissen, wie man sensible Daten wie personenbezogene Kundendaten oder Geschäftsgeheimnisse richtig handhabt. Die Schulung umfasst die korrekte Speicherung, Weitergabe und Löschung von Daten.",
    "Zaštita mobilnih uređaja": "Schutz mobiler Geräte",
    "S obzirom na sve veću upotrebu mobilnih uređaja u poslovnom okruženju, važno je da zaposleni budu obučeni o bezbednosnim merama koje treba preduzeti kako bi zaštitili podatke na svojim mobilnim uređajima.":
        "Angesichts der zunehmenden Nutzung mobiler Geräte im Arbeitsumfeld ist es wichtig, Mitarbeiter in den Sicherheitsmaßnahmen zu schulen, um die Daten auf ihren Geräten zu schützen.",
    "Politike informacione bezbednosti": "Richtlinien der Informationssicherheit",
    "Zaposleni treba da budu upoznati sa internim politikama i procedurama informacione bezbednosti organizacije, uključujući pravila za kreiranje i čuvanje jakih lozinki, upotrebu VPN-a, i pristup osetljivim informacijama.":
        "Mitarbeiter sollten die internen Richtlinien und Verfahren zur Informationssicherheit kennen, einschließlich Regeln zur Erstellung und Aufbewahrung starker Passwörter, zur VPN-Nutzung und zum Zugriff auf sensible Informationen.",
    "Redovno ažuriranje znanja": "Regelmäßige Wissensaktualisierung",
    "Informaciona bezbednost je dinamično polje, pa je redovno ažuriranje znanja od suštinskog značaja. Organizacije treba da obezbede kontinuirane obuke i informacije o novim pretnjama i najboljim praksama u oblasti informacione bezbednosti.":
        "Informationssicherheit ist ein dynamisches Feld, daher ist die regelmäßige Wissensaktualisierung entscheidend. Organisationen sollten kontinuierliche Schulungen und Informationen über neue Bedrohungen und Best Practices bereitstellen.",

    "Naš tim stručnjaka će rado odgovoriti i na najteže izazove":
        "Unser Expertenteam stellt sich gerne auch den schwierigsten Herausforderungen",
    "Adresa:": "Adresse:",
    "Email:": "E-Mail:",
    "Mobilni:": "Mobil:",
    "Telefon:": "Telefon:",
    "Vaše ime": "Ihr Name",
    "Vaš email": "Ihre E-Mail",
    "Naslov": "Betreff",
    "Poruka": "Nachricht",
    "Učitavanje": "Wird geladen",
    "Vaša poruka je poslata. Hvala!": "Ihre Nachricht wurde gesendet. Danke!",
    "Pošalji poruku": "Nachricht senden",
}

# =================== PODSTRANICE (tela, naslovi, meta) ===================
EN.update({
    # --- Titlovi ---
    "Održavanje i servis računara - GeoBiz": "Computer maintenance and repair - GeoBiz",
    "Projektovanje i izvođenje mrežne infrastrukture - GeoBiz": "Network infrastructure design & deployment - GeoBiz",
    "Održavanje servera i virtuelizacija - GeoBiz": "Server maintenance & virtualization - GeoBiz",
    # --- Meta opisi / keywords ---
    "Profesionalno održavanje i servis računara — vaš pouzdan partner za besprekorno digitalno iskustvo.":
        "Professional computer maintenance and repair - your reliable partner for a flawless digital experience.",
    "održavanje računara, servis računara, IT podrška, GeoBiz": "computer maintenance, computer repair, IT support, GeoBiz",
    "Projektovanje i izvođenje pouzdane i bezbedne mrežne infrastrukture — temelj vašeg digitalnog poslovanja.":
        "Design and deployment of a reliable and secure network infrastructure - the foundation of your digital business.",
    "mrežna infrastruktura, projektovanje mreža, LAN, WiFi, GeoBiz": "network infrastructure, network design, LAN, WiFi, GeoBiz",
    "Održavanje servera i virtuelizacija za optimizaciju vaše poslovne infrastrukture i pouzdan rad sistema.":
        "Server maintenance and virtualization to optimize your business infrastructure and ensure reliable system operation.",
    "održavanje servera, virtuelizacija, serverska infrastruktura, GeoBiz": "server maintenance, virtualization, server infrastructure, GeoBiz",
    "Bezbedno skladištenje i zaštita vaših podataka. GeoBiz data storage rešenja za pouzdano čuvanje i dostupnost poslovnih podataka.":
        "Secure storage and protection of your data. GeoBiz data storage solutions for reliable storage and availability of business data.",
    "data storage, skladištenje podataka, backup, GeoBiz": "data storage, data backup, GeoBiz",
    "Moderna veb rešenja — dizajn i razvoj veb sajtova koji unapređuju vaše poslovanje i prisustvo na internetu.":
        "Modern web solutions - design and development of websites that improve your business and online presence.",
    "Razvoj prilagođenih web, desktop i mobilnih aplikacija i baza podataka koji ubrzavaju i unapređuju vaše poslovanje.":
        "Development of custom web, desktop and mobile applications and databases that accelerate and improve your business.",
    "Implementacija i održavanje bezbednosti informacija prema ISO 27001 — zaštita vaših podataka u digitalnom svetu.":
        "Implementation and maintenance of information security according to ISO 27001 - protecting your data in the digital world.",
    "Implementacija kontinuiteta poslovanja prema ISO 22301 — vaša sigurnost i spremnost u svakoj situaciji.":
        "Business continuity implementation according to ISO 22301 - your security and readiness in any situation.",
    "Konsultacije za implementaciju ISO/IEC 20000-1 — izvrsnost u upravljanju IT uslugama vaše organizacije.":
        "Consulting for ISO/IEC 20000-1 implementation - excellence in IT service management for your organization.",
    "Upravljanje rizicima prema ISO 31000 — identifikacija, procena i smanjenje rizika u vašoj organizaciji.":
        "Risk management according to ISO 31000 - identification, assessment and reduction of risks in your organization.",
    "Testiranje bezbednosti IT sistema — identifikacija ranjivosti i zaštita vaše digitalne imovine od napada i pretnji.":
        "IT systems security testing - identifying vulnerabilities and protecting your digital assets from attacks and threats.",
    "GeoBiz kontakt, IT podrška, Sremska Mitrovica, office@geo-biz.com": "GeoBiz contact, IT support, Sremska Mitrovica, office@geo-biz.com",
    # --- Breadcrumbs / kratki naslovi ---
    "Održavanje računara": "Computer maintenance",
    "Projektovanje i izvođenje mreža": "Network design & deployment",
    "Održavanje servera": "Server maintenance",
    "Optimizacija vaše poslovne infrastrukture": "Optimization of your business infrastructure",
    "Vaš ključ za digitalni napredak": "Your key to digital progress",
    "Vaš pouzdan partner za besprekorno digitalno iskustvo": "Your reliable partner for a flawless digital experience",
    "Temelj vašeg digitalnog uspeha": "The foundation of your digital success",
    "Ogledalo vaše kompanije": "The mirror of your company",
    "Čuvanje vaših digitalnih podataka": "Storing your digital data",
    "Zaštitite vaše poslovanje": "Protect your business",
    "Unapređenje Sistema kontinuiteta poslovanja": "Improving the business continuity system",
    # --- Liste / kratke stavke ---
    "Naše usluge uključuju:": "Our services include:",
    "To uključuje redovno:": "This includes regular:",
    "To uključuje zaštitu podataka od:": "This includes protecting data from:",
    "Pružamo redovno:": "We regularly provide:",
    "Koristimo najsavremenije alate i tehnike, uključujući:": "We use state-of-the-art tools and techniques, including:",
    "Ažuriranje softvera": "Software updates",
    "Praćenje performansi": "Performance monitoring",
    "Praćenje rizika": "Risk monitoring",
    "Rešavanje problema i preventivno održavanje radi sprečavanja budućih problema":
        "Troubleshooting and preventive maintenance to avoid future problems",
    "Rešavanje problema kako bismo osigurali kontinuiranu dostupnost vaših aplikacija i podataka":
        "Troubleshooting to ensure continuous availability of your applications and data",
    "Održavanje servera": "Server maintenance",
    "Održavanje i": "Maintenance and",
    "Korisničko iskustvo": "User experience",
    "Optimizovanost za različite uređaje": "Optimization for various devices",
    "Optimizacija za pretraživače": "Search engine optimization",
    "Aplikacija za mobilne uređaje": "Mobile applications",
    "Etičko hakovanje": "Ethical hacking",
    "Otklanjanje uočenih ranjivosti": "Remediation of identified vulnerabilities",
    "Otklanjanje uočenih slabosti": "Remediation of identified weaknesses",
    "Poboljšanje sistema": "System improvement",
    "Oštećenja": "Damage",
    "Neovlaštenog pristupa": "Unauthorized access",
    "Detaljan izveštaj i predlog unapređenja sistema": "Detailed report and system improvement proposal",
    "Detaljni izveštaji sa predlogom mera": "Detailed reports with proposed measures",
    "Metabase - izveštaji": "Metabase - reports",
    "Poverljivost i dostupnost podataka vaših klijenata": "Confidentiality and availability of your clients' data",
    "upravljanja informacionom bezbednošću u okviru organizacije": "managing information security within the organization",
    "Kao i podršku tokom sertifikacije": "As well as support during certification",
    "i druge metode kako bismo otkrili i rešili potencijalne sigurnosne rupe.":
        "and other methods to detect and fix potential security gaps.",
    "Radimo sa strašću kako bismo stvorili rješenja koja donose stvarnu vrednost.":
        "We work with passion to create solutions that deliver real value.",
    "Naš tim web dizajnera koristi svoje stručno znanje i kreativnost kako bi kreirao dizajn koji odgovara potrebama i preferencijama klijenta, uzimajući u obzir aspekte kao što su":
        "Our web designers use their expertise and creativity to create a design that matches the client's needs and preferences, taking into account aspects such as",
    "Naš tim stručnjaka posvećen je razvoju prilagođenih baza podataka i aplikacija koje zadovoljavaju specifične potrebe i zahteve naših klijenata. Počevši od:":
        "Our team of experts is dedicated to developing custom databases and applications that meet the specific needs and requirements of our clients. Starting from:",
    "Naša posvećenost bezbednosti informacija obuhvata sve aspekte vašeg poslovanja, uključujući:":
        "Our commitment to information security covers all aspects of your business, including:",
    "Naša posvećenost upravljanju rizicima obuhvata sve aspekte našeg poslovanja, uključujući:":
        "Our commitment to risk management covers all aspects of our business, including:",
    "ISO 27001 je standard koji definiše zahteve za:": "ISO 27001 is a standard that defines requirements for:",
    "ISO 22301 je međunarodni standard koji definiše zahteve za upravljanje kontinuitetom poslovanja, uključujući":
        "ISO 22301 is an international standard that defines requirements for business continuity management, including",
    "ISO 31000 je međunarodni standard koji pruža okvir za upravljanje rizicima u organizaciji, uključujući:":
        "ISO 31000 is an international standard that provides a framework for risk management in an organization, including:",
    "U zavisnosti od veličine vašeg IT sistema, složenosti infrastrukture, broja korisnika, nudimo vam konkurentne cene:":
        "Depending on the size of your IT system, infrastructure complexity and number of users, we offer competitive prices:",
    "do 10 računara": "up to 10 computers",
    "od 10 do 20 računara": "from 10 to 20 computers",
    "20 računara + serveri": "20+ computers + servers",
    "Naša usluga podrazumeva implementaciju virtualnog okruženja najpopularnijih sistema za virtuelizaciju":
        "Our service includes implementing a virtual environment using the most popular virtualization systems",
    "Glavni cilj usluge data storage je osigurati pouzdanost, sigurnost i dostupnost sačuvanih podataka.":
        "The main goal of the data storage service is to ensure the reliability, security and availability of stored data.",
    # --- Veliki pasusi ---
    "Naša usluga održavanja računara obuhvata sve aspekte potrebne za održavanje vaših IT sastava u optimalnom stanju.":
        "Our computer maintenance service covers every aspect needed to keep your IT systems in optimal condition.",
    "današnjem digitalnom dobu, pouzdanost i performanse računarskih sistema su ključne za uspješno poslovanje. Upravo zato, u GeoBiz-u predani smo pružanju vrhunskih usluga održavanja računara koje osiguravaju besprekorno rad vaših IT sistema.":
        "In today's digital age, the reliability and performance of computer systems are crucial for successful business. That is exactly why, at GeoBiz, we are committed to providing top-tier computer maintenance services that ensure the flawless operation of your IT systems.",
    "Naš tim stručnjaka posvećen je održavanju i optimizaciji vaših računarskih resursa kako biste mogli maksimalno iskoristiti svoje IT investicije. Bez obzira jeste li malo preduzeće, srednje preduzeće ili velika korporacija, pružamo vam prilagođene usluge održavanja koje odgovaraju vašim specifičnim potrebama i zahtevima.":
        "Our team of experts is dedicated to maintaining and optimizing your computing resources so you can make the most of your IT investments. Whether you are a small business, a medium-sized company or a large corporation, we provide tailored maintenance services that match your specific needs and requirements.",
    "Naš cilj je osigurati kontinuiranu dostupnost, stabilnost i sigurnost vaših računarskih sistema, kako biste se mogli potpuno posvetiti svojim poslovnim aktivnostima. Kao vaš pouzdan partner za održavanje računara, GeoBiz vam pruža stručnost, iskustvo i predanost potrebne za postizanje izvrsnih rezultata. Kontaktirajte nas danas i osigurajte da vaši računarski sistemi uvek budu u vrhunskom stanju.":
        "Our goal is to ensure the continuous availability, stability and security of your computer systems so you can fully focus on your business activities. As your reliable partner for computer maintenance, GeoBiz provides the expertise, experience and dedication needed to achieve excellent results. Contact us today and make sure your computer systems are always in top condition.",
    "U današnjem povezanom svetu, stabilna i skalabilna mrežna infrastruktura ključna je za uspeh svake organizacije. U GeoBiz kompaniji stručnjaci smo za projekovanje i izvođenje mrežnih infrastruktura koje omogućuju sigurnu i pouzdanu komunikaciju te podržavaju rast i razvoj vašeg poslovanja.":
        "In today's connected world, a stable and scalable network infrastructure is key to the success of any organization. At GeoBiz we are experts in designing and deploying network infrastructures that enable secure and reliable communication and support the growth and development of your business.",
    "Naš tim stručnjaka poseduje bogato iskustvo u implementaciji različitih tehnologija i platformi kako bi se osiguralo da vaša mrežna infrastruktura bude optimalno projektovana i implementirana. Koristimo najnovije alate i prakse kako bismo osigurali visok nivo performansi, pouzdanosti i sigurnosti vaše mrežne infrastrukture.":
        "Our team of experts has extensive experience implementing various technologies and platforms to ensure your network infrastructure is optimally designed and deployed. We use the latest tools and practices to ensure a high level of performance, reliability and security of your network infrastructure.",
    "Kroz našu uslugu projektovanja i izvođenja mrežne infrastrukture, nudimo vam sve potrebno za uspešno vođenje vašeg poslovanja u digitalnom svijetu. Kontaktirajte nas danas i dopustite nam da vam pomognemo izgraditi temelj za vaš digitalni uspjeh.":
        "Through our network infrastructure design and deployment service, we offer everything you need to run your business successfully in the digital world. Contact us today and let us help you build the foundation for your digital success.",
    "U današnjem digitalnom dobu, poslovna infrastruktura mora biti pouzdana, skalabilna i efikasna kako bi podržala rast i razvoj organizacije. U kompaniji GeoBiz, specijalizovani smo za pružanje usluga održavanja servera i virtualizacije koje omogućuju optimizaciju vaše IT infrastrukture.":
        "In today's digital age, business infrastructure must be reliable, scalable and efficient to support the growth and development of an organization. At GeoBiz, we specialize in server maintenance and virtualization services that enable the optimization of your IT infrastructure.",
    "Naš tim stručnjaka posvećen je održavanju i upravljanju vašim serverskim okruženjem kako biste se mogli potpuno posvetiti svojim poslovnim aktivnostima.":
        "Our team of experts is dedicated to maintaining and managing your server environment so you can fully focus on your business activities.",
    "Naš tim stručnjaka posvećen je održavanju i upravljanju vašim serverskim okruženjem kako biste se mogli potpuno posvetiti svojim poslovnim aktivnostima. Pružamo redovno održavanje servera, nadzor performansi, sigurnosne provere i rješavanje problema kako bismo osigurali kontinuiranu dostupnost vaših aplikacija i podataka.":
        "Our team of experts is dedicated to maintaining and managing your server environment so you can fully focus on your business activities. We provide regular server maintenance, performance monitoring, security checks and troubleshooting to ensure the continuous availability of your applications and data.",
    "Uz to, nudimo i usluge virtualizacije koje vam omogućuju iskorišćavanje punog potencijala vaše serverske infrastrukture. Virtualizacija omogućuje optimizaciju resursa, smanjenje troškova i povećanje skalabilnosti, pružajući vam fleksibilnost koja vam je potrebna za prilagođavanje promenjivim poslovnim zahtevima.":
        "In addition, we offer virtualization services that let you harness the full potential of your server infrastructure. Virtualization optimizes resources, reduces costs and increases scalability, giving you the flexibility you need to adapt to changing business requirements.",
    "Kao vaš pouzdan partner za održavanje servera i virtualizaciju, kompanija GeoBiz pruža vam stručnost i podršku potrebnu za postizanje izvrsnih rezultata. Kontaktirajte nas danas i osigurajte da vaša poslovna infrastruktura bude spremna za budućnost.":
        "As your reliable partner for server maintenance and virtualization, GeoBiz provides the expertise and support needed to achieve excellent results. Contact us today and make sure your business infrastructure is ready for the future.",
    "Kontaktirajte nas danas i osigurajte da vaša poslovna infrastruktura bude spremna za budućnost.":
        "Contact us today and make sure your business infrastructure is ready for the future.",
    "VMware vSphere je platforma za virtualizaciju podataka koja omogućuje stvaranje i upravljanje virtualnim mašinama. VMware ESXi je hipervizor koji se koristi kao osnova za virtualizaciju u vSphere okruženju.":
        "VMware vSphere is a virtualization platform that enables the creation and management of virtual machines. VMware ESXi is a hypervisor used as the foundation for virtualization in the vSphere environment.",
    "Hyper-V je Microsoftova platforma za virtualizaciju koja omogućuje stvaranje i upravljanje virtualnim mašinama na Windows okruženju.":
        "Hyper-V is Microsoft's virtualization platform that enables the creation and management of virtual machines in a Windows environment.",
    "VirtualBox je besplatna open-source platforma za virtualizaciju koja podržava stvaranje virtualnih mašina na različitim operativnim sustavima, uključujući Windows, Linux, Mac OS X i druge.":
        "VirtualBox is a free, open-source virtualization platform that supports creating virtual machines on various operating systems, including Windows, Linux, Mac OS X and others.",
    "KVM je hipervizor otvorenog koda koji se koristi u Linux okruženju za virtualizaciju operativnih sistema.":
        "KVM is an open-source hypervisor used in the Linux environment to virtualize operating systems.",
    "XenServer je platforma za virtualizaciju koju razvija Citrix Systems, koja omogućuje stvaranje i upravljanje virtualnim mašinama i podržava različite operativne sisteme.":
        "XenServer is a virtualization platform developed by Citrix Systems that enables the creation and management of virtual machines and supports various operating systems.",
    "Usluga data storage predstavlja pružanje kapaciteta i infrastrukture za čuvanje podataka u digitalnom formatu. Ova usluga omogućuje korisnicima da sigurno čuvaju svoje podatke na udaljenim serverima ili skladištima, pristupaju im kad god je potrebno i dele ih s drugima prema potrebi.":
        "Data storage is the provision of capacity and infrastructure for storing data in digital format. This service allows users to securely store their data on remote servers or storage systems, access it whenever needed and share it with others as required.",
    "Usluga data storage igra ključnu ulogu u modernom informacionom društvu, omogućujući organizacijama i pojedincima da pravilno upravljaju, dele i koriste svoje podatke u svakodnevnom poslovanju i životu.":
        "Data storage plays a key role in modern information society, enabling organizations and individuals to properly manage, share and use their data in everyday business and life.",
    "Usluga data storage može biti implementirana na različite načine, uključujući lokalno čuvanje podataka na vlastitim NAS serverima, korišćenje cloud storage-a kod pružaoca usluga cloud computinga, ili kombinaciju oba pristupa. Korisnici mogu birati između različitih modela čuvanja podataka, kao što su lokalno, cloud ili kombinovano, zavisno o njihovim specifičnim potrebama i zahtevima.":
        "Data storage can be implemented in various ways, including local storage on your own NAS servers, using cloud storage from a cloud computing provider, or a combination of both. Users can choose between different storage models - local, cloud or hybrid - depending on their specific needs and requirements.",
    "Usluga web dizajna obuhvata proces stvaranja i oblikovanja estetski privlačnih, funkcionalnih i korisnički orijentisanih web stranica. Ova usluga uključuje usku saradnju između dizajnera i klijenata kako bi se stvorio online identitet koji odražava brend, ciljeve i vrednosti klijenta.":
        "Web design covers the process of creating and shaping aesthetically appealing, functional and user-oriented websites. This service involves close collaboration between designers and clients to create an online identity that reflects the client's brand, goals and values.",
    "Usluga web dizajna obuhvata sve korake od početnog planiranja i konceptualizacije do implementacije i testiranja web stranice. Naši dizajneri rade na stvaranju jedinstvenih i privlačnih dizajna koji privlače pažnju posetilaca i podstiču ih na interakciju sa sadržajem.":
        "Web design covers all steps from initial planning and conceptualization to the implementation and testing of the website. Our designers work to create unique and appealing designs that capture visitors' attention and encourage them to interact with the content.",
    "Cilj nam je stvoriti web stranice koja pružaju pozitivno korisničko iskustvo, olakšava navigaciju, podstiče angažman korisnika i doprinosi postizanju poslovnih ciljeva klijenta. , promociji usluga ili deljenju informacija.":
        "Our goal is to create websites that provide a positive user experience, ease navigation, encourage user engagement and help achieve the client's business goals, whether promoting services or sharing information.",
    "U GeoBiz kompaniji specijalizovani smo jedinstveno kreiranje baza i aplikacija koje podstiču digitalni napredak i unapređuju poslovanje naših klijenata.":
        "At GeoBiz we specialize in creating unique databases and applications that drive digital progress and improve our clients' business.",
    "Kreiramo aplikacije koje su prilagođenje vašem poslovanju, aplikacije koje će ubrzati vaše poslovanje, olakšati rad i omogućiti menadžmentu brže donošenje pravih odluka na osnovu izveštaja koje pravimo.":
        "We create applications tailored to your business - applications that speed up your operations, make work easier and enable management to make the right decisions faster based on the reports we build.",
    "Kroz naše usluge, klijenti dobijaju prilagođene baze podataka koje omogućuju efikasno upravljanje i analizu podataka, kao i aplikacije koje poboljšavaju produktivnost, automatizuju procese i poboljšavaju korisničko iskustvo.":
        "Through our services, clients receive custom databases that enable efficient data management and analysis, as well as applications that improve productivity, automate processes and enhance the user experience.",
    "Nezavisno o veličini vaše kompanije ili industrije, razvićemo za vas potrebne alate i resurse za uspešno vođenje vašeg poslovanja u digitalnom svetu. Kontaktirajte nas danas i otkrijte kako možemo transformisati vaše poslovanje putem naprednih tehnoloških rešenja.":
        "Regardless of the size of your company or industry, we will develop the tools and resources you need to run your business successfully in the digital world. Contact us today and discover how we can transform your business through advanced technological solutions.",
    "U GeoBiz kompaniji posvećeni smo pružanju najvišeg nivoa bezbednosti informacija našim klijentima. Kao deo naše usluge, implementiramo i održavamo bezbednosne standarde prema ISO 27001 standardu, osiguravajući da vaši podaci budu zaštićeni u skladu sa međunarodno priznatim normama.":
        "At GeoBiz we are committed to providing the highest level of information security to our clients. As part of our service, we implement and maintain security standards according to ISO 27001, ensuring your data is protected in line with internationally recognized norms.",
    "Kroz primenu ovog standarda, mi osiguravamo da su informacije naših klijenata zaštićene od svih mogućih prijetnji, uključujući neovlašteni pristup, gubitak ili krađu podataka.":
        "By applying this standard, we ensure our clients' information is protected from all possible threats, including unauthorized access, loss or theft of data.",
    "U GeoBiz kompaniji razumemo važnost kontinuiteta poslovanja za naše klijente. Kao deo naše usluge, implementiramo zahteve kontinuiteta poslovanja prema ISO 22301 standardu, osiguravajući da vaše poslovanje ostane stabilno i funkcionalno čak i u nepredviđenim situacijama.":
        "At GeoBiz we understand the importance of business continuity for our clients. As part of our service, we implement business continuity requirements according to ISO 22301, ensuring your business remains stable and functional even in unforeseen situations.",
    "Naša posvećenost kontinuitetu poslovanja obuhvata sve aspekte vašeg poslovanja, uključujući infrastrukturu, operativne procese, osoblje i partnere. Kroz implementaciju strogo planiranje infrastrukture, redovne vežbe i testiranja, te kontinuirano praćenje i poboljšavanje, osiguravamo da naši klijenti budu spremni suočiti se s izazovima i očuvati kontinuitet poslovanja u svakoj situaciji.":
        "Our commitment to business continuity covers all aspects of your business, including infrastructure, operational processes, staff and partners. Through rigorous infrastructure planning, regular drills and testing, and continuous monitoring and improvement, we ensure our clients are ready to face challenges and maintain business continuity in any situation.",
    "Kroz našu uslugu implementacije kontinuiteta poslovanja prema ISO standardima, pružamo vam miran san i sigurnost u pouzdanost vašeg poslovanja, čak i u nepredviđenim okolnostima. Kontaktirajte nas danas i otkrijte kako možemo unaprijediti kontinuitet vašeg poslovanja i osigurati vašu sigurnost u svakoj situaciji.":
        "Through our business continuity implementation service based on ISO standards, we give you peace of mind and confidence in the reliability of your business, even in unforeseen circumstances. Contact us today and discover how we can improve your business continuity and ensure your security in any situation.",
    "U GeoBiz kompaniji, predani smo pružanju visokih standarda sigurnosti i pouzdanosti za naše klijente. Kao deo naše usluge, implementiramo zahteve Sistema upravljanja rizicima prema ISO 31000 standardu, osiguravajući da vaše poslovanje bude otporno na rizike i pripremljeno za suočavanje s izazovima.":
        "At GeoBiz we are committed to providing high standards of security and reliability for our clients. As part of our service, we implement risk management system requirements according to ISO 31000, ensuring your business is resilient to risks and prepared to face challenges.",
    "Kroz primjenu ovog standarda, mi pomažemo našim klijentima da prepoznaju potencijalne prijetnje, identifikuju ranjive tačke i razviju strategije za minimiziranje i upravljanje rizicima.":
        "By applying this standard, we help our clients recognize potential threats, identify weak points and develop strategies to minimize and manage risks.",
    "Kroz primjenu ovog standarda, mi pomažemo našim klijentima da identifikuju ključne procese, resurse i rizike te razviju strategije za njihovo očuvanje i obnovu u slučaju prekida poslovanja.":
        "By applying this standard, we help our clients identify key processes, resources and risks and develop strategies for their preservation and recovery in the event of a business disruption.",
    "Kroz implementaciju stroge metodologije upravljanja rizicima, redovno praćenje i analizu, te kontinuirano poboljšanje, osiguravamo da naši klijenti budu otporni na rizike i spremni suočiti se s neizvesnostima.":
        "Through a rigorous risk management methodology, regular monitoring and analysis, and continuous improvement, we ensure our clients are resilient to risks and ready to face uncertainties.",
    "Kroz našu uslugu implementacije Sistema upravljanja rizicima prema ISO standardima, pružamo vam miran san i sigurnost i pouzdanost vašeg poslovanja, čak i u nepredviđenim okolnostima. Kontaktirajte nas danas i otkrijte kako možemo unaprediti upravljanje rizicima u vašoj organizaciji i osigurati vašu zaštitu od neizvesnosti.":
        "Through our risk management system implementation service based on ISO standards, we give you peace of mind and confidence in the security and reliability of your business, even in unforeseen circumstances. Contact us today and discover how we can improve risk management in your organization and ensure your protection against uncertainty.",
    "U GeoBiz kompaniji predani smo osiguravanju visokih standarda sigurnosti za naše klijente. Kao deo naše usluge, pružamo testiranje sigurnosti IT sistema kako bismo identifikovali potencijalne ranjivosti i osigurali da vaša digitalna imovina bude zaštićena od napada i pretnji. Naš tim stručnjaka sprovodi temeljna ispitivanja i analize kako bi identifikovali ranjivosti u vašem IT okruženju, uključujući mrežne sisteme, aplikacije, baze podataka i infrastrukturu.":
        "At GeoBiz we are committed to ensuring high security standards for our clients. As part of our service, we provide IT systems security testing to identify potential vulnerabilities and ensure your digital assets are protected from attacks and threats. Our team of experts conducts thorough testing and analysis to identify vulnerabilities in your IT environment, including networks, applications, databases and infrastructure.",
    "Naš cilj je osigurati da vaši IT sistemi budu otporni na napade, sigurni od neovlašćenog pristupa i pouzdani u zaštiti vaših osetljivih informacija. Nakon sprovedenog testiranja, pružamo vam detaljne izveštaje i preporuke za poboljšanje sigurnosti vašeg IT okruženja.":
        "Our goal is to ensure your IT systems are resilient to attacks, safe from unauthorized access and reliable in protecting your sensitive information. After testing, we provide detailed reports and recommendations to improve the security of your IT environment.",
    "Kroz našu uslugu testiranja sigurnosti IT sistema, pružamo vam miran san i sigurnost u pouzdanost vaše digitalne imovine. Kontaktirajte nas danas i osigurajte da vaši IT sistemi budu u skladu s najvišim standardima sigurnosti.":
        "Through our IT systems security testing service, we give you peace of mind and confidence in the reliability of your digital assets. Contact us today and make sure your IT systems meet the highest security standards.",
    "Dobrodošli u našu firmu, vašeg partnera za implementaciju ISO/IEC 20000-1 standarda! Naša usluga konsultacija za implementaciju ISO/IEC 20000-1 osmišljena je kako bismo vam pomogli da vaša organizacija postigne izvrsnost u upravljanju IT uslugama.":
        "Welcome to our company, your partner for implementing the ISO/IEC 20000-1 standard! Our ISO/IEC 20000-1 implementation consulting service is designed to help your organization achieve excellence in IT service management.",
    "Sa našim iskusnim timom stručnjaka, pružamo sveobuhvatnu podršku u procesu implementacije ovog važnog standarda. Naš pristup je prilagođen vašim specifičnim potrebama i ciljevima, uzimajući u obzir veličinu vaše organizacije, industrijski sektor i postojeće prakse.":
        "With our experienced team of experts, we provide comprehensive support throughout the implementation of this important standard. Our approach is tailored to your specific needs and goals, taking into account the size of your organization, industry sector and existing practices.",
    "Naš cilj je da vam pružimo sve potrebne alate i znanje kako biste uspešno implementirali ISO/IEC 20000-1 standard i postigli kontinuirano unapređenje vaših IT usluga.":
        "Our goal is to provide you with all the tools and knowledge you need to successfully implement the ISO/IEC 20000-1 standard and achieve continuous improvement of your IT services.",
    "Poverite nam vaše izazove, a mi ćemo vam pomoći da postignete visoke standarde u upravljanju IT uslugama, što će rezultirati povećanom efikasnošću, smanjenjem rizika i većim zadovoljstvom korisnika. Kontaktirajte nas danas i zajedno ćemo graditi put ka uspehu vaše organizacije u digitalnom dobu.":
        "Entrust us with your challenges, and we will help you achieve high standards in IT service management, resulting in increased efficiency, reduced risk and greater user satisfaction. Contact us today and together we will build the path to your organization's success in the digital age.",
})

RU.update({
    "Održavanje i servis računara - GeoBiz": "Обслуживание и ремонт компьютеров - GeoBiz",
    "Projektovanje i izvođenje mrežne infrastrukture - GeoBiz": "Проектирование и развёртывание сетевой инфраструктуры - GeoBiz",
    "Održavanje servera i virtuelizacija - GeoBiz": "Обслуживание серверов и виртуализация - GeoBiz",
    "Profesionalno održavanje i servis računara — vaš pouzdan partner za besprekorno digitalno iskustvo.":
        "Профессиональное обслуживание и ремонт компьютеров — ваш надёжный партнёр для безупречной цифровой работы.",
    "održavanje računara, servis računara, IT podrška, GeoBiz": "обслуживание компьютеров, ремонт компьютеров, ИТ-поддержка, GeoBiz",
    "Projektovanje i izvođenje pouzdane i bezbedne mrežne infrastrukture — temelj vašeg digitalnog poslovanja.":
        "Проектирование и развёртывание надёжной и безопасной сетевой инфраструктуры — основа вашего цифрового бизнеса.",
    "mrežna infrastruktura, projektovanje mreža, LAN, WiFi, GeoBiz": "сетевая инфраструктура, проектирование сетей, LAN, WiFi, GeoBiz",
    "Održavanje servera i virtuelizacija za optimizaciju vaše poslovne infrastrukture i pouzdan rad sistema.":
        "Обслуживание серверов и виртуализация для оптимизации вашей бизнес-инфраструктуры и надёжной работы систем.",
    "održavanje servera, virtuelizacija, serverska infrastruktura, GeoBiz": "обслуживание серверов, виртуализация, серверная инфраструктура, GeoBiz",
    "Bezbedno skladištenje i zaštita vaših podataka. GeoBiz data storage rešenja za pouzdano čuvanje i dostupnost poslovnih podataka.":
        "Безопасное хранение и защита ваших данных. Решения GeoBiz для надёжного хранения и доступности бизнес-данных.",
    "data storage, skladištenje podataka, backup, GeoBiz": "хранение данных, резервное копирование, GeoBiz",
    "Moderna veb rešenja — dizajn i razvoj veb sajtova koji unapređuju vaše poslovanje i prisustvo na internetu.":
        "Современные веб-решения — проектирование и разработка сайтов, повышающих эффективность бизнеса и присутствие в интернете.",
    "Razvoj prilagođenih web, desktop i mobilnih aplikacija i baza podataka koji ubrzavaju i unapređuju vaše poslovanje.":
        "Разработка индивидуальных веб-, десктоп- и мобильных приложений и баз данных, ускоряющих и улучшающих ваш бизнес.",
    "Implementacija i održavanje bezbednosti informacija prema ISO 27001 — zaštita vaših podataka u digitalnom svetu.":
        "Внедрение и поддержка информационной безопасности по ISO 27001 — защита ваших данных в цифровом мире.",
    "Implementacija kontinuiteta poslovanja prema ISO 22301 — vaša sigurnost i spremnost u svakoj situaciji.":
        "Внедрение непрерывности бизнеса по ISO 22301 — ваша безопасность и готовность в любой ситуации.",
    "Konsultacije za implementaciju ISO/IEC 20000-1 — izvrsnost u upravljanju IT uslugama vaše organizacije.":
        "Консалтинг по внедрению ISO/IEC 20000-1 — совершенство в управлении ИТ-услугами вашей организации.",
    "Upravljanje rizicima prema ISO 31000 — identifikacija, procena i smanjenje rizika u vašoj organizaciji.":
        "Управление рисками по ISO 31000 — идентификация, оценка и снижение рисков в вашей организации.",
    "Testiranje bezbednosti IT sistema — identifikacija ranjivosti i zaštita vaše digitalne imovine od napada i pretnji.":
        "Тестирование безопасности ИТ-систем — выявление уязвимостей и защита ваших цифровых активов от атак и угроз.",
    "GeoBiz kontakt, IT podrška, Sremska Mitrovica, office@geo-biz.com": "Контакты GeoBiz, ИТ-поддержка, Сремска-Митровица, office@geo-biz.com",
    "Održavanje računara": "Обслуживание компьютеров",
    "Projektovanje i izvođenje mreža": "Проектирование и развёртывание сетей",
    "Održavanje servera": "Обслуживание серверов",
    "Optimizacija vaše poslovne infrastrukture": "Оптимизация вашей бизнес-инфраструктуры",
    "Vaš ključ za digitalni napredak": "Ваш ключ к цифровому развитию",
    "Vaš pouzdan partner za besprekorno digitalno iskustvo": "Ваш надёжный партнёр для безупречной цифровой работы",
    "Temelj vašeg digitalnog uspeha": "Основа вашего цифрового успеха",
    "Ogledalo vaše kompanije": "Зеркало вашей компании",
    "Čuvanje vaših digitalnih podataka": "Хранение ваших цифровых данных",
    "Zaštitite vaše poslovanje": "Защитите свой бизнес",
    "Unapređenje Sistema kontinuiteta poslovanja": "Совершенствование системы непрерывности бизнеса",
    "Naše usluge uključuju:": "Наши услуги включают:",
    "To uključuje redovno:": "Это включает регулярно:",
    "To uključuje zaštitu podataka od:": "Это включает защиту данных от:",
    "Pružamo redovno:": "Мы регулярно предоставляем:",
    "Koristimo najsavremenije alate i tehnike, uključujući:": "Мы используем самые современные инструменты и методы, включая:",
    "Ažuriranje softvera": "Обновление ПО",
    "Praćenje performansi": "Мониторинг производительности",
    "Praćenje rizika": "Мониторинг рисков",
    "Rešavanje problema i preventivno održavanje radi sprečavanja budućih problema":
        "Устранение проблем и профилактическое обслуживание для предотвращения будущих сбоев",
    "Rešavanje problema kako bismo osigurali kontinuiranu dostupnost vaših aplikacija i podataka":
        "Устранение проблем для обеспечения непрерывной доступности ваших приложений и данных",
    "Održavanje servera": "Обслуживание серверов",
    "Održavanje i": "Обслуживание и",
    "Korisničko iskustvo": "Пользовательский опыт",
    "Optimizovanost za različite uređaje": "Оптимизация под разные устройства",
    "Optimizacija za pretraživače": "Поисковая оптимизация",
    "Aplikacija za mobilne uređaje": "Мобильные приложения",
    "Etičko hakovanje": "Этичный хакинг",
    "Otklanjanje uočenih ranjivosti": "Устранение выявленных уязвимостей",
    "Otklanjanje uočenih slabosti": "Устранение выявленных слабых мест",
    "Poboljšanje sistema": "Улучшение системы",
    "Oštećenja": "Повреждения",
    "Neovlaštenog pristupa": "Несанкционированный доступ",
    "Detaljan izveštaj i predlog unapređenja sistema": "Подробный отчёт и предложение по улучшению системы",
    "Detaljni izveštaji sa predlogom mera": "Подробные отчёты с предложением мер",
    "Metabase - izveštaji": "Metabase — отчёты",
    "Poverljivost i dostupnost podataka vaših klijenata": "Конфиденциальность и доступность данных ваших клиентов",
    "upravljanja informacionom bezbednošću u okviru organizacije": "управления информационной безопасностью в организации",
    "Kao i podršku tokom sertifikacije": "А также поддержку во время сертификации",
    "i druge metode kako bismo otkrili i rešili potencijalne sigurnosne rupe.":
        "и другие методы, чтобы выявить и устранить потенциальные бреши в безопасности.",
    "Radimo sa strašću kako bismo stvorili rješenja koja donose stvarnu vrednost.":
        "Мы работаем с увлечением, чтобы создавать решения, приносящие реальную ценность.",
    "Naš tim web dizajnera koristi svoje stručno znanje i kreativnost kako bi kreirao dizajn koji odgovara potrebama i preferencijama klijenta, uzimajući u obzir aspekte kao što su":
        "Наша команда веб-дизайнеров использует свои знания и креативность, чтобы создать дизайн, отвечающий потребностям и предпочтениям клиента, учитывая такие аспекты, как",
    "Naš tim stručnjaka posvećen je razvoju prilagođenih baza podataka i aplikacija koje zadovoljavaju specifične potrebe i zahteve naših klijenata. Počevši od:":
        "Наша команда специалистов занимается разработкой индивидуальных баз данных и приложений, отвечающих конкретным потребностям наших клиентов. Начиная с:",
    "Naša posvećenost bezbednosti informacija obuhvata sve aspekte vašeg poslovanja, uključujući:":
        "Наша приверженность информационной безопасности охватывает все аспекты вашего бизнеса, включая:",
    "Naša posvećenost upravljanju rizicima obuhvata sve aspekte našeg poslovanja, uključujući:":
        "Наша приверженность управлению рисками охватывает все аспекты нашего бизнеса, включая:",
    "ISO 27001 je standard koji definiše zahteve za:": "ISO 27001 — стандарт, определяющий требования к:",
    "ISO 22301 je međunarodni standard koji definiše zahteve za upravljanje kontinuitetom poslovanja, uključujući":
        "ISO 22301 — международный стандарт, определяющий требования к управлению непрерывностью бизнеса, включая",
    "ISO 31000 je međunarodni standard koji pruža okvir za upravljanje rizicima u organizaciji, uključujući:":
        "ISO 31000 — международный стандарт, предоставляющий основу для управления рисками в организации, включая:",
    "U zavisnosti od veličine vašeg IT sistema, složenosti infrastrukture, broja korisnika, nudimo vam konkurentne cene:":
        "В зависимости от размера вашей ИТ-системы, сложности инфраструктуры и числа пользователей мы предлагаем конкурентные цены:",
    "do 10 računara": "до 10 компьютеров",
    "od 10 do 20 računara": "от 10 до 20 компьютеров",
    "20 računara + serveri": "20+ компьютеров + серверы",
    "Naša usluga podrazumeva implementaciju virtualnog okruženja najpopularnijih sistema za virtuelizaciju":
        "Наша услуга включает развёртывание виртуальной среды на базе самых популярных систем виртуализации",
    "Glavni cilj usluge data storage je osigurati pouzdanost, sigurnost i dostupnost sačuvanih podataka.":
        "Главная цель услуги хранения данных — обеспечить надёжность, безопасность и доступность сохранённых данных.",
    "Naša usluga održavanja računara obuhvata sve aspekte potrebne za održavanje vaših IT sastava u optimalnom stanju.":
        "Наша услуга обслуживания компьютеров охватывает все аспекты, необходимые для поддержания ваших ИТ-систем в оптимальном состоянии.",
    "današnjem digitalnom dobu, pouzdanost i performanse računarskih sistema su ključne za uspješno poslovanje. Upravo zato, u GeoBiz-u predani smo pružanju vrhunskih usluga održavanja računara koje osiguravaju besprekorno rad vaših IT sistema.":
        "В современную цифровую эпоху надёжность и производительность компьютерных систем критически важны для успешного бизнеса. Именно поэтому в GeoBiz мы стремимся предоставлять первоклассные услуги обслуживания компьютеров, обеспечивающие безупречную работу ваших ИТ-систем.",
    "Naš tim stručnjaka posvećen je održavanju i optimizaciji vaših računarskih resursa kako biste mogli maksimalno iskoristiti svoje IT investicije. Bez obzira jeste li malo preduzeće, srednje preduzeće ili velika korporacija, pružamo vam prilagođene usluge održavanja koje odgovaraju vašim specifičnim potrebama i zahtevima.":
        "Наша команда специалистов занимается обслуживанием и оптимизацией ваших компьютерных ресурсов, чтобы вы могли максимально использовать ИТ-инвестиции. Будь то малый бизнес, среднее предприятие или крупная корпорация, мы предоставляем индивидуальные услуги обслуживания, отвечающие вашим потребностям.",
    "Naš cilj je osigurati kontinuiranu dostupnost, stabilnost i sigurnost vaših računarskih sistema, kako biste se mogli potpuno posvetiti svojim poslovnim aktivnostima. Kao vaš pouzdan partner za održavanje računara, GeoBiz vam pruža stručnost, iskustvo i predanost potrebne za postizanje izvrsnih rezultata. Kontaktirajte nas danas i osigurajte da vaši računarski sistemi uvek budu u vrhunskom stanju.":
        "Наша цель — обеспечить постоянную доступность, стабильность и безопасность ваших компьютерных систем, чтобы вы могли полностью сосредоточиться на бизнесе. Как ваш надёжный партнёр по обслуживанию компьютеров, GeoBiz предоставляет опыт и преданность делу для достижения отличных результатов. Свяжитесь с нами сегодня и обеспечьте, чтобы ваши компьютерные системы всегда были в идеальном состоянии.",
    "U današnjem povezanom svetu, stabilna i skalabilna mrežna infrastruktura ključna je za uspeh svake organizacije. U GeoBiz kompaniji stručnjaci smo za projekovanje i izvođenje mrežnih infrastruktura koje omogućuju sigurnu i pouzdanu komunikaciju te podržavaju rast i razvoj vašeg poslovanja.":
        "В современном взаимосвязанном мире стабильная и масштабируемая сетевая инфраструктура — ключ к успеху любой организации. В GeoBiz мы специалисты по проектированию и развёртыванию сетевых инфраструктур, обеспечивающих безопасную и надёжную связь и поддерживающих рост вашего бизнеса.",
    "Naš tim stručnjaka poseduje bogato iskustvo u implementaciji različitih tehnologija i platformi kako bi se osiguralo da vaša mrežna infrastruktura bude optimalno projektovana i implementirana. Koristimo najnovije alate i prakse kako bismo osigurali visok nivo performansi, pouzdanosti i sigurnosti vaše mrežne infrastrukture.":
        "Наша команда специалистов обладает богатым опытом внедрения различных технологий и платформ, чтобы ваша сетевая инфраструктура была оптимально спроектирована и развёрнута. Мы используем новейшие инструменты и практики для обеспечения высокого уровня производительности, надёжности и безопасности.",
    "Kroz našu uslugu projektovanja i izvođenja mrežne infrastrukture, nudimo vam sve potrebno za uspešno vođenje vašeg poslovanja u digitalnom svijetu. Kontaktirajte nas danas i dopustite nam da vam pomognemo izgraditi temelj za vaš digitalni uspjeh.":
        "Благодаря нашей услуге проектирования и развёртывания сетевой инфраструктуры мы предлагаем всё необходимое для успешного ведения бизнеса в цифровом мире. Свяжитесь с нами сегодня, и мы поможем построить фундамент вашего цифрового успеха.",
    "U današnjem digitalnom dobu, poslovna infrastruktura mora biti pouzdana, skalabilna i efikasna kako bi podržala rast i razvoj organizacije. U kompaniji GeoBiz, specijalizovani smo za pružanje usluga održavanja servera i virtualizacije koje omogućuju optimizaciju vaše IT infrastrukture.":
        "В современную цифровую эпоху бизнес-инфраструктура должна быть надёжной, масштабируемой и эффективной, чтобы поддерживать рост организации. В GeoBiz мы специализируемся на обслуживании серверов и виртуализации, что позволяет оптимизировать вашу ИТ-инфраструктуру.",
    "Naš tim stručnjaka posvećen je održavanju i upravljanju vašim serverskim okruženjem kako biste se mogli potpuno posvetiti svojim poslovnim aktivnostima.":
        "Наша команда специалистов занимается обслуживанием и управлением вашей серверной средой, чтобы вы могли полностью сосредоточиться на бизнесе.",
    "Naš tim stručnjaka posvećen je održavanju i upravljanju vašim serverskim okruženjem kako biste se mogli potpuno posvetiti svojim poslovnim aktivnostima. Pružamo redovno održavanje servera, nadzor performansi, sigurnosne provere i rješavanje problema kako bismo osigurali kontinuiranu dostupnost vaših aplikacija i podataka.":
        "Наша команда специалистов занимается обслуживанием и управлением вашей серверной средой, чтобы вы могли полностью сосредоточиться на бизнесе. Мы обеспечиваем регулярное обслуживание серверов, мониторинг производительности, проверки безопасности и устранение проблем для непрерывной доступности ваших приложений и данных.",
    "Uz to, nudimo i usluge virtualizacije koje vam omogućuju iskorišćavanje punog potencijala vaše serverske infrastrukture. Virtualizacija omogućuje optimizaciju resursa, smanjenje troškova i povećanje skalabilnosti, pružajući vam fleksibilnost koja vam je potrebna za prilagođavanje promenjivim poslovnim zahtevima.":
        "Кроме того, мы предлагаем услуги виртуализации, позволяющие раскрыть весь потенциал вашей серверной инфраструктуры. Виртуализация оптимизирует ресурсы, снижает затраты и повышает масштабируемость, давая вам гибкость для адаптации к меняющимся бизнес-требованиям.",
    "Kao vaš pouzdan partner za održavanje servera i virtualizaciju, kompanija GeoBiz pruža vam stručnost i podršku potrebnu za postizanje izvrsnih rezultata. Kontaktirajte nas danas i osigurajte da vaša poslovna infrastruktura bude spremna za budućnost.":
        "Как ваш надёжный партнёр по обслуживанию серверов и виртуализации, GeoBiz предоставляет опыт и поддержку для достижения отличных результатов. Свяжитесь с нами сегодня и обеспечьте готовность вашей бизнес-инфраструктуры к будущему.",
    "Kontaktirajte nas danas i osigurajte da vaša poslovna infrastruktura bude spremna za budućnost.":
        "Свяжитесь с нами сегодня и обеспечьте готовность вашей бизнес-инфраструктуры к будущему.",
    "VMware vSphere je platforma za virtualizaciju podataka koja omogućuje stvaranje i upravljanje virtualnim mašinama. VMware ESXi je hipervizor koji se koristi kao osnova za virtualizaciju u vSphere okruženju.":
        "VMware vSphere — платформа виртуализации, позволяющая создавать виртуальные машины и управлять ими. VMware ESXi — гипервизор, используемый как основа виртуализации в среде vSphere.",
    "Hyper-V je Microsoftova platforma za virtualizaciju koja omogućuje stvaranje i upravljanje virtualnim mašinama na Windows okruženju.":
        "Hyper-V — платформа виртуализации Microsoft, позволяющая создавать виртуальные машины и управлять ими в среде Windows.",
    "VirtualBox je besplatna open-source platforma za virtualizaciju koja podržava stvaranje virtualnih mašina na različitim operativnim sustavima, uključujući Windows, Linux, Mac OS X i druge.":
        "VirtualBox — бесплатная платформа виртуализации с открытым кодом, поддерживающая создание виртуальных машин в разных ОС, включая Windows, Linux, Mac OS X и другие.",
    "KVM je hipervizor otvorenog koda koji se koristi u Linux okruženju za virtualizaciju operativnih sistema.":
        "KVM — гипервизор с открытым кодом, используемый в среде Linux для виртуализации операционных систем.",
    "XenServer je platforma za virtualizaciju koju razvija Citrix Systems, koja omogućuje stvaranje i upravljanje virtualnim mašinama i podržava različite operativne sisteme.":
        "XenServer — платформа виртуализации от Citrix Systems, позволяющая создавать виртуальные машины и управлять ими и поддерживающая разные операционные системы.",
    "Usluga data storage predstavlja pružanje kapaciteta i infrastrukture za čuvanje podataka u digitalnom formatu. Ova usluga omogućuje korisnicima da sigurno čuvaju svoje podatke na udaljenim serverima ili skladištima, pristupaju im kad god je potrebno i dele ih s drugima prema potrebi.":
        "Услуга хранения данных — это предоставление ёмкости и инфраструктуры для хранения данных в цифровом формате. Она позволяет пользователям безопасно хранить данные на удалённых серверах или хранилищах, обращаться к ним в любое время и делиться ими при необходимости.",
    "Usluga data storage igra ključnu ulogu u modernom informacionom društvu, omogućujući organizacijama i pojedincima da pravilno upravljaju, dele i koriste svoje podatke u svakodnevnom poslovanju i životu.":
        "Хранение данных играет ключевую роль в современном информационном обществе, позволяя организациям и людям правильно управлять, делиться и использовать данные в повседневной работе и жизни.",
    "Usluga data storage može biti implementirana na različite načine, uključujući lokalno čuvanje podataka na vlastitim NAS serverima, korišćenje cloud storage-a kod pružaoca usluga cloud computinga, ili kombinaciju oba pristupa. Korisnici mogu birati između različitih modela čuvanja podataka, kao što su lokalno, cloud ili kombinovano, zavisno o njihovim specifičnim potrebama i zahtevima.":
        "Хранение данных может быть реализовано разными способами: локально на собственных NAS-серверах, через облачное хранилище у провайдера облачных услуг или комбинированно. Пользователи могут выбирать между разными моделями — локальной, облачной или гибридной — в зависимости от своих потребностей.",
    "Usluga web dizajna obuhvata proces stvaranja i oblikovanja estetski privlačnih, funkcionalnih i korisnički orijentisanih web stranica. Ova usluga uključuje usku saradnju između dizajnera i klijenata kako bi se stvorio online identitet koji odražava brend, ciljeve i vrednosti klijenta.":
        "Веб-дизайн охватывает процесс создания эстетичных, функциональных и ориентированных на пользователя сайтов. Эта услуга предполагает тесное сотрудничество дизайнеров и клиентов для создания онлайн-идентичности, отражающей бренд, цели и ценности клиента.",
    "Usluga web dizajna obuhvata sve korake od početnog planiranja i konceptualizacije do implementacije i testiranja web stranice. Naši dizajneri rade na stvaranju jedinstvenih i privlačnih dizajna koji privlače pažnju posetilaca i podstiču ih na interakciju sa sadržajem.":
        "Веб-дизайн охватывает все этапы — от первоначального планирования и проработки концепции до реализации и тестирования сайта. Наши дизайнеры создают уникальные и привлекательные решения, которые привлекают внимание посетителей и побуждают их взаимодействовать с контентом.",
    "Cilj nam je stvoriti web stranice koja pružaju pozitivno korisničko iskustvo, olakšava navigaciju, podstiče angažman korisnika i doprinosi postizanju poslovnih ciljeva klijenta. , promociji usluga ili deljenju informacija.":
        "Наша цель — создавать сайты, которые обеспечивают положительный пользовательский опыт, упрощают навигацию, повышают вовлечённость и способствуют достижению бизнес-целей клиента, будь то продвижение услуг или распространение информации.",
    "U GeoBiz kompaniji specijalizovani smo jedinstveno kreiranje baza i aplikacija koje podstiču digitalni napredak i unapređuju poslovanje naših klijenata.":
        "В GeoBiz мы специализируемся на создании уникальных баз данных и приложений, которые способствуют цифровому развитию и улучшают бизнес наших клиентов.",
    "Kreiramo aplikacije koje su prilagođenje vašem poslovanju, aplikacije koje će ubrzati vaše poslovanje, olakšati rad i omogućiti menadžmentu brže donošenje pravih odluka na osnovu izveštaja koje pravimo.":
        "Мы создаём приложения, адаптированные под ваш бизнес, — приложения, которые ускоряют работу, облегчают её и позволяют руководству быстрее принимать правильные решения на основе подготовленных нами отчётов.",
    "Kroz naše usluge, klijenti dobijaju prilagođene baze podataka koje omogućuju efikasno upravljanje i analizu podataka, kao i aplikacije koje poboljšavaju produktivnost, automatizuju procese i poboljšavaju korisničko iskustvo.":
        "Благодаря нашим услугам клиенты получают индивидуальные базы данных для эффективного управления и анализа данных, а также приложения, повышающие продуктивность, автоматизирующие процессы и улучшающие пользовательский опыт.",
    "Nezavisno o veličini vaše kompanije ili industrije, razvićemo za vas potrebne alate i resurse za uspešno vođenje vašeg poslovanja u digitalnom svetu. Kontaktirajte nas danas i otkrijte kako možemo transformisati vaše poslovanje putem naprednih tehnoloških rešenja.":
        "Независимо от размера вашей компании или отрасли, мы разработаем необходимые инструменты и ресурсы для успешного ведения бизнеса в цифровом мире. Свяжитесь с нами сегодня и узнайте, как мы можем преобразить ваш бизнес с помощью передовых технологических решений.",
    "U GeoBiz kompaniji posvećeni smo pružanju najvišeg nivoa bezbednosti informacija našim klijentima. Kao deo naše usluge, implementiramo i održavamo bezbednosne standarde prema ISO 27001 standardu, osiguravajući da vaši podaci budu zaštićeni u skladu sa međunarodno priznatim normama.":
        "В GeoBiz мы стремимся обеспечить нашим клиентам высочайший уровень информационной безопасности. В рамках нашей услуги мы внедряем и поддерживаем стандарты безопасности по ISO 27001, гарантируя защиту ваших данных в соответствии с международно признанными нормами.",
    "Kroz primenu ovog standarda, mi osiguravamo da su informacije naših klijenata zaštićene od svih mogućih prijetnji, uključujući neovlašteni pristup, gubitak ili krađu podataka.":
        "Применяя этот стандарт, мы обеспечиваем защиту информации наших клиентов от всех возможных угроз, включая несанкционированный доступ, потерю или кражу данных.",
    "U GeoBiz kompaniji razumemo važnost kontinuiteta poslovanja za naše klijente. Kao deo naše usluge, implementiramo zahteve kontinuiteta poslovanja prema ISO 22301 standardu, osiguravajući da vaše poslovanje ostane stabilno i funkcionalno čak i u nepredviđenim situacijama.":
        "В GeoBiz мы понимаем важность непрерывности бизнеса для наших клиентов. В рамках услуги мы внедряем требования непрерывности бизнеса по ISO 22301, обеспечивая стабильную и бесперебойную работу даже в непредвиденных ситуациях.",
    "Naša posvećenost kontinuitetu poslovanja obuhvata sve aspekte vašeg poslovanja, uključujući infrastrukturu, operativne procese, osoblje i partnere. Kroz implementaciju strogo planiranje infrastrukture, redovne vežbe i testiranja, te kontinuirano praćenje i poboljšavanje, osiguravamo da naši klijenti budu spremni suočiti se s izazovima i očuvati kontinuitet poslovanja u svakoj situaciji.":
        "Наша приверженность непрерывности бизнеса охватывает все аспекты вашей деятельности, включая инфраструктуру, операционные процессы, персонал и партнёров. Благодаря тщательному планированию инфраструктуры, регулярным учениям и тестированию, постоянному мониторингу и улучшению мы обеспечиваем готовность клиентов к вызовам и непрерывность бизнеса в любой ситуации.",
    "Kroz našu uslugu implementacije kontinuiteta poslovanja prema ISO standardima, pružamo vam miran san i sigurnost u pouzdanost vašeg poslovanja, čak i u nepredviđenim okolnostima. Kontaktirajte nas danas i otkrijte kako možemo unaprijediti kontinuitet vašeg poslovanja i osigurati vašu sigurnost u svakoj situaciji.":
        "Благодаря нашей услуге внедрения непрерывности бизнеса по стандартам ISO мы обеспечиваем вам спокойствие и уверенность в надёжности вашего бизнеса даже в непредвиденных обстоятельствах. Свяжитесь с нами сегодня и узнайте, как мы можем улучшить непрерывность вашего бизнеса и обеспечить безопасность в любой ситуации.",
    "U GeoBiz kompaniji, predani smo pružanju visokih standarda sigurnosti i pouzdanosti za naše klijente. Kao deo naše usluge, implementiramo zahteve Sistema upravljanja rizicima prema ISO 31000 standardu, osiguravajući da vaše poslovanje bude otporno na rizike i pripremljeno za suočavanje s izazovima.":
        "В GeoBiz мы привержены обеспечению высоких стандартов безопасности и надёжности для наших клиентов. В рамках услуги мы внедряем требования системы управления рисками по ISO 31000, обеспечивая устойчивость вашего бизнеса к рискам и готовность к вызовам.",
    "Kroz primjenu ovog standarda, mi pomažemo našim klijentima da prepoznaju potencijalne prijetnje, identifikuju ranjive tačke i razviju strategije za minimiziranje i upravljanje rizicima.":
        "Применяя этот стандарт, мы помогаем клиентам распознавать потенциальные угрозы, выявлять слабые места и разрабатывать стратегии минимизации и управления рисками.",
    "Kroz primjenu ovog standarda, mi pomažemo našim klijentima da identifikuju ključne procese, resurse i rizike te razviju strategije za njihovo očuvanje i obnovu u slučaju prekida poslovanja.":
        "Применяя этот стандарт, мы помогаем клиентам определить ключевые процессы, ресурсы и риски и разработать стратегии их сохранения и восстановления при прерывании бизнеса.",
    "Kroz implementaciju stroge metodologije upravljanja rizicima, redovno praćenje i analizu, te kontinuirano poboljšanje, osiguravamo da naši klijenti budu otporni na rizike i spremni suočiti se s neizvesnostima.":
        "Благодаря строгой методологии управления рисками, регулярному мониторингу и анализу, а также постоянному совершенствованию мы обеспечиваем устойчивость клиентов к рискам и готовность к неопределённостям.",
    "Kroz našu uslugu implementacije Sistema upravljanja rizicima prema ISO standardima, pružamo vam miran san i sigurnost i pouzdanost vašeg poslovanja, čak i u nepredviđenim okolnostima. Kontaktirajte nas danas i otkrijte kako možemo unaprediti upravljanje rizicima u vašoj organizaciji i osigurati vašu zaštitu od neizvesnosti.":
        "Благодаря нашей услуге внедрения системы управления рисками по стандартам ISO мы обеспечиваем вам спокойствие, безопасность и надёжность бизнеса даже в непредвиденных обстоятельствах. Свяжитесь с нами сегодня и узнайте, как мы можем улучшить управление рисками в вашей организации и защитить вас от неопределённости.",
    "U GeoBiz kompaniji predani smo osiguravanju visokih standarda sigurnosti za naše klijente. Kao deo naše usluge, pružamo testiranje sigurnosti IT sistema kako bismo identifikovali potencijalne ranjivosti i osigurali da vaša digitalna imovina bude zaštićena od napada i pretnji. Naš tim stručnjaka sprovodi temeljna ispitivanja i analize kako bi identifikovali ranjivosti u vašem IT okruženju, uključujući mrežne sisteme, aplikacije, baze podataka i infrastrukturu.":
        "В GeoBiz мы привержены обеспечению высоких стандартов безопасности для наших клиентов. В рамках услуги мы проводим тестирование безопасности ИТ-систем, чтобы выявить потенциальные уязвимости и обеспечить защиту ваших цифровых активов от атак и угроз. Наша команда специалистов проводит тщательные проверки и анализ для выявления уязвимостей в вашей ИТ-среде, включая сети, приложения, базы данных и инфраструктуру.",
    "Naš cilj je osigurati da vaši IT sistemi budu otporni na napade, sigurni od neovlašćenog pristupa i pouzdani u zaštiti vaših osetljivih informacija. Nakon sprovedenog testiranja, pružamo vam detaljne izveštaje i preporuke za poboljšanje sigurnosti vašeg IT okruženja.":
        "Наша цель — обеспечить устойчивость ваших ИТ-систем к атакам, защиту от несанкционированного доступа и надёжную защиту конфиденциальной информации. После тестирования мы предоставляем подробные отчёты и рекомендации по повышению безопасности вашей ИТ-среды.",
    "Kroz našu uslugu testiranja sigurnosti IT sistema, pružamo vam miran san i sigurnost u pouzdanost vaše digitalne imovine. Kontaktirajte nas danas i osigurajte da vaši IT sistemi budu u skladu s najvišim standardima sigurnosti.":
        "Благодаря нашей услуге тестирования безопасности ИТ-систем мы обеспечиваем вам спокойствие и уверенность в надёжности ваших цифровых активов. Свяжитесь с нами сегодня и обеспечьте соответствие ваших ИТ-систем высочайшим стандартам безопасности.",
    "Dobrodošli u našu firmu, vašeg partnera za implementaciju ISO/IEC 20000-1 standarda! Naša usluga konsultacija za implementaciju ISO/IEC 20000-1 osmišljena je kako bismo vam pomogli da vaša organizacija postigne izvrsnost u upravljanju IT uslugama.":
        "Добро пожаловать в нашу компанию — вашего партнёра по внедрению стандарта ISO/IEC 20000-1! Наша консультационная услуга по внедрению ISO/IEC 20000-1 призвана помочь вашей организации достичь совершенства в управлении ИТ-услугами.",
    "Sa našim iskusnim timom stručnjaka, pružamo sveobuhvatnu podršku u procesu implementacije ovog važnog standarda. Naš pristup je prilagođen vašim specifičnim potrebama i ciljevima, uzimajući u obzir veličinu vaše organizacije, industrijski sektor i postojeće prakse.":
        "С нашей опытной командой специалистов мы предоставляем всестороннюю поддержку при внедрении этого важного стандарта. Наш подход адаптирован под ваши конкретные потребности и цели, с учётом размера организации, отрасли и существующих практик.",
    "Naš cilj je da vam pružimo sve potrebne alate i znanje kako biste uspešno implementirali ISO/IEC 20000-1 standard i postigli kontinuirano unapređenje vaših IT usluga.":
        "Наша цель — предоставить вам все инструменты и знания для успешного внедрения стандарта ISO/IEC 20000-1 и достижения постоянного улучшения ваших ИТ-услуг.",
    "Poverite nam vaše izazove, a mi ćemo vam pomoći da postignete visoke standarde u upravljanju IT uslugama, što će rezultirati povećanom efikasnošću, smanjenjem rizika i većim zadovoljstvom korisnika. Kontaktirajte nas danas i zajedno ćemo graditi put ka uspehu vaše organizacije u digitalnom dobu.":
        "Доверьте нам свои задачи, и мы поможем вам достичь высоких стандартов в управлении ИТ-услугами, что приведёт к повышению эффективности, снижению рисков и большей удовлетворённости пользователей. Свяжитесь с нами сегодня, и вместе мы построим путь к успеху вашей организации в цифровую эпоху.",
})

DE.update({
    "Održavanje i servis računara - GeoBiz": "Computerwartung und -reparatur - GeoBiz",
    "Projektovanje i izvođenje mrežne infrastrukture - GeoBiz": "Planung und Aufbau der Netzwerkinfrastruktur - GeoBiz",
    "Održavanje servera i virtuelizacija - GeoBiz": "Serverwartung & Virtualisierung - GeoBiz",
    "Profesionalno održavanje i servis računara — vaš pouzdan partner za besprekorno digitalno iskustvo.":
        "Professionelle Computerwartung und -reparatur - Ihr zuverlässiger Partner für ein reibungsloses digitales Erlebnis.",
    "održavanje računara, servis računara, IT podrška, GeoBiz": "Computerwartung, Computerreparatur, IT-Support, GeoBiz",
    "Projektovanje i izvođenje pouzdane i bezbedne mrežne infrastrukture — temelj vašeg digitalnog poslovanja.":
        "Planung und Aufbau einer zuverlässigen und sicheren Netzwerkinfrastruktur - die Grundlage Ihres digitalen Geschäfts.",
    "mrežna infrastruktura, projektovanje mreža, LAN, WiFi, GeoBiz": "Netzwerkinfrastruktur, Netzwerkplanung, LAN, WLAN, GeoBiz",
    "Održavanje servera i virtuelizacija za optimizaciju vaše poslovne infrastrukture i pouzdan rad sistema.":
        "Serverwartung und Virtualisierung zur Optimierung Ihrer Geschäftsinfrastruktur und für einen zuverlässigen Systembetrieb.",
    "održavanje servera, virtuelizacija, serverska infrastruktura, GeoBiz": "Serverwartung, Virtualisierung, Serverinfrastruktur, GeoBiz",
    "Bezbedno skladištenje i zaštita vaših podataka. GeoBiz data storage rešenja za pouzdano čuvanje i dostupnost poslovnih podataka.":
        "Sichere Speicherung und Schutz Ihrer Daten. GeoBiz Data-Storage-Lösungen für zuverlässige Speicherung und Verfügbarkeit von Geschäftsdaten.",
    "data storage, skladištenje podataka, backup, GeoBiz": "Datenspeicherung, Datensicherung, Backup, GeoBiz",
    "Moderna veb rešenja — dizajn i razvoj veb sajtova koji unapređuju vaše poslovanje i prisustvo na internetu.":
        "Moderne Web-Lösungen - Gestaltung und Entwicklung von Websites, die Ihr Geschäft und Ihre Online-Präsenz stärken.",
    "Razvoj prilagođenih web, desktop i mobilnih aplikacija i baza podataka koji ubrzavaju i unapređuju vaše poslovanje.":
        "Entwicklung maßgeschneiderter Web-, Desktop- und mobiler Anwendungen und Datenbanken, die Ihr Geschäft beschleunigen und verbessern.",
    "Implementacija i održavanje bezbednosti informacija prema ISO 27001 — zaštita vaših podataka u digitalnom svetu.":
        "Implementierung und Pflege der Informationssicherheit gemäß ISO 27001 - Schutz Ihrer Daten in der digitalen Welt.",
    "Implementacija kontinuiteta poslovanja prema ISO 22301 — vaša sigurnost i spremnost u svakoj situaciji.":
        "Umsetzung der Geschäftskontinuität gemäß ISO 22301 - Ihre Sicherheit und Bereitschaft in jeder Situation.",
    "Konsultacije za implementaciju ISO/IEC 20000-1 — izvrsnost u upravljanju IT uslugama vaše organizacije.":
        "Beratung zur Implementierung von ISO/IEC 20000-1 - Exzellenz im IT-Service-Management Ihrer Organisation.",
    "Upravljanje rizicima prema ISO 31000 — identifikacija, procena i smanjenje rizika u vašoj organizaciji.":
        "Risikomanagement gemäß ISO 31000 - Identifikation, Bewertung und Reduzierung von Risiken in Ihrer Organisation.",
    "Testiranje bezbednosti IT sistema — identifikacija ranjivosti i zaštita vaše digitalne imovine od napada i pretnji.":
        "Sicherheitstests von IT-Systemen - Schwachstellen erkennen und Ihre digitalen Werte vor Angriffen und Bedrohungen schützen.",
    "GeoBiz kontakt, IT podrška, Sremska Mitrovica, office@geo-biz.com": "GeoBiz Kontakt, IT-Support, Sremska Mitrovica, office@geo-biz.com",
    "Održavanje računara": "Computerwartung",
    "Projektovanje i izvođenje mreža": "Netzwerkplanung und -aufbau",
    "Održavanje servera": "Serverwartung",
    "Optimizacija vaše poslovne infrastrukture": "Optimierung Ihrer Geschäftsinfrastruktur",
    "Vaš ključ za digitalni napredak": "Ihr Schlüssel zum digitalen Fortschritt",
    "Vaš pouzdan partner za besprekorno digitalno iskustvo": "Ihr zuverlässiger Partner für ein reibungsloses digitales Erlebnis",
    "Temelj vašeg digitalnog uspeha": "Die Grundlage Ihres digitalen Erfolgs",
    "Ogledalo vaše kompanije": "Der Spiegel Ihres Unternehmens",
    "Čuvanje vaših digitalnih podataka": "Speicherung Ihrer digitalen Daten",
    "Zaštitite vaše poslovanje": "Schützen Sie Ihr Unternehmen",
    "Unapređenje Sistema kontinuiteta poslovanja": "Verbesserung des Business-Continuity-Systems",
    "Naše usluge uključuju:": "Unsere Leistungen umfassen:",
    "To uključuje redovno:": "Dazu gehört regelmäßig:",
    "To uključuje zaštitu podataka od:": "Dazu gehört der Schutz von Daten vor:",
    "Pružamo redovno:": "Wir bieten regelmäßig:",
    "Koristimo najsavremenije alate i tehnike, uključujući:": "Wir verwenden modernste Werkzeuge und Techniken, darunter:",
    "Ažuriranje softvera": "Software-Updates",
    "Praćenje performansi": "Leistungsüberwachung",
    "Praćenje rizika": "Risikoüberwachung",
    "Rešavanje problema i preventivno održavanje radi sprečavanja budućih problema":
        "Problembehebung und vorbeugende Wartung zur Vermeidung künftiger Probleme",
    "Rešavanje problema kako bismo osigurali kontinuiranu dostupnost vaših aplikacija i podataka":
        "Problembehebung, um die kontinuierliche Verfügbarkeit Ihrer Anwendungen und Daten sicherzustellen",
    "Održavanje servera": "Serverwartung",
    "Održavanje i": "Wartung und",
    "Korisničko iskustvo": "Benutzererfahrung",
    "Optimizovanost za različite uređaje": "Optimierung für verschiedene Geräte",
    "Optimizacija za pretraživače": "Suchmaschinenoptimierung",
    "Aplikacija za mobilne uređaje": "Mobile Anwendungen",
    "Etičko hakovanje": "Ethisches Hacking",
    "Otklanjanje uočenih ranjivosti": "Beseitigung erkannter Schwachstellen",
    "Otklanjanje uočenih slabosti": "Beseitigung erkannter Schwächen",
    "Poboljšanje sistema": "Systemverbesserung",
    "Oštećenja": "Beschädigungen",
    "Neovlaštenog pristupa": "Unbefugter Zugriff",
    "Detaljan izveštaj i predlog unapređenja sistema": "Detaillierter Bericht und Vorschlag zur Systemverbesserung",
    "Detaljni izveštaji sa predlogom mera": "Detaillierte Berichte mit Maßnahmenvorschlägen",
    "Metabase - izveštaji": "Metabase - Berichte",
    "Poverljivost i dostupnost podataka vaših klijenata": "Vertraulichkeit und Verfügbarkeit der Daten Ihrer Kunden",
    "upravljanja informacionom bezbednošću u okviru organizacije": "Management der Informationssicherheit innerhalb der Organisation",
    "Kao i podršku tokom sertifikacije": "Sowie Unterstützung während der Zertifizierung",
    "i druge metode kako bismo otkrili i rešili potencijalne sigurnosne rupe.":
        "und weitere Methoden, um potenzielle Sicherheitslücken aufzudecken und zu beheben.",
    "Radimo sa strašću kako bismo stvorili rješenja koja donose stvarnu vrednost.":
        "Wir arbeiten mit Leidenschaft, um Lösungen zu schaffen, die echten Mehrwert bieten.",
    "Naš tim web dizajnera koristi svoje stručno znanje i kreativnost kako bi kreirao dizajn koji odgovara potrebama i preferencijama klijenta, uzimajući u obzir aspekte kao što su":
        "Unser Webdesign-Team nutzt sein Fachwissen und seine Kreativität, um ein Design zu erstellen, das den Bedürfnissen und Vorlieben des Kunden entspricht und Aspekte berücksichtigt wie",
    "Naš tim stručnjaka posvećen je razvoju prilagođenih baza podataka i aplikacija koje zadovoljavaju specifične potrebe i zahteve naših klijenata. Počevši od:":
        "Unser Expertenteam widmet sich der Entwicklung maßgeschneiderter Datenbanken und Anwendungen, die den spezifischen Anforderungen unserer Kunden gerecht werden. Beginnend mit:",
    "Naša posvećenost bezbednosti informacija obuhvata sve aspekte vašeg poslovanja, uključujući:":
        "Unser Engagement für Informationssicherheit umfasst alle Aspekte Ihres Geschäfts, einschließlich:",
    "Naša posvećenost upravljanju rizicima obuhvata sve aspekte našeg poslovanja, uključujući:":
        "Unser Engagement für das Risikomanagement umfasst alle Aspekte unseres Geschäfts, einschließlich:",
    "ISO 27001 je standard koji definiše zahteve za:": "ISO 27001 ist ein Standard, der Anforderungen festlegt für:",
    "ISO 22301 je međunarodni standard koji definiše zahteve za upravljanje kontinuitetom poslovanja, uključujući":
        "ISO 22301 ist ein internationaler Standard, der Anforderungen an das Business-Continuity-Management definiert, einschließlich",
    "ISO 31000 je međunarodni standard koji pruža okvir za upravljanje rizicima u organizaciji, uključujući:":
        "ISO 31000 ist ein internationaler Standard, der einen Rahmen für das Risikomanagement in einer Organisation bietet, einschließlich:",
    "U zavisnosti od veličine vašeg IT sistema, složenosti infrastrukture, broja korisnika, nudimo vam konkurentne cene:":
        "Je nach Größe Ihres IT-Systems, Komplexität der Infrastruktur und Anzahl der Nutzer bieten wir Ihnen wettbewerbsfähige Preise:",
    "do 10 računara": "bis zu 10 Computer",
    "od 10 do 20 računara": "von 10 bis 20 Computer",
    "20 računara + serveri": "20+ Computer + Server",
    "Naša usluga podrazumeva implementaciju virtualnog okruženja najpopularnijih sistema za virtuelizaciju":
        "Unser Service umfasst die Einrichtung einer virtuellen Umgebung mit den beliebtesten Virtualisierungssystemen",
    "Glavni cilj usluge data storage je osigurati pouzdanost, sigurnost i dostupnost sačuvanih podataka.":
        "Das Hauptziel des Data-Storage-Dienstes ist es, die Zuverlässigkeit, Sicherheit und Verfügbarkeit der gespeicherten Daten zu gewährleisten.",
    "Naša usluga održavanja računara obuhvata sve aspekte potrebne za održavanje vaših IT sastava u optimalnom stanju.":
        "Unser Computerwartungsdienst deckt alle Aspekte ab, die erforderlich sind, um Ihre IT-Systeme in optimalem Zustand zu halten.",
    "današnjem digitalnom dobu, pouzdanost i performanse računarskih sistema su ključne za uspješno poslovanje. Upravo zato, u GeoBiz-u predani smo pružanju vrhunskih usluga održavanja računara koje osiguravaju besprekorno rad vaših IT sistema.":
        "Im heutigen digitalen Zeitalter sind Zuverlässigkeit und Leistung von Computersystemen entscheidend für den Geschäftserfolg. Genau deshalb sind wir bei GeoBiz bestrebt, erstklassige Computerwartungsdienste zu bieten, die den reibungslosen Betrieb Ihrer IT-Systeme sicherstellen.",
    "Naš tim stručnjaka posvećen je održavanju i optimizaciji vaših računarskih resursa kako biste mogli maksimalno iskoristiti svoje IT investicije. Bez obzira jeste li malo preduzeće, srednje preduzeće ili velika korporacija, pružamo vam prilagođene usluge održavanja koje odgovaraju vašim specifičnim potrebama i zahtevima.":
        "Unser Expertenteam widmet sich der Wartung und Optimierung Ihrer Computerressourcen, damit Sie Ihre IT-Investitionen optimal nutzen können. Ob Kleinunternehmen, mittelständisches Unternehmen oder Großkonzern - wir bieten maßgeschneiderte Wartungsdienste, die Ihren Anforderungen entsprechen.",
    "Naš cilj je osigurati kontinuiranu dostupnost, stabilnost i sigurnost vaših računarskih sistema, kako biste se mogli potpuno posvetiti svojim poslovnim aktivnostima. Kao vaš pouzdan partner za održavanje računara, GeoBiz vam pruža stručnost, iskustvo i predanost potrebne za postizanje izvrsnih rezultata. Kontaktirajte nas danas i osigurajte da vaši računarski sistemi uvek budu u vrhunskom stanju.":
        "Unser Ziel ist es, die kontinuierliche Verfügbarkeit, Stabilität und Sicherheit Ihrer Computersysteme zu gewährleisten, damit Sie sich voll auf Ihr Geschäft konzentrieren können. Als Ihr zuverlässiger Partner für die Computerwartung bietet GeoBiz das Fachwissen und Engagement für hervorragende Ergebnisse. Kontaktieren Sie uns heute und sorgen Sie dafür, dass Ihre Computersysteme stets in Bestform sind.",
    "U današnjem povezanom svetu, stabilna i skalabilna mrežna infrastruktura ključna je za uspeh svake organizacije. U GeoBiz kompaniji stručnjaci smo za projekovanje i izvođenje mrežnih infrastruktura koje omogućuju sigurnu i pouzdanu komunikaciju te podržavaju rast i razvoj vašeg poslovanja.":
        "In der heutigen vernetzten Welt ist eine stabile und skalierbare Netzwerkinfrastruktur entscheidend für den Erfolg jeder Organisation. Bei GeoBiz sind wir Experten für die Planung und den Aufbau von Netzwerkinfrastrukturen, die eine sichere und zuverlässige Kommunikation ermöglichen und das Wachstum Ihres Unternehmens unterstützen.",
    "Naš tim stručnjaka poseduje bogato iskustvo u implementaciji različitih tehnologija i platformi kako bi se osiguralo da vaša mrežna infrastruktura bude optimalno projektovana i implementirana. Koristimo najnovije alate i prakse kako bismo osigurali visok nivo performansi, pouzdanosti i sigurnosti vaše mrežne infrastrukture.":
        "Unser Expertenteam verfügt über umfangreiche Erfahrung bei der Implementierung verschiedener Technologien und Plattformen, um sicherzustellen, dass Ihre Netzwerkinfrastruktur optimal geplant und umgesetzt wird. Wir nutzen modernste Werkzeuge und Praktiken für ein hohes Maß an Leistung, Zuverlässigkeit und Sicherheit.",
    "Kroz našu uslugu projektovanja i izvođenja mrežne infrastrukture, nudimo vam sve potrebno za uspešno vođenje vašeg poslovanja u digitalnom svijetu. Kontaktirajte nas danas i dopustite nam da vam pomognemo izgraditi temelj za vaš digitalni uspjeh.":
        "Mit unserem Service für die Planung und den Aufbau der Netzwerkinfrastruktur bieten wir Ihnen alles, was Sie für ein erfolgreiches Geschäft in der digitalen Welt brauchen. Kontaktieren Sie uns heute und lassen Sie uns gemeinsam die Grundlage für Ihren digitalen Erfolg schaffen.",
    "U današnjem digitalnom dobu, poslovna infrastruktura mora biti pouzdana, skalabilna i efikasna kako bi podržala rast i razvoj organizacije. U kompaniji GeoBiz, specijalizovani smo za pružanje usluga održavanja servera i virtualizacije koje omogućuju optimizaciju vaše IT infrastrukture.":
        "Im heutigen digitalen Zeitalter muss die Geschäftsinfrastruktur zuverlässig, skalierbar und effizient sein, um das Wachstum der Organisation zu unterstützen. Bei GeoBiz sind wir auf Serverwartung und Virtualisierung spezialisiert, die die Optimierung Ihrer IT-Infrastruktur ermöglichen.",
    "Naš tim stručnjaka posvećen je održavanju i upravljanju vašim serverskim okruženjem kako biste se mogli potpuno posvetiti svojim poslovnim aktivnostima.":
        "Unser Expertenteam widmet sich der Wartung und Verwaltung Ihrer Serverumgebung, damit Sie sich voll auf Ihr Geschäft konzentrieren können.",
    "Naš tim stručnjaka posvećen je održavanju i upravljanju vašim serverskim okruženjem kako biste se mogli potpuno posvetiti svojim poslovnim aktivnostima. Pružamo redovno održavanje servera, nadzor performansi, sigurnosne provere i rješavanje problema kako bismo osigurali kontinuiranu dostupnost vaših aplikacija i podataka.":
        "Unser Expertenteam widmet sich der Wartung und Verwaltung Ihrer Serverumgebung, damit Sie sich voll auf Ihr Geschäft konzentrieren können. Wir bieten regelmäßige Serverwartung, Leistungsüberwachung, Sicherheitsprüfungen und Problembehebung, um die kontinuierliche Verfügbarkeit Ihrer Anwendungen und Daten sicherzustellen.",
    "Uz to, nudimo i usluge virtualizacije koje vam omogućuju iskorišćavanje punog potencijala vaše serverske infrastrukture. Virtualizacija omogućuje optimizaciju resursa, smanjenje troškova i povećanje skalabilnosti, pružajući vam fleksibilnost koja vam je potrebna za prilagođavanje promenjivim poslovnim zahtevima.":
        "Darüber hinaus bieten wir Virtualisierungsdienste, mit denen Sie das volle Potenzial Ihrer Serverinfrastruktur ausschöpfen. Virtualisierung optimiert Ressourcen, senkt Kosten und erhöht die Skalierbarkeit und gibt Ihnen die Flexibilität, sich an veränderte Geschäftsanforderungen anzupassen.",
    "Kao vaš pouzdan partner za održavanje servera i virtualizaciju, kompanija GeoBiz pruža vam stručnost i podršku potrebnu za postizanje izvrsnih rezultata. Kontaktirajte nas danas i osigurajte da vaša poslovna infrastruktura bude spremna za budućnost.":
        "Als Ihr zuverlässiger Partner für Serverwartung und Virtualisierung bietet GeoBiz das Fachwissen und die Unterstützung für hervorragende Ergebnisse. Kontaktieren Sie uns heute und sorgen Sie dafür, dass Ihre Geschäftsinfrastruktur für die Zukunft gerüstet ist.",
    "Kontaktirajte nas danas i osigurajte da vaša poslovna infrastruktura bude spremna za budućnost.":
        "Kontaktieren Sie uns heute und sorgen Sie dafür, dass Ihre Geschäftsinfrastruktur für die Zukunft gerüstet ist.",
    "VMware vSphere je platforma za virtualizaciju podataka koja omogućuje stvaranje i upravljanje virtualnim mašinama. VMware ESXi je hipervizor koji se koristi kao osnova za virtualizaciju u vSphere okruženju.":
        "VMware vSphere ist eine Virtualisierungsplattform, die das Erstellen und Verwalten virtueller Maschinen ermöglicht. VMware ESXi ist ein Hypervisor, der als Grundlage für die Virtualisierung in der vSphere-Umgebung dient.",
    "Hyper-V je Microsoftova platforma za virtualizaciju koja omogućuje stvaranje i upravljanje virtualnim mašinama na Windows okruženju.":
        "Hyper-V ist die Virtualisierungsplattform von Microsoft, die das Erstellen und Verwalten virtueller Maschinen in einer Windows-Umgebung ermöglicht.",
    "VirtualBox je besplatna open-source platforma za virtualizaciju koja podržava stvaranje virtualnih mašina na različitim operativnim sustavima, uključujući Windows, Linux, Mac OS X i druge.":
        "VirtualBox ist eine kostenlose Open-Source-Virtualisierungsplattform, die das Erstellen virtueller Maschinen auf verschiedenen Betriebssystemen unterstützt, darunter Windows, Linux, Mac OS X und andere.",
    "KVM je hipervizor otvorenog koda koji se koristi u Linux okruženju za virtualizaciju operativnih sistema.":
        "KVM ist ein Open-Source-Hypervisor, der in der Linux-Umgebung zur Virtualisierung von Betriebssystemen verwendet wird.",
    "XenServer je platforma za virtualizaciju koju razvija Citrix Systems, koja omogućuje stvaranje i upravljanje virtualnim mašinama i podržava različite operativne sisteme.":
        "XenServer ist eine von Citrix Systems entwickelte Virtualisierungsplattform, die das Erstellen und Verwalten virtueller Maschinen ermöglicht und verschiedene Betriebssysteme unterstützt.",
    "Usluga data storage predstavlja pružanje kapaciteta i infrastrukture za čuvanje podataka u digitalnom formatu. Ova usluga omogućuje korisnicima da sigurno čuvaju svoje podatke na udaljenim serverima ili skladištima, pristupaju im kad god je potrebno i dele ih s drugima prema potrebi.":
        "Data Storage ist die Bereitstellung von Kapazität und Infrastruktur zur Speicherung von Daten im digitalen Format. Dieser Dienst ermöglicht es Nutzern, ihre Daten sicher auf entfernten Servern oder Speichern abzulegen, jederzeit darauf zuzugreifen und sie bei Bedarf mit anderen zu teilen.",
    "Usluga data storage igra ključnu ulogu u modernom informacionom društvu, omogućujući organizacijama i pojedincima da pravilno upravljaju, dele i koriste svoje podatke u svakodnevnom poslovanju i životu.":
        "Data Storage spielt eine Schlüsselrolle in der modernen Informationsgesellschaft und ermöglicht es Organisationen und Einzelpersonen, ihre Daten im Alltag und Geschäft richtig zu verwalten, zu teilen und zu nutzen.",
    "Usluga data storage može biti implementirana na različite načine, uključujući lokalno čuvanje podataka na vlastitim NAS serverima, korišćenje cloud storage-a kod pružaoca usluga cloud computinga, ili kombinaciju oba pristupa. Korisnici mogu birati između različitih modela čuvanja podataka, kao što su lokalno, cloud ili kombinovano, zavisno o njihovim specifičnim potrebama i zahtevima.":
        "Data Storage kann auf verschiedene Weise umgesetzt werden, darunter lokale Speicherung auf eigenen NAS-Servern, Cloud-Speicher bei einem Cloud-Anbieter oder eine Kombination aus beidem. Nutzer können zwischen verschiedenen Modellen wählen - lokal, Cloud oder hybrid - je nach ihren spezifischen Anforderungen.",
    "Usluga web dizajna obuhvata proces stvaranja i oblikovanja estetski privlačnih, funkcionalnih i korisnički orijentisanih web stranica. Ova usluga uključuje usku saradnju između dizajnera i klijenata kako bi se stvorio online identitet koji odražava brend, ciljeve i vrednosti klijenta.":
        "Webdesign umfasst den Prozess der Gestaltung ästhetisch ansprechender, funktionaler und nutzerorientierter Websites. Dieser Dienst beinhaltet eine enge Zusammenarbeit zwischen Designern und Kunden, um eine Online-Identität zu schaffen, die Marke, Ziele und Werte des Kunden widerspiegelt.",
    "Usluga web dizajna obuhvata sve korake od početnog planiranja i konceptualizacije do implementacije i testiranja web stranice. Naši dizajneri rade na stvaranju jedinstvenih i privlačnih dizajna koji privlače pažnju posetilaca i podstiču ih na interakciju sa sadržajem.":
        "Webdesign umfasst alle Schritte von der ersten Planung und Konzeption bis zur Umsetzung und zum Testen der Website. Unsere Designer schaffen einzigartige und ansprechende Designs, die die Aufmerksamkeit der Besucher gewinnen und sie zur Interaktion mit den Inhalten anregen.",
    "Cilj nam je stvoriti web stranice koja pružaju pozitivno korisničko iskustvo, olakšava navigaciju, podstiče angažman korisnika i doprinosi postizanju poslovnih ciljeva klijenta. , promociji usluga ili deljenju informacija.":
        "Unser Ziel ist es, Websites zu schaffen, die ein positives Nutzererlebnis bieten, die Navigation erleichtern, das Engagement fördern und zur Erreichung der Geschäftsziele des Kunden beitragen - sei es zur Bewerbung von Dienstleistungen oder zur Weitergabe von Informationen.",
    "U GeoBiz kompaniji specijalizovani smo jedinstveno kreiranje baza i aplikacija koje podstiču digitalni napredak i unapređuju poslovanje naših klijenata.":
        "Bei GeoBiz sind wir auf die Erstellung einzigartiger Datenbanken und Anwendungen spezialisiert, die den digitalen Fortschritt fördern und das Geschäft unserer Kunden verbessern.",
    "Kreiramo aplikacije koje su prilagođenje vašem poslovanju, aplikacije koje će ubrzati vaše poslovanje, olakšati rad i omogućiti menadžmentu brže donošenje pravih odluka na osnovu izveštaja koje pravimo.":
        "Wir entwickeln auf Ihr Geschäft zugeschnittene Anwendungen - Anwendungen, die Ihre Abläufe beschleunigen, die Arbeit erleichtern und es dem Management ermöglichen, anhand der von uns erstellten Berichte schneller die richtigen Entscheidungen zu treffen.",
    "Kroz naše usluge, klijenti dobijaju prilagođene baze podataka koje omogućuju efikasno upravljanje i analizu podataka, kao i aplikacije koje poboljšavaju produktivnost, automatizuju procese i poboljšavaju korisničko iskustvo.":
        "Durch unsere Leistungen erhalten Kunden maßgeschneiderte Datenbanken für effizientes Datenmanagement und -analyse sowie Anwendungen, die die Produktivität steigern, Prozesse automatisieren und die Benutzererfahrung verbessern.",
    "Nezavisno o veličini vaše kompanije ili industrije, razvićemo za vas potrebne alate i resurse za uspešno vođenje vašeg poslovanja u digitalnom svetu. Kontaktirajte nas danas i otkrijte kako možemo transformisati vaše poslovanje putem naprednih tehnoloških rešenja.":
        "Unabhängig von Größe oder Branche Ihres Unternehmens entwickeln wir die Werkzeuge und Ressourcen, die Sie für ein erfolgreiches Geschäft in der digitalen Welt benötigen. Kontaktieren Sie uns heute und entdecken Sie, wie wir Ihr Geschäft mit fortschrittlichen Technologielösungen transformieren können.",
    "U GeoBiz kompaniji posvećeni smo pružanju najvišeg nivoa bezbednosti informacija našim klijentima. Kao deo naše usluge, implementiramo i održavamo bezbednosne standarde prema ISO 27001 standardu, osiguravajući da vaši podaci budu zaštićeni u skladu sa međunarodno priznatim normama.":
        "Bei GeoBiz setzen wir uns dafür ein, unseren Kunden das höchste Maß an Informationssicherheit zu bieten. Im Rahmen unseres Dienstes implementieren und pflegen wir Sicherheitsstandards gemäß ISO 27001 und stellen sicher, dass Ihre Daten gemäß international anerkannten Normen geschützt sind.",
    "Kroz primenu ovog standarda, mi osiguravamo da su informacije naših klijenata zaštićene od svih mogućih prijetnji, uključujući neovlašteni pristup, gubitak ili krađu podataka.":
        "Durch die Anwendung dieses Standards stellen wir sicher, dass die Informationen unserer Kunden vor allen möglichen Bedrohungen geschützt sind, einschließlich unbefugtem Zugriff, Datenverlust oder Datendiebstahl.",
    "U GeoBiz kompaniji razumemo važnost kontinuiteta poslovanja za naše klijente. Kao deo naše usluge, implementiramo zahteve kontinuiteta poslovanja prema ISO 22301 standardu, osiguravajući da vaše poslovanje ostane stabilno i funkcionalno čak i u nepredviđenim situacijama.":
        "Bei GeoBiz verstehen wir die Bedeutung der Geschäftskontinuität für unsere Kunden. Im Rahmen unseres Dienstes implementieren wir die Anforderungen an die Geschäftskontinuität gemäß ISO 22301 und stellen sicher, dass Ihr Geschäft auch in unvorhergesehenen Situationen stabil und funktionsfähig bleibt.",
    "Naša posvećenost kontinuitetu poslovanja obuhvata sve aspekte vašeg poslovanja, uključujući infrastrukturu, operativne procese, osoblje i partnere. Kroz implementaciju strogo planiranje infrastrukture, redovne vežbe i testiranja, te kontinuirano praćenje i poboljšavanje, osiguravamo da naši klijenti budu spremni suočiti se s izazovima i očuvati kontinuitet poslovanja u svakoj situaciji.":
        "Unser Engagement für die Geschäftskontinuität umfasst alle Aspekte Ihres Geschäfts, einschließlich Infrastruktur, operativer Prozesse, Personal und Partner. Durch sorgfältige Infrastrukturplanung, regelmäßige Übungen und Tests sowie kontinuierliche Überwachung und Verbesserung stellen wir sicher, dass unsere Kunden auf Herausforderungen vorbereitet sind und die Geschäftskontinuität in jeder Situation wahren.",
    "Kroz našu uslugu implementacije kontinuiteta poslovanja prema ISO standardima, pružamo vam miran san i sigurnost u pouzdanost vašeg poslovanja, čak i u nepredviđenim okolnostima. Kontaktirajte nas danas i otkrijte kako možemo unaprijediti kontinuitet vašeg poslovanja i osigurati vašu sigurnost u svakoj situaciji.":
        "Mit unserem Service zur Umsetzung der Geschäftskontinuität nach ISO-Standards geben wir Ihnen Sicherheit und Vertrauen in die Zuverlässigkeit Ihres Geschäfts, selbst unter unvorhergesehenen Umständen. Kontaktieren Sie uns heute und entdecken Sie, wie wir Ihre Geschäftskontinuität verbessern und Ihre Sicherheit in jeder Situation gewährleisten können.",
    "U GeoBiz kompaniji, predani smo pružanju visokih standarda sigurnosti i pouzdanosti za naše klijente. Kao deo naše usluge, implementiramo zahteve Sistema upravljanja rizicima prema ISO 31000 standardu, osiguravajući da vaše poslovanje bude otporno na rizike i pripremljeno za suočavanje s izazovima.":
        "Bei GeoBiz setzen wir uns für hohe Sicherheits- und Zuverlässigkeitsstandards für unsere Kunden ein. Im Rahmen unseres Dienstes implementieren wir die Anforderungen des Risikomanagementsystems gemäß ISO 31000 und stellen sicher, dass Ihr Geschäft widerstandsfähig gegenüber Risiken und auf Herausforderungen vorbereitet ist.",
    "Kroz primjenu ovog standarda, mi pomažemo našim klijentima da prepoznaju potencijalne prijetnje, identifikuju ranjive tačke i razviju strategije za minimiziranje i upravljanje rizicima.":
        "Durch die Anwendung dieses Standards helfen wir unseren Kunden, potenzielle Bedrohungen zu erkennen, Schwachstellen zu identifizieren und Strategien zur Minimierung und Steuerung von Risiken zu entwickeln.",
    "Kroz primjenu ovog standarda, mi pomažemo našim klijentima da identifikuju ključne procese, resurse i rizike te razviju strategije za njihovo očuvanje i obnovu u slučaju prekida poslovanja.":
        "Durch die Anwendung dieses Standards helfen wir unseren Kunden, Schlüsselprozesse, Ressourcen und Risiken zu identifizieren und Strategien für deren Erhalt und Wiederherstellung im Falle einer Geschäftsunterbrechung zu entwickeln.",
    "Kroz implementaciju stroge metodologije upravljanja rizicima, redovno praćenje i analizu, te kontinuirano poboljšanje, osiguravamo da naši klijenti budu otporni na rizike i spremni suočiti se s neizvesnostima.":
        "Durch eine strenge Risikomanagement-Methodik, regelmäßige Überwachung und Analyse sowie kontinuierliche Verbesserung stellen wir sicher, dass unsere Kunden widerstandsfähig gegenüber Risiken und auf Unsicherheiten vorbereitet sind.",
    "Kroz našu uslugu implementacije Sistema upravljanja rizicima prema ISO standardima, pružamo vam miran san i sigurnost i pouzdanost vašeg poslovanja, čak i u nepredviđenim okolnostima. Kontaktirajte nas danas i otkrijte kako možemo unaprediti upravljanje rizicima u vašoj organizaciji i osigurati vašu zaštitu od neizvesnosti.":
        "Mit unserem Service zur Umsetzung des Risikomanagementsystems nach ISO-Standards geben wir Ihnen Sicherheit sowie Vertrauen in die Zuverlässigkeit Ihres Geschäfts, selbst unter unvorhergesehenen Umständen. Kontaktieren Sie uns heute und entdecken Sie, wie wir das Risikomanagement in Ihrer Organisation verbessern und Sie vor Unsicherheiten schützen können.",
    "U GeoBiz kompaniji predani smo osiguravanju visokih standarda sigurnosti za naše klijente. Kao deo naše usluge, pružamo testiranje sigurnosti IT sistema kako bismo identifikovali potencijalne ranjivosti i osigurali da vaša digitalna imovina bude zaštićena od napada i pretnji. Naš tim stručnjaka sprovodi temeljna ispitivanja i analize kako bi identifikovali ranjivosti u vašem IT okruženju, uključujući mrežne sisteme, aplikacije, baze podataka i infrastrukturu.":
        "Bei GeoBiz setzen wir uns für hohe Sicherheitsstandards für unsere Kunden ein. Im Rahmen unseres Dienstes führen wir Sicherheitstests von IT-Systemen durch, um potenzielle Schwachstellen zu erkennen und Ihre digitalen Werte vor Angriffen und Bedrohungen zu schützen. Unser Expertenteam führt gründliche Prüfungen und Analysen durch, um Schwachstellen in Ihrer IT-Umgebung zu identifizieren - einschließlich Netzwerke, Anwendungen, Datenbanken und Infrastruktur.",
    "Naš cilj je osigurati da vaši IT sistemi budu otporni na napade, sigurni od neovlašćenog pristupa i pouzdani u zaštiti vaših osetljivih informacija. Nakon sprovedenog testiranja, pružamo vam detaljne izveštaje i preporuke za poboljšanje sigurnosti vašeg IT okruženja.":
        "Unser Ziel ist es, Ihre IT-Systeme widerstandsfähig gegen Angriffe, sicher vor unbefugtem Zugriff und zuverlässig beim Schutz Ihrer sensiblen Daten zu machen. Nach dem Test stellen wir Ihnen detaillierte Berichte und Empfehlungen zur Verbesserung der Sicherheit Ihrer IT-Umgebung bereit.",
    "Kroz našu uslugu testiranja sigurnosti IT sistema, pružamo vam miran san i sigurnost u pouzdanost vaše digitalne imovine. Kontaktirajte nas danas i osigurajte da vaši IT sistemi budu u skladu s najvišim standardima sigurnosti.":
        "Mit unserem Service für Sicherheitstests von IT-Systemen geben wir Ihnen Sicherheit und Vertrauen in die Zuverlässigkeit Ihrer digitalen Werte. Kontaktieren Sie uns heute und stellen Sie sicher, dass Ihre IT-Systeme den höchsten Sicherheitsstandards entsprechen.",
    "Dobrodošli u našu firmu, vašeg partnera za implementaciju ISO/IEC 20000-1 standarda! Naša usluga konsultacija za implementaciju ISO/IEC 20000-1 osmišljena je kako bismo vam pomogli da vaša organizacija postigne izvrsnost u upravljanju IT uslugama.":
        "Willkommen bei unserem Unternehmen, Ihrem Partner für die Implementierung des Standards ISO/IEC 20000-1! Unser Beratungsservice zur Implementierung von ISO/IEC 20000-1 soll Ihrer Organisation helfen, Exzellenz im IT-Service-Management zu erreichen.",
    "Sa našim iskusnim timom stručnjaka, pružamo sveobuhvatnu podršku u procesu implementacije ovog važnog standarda. Naš pristup je prilagođen vašim specifičnim potrebama i ciljevima, uzimajući u obzir veličinu vaše organizacije, industrijski sektor i postojeće prakse.":
        "Mit unserem erfahrenen Expertenteam bieten wir umfassende Unterstützung bei der Implementierung dieses wichtigen Standards. Unser Ansatz ist auf Ihre spezifischen Bedürfnisse und Ziele zugeschnitten und berücksichtigt die Größe Ihrer Organisation, die Branche und bestehende Praktiken.",
    "Naš cilj je da vam pružimo sve potrebne alate i znanje kako biste uspešno implementirali ISO/IEC 20000-1 standard i postigli kontinuirano unapređenje vaših IT usluga.":
        "Unser Ziel ist es, Ihnen alle Werkzeuge und das Wissen bereitzustellen, um den Standard ISO/IEC 20000-1 erfolgreich umzusetzen und eine kontinuierliche Verbesserung Ihrer IT-Services zu erreichen.",
    "Poverite nam vaše izazove, a mi ćemo vam pomoći da postignete visoke standarde u upravljanju IT uslugama, što će rezultirati povećanom efikasnošću, smanjenjem rizika i većim zadovoljstvom korisnika. Kontaktirajte nas danas i zajedno ćemo graditi put ka uspehu vaše organizacije u digitalnom dobu.":
        "Vertrauen Sie uns Ihre Herausforderungen an, und wir helfen Ihnen, hohe Standards im IT-Service-Management zu erreichen, was zu höherer Effizienz, geringerem Risiko und größerer Nutzerzufriedenheit führt. Kontaktieren Sie uns heute, und gemeinsam gestalten wir den Weg zum Erfolg Ihrer Organisation im digitalen Zeitalter.",
})

# =================== Titlovi, meta, keywords (bez dijakritika) ===================
EN.update({
    "GeoBiz — IT usluge, konsalting i bezbednost | Sremska Mitrovica": "GeoBiz — IT services, consulting and security | Sremska Mitrovica",
    "GeoBiz pruža kompletne IT usluge: održavanje računara i servera, mrežnu infrastrukturu, data storage, web dizajn, razvoj aplikacija, IT konsalting (ISO 27001, 22301, 31000, 20000-1) i testiranje bezbednosti.":
        "GeoBiz provides complete IT services: computer and server maintenance, network infrastructure, data storage, web design, application development, IT consulting (ISO 27001, 22301, 31000, 20000-1) and security testing.",
    "GeoBiz, IT usluge, IT konsalting, održavanje računara, održavanje servera, virtuelizacija, mrežna infrastruktura, data storage, web dizajn, razvoj aplikacija, bezbednost informacija, ISO 27001, Sremska Mitrovica":
        "GeoBiz, IT services, IT consulting, computer maintenance, server maintenance, virtualization, network infrastructure, data storage, web design, application development, information security, ISO 27001, Sremska Mitrovica",
    "Kontakt - GeoBiz": "Contact - GeoBiz",
    "Kontaktirajte GeoBiz — IT usluge, konsalting i bezbednost. Mirna 1, Sremska Mitrovica. Email: office@geo-biz.com, tel: +381 63 12 61 227.":
        "Contact GeoBiz — IT services, consulting and security. Mirna 1, Sremska Mitrovica. Email: office@geo-biz.com, phone: +381 63 12 61 227.",
    "Programi - GeoBiz": "Software - GeoBiz",
    "GeoBiz softverski proizvodi: GeoBiz (geodetske firme), GeoDent (zubarske ordinacije), GeoMed (klinike i bolnice), GeoErp (poslovni softver).":
        "GeoBiz software products: GeoBiz (surveying companies), GeoDent (dental offices), GeoMed (clinics and hospitals), GeoErp (business software).",
    "GeoBiz, GeoDent, GeoMed, GeoErp, poslovni softver, programi": "GeoBiz, GeoDent, GeoMed, GeoErp, business software, software",
    "Data storage - GeoBiz": "Data storage - GeoBiz",
    "Web dizajn i razvoj veb sajtova - GeoBiz": "Web design and website development - GeoBiz",
    "web dizajn, izrada sajtova, veb razvoj, GeoBiz": "web design, website creation, web development, GeoBiz",
    "Razvoj aplikacija i baza podataka - GeoBiz": "Application & database development - GeoBiz",
    "razvoj aplikacija, baze podataka, web aplikacije, GeoBiz": "application development, databases, web applications, GeoBiz",
    "Bezbednost informacija (ISO 27001) - GeoBiz": "Information security (ISO 27001) - GeoBiz",
    "bezbednost informacija, ISO 27001, informaciona bezbednost, GeoBiz": "information security, ISO 27001, GeoBiz",
    "Kontinuitet poslovanja (ISO 22301) - GeoBiz": "Business continuity (ISO 22301) - GeoBiz",
    "kontinuitet poslovanja, ISO 22301, business continuity, GeoBiz": "business continuity, ISO 22301, GeoBiz",
    "Upravljanje rizicima (ISO 31000) - GeoBiz": "Risk management (ISO 31000) - GeoBiz",
    "upravljanje rizicima, ISO 31000, procena rizika, GeoBiz": "risk management, ISO 31000, risk assessment, GeoBiz",
    "Upravljanje IT uslugama (ISO/IEC 20000-1) - GeoBiz": "IT service management (ISO/IEC 20000-1) - GeoBiz",
    "upravljanje IT uslugama, ISO 20000, ITSM, GeoBiz": "IT service management, ISO 20000, ITSM, GeoBiz",
    "Testiranje bezbednosti IT sistema - GeoBiz": "IT systems security testing - GeoBiz",
    "testiranje bezbednosti, penetraciono testiranje, IT bezbednost, GeoBiz": "security testing, penetration testing, IT security, GeoBiz",
    "Tim mladih stručnjaka, entuzijasta, ljubitelja tehnologije Vama na usluzi": "A team of young experts, enthusiasts and technology lovers at your service",
})
RU.update({
    "GeoBiz — IT usluge, konsalting i bezbednost | Sremska Mitrovica": "GeoBiz — ИТ-услуги, консалтинг и безопасность | Сремска-Митровица",
    "GeoBiz pruža kompletne IT usluge: održavanje računara i servera, mrežnu infrastrukturu, data storage, web dizajn, razvoj aplikacija, IT konsalting (ISO 27001, 22301, 31000, 20000-1) i testiranje bezbednosti.":
        "GeoBiz предоставляет полный спектр ИТ-услуг: обслуживание компьютеров и серверов, сетевая инфраструктура, хранение данных, веб-дизайн, разработка приложений, ИТ-консалтинг (ISO 27001, 22301, 31000, 20000-1) и тестирование безопасности.",
    "GeoBiz, IT usluge, IT konsalting, održavanje računara, održavanje servera, virtuelizacija, mrežna infrastruktura, data storage, web dizajn, razvoj aplikacija, bezbednost informacija, ISO 27001, Sremska Mitrovica":
        "GeoBiz, ИТ-услуги, ИТ-консалтинг, обслуживание компьютеров, обслуживание серверов, виртуализация, сетевая инфраструктура, хранение данных, веб-дизайн, разработка приложений, информационная безопасность, ISO 27001, Сремска-Митровица",
    "Kontakt - GeoBiz": "Контакт - GeoBiz",
    "Kontaktirajte GeoBiz — IT usluge, konsalting i bezbednost. Mirna 1, Sremska Mitrovica. Email: office@geo-biz.com, tel: +381 63 12 61 227.":
        "Свяжитесь с GeoBiz — ИТ-услуги, консалтинг и безопасность. Mirna 1, Сремска-Митровица. Email: office@geo-biz.com, тел.: +381 63 12 61 227.",
    "Programi - GeoBiz": "Программы - GeoBiz",
    "GeoBiz softverski proizvodi: GeoBiz (geodetske firme), GeoDent (zubarske ordinacije), GeoMed (klinike i bolnice), GeoErp (poslovni softver).":
        "Программные продукты GeoBiz: GeoBiz (геодезические компании), GeoDent (стоматологии), GeoMed (клиники и больницы), GeoErp (бизнес-ПО).",
    "GeoBiz, GeoDent, GeoMed, GeoErp, poslovni softver, programi": "GeoBiz, GeoDent, GeoMed, GeoErp, бизнес-ПО, программы",
    "Data storage - GeoBiz": "Хранение данных - GeoBiz",
    "Web dizajn i razvoj veb sajtova - GeoBiz": "Веб-дизайн и разработка сайтов - GeoBiz",
    "web dizajn, izrada sajtova, veb razvoj, GeoBiz": "веб-дизайн, создание сайтов, веб-разработка, GeoBiz",
    "Razvoj aplikacija i baza podataka - GeoBiz": "Разработка приложений и баз данных - GeoBiz",
    "razvoj aplikacija, baze podataka, web aplikacije, GeoBiz": "разработка приложений, базы данных, веб-приложения, GeoBiz",
    "Bezbednost informacija (ISO 27001) - GeoBiz": "Информационная безопасность (ISO 27001) - GeoBiz",
    "bezbednost informacija, ISO 27001, informaciona bezbednost, GeoBiz": "информационная безопасность, ISO 27001, GeoBiz",
    "Kontinuitet poslovanja (ISO 22301) - GeoBiz": "Непрерывность бизнеса (ISO 22301) - GeoBiz",
    "kontinuitet poslovanja, ISO 22301, business continuity, GeoBiz": "непрерывность бизнеса, ISO 22301, GeoBiz",
    "Upravljanje rizicima (ISO 31000) - GeoBiz": "Управление рисками (ISO 31000) - GeoBiz",
    "upravljanje rizicima, ISO 31000, procena rizika, GeoBiz": "управление рисками, ISO 31000, оценка рисков, GeoBiz",
    "Upravljanje IT uslugama (ISO/IEC 20000-1) - GeoBiz": "Управление ИТ-услугами (ISO/IEC 20000-1) - GeoBiz",
    "upravljanje IT uslugama, ISO 20000, ITSM, GeoBiz": "управление ИТ-услугами, ISO 20000, ITSM, GeoBiz",
    "Testiranje bezbednosti IT sistema - GeoBiz": "Тестирование безопасности ИТ-систем - GeoBiz",
    "testiranje bezbednosti, penetraciono testiranje, IT bezbednost, GeoBiz": "тестирование безопасности, пентест, ИТ-безопасность, GeoBiz",
    "Tim mladih stručnjaka, entuzijasta, ljubitelja tehnologije Vama na usluzi": "Команда молодых специалистов, энтузиастов и любителей технологий к вашим услугам",
})
DE.update({
    "GeoBiz — IT usluge, konsalting i bezbednost | Sremska Mitrovica": "GeoBiz — IT-Dienste, Beratung und Sicherheit | Sremska Mitrovica",
    "GeoBiz pruža kompletne IT usluge: održavanje računara i servera, mrežnu infrastrukturu, data storage, web dizajn, razvoj aplikacija, IT konsalting (ISO 27001, 22301, 31000, 20000-1) i testiranje bezbednosti.":
        "GeoBiz bietet umfassende IT-Dienste: Computer- und Serverwartung, Netzwerkinfrastruktur, Datenspeicherung, Webdesign, Anwendungsentwicklung, IT-Beratung (ISO 27001, 22301, 31000, 20000-1) und Sicherheitstests.",
    "GeoBiz, IT usluge, IT konsalting, održavanje računara, održavanje servera, virtuelizacija, mrežna infrastruktura, data storage, web dizajn, razvoj aplikacija, bezbednost informacija, ISO 27001, Sremska Mitrovica":
        "GeoBiz, IT-Dienste, IT-Beratung, Computerwartung, Serverwartung, Virtualisierung, Netzwerkinfrastruktur, Datenspeicherung, Webdesign, Anwendungsentwicklung, Informationssicherheit, ISO 27001, Sremska Mitrovica",
    "Kontakt - GeoBiz": "Kontakt - GeoBiz",
    "Kontaktirajte GeoBiz — IT usluge, konsalting i bezbednost. Mirna 1, Sremska Mitrovica. Email: office@geo-biz.com, tel: +381 63 12 61 227.":
        "Kontaktieren Sie GeoBiz — IT-Dienste, Beratung und Sicherheit. Mirna 1, Sremska Mitrovica. E-Mail: office@geo-biz.com, Tel.: +381 63 12 61 227.",
    "Programi - GeoBiz": "Software - GeoBiz",
    "GeoBiz softverski proizvodi: GeoBiz (geodetske firme), GeoDent (zubarske ordinacije), GeoMed (klinike i bolnice), GeoErp (poslovni softver).":
        "GeoBiz Softwareprodukte: GeoBiz (Vermessungsfirmen), GeoDent (Zahnarztpraxen), GeoMed (Kliniken und Krankenhäuser), GeoErp (Unternehmenssoftware).",
    "GeoBiz, GeoDent, GeoMed, GeoErp, poslovni softver, programi": "GeoBiz, GeoDent, GeoMed, GeoErp, Unternehmenssoftware, Software",
    "Data storage - GeoBiz": "Datenspeicherung - GeoBiz",
    "Web dizajn i razvoj veb sajtova - GeoBiz": "Webdesign und Website-Entwicklung - GeoBiz",
    "web dizajn, izrada sajtova, veb razvoj, GeoBiz": "Webdesign, Website-Erstellung, Webentwicklung, GeoBiz",
    "Razvoj aplikacija i baza podataka - GeoBiz": "Anwendungs- und Datenbankentwicklung - GeoBiz",
    "razvoj aplikacija, baze podataka, web aplikacije, GeoBiz": "Anwendungsentwicklung, Datenbanken, Web-Anwendungen, GeoBiz",
    "Bezbednost informacija (ISO 27001) - GeoBiz": "Informationssicherheit (ISO 27001) - GeoBiz",
    "bezbednost informacija, ISO 27001, informaciona bezbednost, GeoBiz": "Informationssicherheit, ISO 27001, GeoBiz",
    "Kontinuitet poslovanja (ISO 22301) - GeoBiz": "Geschäftskontinuität (ISO 22301) - GeoBiz",
    "kontinuitet poslovanja, ISO 22301, business continuity, GeoBiz": "Geschäftskontinuität, ISO 22301, GeoBiz",
    "Upravljanje rizicima (ISO 31000) - GeoBiz": "Risikomanagement (ISO 31000) - GeoBiz",
    "upravljanje rizicima, ISO 31000, procena rizika, GeoBiz": "Risikomanagement, ISO 31000, Risikobewertung, GeoBiz",
    "Upravljanje IT uslugama (ISO/IEC 20000-1) - GeoBiz": "IT-Service-Management (ISO/IEC 20000-1) - GeoBiz",
    "upravljanje IT uslugama, ISO 20000, ITSM, GeoBiz": "IT-Service-Management, ISO 20000, ITSM, GeoBiz",
    "Testiranje bezbednosti IT sistema - GeoBiz": "Sicherheitstests von IT-Systemen - GeoBiz",
    "testiranje bezbednosti, penetraciono testiranje, IT bezbednost, GeoBiz": "Sicherheitstests, Penetrationstests, IT-Sicherheit, GeoBiz",
    "Tim mladih stručnjaka, entuzijasta, ljubitelja tehnologije Vama na usluzi": "Ein Team junger Experten, Enthusiasten und Technikbegeisterter zu Ihren Diensten",
})

# =================== Kratke stavke / liste / cenovnik / breadcrumbs (bez dijakritika) ===================
EN.update({
    "Dizajniranja": "Design", "Estetika": "Aesthetics", "Funkcionalnost": "Functionality",
    "Gubitka": "Loss", "Identifikaciju": "Identification", "Implementaciju": "Implementation",
    "Implementiramo:": "We implement:", "Infrastrukturu": "Infrastructure", "Odaberi": "Choose",
    "Partnere": "Partners", "Planiranje": "Planning", "Procenu": "Assessment", "Procese": "Processes",
    "Razvoja": "Development", "Uspostavljanje": "Establishment", "Deljenju informacija": "Sharing information",
    "Desktop aplikacija": "Desktop applications", "Enkripciju podataka": "Data encryption",
    "Implementacije aplikacija": "Application implementation", "Nadzor performansi": "Performance monitoring",
    "Obuku zaposlenih": "Employee training", "Operativne procese": "Operational processes",
    "Penetracijski testovi": "Penetration tests", "Penetracijsko testiranje": "Penetration testing",
    "Penetraciono testiranje": "Penetration testing", "Prodaji proizvoda": "Product sales",
    "Razvoj aplikacija": "Application development", "Razvoj dokumentacije": "Documentation development",
    "Sigurnosne provere": "Security checks", "Terstiranja i": "Testing and", "Upravljanje i": "Management and",
    "Upravljanje uslugama": "Service management", "WEB Designe": "Web design", "WEB Dizajn": "Web design",
    "WEB aplikacija": "Web applications", "Zaposlene i": "Employees and",
    "Aplikacija za administraciju": "Administration application", "Izradu plana implementacije": "Implementation plan development",
    "Procenu trenutnog stanja": "Current-state assessment", "Promociji usluga ili": "Service promotion or",
    "Redovne sigurnosne provere": "Regular security checks", "Skeniranje na ranjivosti": "Vulnerability scanning",
    "Stroge kontrole pristupa": "Strict access controls", "Testiranje IT sistema": "IT systems testing",
    "GeoBiz - baza klijenata": "GeoBiz - client database", "Gevidencija - evidencija C-Linija": "Gevidencija - C-Line records",
    "Testiranje Sigurnosti IT sistema": "IT systems security testing",
    "Bezbednost informacija prema ISO standardima": "Information security according to ISO standards",
    "Bilo da se radi o:": "Whether it involves:", "Razvoju i optimizaciji baza podataka": "Database development and optimization",
    "Bilo da se radi o razvoju:": "Whether it involves the development of:",
    "Detaljnog analiziranja poslovnih procesa i potreba": "Detailed analysis of business processes and needs",
    "Obuke zaposlenih kako bismo osigurali integritet": "Employee training to ensure integrity",
    "Implementacija Sistema Kontinuiteta Poslovanja prema ISO standardu": "Implementation of a Business Continuity System according to the ISO standard",
    "Implementacija Sistema Upravljanja Rizicima prema ISO Standardu": "Implementation of a Risk Management System according to the ISO standard",
    "Obratite nam se za sva pitanja i nedoumice": "Contact us with any questions or concerns",
    "Implementacija Sistema Informacione tehnologije – upravljanje uslugama ISO/IEC 20000-1": "Implementation of an Information Technology Service Management System ISO/IEC 20000-1",
    "Kao i osiguranje njihove dostupnosti korisnicima u svakom trenutku": "As well as ensuring their availability to users at all times",
    "razvoj aplikacija, baze podataka, web aplikacije, desktop aplikacije, GeoBiz": "application development, databases, web applications, desktop applications, GeoBiz",
    "Cenovnik usluge": "Service pricing", "Mob:": "Mobile:",
    "Ilustracija održavanja i servisa računara": "Illustration of computer maintenance and repair",
})
RU.update({
    "Dizajniranja": "Проектирование", "Estetika": "Эстетика", "Funkcionalnost": "Функциональность",
    "Gubitka": "Потеря", "Identifikaciju": "Идентификацию", "Implementaciju": "Внедрение",
    "Implementiramo:": "Мы внедряем:", "Infrastrukturu": "Инфраструктуру", "Odaberi": "Выбрать",
    "Partnere": "Партнёров", "Planiranje": "Планирование", "Procenu": "Оценку", "Procese": "Процессы",
    "Razvoja": "Разработка", "Uspostavljanje": "Создание", "Deljenju informacija": "Обмен информацией",
    "Desktop aplikacija": "Десктоп-приложения", "Enkripciju podataka": "Шифрование данных",
    "Implementacije aplikacija": "Внедрение приложений", "Nadzor performansi": "Мониторинг производительности",
    "Obuku zaposlenih": "Обучение сотрудников", "Operativne procese": "Операционные процессы",
    "Penetracijski testovi": "Тесты на проникновение", "Penetracijsko testiranje": "Тестирование на проникновение",
    "Penetraciono testiranje": "Тестирование на проникновение", "Prodaji proizvoda": "Продажа продуктов",
    "Razvoj aplikacija": "Разработка приложений", "Razvoj dokumentacije": "Разработка документации",
    "Sigurnosne provere": "Проверки безопасности", "Terstiranja i": "Тестирование и", "Upravljanje i": "Управление и",
    "Upravljanje uslugama": "Управление услугами", "WEB Designe": "Веб-дизайн", "WEB Dizajn": "Веб-дизайн",
    "WEB aplikacija": "Веб-приложения", "Zaposlene i": "Сотрудников и",
    "Aplikacija za administraciju": "Приложение для администрирования", "Izradu plana implementacije": "Разработку плана внедрения",
    "Procenu trenutnog stanja": "Оценку текущего состояния", "Promociji usluga ili": "Продвижение услуг или",
    "Redovne sigurnosne provere": "Регулярные проверки безопасности", "Skeniranje na ranjivosti": "Сканирование уязвимостей",
    "Stroge kontrole pristupa": "Строгий контроль доступа", "Testiranje IT sistema": "Тестирование ИТ-систем",
    "GeoBiz - baza klijenata": "GeoBiz - база клиентов", "Gevidencija - evidencija C-Linija": "Gevidencija - учёт C-линии",
    "Testiranje Sigurnosti IT sistema": "Тестирование безопасности ИТ-систем",
    "Bezbednost informacija prema ISO standardima": "Информационная безопасность по стандартам ISO",
    "Bilo da se radi o:": "Будь то:", "Razvoju i optimizaciji baza podataka": "Разработка и оптимизация баз данных",
    "Bilo da se radi o razvoju:": "Будь то разработка:",
    "Detaljnog analiziranja poslovnih procesa i potreba": "Детального анализа бизнес-процессов и потребностей",
    "Obuke zaposlenih kako bismo osigurali integritet": "Обучение сотрудников для обеспечения целостности",
    "Implementacija Sistema Kontinuiteta Poslovanja prema ISO standardu": "Внедрение системы непрерывности бизнеса по стандарту ISO",
    "Implementacija Sistema Upravljanja Rizicima prema ISO Standardu": "Внедрение системы управления рисками по стандарту ISO",
    "Obratite nam se za sva pitanja i nedoumice": "Свяжитесь с нами по любым вопросам",
    "Implementacija Sistema Informacione tehnologije – upravljanje uslugama ISO/IEC 20000-1": "Внедрение системы управления ИТ-услугами ISO/IEC 20000-1",
    "Kao i osiguranje njihove dostupnosti korisnicima u svakom trenutku": "А также обеспечение их доступности пользователям в любой момент",
    "razvoj aplikacija, baze podataka, web aplikacije, desktop aplikacije, GeoBiz": "разработка приложений, базы данных, веб-приложения, десктоп-приложения, GeoBiz",
    "Cenovnik usluge": "Прайс-лист услуги", "Mob:": "Моб.:",
    "Ilustracija održavanja i servisa računara": "Иллюстрация обслуживания и ремонта компьютеров",
})
DE.update({
    "Dizajniranja": "Gestaltung", "Estetika": "Ästhetik", "Funkcionalnost": "Funktionalität",
    "Gubitka": "Verlust", "Identifikaciju": "Identifikation", "Implementaciju": "Implementierung",
    "Implementiramo:": "Wir implementieren:", "Infrastrukturu": "Infrastruktur", "Odaberi": "Auswählen",
    "Partnere": "Partner", "Planiranje": "Planung", "Procenu": "Bewertung", "Procese": "Prozesse",
    "Razvoja": "Entwicklung", "Uspostavljanje": "Einrichtung", "Deljenju informacija": "Weitergabe von Informationen",
    "Desktop aplikacija": "Desktop-Anwendungen", "Enkripciju podataka": "Datenverschlüsselung",
    "Implementacije aplikacija": "Implementierung von Anwendungen", "Nadzor performansi": "Leistungsüberwachung",
    "Obuku zaposlenih": "Mitarbeiterschulung", "Operativne procese": "Betriebsprozesse",
    "Penetracijski testovi": "Penetrationstests", "Penetracijsko testiranje": "Penetrationstests",
    "Penetraciono testiranje": "Penetrationstests", "Prodaji proizvoda": "Produktverkauf",
    "Razvoj aplikacija": "Anwendungsentwicklung", "Razvoj dokumentacije": "Dokumentationserstellung",
    "Sigurnosne provere": "Sicherheitsprüfungen", "Terstiranja i": "Testen und", "Upravljanje i": "Verwaltung und",
    "Upravljanje uslugama": "Service-Management", "WEB Designe": "Webdesign", "WEB Dizajn": "Webdesign",
    "WEB aplikacija": "Web-Anwendungen", "Zaposlene i": "Mitarbeiter und",
    "Aplikacija za administraciju": "Anwendung zur Verwaltung", "Izradu plana implementacije": "Erstellung eines Implementierungsplans",
    "Procenu trenutnog stanja": "Bewertung des Ist-Zustands", "Promociji usluga ili": "Bewerbung von Dienstleistungen oder",
    "Redovne sigurnosne provere": "Regelmäßige Sicherheitsprüfungen", "Skeniranje na ranjivosti": "Schwachstellenscan",
    "Stroge kontrole pristupa": "Strenge Zugriffskontrollen", "Testiranje IT sistema": "Testen von IT-Systemen",
    "GeoBiz - baza klijenata": "GeoBiz - Kundendatenbank", "Gevidencija - evidencija C-Linija": "Gevidencija - C-Linien-Erfassung",
    "Testiranje Sigurnosti IT sistema": "Sicherheitstests von IT-Systemen",
    "Bezbednost informacija prema ISO standardima": "Informationssicherheit nach ISO-Standards",
    "Bilo da se radi o:": "Ob es sich handelt um:", "Razvoju i optimizaciji baza podataka": "Entwicklung und Optimierung von Datenbanken",
    "Bilo da se radi o razvoju:": "Ob es um die Entwicklung von Folgendem geht:",
    "Detaljnog analiziranja poslovnih procesa i potreba": "Detaillierter Analyse der Geschäftsprozesse und Bedürfnisse",
    "Obuke zaposlenih kako bismo osigurali integritet": "Mitarbeiterschulung, um die Integrität zu gewährleisten",
    "Implementacija Sistema Kontinuiteta Poslovanja prema ISO standardu": "Implementierung eines Business-Continuity-Systems nach ISO-Standard",
    "Implementacija Sistema Upravljanja Rizicima prema ISO Standardu": "Implementierung eines Risikomanagementsystems nach ISO-Standard",
    "Obratite nam se za sva pitanja i nedoumice": "Kontaktieren Sie uns bei allen Fragen und Unklarheiten",
    "Implementacija Sistema Informacione tehnologije – upravljanje uslugama ISO/IEC 20000-1": "Implementierung eines IT-Service-Management-Systems ISO/IEC 20000-1",
    "Kao i osiguranje njihove dostupnosti korisnicima u svakom trenutku": "Sowie die Gewährleistung ihrer Verfügbarkeit für die Nutzer zu jeder Zeit",
    "razvoj aplikacija, baze podataka, web aplikacije, desktop aplikacije, GeoBiz": "Anwendungsentwicklung, Datenbanken, Web-Anwendungen, Desktop-Anwendungen, GeoBiz",
    "Cenovnik usluge": "Preisliste der Leistung", "Mob:": "Mobil:",
    "Ilustracija održavanja i servisa računara": "Illustration der Computerwartung und -reparatur",
})

TRANSLATIONS = {'en': EN, 'ru': RU, 'de': DE}
