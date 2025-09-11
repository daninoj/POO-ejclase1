# autor: Daniel Niño

import random

#EJERCICIO 31
def ejr31():
    class Planeta:
        def __init__(self, nombre, masa, densidad, diametro, distancia_sol):
            self.nombre = nombre
            self.masa = masa
            self.densidad = densidad
            self.diametro = diametro
            self.distancia_sol = distancia_sol

        def mostrar_info(self):
            print(f"Planeta: {self.nombre}")
            print(f"  Masa: {self.masa} kg")
            print(f"  Densidad: {self.densidad} g/cm³")
            print(f"  Diámetro: {self.diametro} km")
            print(f"  Distancia al sol: {self.distancia_sol} km\n")

    tierra = Planeta("Tierra", "5.97e24", "5.51", "12742", "149.6e6")
    marte = Planeta("Marte", "6.39e23", "3.93", "6779", "227.9e6")

    tierra.mostrar_info()
    marte.mostrar_info()


#EJERCICIO 32
def ejr32():
    print("En Python también se puede tener varios archivos con funciones definidas.")
    print("El punto de entrada de ejecución se controla con el bloque especial:")
    print("\nif __name__ == '__main__':")
    print("    # código principal\n")
    print("Esto asegura que el código solo se ejecute si el archivo se corre directamente,")
    print("y no cuando se importa como módulo en otro archivo.")


# EJERCICIO 33
def ejr33():
    def burbuja(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivote = arr[len(arr)//2]
        izquierda = [x for x in arr if x < pivote]
        centro = [x for x in arr if x == pivote]
        derecha = [x for x in arr if x > pivote]
        return quicksort(izquierda) + centro + quicksort(derecha)

    n = int(input("¿Cuántos números aleatorios deseas generar? "))
    numeros = [random.randint(1, 100) for _ in range(n)]
    print("\nLista generada:", numeros)

    metodo = input("Elige el método de ordenamiento (burbuja/quicksort): ").lower()
    if metodo == "burbuja":
        print("Lista ordenada:", burbuja(numeros))
    else:
        print("Lista ordenada:", quicksort(numeros))


#EJERCICIO 34
def ejr34():
    class Vehiculo:
        def __init__(self, marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio):
            self.marca = marca
            self.modelo = modelo
            self.año = año
            self.pasajeros = pasajeros
            self.tripulacion = tripulacion
            self.ruedas = ruedas
            self.matricula = matricula
            self.medio = medio

        def mostrar_info(self):
            print(f"Vehículo {self.marca} {self.modelo} ({self.año})")
            print(f"  Pasajeros: {self.pasajeros}")
            print(f"  Tripulación: {self.tripulacion}")
            print(f"  Ruedas: {self.ruedas}")
            print(f"  Matrícula: {self.matricula}")
            print(f"  Medio: {self.medio}\n")

    vehiculos = []
    for i in range(3):  # decia 10 pero 3 mejor para probar
        print(f"\n=== Ingreso del vehículo {i+1} ===")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        año = input("Año: ")
        pasajeros = input("Pasajeros: ")
        tripulacion = input("¿Tiene tripulación? (sí/no): ")
        ruedas = input("Número de ruedas: ")
        matricula = input("Matrícula: ")
        medio = input("Medio (tierra/agua/aire): ")

        vehiculos.append(Vehiculo(marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio))

    print("\n=== Información de los vehículos ingresados ===")
    for v in vehiculos:
        v.mostrar_info()


# EJERCICIO 35 

class Vehiculo:
    def __init__(self, marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.pasajeros = pasajeros
        self.tripulacion = tripulacion
        self.ruedas = ruedas
        self.matricula = matricula
        self.medio = medio

    def mostrar_info(self):
        print(f"\nVehículo {self.marca} {self.modelo} ({self.año})")
        print(f"  Pasajeros: {self.pasajeros}")
        print(f"  Tripulación: {'sí' if self.tripulacion else 'no'}")
        print(f"  Ruedas: {self.ruedas}")
        print(f"  Matrícula: {self.matricula}")
        print(f"  Medio: {self.medio}")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio, cinco_puertas):
        super().__init__(marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio)
        self.cinco_puertas = cinco_puertas  # True = 5 puertas, False = 3 puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  ¿Cinco puertas?: {'Sí (5)' if self.cinco_puertas else 'No (3)'}")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio, deportiva):
        super().__init__(marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio)
        self.deportiva = deportiva

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  ¿Deportiva?: {'Sí' if self.deportiva else 'No'}")


class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio, altura):
        super().__init__(marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio)
        self.altura = altura

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Altura: {self.altura} m")


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio, tipo):
        super().__init__(marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio)
        self.tipo = tipo  

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Tipo de bicicleta: {self.tipo}")


class Lancha(Vehiculo):
    def __init__(self, marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio, motor):
        super().__init__(marca, modelo, año, pasajeros, tripulacion, ruedas, matricula, medio)
        self.motor = motor  

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Tipo de motor: {self.motor}")


def ejr35():
    print("\n Ejercicio 35: Vehículos con herencia ")


    coche = Coche("Toyota", "Yaris", 2021, 5, False, 4, "AAA111", "tierra", True)
    moto = Moto("Yamaha", "R3", 2020, 2, False, 2, "BBB222", "tierra", True)
    camion = Camion("Volvo", "FH", 2019, 2, True, 12, "CCC333", "tierra", 4.2)
    bicicleta = Bicicleta("Trek", "Marlin 5", 2022, 1, False, 2, "DDD444", "tierra", "montaña")
    lancha = Lancha("Yamaha", "WaveRunner", 2023, 4, False, 0, "EEE555", "agua", "fuera de borda")

    vehiculos = [coche, moto, camion, bicicleta, lancha]

 
    for v in vehiculos:
        v.mostrar_info()



if __name__ == "__main__":
    ejr35()


# MENÚ PRINCIPAL
def menu():
    while True:
        print("\n MENÚ DE EJERCICIOS (31-35) ")
        print("1. Ejercicio 31 - Sistema planetario")
        print("2. Ejercicio 32 - Punto de entrada en Python")
        print("3. Ejercicio 33 - Ordenamiento de números")
        print("4. Ejercicio 34 - Clase Vehiculo (ingreso de datos)")
        print("5. Ejercicio 35 - Herencia de Vehiculos")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            ejr31()
        elif opcion == "2":
            ejr32()
        elif opcion == "3":
            ejr33()
        elif opcion == "4":
            ejr34()
        elif opcion == "5":
            ejr35()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()