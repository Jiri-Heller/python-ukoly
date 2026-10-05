import random
while True :
    cislo = input("zadej číslo: ")
    cislo = float(cislo)
    absolut_cislo = cislo
    if cislo > 0:
        print("Kladné")
    elif cislo < 0:
        print("Záporné")
        absolut_cislo =-cislo
    else:
        print("Nula")
    print(f"Absolutní hodnota z {cislo} je: {absolut_cislo}")