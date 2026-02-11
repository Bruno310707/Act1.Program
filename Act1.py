from datetime import date, datetime

class Asignatura:
    def __init__(self, nombre, creditos, curso, cuatrimestre):
        self.nombre = str(nombre) 
        self.creditos = float(creditos) 
        self.curso = int(curso) 
        self.cuatrimestre = int(cuatrimestre)
    def set_curso(self, nuevo_curso):
        self.curso = nuevo_curso 

    def set_cuatrimestre(self, nuevo_cuatri):
        self.cuatrimestre = nuevo_cuatri 

class Persona:
    def __init__(self, apellidos, nombre, dni, fechaNac):
        self.apellidos = apellidos 
        self.nombre = nombre 
        self.dni = dni 
        self.fechaNac = fechaNac 

    def getEdad(self):
        hoy = date.today()
        return hoy.year - self.fechaNac.year - ((hoy.month, hoy.day) < (self.fechaNac.month, self.fechaNac.day)) 

class Alumno(Persona):
    def __init__(self, apellidos, nombre, dni, fechaNac, grupo):
        super().__init__(apellidos, nombre, dni, fechaNac) 
        self.asignaturas = [] 
        self.grupo = int(grupo) 

    def set_grupo(self, nuevo_grupo):
        self.grupo = nuevo_grupo 

    def getNúmeroCreditosSuperados(self):
        return sum(asig.creditos for asig, nota in self.asignaturas if nota >= 5.0)

    def getNotaMedia(self):
        if not self.asignaturas: return 0.0
        return sum(nota for _, nota in self.asignaturas) / len(self.asignaturas) 
    
class Profesor(Persona):
    def __init__(self, apellidos, nombre, dni, fechaNac, nombreAsignatura):
        super().__init__(apellidos, nombre, dni, fechaNac) 
        self.nombreAsignatura = nombreAsignatura 
        self.alumnos = [] 

    def set_nota_alumno(self, dni, nota):
        for alumno in self.alumnos: 
            if alumno.dni == dni: 
                for i, (asig, n) in enumerate(alumno.asignaturas):
                    if asig.nombre == self.nombreAsignatura:
                        alumno.asignaturas[i] = (asig, float(nota))


import csv
from datetime import datetime

def cargar_datos():
    # 1. Cargar Asignaturas
    mapa_asignaturas = {}
    with open('asignaturas.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        for row in reader:
            asig = Asignatura(row['nombre'], row['creditos'], row['curso'], row['cuatrimestre '])
            mapa_asignaturas[row['nombre']] = asig

    # 2. Cargar Alumnos
    mapa_alumnos = {}
    with open('alumnos.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        for row in reader:
            # Formato fecha: 2002-05-20 [cite: 37]
            f_nac = datetime.strptime(row['fechaNac'].strip(), '%Y-%m-%d').date()
            alum = Alumno(row['apellidos'], row['nombre'], row['dni'], f_nac, row['grupo '])
            mapa_alumnos[row['dni']] = alum

    # 3. Cargar Notas y vincularlas a los Alumnos [cite: 38]
    with open('notas.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        for row in reader:
            dni = row['dni_alumno']
            nom_asig = row['nombre_asignatura']
            nota = float(row['nota '])
            
            if dni in mapa_alumnos and nom_asig in mapa_asignaturas:
                mapa_alumnos[dni].asignaturas.append((mapa_asignaturas[nom_asig], nota))

    return mapa_asignaturas, mapa_alumnos


# Ejecución del programa
if __name__ == "__main__":
    asignaturas, alumnos = cargar_datos()

    # Crear un profesor de ejemplo (por ejemplo, de Física) con todos los alumnos 
    profesor = Profesor("Einstein", "Albert", "00000000X", date(1879, 3, 14), "Física")
    profesor.alumnos = list(alumnos.values()) 

    print(f"Listado de alumnos para el profesor de {profesor.nombreAsignatura}:")
    print("-" * 60)
    
    # Mostrar listado [cite: 85]
    for alum in profesor.alumnos:
        print(f"Alumno: {alum.nombre} {alum.apellidos}")
        print(f"  - Nota Media: {alum.getNotaMedia():.2f}")
        print(f"  - Créditos Superados (>5): {alum.getNúmeroCreditosSuperados()}")
        print("-" * 30)