# kalkulačka spropitného
# 30. 9. 2026
print("KAOLKULAČKA SPROPITNÉHO")

celkova_cena = input("Zadej celkovou cenu: ")
celkova_cena = float(celkova_cena)
pocet_lidi = int(input("Zadej počet lidí: "))
spropitne = int(input("Zadej velikost spropitné: "))
celkova_cena += celkova_cena * (spropitne/100)
clovek_cena = round(celkova_cena/pocet_lidi+0.5) #+0.5 - zaokrouhlit nahoru
print (f"Celková cena: {celkova_cena} dělená {pocet_lidi} je po zaokrouhlení {clovek_cena}")
