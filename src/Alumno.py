from Persona import Persona
from datetime import datetime,date 

class Alumno(Persona):
    def __init__(self, apellidos, nombre, dni, fechaNac, grupo):
        super().__init__(apellidos, nombre, dni, fechaNac) 
        self.asignaturas = [] 
        self.set_grupo(grupo) 

    def set_grupo(self, nuevo_grupo):
        try:
            self.grupo = int(nuevo_grupo) 
        except ValueError:
            raise ValueError("El grupo debe ser un número entero.")

    def getNúmeroCreditosSuperados(self):
        return sum(asig.creditos for asig, nota in self.asignaturas if nota >= 5.0)

    def getNotaMedia(self):
        if not self.asignaturas: return 0.0
        return sum(nota for _, nota in self.asignaturas) / len(self.asignaturas) 

    
