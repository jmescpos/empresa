__author__ = 'Juanma'

class empleado():
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        self.nombre = nombre
        self.apellido = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario


    def get_salario(self):
        return self.salario

    def get_dni(self):
        return self.dni

    def get_nombre_apellidos(self):
        return self.nombre + ' ' + self.apellidos

