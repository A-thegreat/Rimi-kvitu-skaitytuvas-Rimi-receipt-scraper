# Rimi Receipt Scraper & Parser | Rimi kvitų skaitytuvas ir analizatorius

## English

Automatically downloads receipts from Rimi.lt and parses them using OCR + Ollama LLM.

### Features
- Scrapes all receipts from your Rimi account
- Downloads PDF receipts automatically  
- Parses receipt data using OCR
- Fixes OCR errors using local LLM (Ollama)
- Stores data in SQLite database

### Setup
1. Copy `scraper/.env.example` to `scraper/.env` and add your Rimi credentials
2. Run `python scraper/scraper.py` to download receipts
3. Run `python parser.py` to parse them

---

## Lietuvių

Automatiniu būdu atsisiunčia kvitus iš Rimi.lt ir juos apdoroja naudojant OCR + Ollama DI.

### Funkcijos
- Automatiškai atsisiunčia visus kvitus iš Rimi paskyros
- Išsaugo PDF kvitus
- Apdoroja kvitų duomenis naudojant OCR
- Taiso OCR klaidas naudojant lokalų DI (Ollama)
- Saugo duomenis SQLite duomenų bazėje

### Nustatymai
1. Nukopijuokite `scraper/.env.example` į `scraper/.env` ir įrašykite savo Rimi prisijungimo duomenis
2. Paleiskite `python scraper/scraper.py` kad atsisiųstumėte kvitus  
3. Paleiskite `python parser.py` kad apdorotumėte kvitus

## License | Licencija
MIT
