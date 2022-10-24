#Tupla de un solo elemento:
tup=("I",)
print(type(("I",)))
#Una tupla es un elemento inmutabl, no la podemos modificar una vez creada
tup=("I","r","o","n","h","a","c","k") #si queremos que tup (la tupla) contenga nuevos elementos debemos modificar el valor de tup asignándole una nueva tupla
#Crea las tuplas 1 y 2 con los valores ("I","r","o","n")(), respectivamente
tup_1 = tup[0:4]
print(tup_1)
tup_2=tup[4:]
print(tup_2)
#Crea la tupla 3 con los valores de tup_1 y tup_2
tup_3=tup_1+tup_2
print(tup_3)
#Cuenta el número de elementos de las tuplas 1 y dos y 
#comprueba que la suma es igual al número de elementos de la
#tupla 3
print("Numero de elementos en tup1: ", len(tup_1))
print ("Numero de elementos en tup2: ", len(tup_2))
print ("La suma del número de elementos en tup1, tup2", len(tup_1)+len(tup_2))
print("Numero de elementos en tup2:", len(tup_3))
if len(tup_1)+ len(tup_2) == len(tup_3):
    print("La suma del número de elementos en tup1, tup2 es igual al número de elementos de la tupla 3")
else:
    pass

#busca la posición de la letra "h" en la tupla 3
print("La posición de la letra h en la tupla 3 es: ", tup_3.index("h"))

#Busca los elementos de la siguiente lista en la tupla 3
letters = ["a", "b", "c", "d", "e"]
for i in letters:
    if i in tup_3:
        print(i, "esta en la tupla 3")