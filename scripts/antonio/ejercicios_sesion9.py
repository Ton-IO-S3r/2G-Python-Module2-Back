class Hogar(object):
    def __init__(self, superficie, numCuartos,numHabitantes):
        self.superficie = superficie
        self.numCuartos = numCuartos
        self.numHabitantes = numHabitantes
    def __add__(self, obj:Hogar) -> int:
        if isinstance(obj, Hogar):
            print(f'Total de habitaciones: {self.numCuartos + obj.numCuartos}')
            return(self.numCuartos + obj.numCuartos)
        elif isinstance(obj, int):
            print(f'Total de habitaciones: {self.numCuartos + obj}')
            return(self.numCuartos + obj)
        else:
            print("No se pueden contar cuartos de un a clase que no sea Hogar o Departamento")
            return None
    def __len__(self) -> int:
        print(f"Superficie {self.superficie} m2")
        return(self.superficie)

class Departamento(Hogar):
    def __init__(self, superficie, numCuartos,numHabitantes,piso):
        self.superficie = superficie
        self.numCuartos = numCuartos
        self.numHabitantes = numHabitantes
        self.piso = piso

casa1 = Hogar(200,5,6)
casa2 = Hogar(80,3,4)
depa1 = Departamento(60,3,3,12)
depa2 = Departamento(80,4,5,7)
casa1 + depa1 # número de cuartos
len(casa1) # M2

## Video juevos
## Vida y Ataques
# class Arquero():
#     def __init__(self,vida, ataque):
#         self.vida = vida
#         self.ataque = ataque
#     def atacar(self, guerrero:Guerrero):
#         guerrero.recibir_ataque(self.ataque)
#     def recibir_ataque(self, ataque):
#         self.vida -= ataque
#         if(self.vida <= 0):
#             print('El arquero ha sido derrotado')
#         else:
#             print(f'El arquero tiene {self.vida} puntos de vida')
            
# class Guerrero():
#     def __init__(self,vida, ataque):
#         self.vida = vida
#         self.ataque = ataque
#     def atacar(self, arquero:Arquero):
#         arquero.recibir_ataque(self.ataque)
#     def recibir_ataque(self, ataque):
#         self.vida -= ataque
#         if(self.vida <= 0):
#             print('El guerrero ha sido derrotado')
#         else:
#             print(f'El guerrero tiene {self.vida} puntos de vida')

# guerrero1 = Guerrero(100, 20)
# arquero1 = Arquero(100,15)

# guerrero1.atacar(arquero1)      

class Character():
    def __init__(self, vida: int, ataque: int, categoria=None):
        self.vida = vida
        self.ataque = ataque
        self.categoria = categoria
    def recibir_ataque(self, ataque):
        self.vida -= ataque
        if(self.vida <= 0):
            print(f'El {self.categoria} ha sido derrotado')
        else:
            print(f'El {self.categoria} tiene {self.vida} puntos de vida')

class Arquero(Character):
    def __init__(self, vida, ataque):
        super().__init__(vida, ataque,'arquero')
        
    def atacar(self, enemy:Character):
        enemy.recibir_ataque(self.ataque)
    

class Guerrero(Character):
    def __init__(self, vida, ataque):
        super().__init__(vida, ataque,'guerrero')
    def atacar(self, enemy:Character):
        enemy.recibir_ataque(self.ataque)
    

guerrero1 = Guerrero(100, 20)
arquero1 = Arquero(100,15)

guerrero1.atacar(arquero1)
arquero1.atacar(guerrero1)
