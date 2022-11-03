#print("Addj megy egy számot")
#a = int(input())
#print("Addj megy egy számot")
#b = int(input())
#print("Addj megy egy számot")
#c = int(input())
#print("Addj megy egy számot")
#d = int(input())
#print("Addj megy egy számot")
#e = int(input())
#lista = [a,b,c,d,e,]
#print(lista)
#atlag = (a+b+c+d+e)/5
#print("A lista átlaga: " ,atlag,)


#lista = [1,2,3,4,5,6,7]
#lista[0] = 100
#print(lista[0])
#
#for i,j in enumerate(lista):
#    print(i,j)
#    lista[i] = lista[i]+100
#    print(i,lista[i])
#    print(lista.sort)

lista=[]
osszeg = 0
maximum  = -1
for i in range(5):
    a = int(input())
    lista.append(a)
    osszeg = osszeg+a
    if maximum < a:
        maximum = a
print(lista)
print(osszeg/len(lista))
print(maximum,lista.index(maximum))
for i,j in enumerate(lista):
    m = lista[i] = lista[i] + maximum/len(lista)
    print(m)
