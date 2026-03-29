# repair.py
import json
import requests
from config import OLLAMA_URL, OLLAMA_MODEL, OLLAMA_TIMEOUT
from products import KNOWN_PRODUCTS

BATCH = 10  # smaller batches

def repair(conn):
    from db import known_names, all_names

    db_known  = set(known_names(conn, min_count=2))
    all_known = list(dict.fromkeys(KNOWN_PRODUCTS + list(db_known)))

    all_in_db = all_names(conn)
    garbled   = [n for n in all_in_db if n not in set(all_known)]

    if not garbled:
        print('Nothing to repair')
        return

    print(f'Repairing {len(garbled)} names against {len(all_known)} known products...')
    corrections = {}

    for i in range(0, len(garbled), BATCH):
        batch = garbled[i:i + BATCH]
        print(f'  batch {i//BATCH + 1}/{(len(garbled)-1)//BATCH + 1} ({len(batch)} names)...')
        corrections.update(_ask_llm(all_known, batch))

    applied = 0
    for old, new in corrections.items():
        if old != new and new.strip():
            print(f'  {old!r}\n    → {new!r}')
            conn.execute(
                'UPDATE inventory SET pavadinimas = ? WHERE pavadinimas = ?',
                (new, old)
            )
            applied += 1

    conn.commit()
    print(f'Applied {applied} corrections')


def _find_candidates(known, garbled_batch):
    """Only send known names that share at least one word with the garbled names."""
    # collect all words from garbled batch
    garbled_words = set()
    for name in garbled_batch:
        for w in name.lower().split():
            if len(w) > 3:
                garbled_words.add(w)

    candidates = []
    for name in known:
        for w in name.lower().split():
            if len(w) > 3 and w in garbled_words:
                candidates.append(name)
                break

    # always include at least some known names as anchors
    if len(candidates) < 10:
        candidates = known[:20]

    return candidates


def _ask_llm(known, garbled):
    # only send relevant subset of known names
    candidates = _find_candidates(known, garbled)

    prompt = f"""Fix garbled OCR product names from Lithuanian grocery receipts.

Known correct names:
{json.dumps(candidates, ensure_ascii=False)}

Garbled names to fix:
{json.dumps(garbled, ensure_ascii=False)}

Rules:
- Match to a known name if clearly the same product
- Otherwise clean obvious OCR noise only (RIHI→RIMI, =z→s, etc.)
- Never invent names
- Return ONLY a JSON object mapping each garbled name to its correction
- Every input name must appear as a key"""

    try:
        r = requests.post(OLLAMA_URL, json={
            'model':  OLLAMA_MODEL,
            'prompt': prompt,
            'stream': False,
            'format': 'json',
        }, timeout=OLLAMA_TIMEOUT)
        return json.loads(r.json()['response'])
    except Exception as e:
        print(f'  LLM error: {e}')
        return {}