import math

a = int(input())
b = int(input())

muvelet = input()

eredmeny = -1
if muvelet == "+":
    eredmeny = a+b
elif muvelet == "-":
    eredmeny = a-b
elif muvelet == "*":
    eredmeny = a*b
elif muvelet == "%":
    eredmeny = a%b
elif muvelet == "**":
    eredmeny = a**b
elif muvelet == "!":
    eredmeny = math.sqrt(a)
else:
    print("Nincs ilyen művelet")
print(eredmeny)