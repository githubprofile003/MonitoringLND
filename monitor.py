import requests
from bs4 import BeautifulSoup

URL = "https://piemontevda.lnd.it/comunicati-ufficiali-piemonte-valle-daosta-2026-2027/"

r = requests.get(URL, timeout=20)

print("Status:", r.status_code)

soup = BeautifulSoup(r.text, "html.parser")

print("Titolo pagina:")
print(soup.title)

links = soup.find_all("a")

print("Numero link trovati:", len(links))

print("Link contenenti CU o comunicati:")

for a in links:
    testo = a.get_text(strip=True)
    href = a.get("href", "")

    if "CU" in testo.upper() or "COMUNICATO" in testo.upper():
        print(testo, href)
