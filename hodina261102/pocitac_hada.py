dole = 1
nahore = 100
pokusy = 0
odpoved = ""
spatne_napsane=""
print()
while odpoved != "s":
    tip = (dole + nahore)//2
    odpoved = input(f"je vaše číslo {tip}?{spatne_napsane} ")
    pokusy+=1
    if odpoved=="v":
        dole=tip+1
    elif odpoved=="m":
        nahore=tip
    elif odpoved=="s":
        break
    else:
        pokusy-=1
        spatne_napsane=" (v/m/s)"
        continue
print("")