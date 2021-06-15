dict_times={}
flag='SI'
while flag != 'NO':
  name_alumno = input('Ingresa el nombre del alumno: ')
  if name_alumno in dict_times:
    print(f'El usuario {name_alumno} ya existe. Intentalo nuevamente')
    continue
  time2work = int(input('Cuantos minutos tarda en llegar a su trabajo? '))
  dict_times.update({name_alumno:time2work})
  flag = input('Deseas continuar (SI, NO)? ')

for name,time in dict_times.items(): 
  print(f'{name} ocupa {time} minutos para llegar al trabajo!')