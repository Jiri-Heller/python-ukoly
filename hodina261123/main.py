def ctverec(strana):
    radek=0
    while radek < strana:
        print("*" * strana)
        radek+=1
def ctverec_duty(strana):
    radek=0
    while radek < strana:
        if radek == 0 or radek==(strana-1):
            print("*"*strana)
        else:
            print("*"+" "*(strana-2) +"*")
        radek+=1
def trojuhelnik(strana):
    radek=0
    while radek < strana:
        print ("*"*(radek+1))
        radek+=1
while True:
    obrazec = input("zadej obrazec ")
    if obrazec == "c":
        velikost= int(input("zadej velikost "))
        ctverec(velikost)
    elif obrazec == "cd":
        velikost= int(input("zadej velikost "))
        ctverec_duty(velikost)
    elif obrazec == "t":
        velikost= int(input("zadej velikost "))
        trojuhelnik(velikost)
    odpoved = input("Chceš další? (ano) ")
    if odpoved != "ano":
        break
print("konec")