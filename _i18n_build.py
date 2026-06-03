# -*- coding: utf-8 -*-
"""
GeoBiz i18n generator.
Pravi jezičke kopije (/en, /ru, /de) iz SR originala (root):
  - assets putanje: +1 nivo dublje (jer su strane u podfolderu jezika)
  - forms/contact.php: postavlja se na tačnu putanju po dubini (root /forms/)
  - ubacuje prekidač jezika u header + hreflang alternate u <head>
  - <html lang=".."> po jeziku
  - primenjuje prevode iz translations.py (najduži stringovi prvi)
Takođe ažurira SR strane (prekidač + hreflang + ispravna forms putanja).
Build alat — ne servira se kao deo sajta.
"""
import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from translations import TRANSLATIONS  # { 'en': {sr:tr,...}, 'ru':{...}, 'de':{...} }

PAGES = [
    'index.html', 'contact.html', 'inner-page.html',
    'usluge/odrzavanje-racunara.html', 'usluge/mreze.html', 'usluge/odrzavanje-servera.html',
    'usluge/data-storage.html', 'usluge/web-designe.html', 'usluge/razvoj-aplikacija.html',
    'it-konsulting/bezbednost-informacija.html', 'it-konsulting/kontinuitet-poslovanja.html',
    'it-konsulting/upravljanje-it-uslugama.html', 'it-konsulting/upravljanje-rizicima.html',
    'bezbednost/testiranje-bezbednosti.html',
    'programi/geobiz.html', 'programi/inner-page.html',
]
LANGS = ['en', 'ru', 'de']
ALL = [('sr', 'SR', ''), ('en', 'EN', 'en/'), ('ru', 'RU', 'ru/'), ('de', 'DE', 'de/')]

def switcher(prefix, cur, rel):
    items = []
    for code, label, folder in ALL:
        href = prefix + folder + rel
        active = ' active' if code == cur else ''
        items.append('<a class="lang-link%s" hreflang="%s" href="%s">%s</a>' % (active, code, href, label))
    return '<div class="lang-switch">' + ''.join(items) + '</div>\n      '

def hreflangs(prefix, rel):
    out = []
    for code, label, folder in ALL:
        out.append('  <link rel="alternate" hreflang="%s" href="%s%s%s">' % (code, prefix, folder, rel))
    return '\n'.join(out) + '\n'

def clean(s):
    # ukloni postojeći prekidač i hreflang (idempotentnost pri ponovnom pokretanju)
    s = re.sub(r'<div class="lang-switch">.*?</div>\s*', '', s, flags=re.S)
    s = re.sub(r'[ \t]*<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n?', '', s)
    return s

def add_asset_level(s):
    # prepend one ../ to every assets/ reference (src/href)
    return re.sub(r'(src|href)="((?:\.\./)*)assets/', r'\1="\2../assets/', s)

_WORD = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789čćžšđČĆŽŠĐ"

def apply_translations(s, table):
    # najduži ključevi prvi; fleksibilan razmak (hvata višelinijski tekst); granice reči
    for sr, tr in sorted(table.items(), key=lambda kv: -len(kv[0])):
        if not sr:
            continue
        parts = sr.split()
        if not parts:
            continue
        pat = r'\s+'.join(re.escape(p) for p in parts)
        if sr[0] in _WORD:
            pat = r'(?<![' + _WORD + r'])' + pat
        if sr[-1] in _WORD:
            pat = pat + r'(?![' + _WORD + r'])'
        s = re.sub(pat, lambda m, t=tr: t, s)
    return s

def transform(src, lang, rel):
    depth = rel.count('/') + 1          # dubina jezičke strane od root-a
    prefix = '../' * depth
    s = clean(src)
    # assets +1 nivo
    s = add_asset_level(s)
    # forms putanja tačno po dubini
    s = re.sub(r'action="[^"]*forms/contact\.php"', 'action="%sforms/contact.php"' % prefix, s)
    # lang atribut
    s = re.sub(r'<html lang="[^"]*">', '<html lang="%s">' % lang, s)
    # hreflang u head
    s = s.replace('</head>', hreflangs(prefix, rel) + '</head>', 1)
    # prekidač jezika pre Podrška dugmeta
    s = s.replace('<a class="btn-getstarted', switcher(prefix, lang, rel) + '<a class="btn-getstarted', 1)
    # prevodi
    s = apply_translations(s, TRANSLATIONS.get(lang, {}))
    return s

def update_sr(src, rel):
    depth = rel.count('/')
    prefix = '../' * depth
    s = clean(src)
    s = re.sub(r'action="[^"]*forms/contact\.php"', 'action="%sforms/contact.php"' % prefix, s)
    s = s.replace('</head>', hreflangs(prefix, rel) + '</head>', 1)
    s = s.replace('<a class="btn-getstarted', switcher(prefix, 'sr', rel) + '<a class="btn-getstarted', 1)
    return s

def main():
    # jezičke kopije
    for lang in LANGS:
        for rel in PAGES:
            src = open(rel, encoding='utf-8').read()
            out = transform(src, lang, rel)
            dst = os.path.join(lang, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            open(dst, 'w', encoding='utf-8').write(out)
    # SR strane (prekidač + hreflang + forms)
    for rel in PAGES:
        src = open(rel, encoding='utf-8').read()
        open(rel, 'w', encoding='utf-8').write(update_sr(src, rel))
    print('Generisano:', len(LANGS), 'jezika x', len(PAGES), 'strana =', len(LANGS) * len(PAGES), '+ SR azurirano')

if __name__ == '__main__':
    main()
