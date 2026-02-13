from Persona import Persona
from datetime import date, datetime

class Profesor(Persona):
    def __init__(self, apellidos, nombre, dni, fechaNac, nombreAsignatura):
        super().__init__(apellidos, nombre, dni, fechaNac) 
        self.nombreAsignatura = nombreAsignatura 
        self.alumnos = [] 

    def set_nota_alumno(self, dni, nota):
        try:
            nota_float = float(nota)
        except ValueError:
            raise ValueError("La nota introducida debe ser un número.")
            
        for alumno in self.alumnos: 
            if alumno.dni == dni: 
                for i, (asig, n) in enumerate(alumno.asignaturas):
                    if asig.nombre == self.nombreAsignatura:
                        alumno.asignaturas[i] = (asig, nota_float)
    
    def get_top_n_alumnos(self, n):
        ordenados = sorted(self.alumnos, key=lambda a: a.getNotaMedia(), reverse=True)
        return ordenados[:n]

    def get_medias_por_asignatura(self):
        acumulador = {}
        for alu in self.alumnos:
            for asig, nota in alu.asignaturas:
                if asig.nombre not in acumulador:
                    acumulador[asig.nombre] = []
                acumulador[asig.nombre].append(nota)
                
        medias = {}
        for asig, notas in acumulador.items():
            medias[asig] = sum(notas) / len(notas)
        return medias

    def get_edad_media_por_curso(self, curso_n):
        edades = []
        for alu in self.alumnos:
            if any(asig.curso == curso_n for asig, nota in alu.asignaturas):
                edades.append(alu.getEdad())
                
        if not edades: return 0.0
        return sum(edades) / len(edades)
    
    def aplicar_bonus_aprobados(self):
        for alumno in self.alumnos:
            nuevas_notas_alumno = []
            
            for asig, nota in alumno.asignaturas:
                if nota >= 5.0:
                    nueva_nota = min(10.0, nota + 1.0)
                    nuevas_notas_alumno.append((asig, nueva_nota))
                else:
                    nuevas_notas_alumno.append((asig, nota))
            
            alumno.asignaturas = nuevas_notas_alumno
