### 8 ¿Aplicar 2 operaciones con Bool?
#< menor que
#> mayor que
#>= mayor o igual que
#<= menor o igual que

# and, &
# or, |

# True & True = True
print("True & True:", True & True)
# True & False = False
print("True & False:", True & False)
# False & True = False
print("False & True:", False & True)
# False & False = False
print("False & False:", False & False)


# True | True = True
print("True | True", True | True)
# False | True = True
print("False | True", False | True)
# True | False = True
print("True | False", True | False)
# False | False = False 
print("False | False", False | False)

not (True & True) # -> False
not (True & False) # -> True
not (False and False) # -> True
not (False or False) # -> True

## in
lista_temporal = [1,2,4]
14 in lista_temporal # -> False

lista_temporal = [1, 2, 4, [14]]
14 in lista_temporal # -> False

lista_temporal = [1, 2, 4, [14]]
[14] in lista_temporal # -> True

lista_lista = [[12,13], [11,12], [3], 12, 11]

validar_lista = lambda lista_lista: len(list(filter(lambda x: isinstance(x, list), lista_lista))) > 0
validar_lista(lista_lista)

otra_lista = [1,23,4]
validar_lista(otra_lista)

"Arturo" in "Arturo Téllez"
"Mundo" in "Hola mundo"
"mundo" in "Hola mundo"


# while condición:
#     código
 
i = 0
while i == 0: #imprime un 0
    print(i)
    break
    #i += 1

i = 0
while i != 0: # No imprime nada
   print(i)
   break
 
#imprimir del 1 al 10
i = 1
while i < 11:
   print(i)
   i += 1
 
 
i = 0
while i < 10:
   i += 1
   print(i)
 
 
# break
i = 0
while True:
    i += 1
    if i == 11:
        break
    else:
        print(i)
 
i = 0

while True:
    i += 1
    print(i)
    if i == 10:
        break
    else:
        pass

i = 0
while True:
    i += 1
    print(i)
    if i == 10:
        break

i = 0
while True:
    i += 1
    print(i)
    if i == 10:
        pass
    else:
        break   


primos = [1,2,3,5,7]
i = 0
while i < 10:
    i += 1
    if i in primos:
        print(i)
    else:
        pass



i = 0
while True:
   i += 1
   print(i)
   if i == 10:
       break
 
i = 0
while True:
   i += 1
   if i == 11:
       break
   else:
       print(i)
 
# continue
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)



 
i = 0
while i < 10:
   i += 2
   print(i)
 
 
 
# pass
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        pass
    print(i)
 
 
 
### zip

l_nombres = ["Rosy", "Ferdinand", "Yair"]
l_horas = ["3", "3", "4"]

### Una forma de crear diccionarios
dict_new = dict(zip(l_nombres, l_horas))
 
u, v = (1,3)
list(zip([2],[3]))

for i, j in zip(l_nombres, l_horas):
    print(f'{i} estudia {j} horas')

l_horas_suenio = ["8", "8", "8"]
for nombre, h_estudio, h_suenio in zip(l_nombres, l_horas, l_horas_suenio):
    print(f'{nombre} estudia {h_estudio} horas y duerme {h_suenio}')
    
 
dict_ejercicio = {}
 
## actualizar el siguiente diccionario dict_ejercicio
l_nombres2 = []
l_horas = []
 
dict_ejercicio = {}
 
for i, j in zip(l_nombres2, l_horas):
   dict_ejercicio.update({i: j})
   # dict_ejercicio.setdefault(i, j)
   # dict_ejercicio[i] = j
   print(f'{i} duerme {j} horas')
 
 
 
### for a in zip()
 
[[i, j] for i, j in dict_new.items()]
[(i, j) for i, j in dict_new.items()]
 
list(dict_new.items())
 
 
 
### Mezclar diccionarios y listas
ejemplo_mixto = {"Arturo":{"Vision computacional":[10, 9, 7]}}
ejemplo_mixto["Arturo"]
#{'Vision computacional': [10, 9, 7]}
ejemplo_mixto["Arturo"].get("Vision computacional")
#[10, 9, 7]
ejemplo_mixto["Arturo"].get("Vision computacional")[1]
#9
ejemplo_mixto["Arturo"].get("Vision computacional")[0]
#10
ejemplo_mixto["Arturo"].get("Vision computacional")[2]
#7

ejemplo_mixto = [
    ("Arturo", {"Vision computacional":[10, 9, 7]})
    ]

# Regresar "Arturo"
ejemplo_mixto[0][0]

# Regresar "Vision computacional"
llave = list(ejemplo_mixto[0][1].keys())[0]
print(llave)

# Regresar [10, 9, 7]
list(ejemplo_mixto[0][1].values())[0]
ejemplo_mixto[0][1].get(llave)
ejemplo_mixto[0][1][llave]







input("Inserta el nombre del alumno")
int(input("Inserta cuanto tiempo tarda al trabajo"))