a= float(input("zadejte 1. číslo: "))
b = float(input("zadejte 2. číslo: "))
c = float(input("zadejte 3. číslo: "))
while a<=b and b<=c:
    if a>b:
        p = a
        a = b
        b = p
    if b>c:
        p = b
        b = c
        c = p
    if a>c:
        p = a
        a = c
        c = p
print(f"{a} {b} {c}")