# kalkulačka spropitného
# 30. 9. 2026
print("KAOLKULAČKA SPROPITNÉHO")
celkova_cena=0.0
celkova_cena = float(input("Zadej celkovou cenu: "))
pocet_lidi = int(input("Zadej počet lidí: "))
spropitne = int(input("Zadej velikost spropitné: "))
celkova_cena += celkova_cena * (spropitne/100)
clovek_cena = celkova_cena/pocet_lidi
if (celkova_cena/pocet_lidi) % 1 > 0:
    clovek_cena = round(clovek_cena+0.5) #+0.5 - zaokrouhlit nahoru
print (f"Celková cena: {celkova_cena} dělená {pocet_lidi} je po zaokrouhlení {clovek_cena}")
