import requests
from bs4 import BeautifulSoup
import os
import json

URL = "https://piemontevda.lnd.it/comunicati-ufficiali-piemonte-valle-daosta-2026-2027/"

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

STATE_FILE = "last.txt"


def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )


r = requests.get(URL, timeout=20)
soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all("a")

pdfs = []

for a in links:
    href = a.get("href", "")
    text = a.get_text(strip=True)

    if "comunicato" in text.lower():
        pdfs.append(text)

if not pdfs:
    exit()

latest = pdfs[0]

old = ""

if os.path.exists(STATE_FILE):
    old = open(STATE_FILE).read().strip()

if latest != old:

    if old:
        send(f"⚽ Nuovo comunicato LND:\n{latest}")

    with open(STATE_FILE, "w") as f:
        f.write(latest)
