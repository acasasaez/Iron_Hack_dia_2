import random
#Creamos la primera lista con 80 números enteros entre el 0 y el 100 sin repetir ningún elemento
sample_list_1=[]
while True:
    a = random.randint(0,100)
    if a not in sample_list_1:
        sample_list_1.append(a)
    if len(sample_list_1) == 80:
        break
sample_list_1.sort() 
print(sample_list_1)   

#print(sample_list_1)
print(len(sample_list_1))
#Convertimos la lista en un set
#Comprobamos que contiene el mismo número de elementos que nuestra lista
set_1 = set(sample_list_1)
print(len(set_1))

#Creamos una segunda lista con las mismas condiciones que la primera, solo que ahora los números se pueden repetir
sample_list_2=[]
for i in range (80):
    i = random.randint(0,100)
    sample_list_2.append(i)
sample_list_2.sort() 
print(sample_list_2)
print(len(sample_list_2))

#Convertimos la lista 2 en un set
set_2 = set(sample_list_2)
print(len(set_2))
#Comprobamos que contiene menos elementos que la lista 2
#En este caso, los elementos repetidos se han eliminado, por lo que len(set()) dependerá del número de elementos en la lista que se repitan
#como los eleemntos de la lista son pseudoaleatorios, el número de elementos repetidos será diferente cada vez que se ejecute el programa
lista_1 =[]
for i in set_1:
    if i not in set_2:
        lista_1.append(i)
print(lista_1)
set_3 = set(lista_1)
Lista_2 =[]
for i in set_2:
    if i not in set_1:
        Lista_2.append(i)
print(Lista_2)
set_4 = set(Lista_2)
Lista_3 =[]
for i in set_1:
    if i in set_2:
        Lista_3.append(i)
print(Lista_3)
set_5 = set(Lista_3)

#Cual es la relación entre el valor de los len(set())
#El valor de len(set_1) Es el número de elementos de sample_list_1	
#El valor de len(set_2) Es el número de elementos sin repetir de sample_list_2
#El valor de len(set_3) Es el número de elementos de set_1 intersección el complementario de set_2
#El valor de len(set_4) Es el número de elementos de set_2 intersección el complementario de set_1
#El valor de len(set_5) Es el número de elementos de set_1 intersección set_2

#Creamos un set 6 que incluya los elementos de set_3 y set_5
set_6 = set_3.union(set_5)

print(set_6)
#Comprobamos si set_6 y set_1 son iguales
if set_1 == set_6:
    print("True")

#Empleamos el metodo "issubset" para comprobar si set_3 y set_2 son subconjuntos de set_1
print(set_2.issubset(set_1))
print(set_3.issubset(set_1))
#Comprobamos si la unión de los sets 3,4,5 es igual a la unión de los sets 1 y 2
set_7 =set_6.union(set_4)
set_8=set_1.union(set_2)
if set_7 == set_8:
    print("True")

print("Set_1 antes del pop ", set_1)
set_1.pop()
print("Set_1 después del pop ", set_1)

list_to_remove = [1, 9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 69, 71, 79, 81, 89, 91, 99]
for i in list_to_remove:
    if i in set_1:
        set_1.remove(i)
print("Set_1 después del remove ", set_1)
