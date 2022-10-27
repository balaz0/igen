print("Add meg az a oldalt:")
a = float(input())

print("Add meg az b oldalt:")
b = float(input())

K =2*(a+b)
T = a*b

if a == b:
    print("A négyzet kerülete", K, "a négyzet területe", T, )
else:
    print("A teglalap kerülete", K, "a Teglalap területe", T, )

