obj1_width = 5
obj1_height = 5
obj1_x = 4
obj1_x2 = obj1_x + obj1_width
obj1_y = 2
obj1_y2 = obj1_y + obj1_height
xb = float(input("Souřadnice x: "))
yb = float(input("Souřadnice y: "))
if (xb > obj1_x and xb< obj1_x2) and (yb > obj1_y and yb < obj1_y2):
    msg = "bod se nachází v poli"
elif xb == obj1_x or xb == obj1_x2:
    if yb >= obj1_y and yb <= obj1_y2:
        msg = "bod se nachází na hraně pole"
elif yb == obj1_y or yb == obj1_y2:
    if xb >= obj1_x and xb <= obj1_x2:
        msg = "bod se nachází na hraně pole"
else:
    msg = "bod se nachazi mimo pole"
print(msg)