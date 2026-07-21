import requests
from bs4 import BeautifulSoup

URL = "https://piemontevda.lnd.it/comunicati-ufficiali-piemonte-valle-daosta-2025-2026/"

r = requests.get(URL, timeout=20)

print("Status:", r.status_code)

soup = BeautifulSoup(r.text, "html.parser")

print("Titolo pagina:")
print(soup.title)

links = soup.find_all("a")

print("Numero link trovati:", len(links))

print("Primi 10 link:")

for a in links[:10]:
    print(a.get_text(strip=True), a.get("href"))

    with open(STATE_FILE, "w") as f:
        f.write(latest)
