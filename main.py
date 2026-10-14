sleva = "Beze slevy"
cena_osoba = 500
lidi = int(input("Zadejte počet lidí: "))
if lidi >= 4:
    sleva = "Skupinová sleva"
    cena_osoba = 375
else:
    vek = float(input("Zadejte věk: "))
    if vek >= 65:
        sleva = "Seniorská sleva"
        cena_osoba = 400
    else:
        while True:
            student = input("Jste student(ano/ne): ")
            if student == "ano" or student == "ne":
                break
        if student == "ano":
            sleva = "Studentská sleva"
            cena_osoba = 350
cena_celek = cena_osoba * lidi
print
print("-"*50)
print(f"Cena za jednu osobu je {cena_osoba}")
print(f"Cena za celek je {cena_celek}")
print(sleva)
print("-"*50)