### __add__
class Entero():
    def __init__(self, x):
        self.x = int(x)
    def __str__(self, x):
        pass
    def __add__(self, ext):
        return(self.x + int(ext.x))
class Cadena():
    def __init__(self, x):
        self.x = str(x)
    def __add__(self, ext):
        return(self.x + str(ext.x))
entero1 = Entero(10)
entero2 = Entero(10)
entero1.__add__(entero2)
cadena1 = Cadena(10)
entero1.__add__(cadena1) #10 + "10"
entero1 + cadena1
cadena2 = Cadena("Hola mundo")
entero1 + cadena2
cadena1 + entero1 #"10" + 10
entero1.x
cadena1.cadena
10 + "10"
### Encapsulamiento
##__
class Producto(object):
    carrito = []
    def __init__(self, precio_sin_iva = 100, iva = 0.16):
        self.__precio_sin_iva = precio_sin_iva
        self.iva = iva
        self.__precio_con_iva = (1 + iva) * precio_sin_iva
        self.__calcular_totales()
    def modificar_precio(self, precio_sin_iva):
        self.__precio_sin_iva = precio_sin_iva
        self.__precio_con_iva = (1 + self.iva) * self.__precio_sin_iva
        self.__calcular_totales()
        # self.precio_con_iva = (1 + self.iva) * nuevo_precio_sin_iva
    def mostrar_precio_iva(self):
        print(self.__precio_con_iva)
    def comprar(self, unidades = 3):
        self.carrito.extend(unidades * [1])
        self.__calcular_totales()
    def __calcular_totales(self):
        self.subtotal = self.__precio_sin_iva * len(self.carrito) #[1, 1, 1]
        self.impuesto = self.subtotal * self.iva
        self.total = self.subtotal + self.impuesto
    def mostrar_totales(self):
        print(f"Has comprado: {len(self.carrito)}, dando un subtotal de: {self.subtotal}, pagas de impuesto: {self.impuesto}, el total que vas a pagar es: {self.total}")
producto1 = Producto(150) # Se crea un producto de un precio sin iba de 150
print(producto1.comprar()) # Se compran 3 unidades de este producto
print(producto1.mostrar_totales()) # Se muestra los detalles de la compra
producto1.precio_sin_iva = 120 # Se intenta modificar el precio sin iva
print(producto1.mostrar_totales())
producto1.modificar_precio(170)