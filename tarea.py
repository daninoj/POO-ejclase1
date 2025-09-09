#Autor Daniel Niño
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau guau!")


class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau miau!")


# Programa principal
print(" Registro de Animales ")

# Ingreso de datos para el perro
nombre_perro = input("Ingrese el nombre del perro: ")
edad_perro = input("Ingrese la edad del perro: ")
perro = Perro(nombre_perro, edad_perro)

# Ingreso de datos para el gato
nombre_gato = input("Ingrese el nombre del gato: ")
edad_gato = input("Ingrese la edad del gato: ")
gato = Gato(nombre_gato, edad_gato)

# Probar los métodos
print("\n Sonidos de los animales :) ")
perro.ladrar()
gato.maullar()