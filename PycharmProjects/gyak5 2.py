homerseklet = float(input("Add meg az alap hőfokot "))
mertekegyseg = input("Add meg a mértékegységet. C = celsius, F = fahrenheit, K = kelvin")
mibe = input("Mibe szeretné átváltani? C = celsius, F = fahrenheit, K = kelvin ")

if mertekegyseg == "C" and mibe == "F":
    print ((homerseklet-32)%1.8)
elif mertekegyseg == "C" and mibe == "K":
    print(homerseklet*1.8+32+273.15)
if mertekegyseg == "F" and mibe == "K":
    print(homerseklet+273.15)
elif mertekegyseg == "F" and mibe == "C":
    print(homerseklet*1.8+32)
if mertekegyseg == "K" and mibe == "C":
    print(homerseklet-273.15)
elif mertekegyseg == "K" and mibe == "F":
    print(1.8*(homerseklet - 273.15) + 32)

