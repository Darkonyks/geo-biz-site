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

    // SMTP server podaci
    'smtp_host'     => 'smtp.example.com',
    'smtp_username' => 'office@geo-biz.com',
    'smtp_password' => 'PROMENI_ME',
    'smtp_port'     => 587,
];
