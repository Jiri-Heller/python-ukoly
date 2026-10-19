cislo1 = float(input("zadejte 1. číslo: "))
cislo2 = float(input("zadejte 2. číslo: "))
cislo3 = float(input("zadejte 3. číslo: "))
if cislo1 >= cislo2 and cislo1 >= cislo3:
    max = cislo1
    if cislo2 <= cislo3:
        min = cislo2
        mid = cislo3
    else:
        min = cislo3
        mid = cislo2
elif cislo2 >= cislo1 and cislo2 >= cislo3:
    max = cislo2
    if cislo1 <= cislo3:
        min = cislo1
        mid = cislo3
    else:
        min = cislo3
        mid = cislo1
else:
    max = cislo3
    if cislo1 <= cislo2:
        min = cislo1
        mid = cislo2
    else:
        min = cislo2
        mid = cislo1
print(min)
print(mid)
print(max)