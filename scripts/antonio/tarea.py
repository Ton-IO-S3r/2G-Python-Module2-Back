### Crear la clase Mercancia
### con los siguientes atributos:
### precio
### nombre
### descuento
### stock
#con los siguientes métodos
### llevarse producto decrementa en una unidad el atributo stock

class Mercancia():
  def __init__(self, precio: float, nombre: str, descuento: float, stock: int):
      self.precio = precio
      self.nombre = nombre
      self.descuento = descuento
      self.stock = stock
  def elegirProducto(self, cantidad) -> int:
    if cantidad <= self.stock:
      self.stock -= cantidad
    else:
      print('La cantidad seleccionada supera el stock')
    return self.stock
  def getStock(self):
    print(f'Stock actual en {self.nombre}: {self.stock} artículos')


### Crea una subclase de Mercancia que se llame botanas
# Agregar los siguientes atributos:
## sabor
## advertencia_calorias
class Botana(Mercancia):
  def __init__(self, precio: float, nombre: str, descuento: float, stock: int, sabor: str, advertencia_calorias: str):
      super().__init__(precio, nombre, descuento, stock)

### Crea la clase Tarjetas,
#con los siguientes atributos:
### dueño
### saldo
### vigencia
#con los siguientes métodos
### compra(self, Mercancia) ### este método disminuye el saldo en la Tarjeta
### deposito(self) ### este método aumenta el saldo en la Tarjeta
class Tarjeta():
  def __init__(self, dueño: str, saldo: float, vigencia: str):
    self.dueño = dueño
    self.saldo = saldo
    self.vigencia = vigencia
  def compra(self, producto:Mercancia, cantidad = 1) -> float:
    if self.saldo < producto.precio:
      print('No se pudo realizar la transaccion: Saldo insuficiente')
    elif producto.stock < cantidad:
      print('No se pudo realizar la transaccion: No hay productos disponibles')
    else:
      self.saldo -= producto.precio
      producto.elegirProducto(cantidad)
    return self.saldo
  def deposito(self,monto):
    self.saldo += monto
    print(f'Se dpositaron $ {monto} a tu cuenta')
    print(f'Saldo actual: $ {self.saldo}')
  def getSaldo(self):
    print(f'Saldo actual: $ {self.saldo}')

### 1. Crear una tarjeta con un saldo inicial de $1000, el dueño eres tú y la vigencia es al día de tu próximo cumple
miTarjeta = Tarjeta('Antonio Servin Mojica', 1000, '30/11/1985')
### 2 Crear una mercancia con precio de $12, nombre fritos, stock, que es el número de unidades en la tienda de 20, y 0% de descuento
fritos = Mercancia(12.00, 'fritos', 0, 20)
### 2 Crear una botana con precio de $12, nombre maruchan, stock, que es el número de unidades en la tienda de 20, y 0% de descuento,
maruchan = Botana(12.00, 'maruchan', 0, 20, 'chipotle', 'Producto alto en calorías')
#calorías altas y sabor chipotle
### Realiza las siguientes compras:
# 1 unos fritos
miTarjeta.compra(fritos)
# 1 unos fritos
miTarjeta.compra(fritos)
# 1 maruchan
miTarjeta.compra(maruchan)
# depósito de nómina de $5000
miTarjeta.deposito(5000)
# 1 maruchan
miTarjeta.compra(maruchan)
# 1 maruchan
miTarjeta.compra(maruchan)
# 1 maruchan
miTarjeta.compra(maruchan)
# 1 maruchan
miTarjeta.compra(maruchan)
#Imprime el saldo actual de la tarjeta y el stock de botana y mercancia
miTarjeta.getSaldo()
fritos.getStock()
maruchan.getStock()