ENG:
A simple tool that automatically downloads your receipts from Rimi.lt and extracts useful data using OCR and a local LLM (Ollama).

What it does:
Logs into your Rimi account and fetches all available receipts
  Downloads receipts as PDF files
  Reads and extracts data from receipts using OCR
  Cleans up OCR mistakes with a local AI model (Ollama)
  Saves everything neatly into an SQLite database

How to use:
  Copy scraper/.env.example → scraper/.env and enter your Rimi login details
  Run python scraper/scraper.py to download your receipts
  Run python parser.py to process and extract the data

----------------------------------------------------------------
Lietuvių

Paprastas įrankis, kuris automatiškai parsisiunčia jūsų kvitus iš Rimi.lt ir ištraukia naudingą informaciją naudodamas OCR bei lokalų DI modelį (Ollama).

Ką jis daro:
  Prisijungia prie jūsų Rimi paskyros ir surenka visus kvitus
  Automatiškai atsisiunčia kvitus PDF formatu
  Nuskaito kvitų informaciją naudodamas OCR
  Pataiso OCR klaidas pasitelkdamas lokalų DI (Ollama)
  Išsaugo visus duomenis SQLite duomenų bazėje

Kaip naudoti:
  Nukopijuokite scraper/.env.example į scraper/.env ir suveskite savo Rimi prisijungimo duomenis
  Paleiskite python scraper/scraper.py, kad atsisiųstumėte kvitus
  Paleiskite python parser.py, kad juos apdorotumėte
  
