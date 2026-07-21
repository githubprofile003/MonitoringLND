import requests
from bs4 import BeautifulSoup
import os

URL = "https://piemontevda.lnd.it/comunicati-ufficiali-piemonte-valle-daosta-2026-2027/"

STATE_FILE = "last.txt"

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        },
        timeout=20
    )


# Scarica la pagina LND
r = requests.get(URL, timeout=20)

soup = BeautifulSoup(r.text, "html.parser")


# Cerca l'ultimo comunicato
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


# Legge l'ultimo comunicato salvato
old = ""

if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        old = f.read().strip()

old = "TEST_FORZATO"

# Prima esecuzione
if old == "":
    print("Prima esecuzione, salvo il comunicato")


# Nuovo comunicato trovato
#elif latest != old:
#    print("NUOVO COMUNICATO TROVATO!")
#    print(latest)

#    send_telegram(
#        f"⚽ Nuovo comunicato LND Piemonte:\n\n{latest}\n\n{URL}"
#    )

elif latest != old:
    print("NUOVO COMUNICATO TROVATO!")
    print(latest)

    send_telegram(
        f"🧪 TEST NOTIFICA LND Piemonte\n\nIl sistema funziona correttamente.\nUltimo comunicato rilevato:\n{latest}"
    )

# Nessuna novità
else:
    print("Nessun nuovo comunicato")


# Salva lo stato attuale
with open(STATE_FILE, "w") as f:
    f.write(latest)

with open(STATE_FILE, "w") as f:
    f.write(latest)
