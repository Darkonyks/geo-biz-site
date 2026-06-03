<?php
/**
 * Primer konfiguracije za kontakt formu.
 *
 * Kopirajte ovaj fajl u `config.php` i popunite stvarnim vrednostima.
 * `config.php` se NE čuva u Git-u (vidi .gitignore) i sadrži tajne podatke.
 *
 *   cp config.example.php config.php
 */

return [
    // Adresa na koju stižu poruke iz forme
    'receiving_email_address' => 'office@geo-biz.com',

    // === Način slanja ===
    // 'mail' = serverov lokalni sendmail (BEZ SMTP autentikacije) — najlakše i najpouzdanije
    //          na shared hostingu (dwhost), jer su sajt i sanduče na istom serveru.
    // 'smtp' = slanje preko SMTP servera (zahteva tačne kredencijale ispod).
    'transport' => 'mail',

    // === SMTP podaci (koriste se SAMO ako je transport = 'smtp') ===
    'smtp_host'       => 'mail.geo-biz.com',  // ili 'localhost' ili 'host107.dwhost.net'
    'smtp_username'   => 'office@geo-biz.com', // puna email adresa naloga
    'smtp_password'   => 'PROMENI_ME',         // TAČNA lozinka mailbox-a (cPanel/webmail)
    'smtp_port'       => 587,                  // 587=TLS, 465=SSL, 25=localhost
    'smtp_encryption' => 'tls',                // 'tls' | 'ssl' | '' (bez enkripcije, npr. localhost)
    'smtp_auth'       => true,                 // false za localhost relay bez autentikacije
    'smtp_debug'      => 0,                    // 1 = upiši SMTP dijalog u PHP error_log (dijagnoza)
];
