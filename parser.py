import re


# ── Normalize ─────────────────────────────────────────────────────────────────

def normalize(text):
    multiline = [
        (
            r'Užstatas\s*-\s*vienkartinė\s*\n+\s*plastiko pakuot[ėe]',
            'Užstatas - vienkartinė plastiko pakuotė'
        ),
    ]
    for p, r in multiline:
        text = re.sub(p, r, text, flags=re.DOTALL)

    fixes = [
        (r'EROR"?\s*',                                      ''),
        (r'\bESP\b',                                        ''),
        (r'^[""\u201c\u201e]\s*(Elektroninis kvitas\s*)?$', ''),
        (r'^Ic?tas kainos.*$',                              ''),
        (r'^Ie\s+laci.*$',                                  ''),
        (r'^TTT\s+Informacija.*$',                          ''),
        (r'^TR\s+Informacija.*$',                           ''),
        (r'\bzpUurga\b',                                    'spurga'),
        (r'\bBŪMBER\b',                                     'BOMBER'),
        (r'\bVICLI\b',                                      'VICI'),
        (r'\bAG0[ŪU]RII\b',                                'ASORTI'),
        (r'\bAG00RII\b',                                    'ASORTI'),
        (r'\bžokolado\b',                                   'šokolado'),
        (r'\bžakoladu\b',                                   'šokoladu'),
        (r'\bEZTRELLA\b',                                   'ESTRELLA'),
        (r'\bEZTEREELLA\b',                                 'ESTRELLA'),
        (r'\bEiaulienos\b',                                 'Kiaulienos'),
        (r'\bLriet\b',                                      'Griet.'),
        (r'\bBandslė\b',                                    'Bandelė'),
        (r'\bsaldžiozios\b',                                'saldžiosios'),
        (r'\bEūris\b',                                      'Sūris'),
        (r'\bEIMHMI\b',                                     'RIMI'),
        (r'\bZBMART\b',                                     'SMART'),
        (r'\bSHART\b',                                      'SMART'),
        (r'\bTILEIT\b',                                     'TILSIT'),
        (r'\bVaflini=z\b',                                  'Vaflinis'),
        (r'\bEINDER\b',                                     'KINDER'),
        (r'\bBUEN[ŪU]\b',                                   'BUENO'),
        (r'\bAtžaldyta\b',                                  'Atšaldyta'),
        (r'\bRIHI\b',                                       'RIMI'),
        (r'\bGaivuzis\b',                                   'Gaivusis'),
        (r'\bGumuštinis\b',                                 'Sumuštinis'),
        (r'\bGumužtinis\b',                                 'Sumuštinis'),
        (r'(?<=\s)=u\b',                                    'su'),
        (r'\b=u\b',                                         'su'),
        (r'\b(\d+)\s*\*\s+',                                r'\1 % '),
        (r'\blkg\b',                                        '1kg'),
        (r'%\s+,',                                          '%,'),
        (r'[ūŪ]ml\b',                                       'ml'),
        (r'(\d),\s+(\d)',                                    r'\1,\2'),
        (r'(?<![A-Za-zĄČĘĖĮŠŲŪŽąčęėįšųūž])O,(\d)',        r'0,\1'),
        (r'\bČ[O0],(\d)[GA]\b',                             r'0,\g<1>9'),
        (r'\bČ[O0],(\d\d)\b',                               r'0,\1'),
        (r'\bEUBR\b',                                       'EUR'),
        (r'\bEU[ERIOU8]\b',                                 'EUR'),
        (r'\bEUE\b',                                        'EUR'),
        (r'\bEUR/k[gq]\b',                                  'EUR/kg'),
        (r'0,l[ūŪ][ŪūUu]',                                 '0,10'),
        (r'0,l[ūŪ]',                                        '0,10'),
        (r'[ūŪ],(\d{3})',                                    r'0,\1'),
        (r'[ūŪ],(\d{2})',                                    r'0,\1'),
        (r'[ūŪ],(\d)([ūŪ])',                                r'0,\g<1>0'),
        (r'[ūŪ][„,](\d)',                                    r'0,\1'),
        (r'(\d),\*[ŽžZz]l\b',                               r'\1,21'),
        (r'(\d),\*[ŽžZz](\d)\b',                            r'\1,\g<2>'),
        (r'(\d)[ūŪ](\d)',                                    r'\g<1>0\2'),
        (r'(?<=[\d,])[ūŪ](?=[\d,])',                        '0'),
        (r'(\d,\d)[ūŪ]\b',                                  r'\g<1>0'),
        (r'(?<!\w)[ūŪ],(\d+)',                               r'0,\1'),
        (r'(?<=\d)l(?=\d)',                                  '1'),
        (r'(?<=,)l(?=\d)',                                   '1'),
        (r'(?<=\d)I(?=\d)',                                  '1'),
        (r'(?<=,)I(?=\d)',                                   '1'),
        (r'(?<=\d)O(?=\d)',                                  '0'),
        (r'(?<=,)O(?=\d)',                                   '0'),
        (r'(?<=\d)[„\u201e](?=\d)',                         ','),
        (r'\b[Vv][na][mt]s?\.?\b',                         'vnt.'),
        (r'\bvnl\.?\b',                                     'vnt.'),
        (r'\bk[gq]\b',                                      'kg'),
        (r'\bkG\b',                                         'kg'),
        (r'vnt\.\.+',                                       'vnt.'),
        (r'\bvnt\.\s+[ZzX×]\s+(\d)',                        r'vnt. X \1'),
        (r'\bvnt\s+[ZzX×]\s+(\d)',                          r'vnt X \1'),
        (r'\bkg\s+[ZzX×]\s+(\d)',                           r'kg X \1'),
        (r'\ba\s+(vnt\.?)',                                  r'2 \1'),
        (r'\bo\s+(vnt\.?)',                                  r'0 \1'),
        (r'\b[NH]M?uol\.?',                                 'Nuol.'),
        (r'\bHuol\.?',                                      'Nuol.'),
        (r'\brAalut\.?',                                    'Galut.'),
        (r'\bralut\.?',                                     'Galut.'),
        (r'\b[Rr]Aalut\.?',                                 'Galut.'),
        (r'Nuol\.aida',                                     'Nuolaida'),
        (r'\bRIHI\b',                                       'RIMI'),
        (r'\bzu\b',                                         'su'),
        (r'\bZu\b',                                         'Su'),
    ]

    for pattern, replacement in fixes:
        text = re.sub(pattern, replacement, text, flags=re.MULTILINE)

    return text


