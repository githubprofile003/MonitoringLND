import requests
from bs4 import BeautifulSoup
import os

URL = "https://piemontevda.lnd.it/comunicati-ufficiali-piemonte-valle-daosta-2026-2027/"

STATE_FILE = "last.txt"

r = requests.get(URL, timeout=20)

soup = BeautifulSoup(r.text, "html.parser")

latest = None

for a in soup.find_all("a"):
    testo = a.get_text(strip=True)

    if testo.lower().startswith("cu_"):
        latest = testo
        break

if latest is None:
    print("Nessun comunicato trovato")
    exit()

print("Ultimo comunicato trovato:")
print(latest)

old = ""

if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        old = f.read().strip()

if old == "":
    print("Prima esecuzione, salvo il comunicato")
    
elif latest != old:
    print("NUOVO COMUNICATO TROVATO!")
    print(latest)

else:
    print("Nessun nuovo comunicato")

with open(STATE_FILE, "w") as f:
    f.write(latest)
