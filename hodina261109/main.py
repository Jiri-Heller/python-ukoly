import math
cislo=int(input("sixseven"))
zprava=True
delitel=3
if cislo<2:
    zprava=False
while delitel<=math.sqrt(cislo):
    if cislo % delitel==0:
        zprava=False
        break
    delitel+=2
