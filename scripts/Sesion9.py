# Métodos especiales
## __len__
# def __getitem__(self, ix):
#         return self.productos[ix]
###objeto[i]
###__eq__
class Poderosa(object):
    def __init__(self, tamanio = 10):
        self.tamanio = tamanio
    def __len__(self) -> int:
        print(f"tamaño {self.tamanio}")
        return(self.tamanio)
    def __floordiv__(self, objeto2) -> int:
        if isinstance(objeto2, Poderosa):
            return(self.tamanio // objeto2.tamanio)
        elif isinstance(objeto2, int):
            return(self.tamanio // objeto2)
        else:
            print("La comparación tiene que hacerse con objetos de la clase Poderosa")
            return None
    def __add__(self, objecto2):
        return(self.tamanio / objecto2.tamanio)

poderosa = Poderosa()
len(poderosa)

poderosa1 = Poderosa(15)
poderosa1.__floordiv__(poderosa)
poderosa1 + poderosa
poderosa1 // 1
poderosa1.__floordiv__(1)




# Operadores binarios
# Operador           Método
# +                  object.__add__(self, other)
# -                  object.__sub__(self, other)
# *                  object.__mul__(self, other)
# //                 object.__floordiv__(self, other)
# /                  object.__div__(self, other)
# %                  object.__mod__(self, other)
# **                 object.__pow__(self, other[, modulo])
# >                 object.__rshift__(self, other)
# &                  object.__and__(self, other)
# ^                  object.__xor__(self, other)
# |                  object.__or__(self, other)
# Operadores de asignación:
# Operador          Método
# +=                object.__iadd__(self, other)
# -=                object.__isub__(self, other)
# *=                object.__imul__(self, other)
# /=                object.__idiv__(self, other)
# //=               object.__ifloordiv__(self, other)
# %=                object.__imod__(self, other)
# **=               object.__ipow__(self, other[, modulo])
# >=               object.__irshift__(self, other)
# &=                object.__iand__(self, other)
# ^=                object.__ixor__(self, other)
# |=                object.__ior__(self, other)
# Operadores unarios:
# Operador          Método
# -                 object.__neg__(self)
# +                 object.__pos__(self)
# abs()             object.__abs__(self)
# ~                 object.__invert__(self)
# complex()         object.__complex__(self)
# int()             object.__int__(self)
# long()            object.__long__(self)
# float()           object.__float__(self)
# oct()             object.__oct__(self)
# hex()             object.__hex__(self)
# Operadores de comparación
# Operador          Método
# =                object.__ge__(self, other)
# >                 object.__gt__(self, other)
# object.__lt__(a, b) <
# object.__le__(a, b) <=
# object.__eq__(a, b) ==
# object.__ne__(a, b) !=
# object.__ge__(a, b) >=
# object.__gt__(a, b) >



### Crear la clase Hogar, crearle por lo menos 3 métodos y atributos, considera adicionalmente el atributo número de cuartos y el de superficie en M2
### y otra clase Departamento crearle por lo menos 3 métodos y atributos, considera adicionalmente el atributo número de cuartos y el de superficie en M2
### Utilizar __add__ en hogar que sume los cuartos de una casa o un departamento con otra casa o departamento.
### Utilizar __len__ para devolver las dimensiones de la casa o depa






casa1 + depa1 # número de cuartos
len(casa1) # M2







class Hogar():
    def __init__(self, n_cuartos, m2):
        self.m2 = m2
        self.n_cuartos = n_cuartos
    def __len__(self):
        return self.m2
    def __add__(self, other):
        if isinstance(other, Hogar):
            return self.n_cuartos + other.n_cuartos
        else:
            print("NO es válida esa adición")
            return None

class Departamento(Hogar):
    def __init__(self, n_cuartos, m2, piso):
        super().__init__(n_cuartos, m2)
        self.piso = piso


depa1 = Departamento(m2 = 50, n_cuartos = 2, piso = 5)
len(depa1) # 50
casa1 = Hogar(7, 120)
depa1 + casa1
depa1 + 112
casa1 + 112
casa1 + depa1
isinstance(depa1, Hogar)
isinstance(casa1, Departamento)
issubclass(Hogar, Departamento)
issubclass(Departamento, Hogar)



### Interacción de clases
class Comida():
    def __init__(self, nombre, tiempo_preparacion, duracion, sabor, *ingredientes):
        self.nombre = nombre
        self.tiempo_preparacion = tiempo_preparacion
        self.duracion = duracion
        self.ingredientes = ingredientes
        self.__sabor = sabor
    def get_sabor(self):
        return(self.__sabor)
    def set_sabor(self, sabor):
        self.__sabor = sabor

class Persona(object):
    def __init__(self, edad: int, estatura: float, nombre: str, peso: float, nacionalidad: str):
        self.edad = edad
        self.estatura = estatura
        self.nombre = nombre
        self.peso = peso
        self.nacionalidad = nacionalidad
    def comer(self, comida:Comida):
        print(f"Estoy comiendo {comida.nombre}")
    def preparar(self, comida:Comida, sabor):
        print(f"Estoy preparando {comida.nombre} y  me va tomar {comida.tiempo_preparacion} en hacerlo")
        comida.set_sabor(sabor)
        print("La comida tuvo un sabor de:", comida.get_sabor())
    def almacenar(self, comida: Comida):
        print(f"Estoy guardando un plato de {comida.nombre} y espero que me dure {comida.duracion} días")
    def comprar_ingredientes(self, comida:Comida):
        print("Tengo que comprar:")
        [print(ingrediente) for ingrediente in comida.ingredientes]

rosy = Persona(48,1.62,"Rosy", 58, "mexicana")
comida_favorita = Comida("Tacos", 45, 7, "rico", "tortillas", "pollo", "crema", "aceite", "salsa", "lechuga")
rosy.comer(comida_favorita)
rosy.preparar(comida_favorita, "Súper ricos")
comida_favorita.get_sabor()
rosy.almacenar(comida_favorita)
rosy.comprar_ingredientes(comida_favorita)



# ## Video juegos
# ## Vida y Ataques
# class Guerrero():
#     def __init__
#         self.vida 
#         self.ataque
#     def ataque(objeto):
#         objeto.recibir_ataque()
#     def recibir_ataque(50):
#         Si ya no tiene vida -> print("El jugador murió")


# class Arquero():
#     def __init__
#         self.vida 
#         self.ataque
#     def ataque(objeto):
#         objeto.recibir_ataque()
#     def recibir_ataque(50):
#         Si ya no tiene vida -> print("El jugador murió")



