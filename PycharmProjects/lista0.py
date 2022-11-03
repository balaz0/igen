a = 56 
lista = [1,2,3,4,5,6,7]
lista[2] = 35
print(lista[2])

for i,j in enumerate(lista):
    lista[i] = lista[i]+a
    print(i, lista[i])

