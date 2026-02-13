
import csv
import os
from Asignaturas import Asignatura
from Alumno import Alumno
from Profesor import Profesor
from Persona import Persona

from datetime import datetime,date 

def cargar_datos():
    carpeta = 'csv'

    # 1. Cargar Asignaturas
    mapa_asignaturas = {}
    # os.path.join une la carpeta y el archivo de forma segura ('csv/asignaturas.csv')
    ruta_asignaturas = os.path.join(carpeta, 'asignaturas.csv')
    
    with open(ruta_asignaturas, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        for row in reader:
            asig = Asignatura(row['nombre'], row['creditos'], row['curso'], row['cuatrimestre '])
            mapa_asignaturas[row['nombre']] = asig

    # 2. Cargar Alumnos
    mapa_alumnos = {}
    ruta_alumnos = os.path.join(carpeta, 'alumnos.csv')
    
    with open(ruta_alumnos, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        for row in reader:
            f_nac = datetime.strptime(row['fechaNac'].strip(), '%Y-%m-%d').date()
            alum = Alumno(row['apellidos'], row['nombre'], row['dni'], f_nac, row['grupo '])
            mapa_alumnos[row['dni']] = alum

    # 3. Cargar Notas y vincularlas a los Alumnos 
    ruta_notas = os.path.join(carpeta, 'notas.csv')
    
    with open(ruta_notas, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        for row in reader:
            dni = row['dni_alumno']
            nom_asig = row['nombre_asignatura']
            nota = float(row['nota '])
            
            if dni in mapa_alumnos and nom_asig in mapa_asignaturas:
                mapa_alumnos[dni].asignaturas.append((mapa_asignaturas[nom_asig], nota))

    return mapa_asignaturas, mapa_alumnos



# CODIGO PRINCIPAL
if __name__ == "__main__":
    asignaturas, alumnos = cargar_datos()

    profesor = Profesor("Einstein", "Albert", "00000000X", date(1879, 3, 14), "Física")
    profesor.alumnos = list(alumnos.values())

    print(f"\nListado de alumnos para el profesor de {profesor.nombreAsignatura}:")
    print("-" * 60)
    
    for alum in profesor.alumnos:
        print(f"Alumno: {alum.nombre} {alum.apellidos}")
        print(f"  - Nota Media: {alum.getNotaMedia():.2f}")
        print(f"  - Créditos Superados (>5): {alum.getNúmeroCreditosSuperados()}")
        print("-" * 30)

    # EJECUCIÓN DE LAS NUEVAS FUNCIONES DEL ANEXO

    print("\n" + "=" * 60)
    print("        RESULTADOS DEL ANEXO DE EJERCICIOS")
    print("=" * 60)

    # 1. Top N Alumnos
    n = 3
    top_alumnos = profesor.get_top_n_alumnos(n)
    print(f"\n1. TOP {n} ALUMNOS CON MEJOR NOTA MEDIA:")
    for i, alu in enumerate(top_alumnos, 1):
        print(f"   {i}º) {alu.nombre} {alu.apellidos} - Media: {alu.getNotaMedia():.2f}")

    # 2. Nota media por asignatura
    print("\n2. NOTA MEDIA POR ASIGNATURA:")
    diccionario_medias = profesor.get_medias_por_asignatura()
    for asig_nombre, media in diccionario_medias.items():
        print(f"   - {asig_nombre}: {media:.2f}")

    # 3. Edad media de los alumnos de un curso
    curso_buscar = 1 # Por ejemplo, los de 1º
    edad_media = profesor.get_edad_media_por_curso(curso_buscar)
    print(f"\n3. EDAD MEDIA DE LOS ALUMNOS DE {curso_buscar}º CURSO:")
    print(f"   - {edad_media:.1f} años")

    # 4. Sumar 1 punto a las asignaturas aprobadas
    print("\n4. APLICANDO BONUS (+1 PUNTO) A LOS APROBADOS...")
    
    profesor.aplicar_bonus_aprobados() 
        
    print("   ¡Bonus aplicado correctamente a todos los alumnos!")

    # EXTRA: Comprobación rápida para ver que las medias han subido
    top_alumnos_post = profesor.get_top_n_alumnos(n)
    print(f"\n--> NUEVO TOP {n} ALUMNOS TRAS EL BONUS:")
    for i, alu in enumerate(top_alumnos_post, 1):
        print(f"   {i}º) {alu.nombre} {alu.apellidos} - Media: {alu.getNotaMedia():.2f}")
    print("\n" + "=" * 60 + "\n")
