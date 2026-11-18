import random
cislo=random.randint(1, 20)
pokusy=0
while True:
    pokusy+=1
    if pokusy==6:
        break
    tip=int(input(f"Uhádni číslo({pokusy} pokusy) : "))
    if tip>20 or tip<0:
        print("Mimo výseč!!")
        continue
    elif tip>cislo:
        print("Moje číslo je MENŠÍ!")
    elif tip<cislo:
        print("Moje číslo je VĚTŠÍ!")
    else:
        break
if pokusy==6:
    print(f"Využil jsi maximální počet pokusů. Číslo bylo {cislo}")
else:
    print("Správně!")
    print(f"počet pokusů: {pokusy}")