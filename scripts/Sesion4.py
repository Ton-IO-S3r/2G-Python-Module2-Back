# Ejercicio 1
suma = lambda x, y: x + y if type(x) == type(y) else str(x) + str(y)
suma(3, "4")

# Ejercicio 2
formato_dict = lambda dict_: "El diccionario tiene como la llave {} con valor de {}".format(dict_.keys(), dict_.values())
dict_ = {
    "yo": "Arturo"
}
formato_dict(dict_)

xiaomi = {
    "ntf":True,
    "camara": True,
    "ram": 5
}
xiaomi["ram"] = xiaomi["ram"] + 10
print(xiaomi)


# Ejercicio 3
nombres = ["Arturo", "Ferdinand", "Yair", "Ivan"]
alturas = [1.72, 1.75, 1.70, 1.70]

resultado = [nombres[i] for i in range(len(alturas)) if alturas[i] > 1.70]
resultado



# Ejercicio 4


# Ejercicio 5
todos = {'Aaron', 'Carlos', 'Ferdinand', 'Rosa', 'Ivan', 'Arturo', 'Osmar', 'Antonio', 'Yair'}
ingenieros = {"Antonio", "Carlos", "Ivan", "Yair", "Osmar"}
chilangos = {"Arturo", "Aaron", "Ivan", }
chilangos & ingenieros # chilangos & ingenieros 
chilangos & (todos - ingenieros)# chilangos & no_ingenieros
(todos - chilangos) & (todos - ingenieros)# no_chilangos & no_ingenieros
(todos - chilangos) & ingenieros# no_chilangos & ingenieros


no_chilangos = {"Rosa", "Ferdinand", "Yair", "Osmar", "Antonio", }
no_ingenieros = {"Arturo", "Rosa", "Aaron", "Ferdinand"}

chilangos & ingenieros 
chilangos & no_ingenieros
no_chilangos & no_ingenieros
no_chilangos & ingenieros

Persona = {
    "ingeniero":True, 
    "chilango":True
}

if Persona["ingeniero"]:
    if Persona["chilango"]:
        print("Eres Ivan")
    else:
        print("Puedes ser : 'Osmar', 'Antonio', 'Yair'")
else:
    if Persona["chilango"]:
        print("Puedes ser : 'Aaron', 'Arturo'")
    else:
        print("Puedes ser : 'Aaron', 'Arturo'")
