import os
import sys
from config import RECEIPTS_DIR
import db
import parser


def run_all(conn, debug=False):
    pdfs = sorted(f for f in os.listdir(RECEIPTS_DIR) if f.endswith('.pdf'))
    print(f'Found {len(pdfs)} receipts')
    for idx, fname in enumerate(pdfs):
        path = os.path.join(RECEIPTS_DIR, fname)
        print(f'[{idx+1}/{len(pdfs)}] {fname}')
        try:
            items = parser.process(path, debug=debug)
            db.save(conn, items)
            print(f'  → {len(items)} items')
        except Exception as e:
            print(f'  ERROR: {e}')


def run_one(conn, path, debug=False):
    items = parser.process(path, debug=debug)
    print(f'\nFound {len(items)} items:')
    for it in items:
        print(f"  {it['name']:<55} {it['quantity']:>6} {it['unit']:<4}  {it['price']:.2f} EUR")
    db.save(conn, items)


if __name__ == '__main__':
    debug  = '--debug'  in sys.argv
    repair = '--repair' in sys.argv
    args   = [a for a in sys.argv[1:] if not a.startswith('--')]

    conn = db.connect()
    db.init(conn)

    if repair:
        import repair as r
        r.repair(conn)
    elif args:
        run_one(conn, args[0], debug=debug)
    else:
        run_all(conn, debug=debug)

    conn.close()