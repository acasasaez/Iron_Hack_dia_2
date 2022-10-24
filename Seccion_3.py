#Creamos el diccionaro indicado 
dict_1 ={"Penelope": 178, "Arnau": 172,"Marta": 175}

#Probando métodos
print("Probando el metodo keys() ", dict_1.keys())
print("Probando el metodo values() ", dict_1.values())
print("Probando el metodo items() ", dict_1.items())

#Añadimos y eliminamos un elemento del diccionario 
dict_1["Andrea"] = 156
print("Diccionario ampliado", dict_1)
del dict_1["Andrea"]
print("Diccionario reducido", dict_1)
