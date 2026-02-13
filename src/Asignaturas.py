from datetime import date, datetime

class Asignatura: 
    def __init__(self, nombre, creditos, curso, cuatrimestre):
        self.nombre = str(nombre) 
        
        try:
            self.creditos = float(creditos) 
        except ValueError:
            raise ValueError("Los créditos deben ser un número.")
            
        self.set_curso(curso)
        self.set_cuatrimestre(cuatrimestre)

    def set_curso(self, nuevo_curso):
        try:
            c = int(nuevo_curso)
            if c < 1 or c > 4: 
                raise ValueError("El curso debe estar entre 1 y 4.")
            self.curso = c
        except ValueError:
            raise ValueError("El curso debe ser un número entero.")

    def set_cuatrimestre(self, nuevo_cuatri):
        try:
            c = int(nuevo_cuatri)
            if c not in (1, 2): 
                raise ValueError("El cuatrimestre debe ser 1 o 2.")
            self.cuatrimestre = c
        except ValueError:
            raise ValueError("El cuatrimestre debe ser un número entero.")
