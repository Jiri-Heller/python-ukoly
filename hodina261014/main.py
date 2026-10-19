sleva = "Beze slevy"
cena = 500
lidi = int(input("Zadejte počet lidí: "))
if lidi >= 4:
    sleva = "Skupinová sleva"
    cena = 375
else:
    vek = float(input("Zadejte věk: "))
    if vek >= 65:
        sleva = "Seniorská sleva"
        cena = 400
    else:
        while True:
            student = input("Jste student(ano/ne): ")
            if student == "ano" or student == "ne":
                break
        if student == "ano":
            sleva = "Studentská sleva"
            cena = 350
cena_celek = cena * lidi
print
print("-"*50)
print(f"Cena za jednu osobu je {cena}")
print(f"Cena za celek je {cena_celek}")
print(sleva)
print("-"*50)