# ── Patterns ──────────────────────────────────────────────────────────────────

_PRICE = re.compile(r'^(.+?)\s+(\d+[.,]\d{2})\s*(?:[AB]\s*)?$')
_QTY   = re.compile(
    r'^(\d+[.,]?\d*)\s*(vnt\.?|kg)\s+[XxZz×]\s+(\d+[.,]\d+)\s+EUR(?:/kg)?',
    re.IGNORECASE
)
_SKIP  = re.compile(
    r'^('
    r'Nuol\.|NMuol\.|Huol\.|HMuol\.|Galut\.'
    r'|SUTEIKTOS|GUTELETOS|GUTEIKTOS|ZUTELETOS'
    r'|MOKĖJIMAS|MOKEJIMAS|MOK\u0116JIMAS'
    r'|BEKONTAKTIS|BEKCNTAKTIS|ATSISKAITYMAS|PARDAVIMAS|PARDAVIHAS'
    r'|BANKO|BANĖECO|BANEO|TERMINALO|TEREKH|LAIKAS|LAIEAS'
    r'|MASTER|HMA5TER|HMAZTER|Debit|Lebit|DEBIT'
    r'|PIRKINYS|PLRELNTYS|PLRELNTS|ELEELHNYS|AUTORIZACIJOS|AUTORLŽ'
    r'|SAUGOKITE|GAUŽO|GAUGŪ|IZREA5UI|LI5RA5|I\u0160RA\u0160UI'
    r'|RRN\b|RRHN\b|RER\s|RR\s'
    r'|Uždirbti|MANO\s|Nuolaida|Su\s+kortele'
    r'|Mok\u0117ti|Hokėti|Mokestis|Hokestis|Banko kortele'
    r'|Kvito|Saugos|KEvito|A\.P\.'
    r'|CR-|http|A\u010CI\u016a|Nemokamas'
    r'|sutaup\u0117te\s+\d'
    r'|Evito\s+Nr\.'
    r'|Užstatas'
    r'|Kitos\s+akcijos'
    r')',
    re.IGNORECASE
)
_HEADER = re.compile(
    r'^('
    r'UAB|PVM|PIRK\u0116JAS|PIRKĖJAS'
    r'|Verta rinktis|Rimi\b'
    r'|[-=*─]{3,}'
    r'|Elektroninis'
    r'|[žŽ]irm'
    r')',
    re.IGNORECASE
)
_STOP = re.compile(
    r'^('
    r'SUTEIKTOS|GUTELETOS|GUTEIKTOS|ZUTELETOS'
    r'|MOKĖJIMAS|MOKEJIMAS|MOK\u0116JIMAS'
    r'|J\u016bs\s+sutaup\u0117te|J\u016aS\s+SUTAUP\u0116TE|J\u016bs sutaupėte'
    r'|J\u016bs\s+zutaup\u0117te|J\u016bs zutaupėte'
    r')',
    re.IGNORECASE
)


def _structural(line):
    return bool(
        _PRICE.match(line) or _QTY.match(line) or
        _SKIP.search(line) or _HEADER.search(line) or _STOP.search(line)
    )

