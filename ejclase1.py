#Autor Daniel Niño
#Diseñar una encuenta para 6 usuarios diferentes
#Nombre, Carrera, Idea de proyecto
def encuensta():
    n=int(input("Cuantas encuestas se van a realizar: "))
    for i in range (0,7):
        nombre=input("Ingresa tu nombre: ")
        carrera=input("Ingresa tu carrera: ")
        idea=input("Ingresa tu idea de proyecto: ")
        print(nombre)
        print(carrera)
        print(idea)
encuensta()