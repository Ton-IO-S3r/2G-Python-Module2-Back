# Ejercicio 1
suma = lambda x,y : x + y if isinstance(x,int) & isinstance(y,int) else str(x)+ str(y)
suma(10,10)

#  Ejercicio 2
leerdiccionario = lambda diccionario : f'El diccionario tiene como la llave list({diccionario.keys()} con valor de {diccionario.values()})'

mydictionary = { 'key': 'value'}
print(leerdiccionario(mydictionary))

# Ejercicio 3
koders = ['Yair', 'Ferdinand', 'Rosy', 'Victor', 'Aaron', 'Carlos', 'Osmar', 'Ivan','Antonio']
alturas = [1.70,1.67,1.60,1.65, 1.65, 1.70, 1.68, 1.67,1.65]

print([koders[i] for i in  range(len(koders)) if alturas[i] > 1.65])

# Ejercicio 4
alturas_reales = [1.65,1.65,1.70,1.75, 1.64, 1.65, 1.72, 1.67,1.65]
acertados = [True if abs(alturas[i] - alturas_reales[i]) <= 0.03 else False for i in  range(len(alturas)) ]
print(acertados)
print(f'Adiviné la altura de mis compañeros en {acertados.count(True)} ocasiones')

# Ejercicio 5

todos = {'Aaron', 'Carlos', 'Ferdinand', 'Rosa', 'Ivan', 'Osmar', 'Antonio', 'Yair'}
ingenieros = {"Antonio", "Carlos", "Ivan", "Yair", "Osmar"}
chilangos = {"Aaron", "Ivan", }
usan_lentes = {"Antonio", "Aaron", "Ivan"}
hombres = {'Aaron', 'Carlos', 'Ferdinand', 'Ivan', 'Osmar', 'Antonio', 'Yair'}
nutriapp = {'Rosa', 'Yair', 'Ivan'}
futapp = {'Ferdinand', 'Antonio', 'Aaron'}
bonificapp = {'Osmar','Victor','Carlos'}

ingenieros_chilangos = chilangos & ingenieros 
ingenieros_no_chilangos = todos - ingenieros_chilangos

preguntas = [
  'La persona es ingeniero?',
  'La persona es chilango?',
  'La persona es usa lentes?',
  'La persona es hombre?',
  'La persona es del equipo Nutriapp?',
  'La persona es del equipo Futapp?',
  'La persona es del equipo Bonificapp?',
]
grupos = [ingenieros,chilangos,usan_lentes,hombres,nutriapp,futapp,bonificapp]

dict_buscar = dict(zip(preguntas, grupos))

grupo_busqueda = {}
for pregunta, grupo in preguntas.items():
  respuesta = input(pregunta + ' (Si / No)')
  if respuesta.lower() == 'si':
    grupo_busqueda = grupo
  else:
    grupo_busqueda = todos - grupo
  
  print(grupo_busqueda)

encontrado = False
while encontrado == False:
  hombre = input('La persona es hombre? (si / no)')
  if hombre == "si":
    grupo_busqueda = hombres
  else:
    grupo_busqueda