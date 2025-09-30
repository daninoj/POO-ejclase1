Taller: POO y modificadores de acceso en Python

Este repositorio contiene las respuestas del taller de Programación Orientada a Objetos (POO) en Python, organizado en tres partes:  

Parte A: Conceptos y lectura de código  
Parte B: Encapsulación con @property y validación  
Parte C: Diseño y refactor  


Parte A – Conceptos y lectura de código


1. Atributos accesibles  
Existen a.x, a._y, a._A__z. El a.__z no es accesible directamente.  

2. Salida del programa  
False True → porque __secret se guarda realmente como _A__secret.  

3. Verdadero/Falso  
_ no impide acceso (solo convención).  
__ no hace imposible acceder, aplica name mangling.  
El name mangling depende del nombre de la clase.  

4. Herencia con _token  
Se imprime "abc" porque _ es solo convención y la subclase lo puede usar.  

5. Name mangling en herencia  
Se imprime (2, 1). __v en cada clase se convierte en atributos distintos (_Base__v, _Sub__v).  

6. Error con __slots__  
AttributeError al asignar c.y, porque __slots__ limita atributos a solo x.  

7. Atributo protegido  
Usar self._dato = 99.  

8. Métodos privados  
True False True. _step existe, __tick se guarda como _M__tick.  

9. Acceso a __data  
Se accede con s._S__data.  

10. Uso de dir()  
Aparece _D__a (forma mangleada de __a).  

Parte B – Encapsulación con @property


11. Cuenta  
Validar que saldo ≥ 0; si es negativo, lanza ValueError.  

12. Termómetro  
temperatura_f como propiedad de solo lectura (C * 9/5 + 32).  

13. Usuario  
nombre siempre debe ser str, de lo contrario lanza TypeError.  

14. Registro  
La lista interna se expone como tupla inmutable (tuple).  


Parte C – Diseño y refactor


15. Motor  
Velocidad validada entre 0 y 200.  

16. Convenciones  
_atributo → convención de interno.  
__atributo → aplica name mangling, útil en herencia.  

17. Buffer  
Error: devolvía la lista interna (modificable).  
Corrección: devolver una tupla inmutable.  

18. Herencia y name mangling  
En la subclase no se accede con __x, sino con self._A__x.  

19. Servicio  
Expone solo el método guardar, oculta _dump y __repo.  

20. ContadorSeguro  
_n → contador protegido.  
inc() → incrementa y llama a __log().  
__log() → imprime "tick".  
n → propiedad de solo lectura.  
