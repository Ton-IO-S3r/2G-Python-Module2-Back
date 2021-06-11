x = list(range(100))
# x.extend([50,50,50,50]) 

### promedio
suma = 0
for i in x :
    suma += i

promedio = suma / len(x)
print(promedio)

### mediana
x.sort()
mitad = int(len(x)/2)
if len(x)-mitad == mitad :
  mediana = x[mitad] 

mediana = x[mitad] if len(x)-mitad == mitad else x[mitad]



### moda


### ordenar