def _clean(name):
    name = re.sub(r'\s*\d+\s*vnt\.?\s+X\s+[\d.,]+\s+EUR\S*', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\.\.+', '', name)
    name = re.sub(r'[ūŪ]ml\b', 'ml', name)
    name = re.sub(r'(\d)[ūŪ](\d)', r'\g<1>0\2', name)
    name = re.sub(r'(\d)[ūŪ]\b', r'\1', name)
    name = re.sub(r'^[^A-Za-zĄČĘĖĮŠŲŪŽąčęėįšųūž0-9]+', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip()

def _collect_name(lines, idx, used):
    parts = []
    for j in range(idx - 1, max(idx - 4, -1), -1):
        if j in used:
            break
        l = lines[j].strip()
        if not l or _structural(l):
            break
        parts.insert(0, l)
        used.add(j)
    return ' '.join(parts).strip()

def _prev_content(lines, idx, used):
    for j in range(idx - 1, -1, -1):
        if j in used:
            continue
        l = lines[j].strip()
        if l and not _structural(l):
            return l, j
    return '', -1


# ── Parse ─────────────────────────────────────────────────────────────────────
def _is_valid_item(item):
    name = item['name']
    # too short
    if len(name) < 5:
        return False
    # price too low to be a real item (deposits, rounding)
    if item['price'] < 0.10:
        return False
    # contains header junk
    if re.search(r'ERrIS=|Elektroninis|PVH\s+mok|mokėtojo', name, re.IGNORECASE):
        return False
    # contains nuolaida/galut lines
    if re.search(r'Nuol\.|Galut\.|Muol\.|Muiol\.', name, re.IGNORECASE):
        return False
    # two items merged — contains a price pattern mid-name
    if re.search(r'\d+[.,]\d{2}\s+[AB]\s+\w', name):
        return False
    # name is mostly digits/symbols
    alpha = sum(c.isalpha() for c in name)
    if alpha < len(name) * 0.3:
        return False
    return True
    
def parse(text):
    text = normalize(text)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    items = []
    used  = set()

    i = 0
    while i < len(lines):
        if i in used:
            i += 1
            continue
        line = lines[i]

        if _STOP.search(line):
            break
        if _SKIP.search(line) or _HEADER.search(line):
            i += 1
            continue

        qm = _QTY.match(line)
        if qm:
            qty  = float(qm.group(1).replace(',', '.'))
            unit = qm.group(2).rstrip('.').lower()
            price = None
            pm = _PRICE.match(line)
            if pm:
                price = float(pm.group(2).replace(',', '.'))
            elif i + 1 < len(lines) and not _STOP.search(lines[i + 1]):
                pm2 = _PRICE.match(lines[i + 1])
                if pm2:
                    price = float(pm2.group(2).replace(',', '.'))
                    used.add(i + 1)
            if price is not None:
                name = _clean(_collect_name(lines, i, used))
                if name:
                    item = {'name': name, 'quantity': qty, 'unit': unit, 'price': price}
                    if _is_valid_item(item):
                        items.append(item)
            i += 1
            continue

        pm = _PRICE.match(line)
        if pm:
            name_part = pm.group(1).strip()
            price     = float(pm.group(2).replace(',', '.'))
            if _QTY.match(name_part):
                qm2  = _QTY.match(name_part)
                qty  = float(qm2.group(1).replace(',', '.'))
                unit = qm2.group(2).rstrip('.').lower()
                name = _clean(_collect_name(lines, i, used))
            else:
                qty  = 1.0
                unit = 'vnt'
                prev, prev_idx = _prev_content(lines, i, used)
                if prev and not _structural(prev):
                    name = _clean((prev + ' ' + name_part).strip())
                    used.add(prev_idx)
                else:
                    name = _clean(name_part)
            if len(name) >= 3:
                item = {'name': name, 'quantity': qty, 'unit': unit, 'price': price}
                if _is_valid_item(item):
                    items.append(item)                    
            i += 1
            continue

        i += 1

    return items


# ── OCR ───────────────────────────────────────────────────────────────────────

def ocr(pdf_path):
    from pdf2image import convert_from_path
    from PIL import ImageFilter, ImageOps
    import pytesseract
    images = convert_from_path(pdf_path, dpi=400)
    text = ''
    for img in images:
        img = img.convert('L')
        img = ImageOps.autocontrast(img, cutoff=2)
        img = img.filter(ImageFilter.SHARPEN)
        text += pytesseract.image_to_string(img, lang='lit') + '\n'
    return text

def process(pdf_path, debug=False):
    raw = ocr(pdf_path)
    if debug:
        print('── RAW OCR ──\n', raw)
        print('── NORMALIZED ──\n', normalize(raw))
        print('── PARSED ──')
    return parse(raw)