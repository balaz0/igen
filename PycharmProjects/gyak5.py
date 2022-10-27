#F to C = (F-32)/1.8
#C to F = C*1.8+32
homerseklet = float(input("Add meg az alap hőfokot "))
print("Add meg a mértékegységet. C = celsius, F = fahrenheit, K = kelvin")
mertekegyseg = input()

if mertekegyseg == "C":
    F = homerseklet*1.8+32
    print("A hőmérséklet celsiusban: ", homerseklet)
    print("A hőmérséklet fahrenheit-ben: ", F)
    print("A hőmérséklet kelvinben: ", homerseklet+273.15)
elif mertekegyseg == "F":
    C = (homerseklet-32)%1.8
    print("A hőmérséklet fahrenheit-ben: ", homerseklet)
    print("A hőmérséklet celsiusban: ", C)
    print("A hőmérséklet kelvinben: ", homerseklet*1.8+32+273.15)

elif mertekegyseg == "K":
    K = homerseklet
    print("A hőmérséklet kelvinben: ", homerseklet)
    print("A hőmérséklet fahrenheit-ben: ",  1.8*(K - 273.15) + 32)
    print("A hőmérséklet celsiusban: ", homerseklet-273.15)
