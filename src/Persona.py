from datetime import date, datetime

class Persona:
    def __init__(self, apellidos, nombre, dni, fechaNac):
        self.apellidos = apellidos 
        self.nombre = nombre 
        self.dni = dni 
        self.fechaNac = fechaNac 

    def getEdad(self):
        hoy = date.today()
        return hoy.year - self.fechaNac.year - ((hoy.month, hoy.day) < (self.fechaNac.month, self.fechaNac.day)) 