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
    'smtp_host'     => 'mail.geo-biz.com',
    'smtp_username' => 'office@geo-biz.com',   // puna email adresa naloga
    'smtp_password' => 'Remorker1!Geobiz',           // TAČNA lozinka mailbox-a (cPanel/webmail)
    'smtp_port'     => 587,                     // 587 za TLS, 465 za SSL
    'smtp_encryption' => 'tls',                 // 'tls' (port 587) ili 'ssl' (port 465)
    'smtp_debug'    => 0,                        // 1 = upiši detaljan SMTP dijalog u PHP error_log (za dijagnozu)
];
