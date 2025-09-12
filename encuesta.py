#Autor Daniel Niño
class Estudiante:
    def __init__(self, nombre, edad, respuestas):
        self.nombre=nombre
        self.edad=edad
        self.respuestas=respuestas



class Encuesta:
    def __init__(self,preguntas):
        self.preguntas = preguntas
        self.respuestas = []
    def agregar_respuesta(self):
        print("\n Nueva respuesta")
        nombre = input("Nombre del estudiante: ")
        edad = input("Edad: ")

        respuestas_est = []
        for pregunta in self.preguntas:
            print("\n"+ pregunta)
            respuesta= input("Respuesta: ")
            respuestas_est.append(respuesta)
        estudiante= Estudiante(nombre, edad, respuestas_est)
        self.respuestas.append(estudiante)

    def mostrar_resultados(self):
        print("\n Resultados de la encuesta: ")
        for estudiante in self.respuestas:
            print(f"\Estudiante: {estudiante.nombre}, Edad:{estudiante.edad}")
            for i, respuesta in enumerate(estudiante.respuestas):
                print(f"{self.preguntas[1]} → {respuesta}")


    def resumen(self):
        print("\n Resumen: ")
        for i, pregunta in enumerate(self.preguntas):
            conteo={}
            for estudiante in self.respuestas:
                resp=estudiante.respuestas [i]
                conteo[resp]=conteo.get(resp,0)+1
            print(f"\n Pregunta: {pregunta}")
            for opcion, cantidad in conteo.items():
                print(f"{opcion}:{cantidad} votos")

if __name__=="__main__":
    preguntas=[
        "¿Qué tema tienes para tu proyecto?", "¿Sabes trabajar en equipo? (Sí/No)"
      ]
    encuesta= Encuesta(preguntas)
    print(" ENCUESTA DE IDEAS DE PROYECTO")
    n= int(input("¿Cuentos estudiantes responderán?"))
    for __ in range(n):
        encuesta.agregar_respuesta()
        encuesta.mostrar_resultados()
        encuesta.resumen()