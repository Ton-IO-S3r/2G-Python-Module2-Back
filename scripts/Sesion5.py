### 8 ¿Aplicar 2 operaciones con Bool?
#< menor que
#> mayor que
#>= mayor o igual que
#<= menor o igual que

# and, &
# or, |

# True & True = True
print("True & True", True & True)
# True & False = False
print("True & False", True & False)
# False & True = False
print("False & True", False & True)
# False & False = False
print("False & False", False & False)


# True | True = True
print("True | True", True | True)
# False | True = True
print("False | True", False | True)
# True | False = True
print("True | False", True | False)
# False | False = False 
print("False | False", False | False)




# while condición:
#     código
 
i = 0
while i == 0: #imprime un 0
   print(i)
   break
 
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
   if i == 10:
       break
   else:
       print(i)
 
 
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
 
### Una forma de crear diccionarios
dict_new = dict(zip(l_nombres2, l_horas))
 
for i, j in zip(l_nombres2, l_horas):
   print(f'{i} duerme {j} horas')
 
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
 
[[i, j] for i, j in horas_suenio_dict_2.items()]
[(i, j) for i, j in horas_suenio_dict_2.items()]
 
list(horas_suenio_dict_2.items())
 
 
 
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
 

input("Inserta el nombre del alumno")
int(input("Inserta cuanto tiempo tarda al trabajo"))