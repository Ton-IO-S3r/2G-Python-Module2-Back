todos = {'Aaron', 'Carlos', 'Ferdinand', 'Rosa', 'Ivan', 'Osmar', 'Antonio', 'Yair', 'Victor'}
ingenieros = {"Antonio", "Carlos", "Ivan", "Yair", "Osmar"}
chilangos = {"Aaron", "Ivan"}
usan_lentes = {"Antonio", "Aaron", "Ivan"}
hombres = {'Aaron', 'Carlos', 'Ferdinand', 'Ivan', 'Osmar', 'Antonio', 'Yair', 'Victor'}
nutriapp = {'Rosa', 'Yair', 'Ivan'}
futapp = {'Ferdinand', 'Antonio', 'Aaron'}
bonificapp = {'Osmar','Victor','Carlos'}

ingenieros_chilangos = chilangos & ingenieros 
ingenieros_no_chilangos = todos - ingenieros_chilangos

preguntas = [
  'La persona es ingeniero?',
  'La persona es chilango?',
  'La persona usa lentes?',
  'La persona es hombre?',
  'La persona es del equipo Nutriapp?',
  'La persona es del equipo Futapp?',
  'La persona es del equipo Bonificapp?',
]
grupos = [ingenieros,chilangos,usan_lentes,hombres,nutriapp,futapp,bonificapp]

dict_buscar = dict(zip(preguntas, grupos))

grupo_busqueda = todos
for pregunta, grupo in dict_buscar.items():
  respuesta = input(pregunta + ' (Si / No)')
  if respuesta.lower() == 'si':
    grupo_busqueda = grupo_busqueda - (grupo_busqueda - grupo)
  else:
    grupo_busqueda = grupo_busqueda & (todos - grupo)
  
  print(grupo_busqueda)
  print(len(grupo_busqueda))
  if len(grupo_busqueda) == 1:
    print(f'La persona que estas buscando es {list(grupo_busqueda)[0]}')
    break
  elif len(grupo_busqueda) < 1:
    print(f'No es posible encontrar una persona con esas caracteristicas')
    break

if len(grupo_busqueda) > 1:
  print('Una de estas puede ser la persona que buscas:')
  for persona in grupo_busqueda:
    print(persona)