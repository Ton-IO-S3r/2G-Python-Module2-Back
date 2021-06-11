x = {1, 3, 4}

x[0]

for valor in x:
    print(valor)

for valor in x:
    valor = 100

set(["A", 6, 1, 5, "B", "F", "C"])

set([1,2,4])


frozenset([1, 2, 3])

y = x


y.add(12)

y

x

y = x.copy()
y.add(20)
x

print(x, y)



z = { 100, 1000, 7, 1}


x | y

x.union(y)


x & y

x.intersection(y).intersection(z)

x.difference(y)



x - y - y

y - x


x ^ y
(x-y)|(y-x)

x

x_sub = {3, 4}

print(x, x_sub)

{1, 3, 4, 12} {3, 4}

x_sub.issubset(x)

x.issubset(x)   

x < x

x.issuperset(x_sub)

x >= x_sub


print(x, y)

x.isdisjoint(y)

x.isdisjoint({100, 1000})

x.issubset(y)

x

list(x)

x.pop()

x

x.clear()

x

y.add(13)

y

y.update([100, 1000, "texto"])
y

y.remove(100)
y

y.discard(8)
y


### Diccionarios
### ejemplo con horas de sueño
l_nombres2 = []
l_horas = []
ejemplo1 = {
   'Arturo':{
       'Horas de suenio': 4,
       'Minutos al trabajo': 20 
   }
}
suma = lambda x, y: x + y
suma(12, 11)

horas_suenio_dict = {
    "Arturo": {"suenio": 6},
    'Carlos': 8,
    'Tonio': [8, 6, 5],
    'Ivan': {
        "75%":8,
        "25%": 6
    },
    "Yair": {
        .75: 8, 
        .25: 7
    },
    "funcion": suma
}
horas_suenio_dict["funcion"](12, 3)

 
for llave, valor in horas_suenio_dict.items():
    print(llave, valor)
    # print(f"{llave}  {str(valor)}")


# Lo anterior es equivalente a las dos líneas anteriores
for nombre_alumno, horas_suenio in horas_suenio_dict.items():
   print(f'{nombre_alumno} duerme {horas_suenio}')
 
list(horas_suenio_dict.keys()) #Si se necesita tener las llaves como listas
 
for llave in horas_suenio_dict.keys():
   print('{llave} duerme {horas_suenio_dict}'.format(llave = llave, horas_suenio_dict = horas_suenio_dict[llave]))
 
suma_horas = 0
for valor in horas_suenio_dict.values():
    print(valor)
    if isinstance(valor, float) or isinstance(valor, int):
        print("Estoy sumando")
        suma_horas += valor

suma_horas = 0
for valor in horas_suenio_dict.values():
    print(valor)
    if str(type(valor)) == "<type 'float'>" or str(type(valor)) == "<type 'int'>":
        print("Estoy sumando")
        suma_horas += valor
 
horas_suenio_dict = {
    "Arturo": 5,
    'Carlos': 8,
    'Tonio': 7,
    'Ivan': 6, 
    "Yair": 4,
    "funcion": suma
}

suma_horas = 0
n = 0
for valor in horas_suenio_dict.values():
    print(valor)
    if str(type(valor)) == "<type 'float'>" or str(type(valor)) == "<type 'int'>":
        print("Estoy sumando")
        suma_horas += valor
        n += 1

print("El promedio de horas de sueño de los alumnos es: "+str( suma_horas / n))
 
 
## .clear deja vacío el diccionario
 
## .copy Crea una copia nueva
##.fromkeys
horas_suenio_dict_2 = dict.fromkeys(["Rosy", "Osmar"], 6)
print(horas_suenio_dict_2)

horas_suenio_dict["Arturo"]
# horas_suenio_dict["Osmar"] Error KeyError:  'Osmar'

 
##horas_suenio_dict_2["Ale Paez"] Error KeyError: 'Ale Paez'
 
## Consultas
# .get
horas_suenio_dict.get("Arturo")

horas_suenio_dict_2
# .pop
horas_suenio_dict_2.pop("Osmar")
8
print(horas_suenio_dict_2)
 
 
#.setdefault
#Agregar un elemento
horas_suenio_dict_2.setdefault("Arturo",7) #Agrega Arturo con 7 horas de sueño
#Parecido al get
horas_suenio_dict_2.setdefault("Arturo")
horas_suenio_dict_2
horas_suenio_dict_2.setdefault("Ferdinand") # al igual que el get no marca error y no devuelve nada
horas_suenio_dict_2["Ferdinand"] = 6

#.update RECIBE UN DICCIONARIO
horas_suenio_dict_2.update({"Tonio": horas_suenio_dict["Tonio"]})
print(horas_suenio_dict_2)
horas_suenio_dict_2["Ivan"] = 10
horas_suenio_dict_2["Ivan"] = 5 
horas_suenio_dict_2.update({"Ivan":6})
horas_suenio_dict_2

horas_suenio_dict_2.get("Alexa", "No se encontró el nombre")
 
# Validar que la llave existe
if "Alexa" in horas_suenio_dict_2.keys():
   print("Sabemos cuanto duerme ")
else:
   print("No sabemos cuanto duerme ")
 


