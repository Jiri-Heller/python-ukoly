import urllib.request
URL = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

odpoved = urllib.request.urlopen(URL)     # odkaz na objekt odpovědi serveru
pocet_dnu = 0
celkem_srazky = 0
radek = odpoved.readline()

while bool(radek):
    text = radek.decode("utf-8").strip()
    srazka = float(text)
    if srazka >= 0:
        celkem_srazky+= srazka


odpoved.close()
print()