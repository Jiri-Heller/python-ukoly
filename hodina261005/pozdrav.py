
cas=float(input("zadej čas: "))
if cas>24 or cas<0:
    print("čas mimo výseč")
elif cas<5:
    print("dobrou noc")
elif cas<10:
    print("dobré ráno")
elif cas<12:
    print("dobré dopoledne")
elif cas==12:
    print("dobré poledne")
elif cas<17:
    print("dobré odpoledne")
elif cas<20:
    print("dobrý večer")
else:
    print("dobrou noc")