from Empleado import *
__author__ = 'Juanma'


class departamento():

    def __init__(self,nombre_depto,d_depto):
        self.nombre_depto = nombre_depto
        self.d_depto = d_depto
        self.listaEmpleados = []

    def aniadir_empleado(self,empleado,):
        self.listaEmpleados.append(empleado)

    def get_salario_total(self):
        cantidad = 0.0
        for empleado in self.listaEmpleados:
            cantidad = cantidad + empleado.get_salario()
        print 'Salario total de empleados:', cantidad
        return cantidad

    def get_nombre_depto(self):
        return self.nombre_depto


    def get_salario_total_mensual(self):
        c = 0.0
        for empleado in self.listaEmpleados:
            c = c + empleado.get_salario_mensual()* 12
        print 'Salario total mensual de empleados:', c
        return c


'''
e1 = empleado("juan","escalante","30225696q","123","25","juanma@gmail",1500)
e2 = empleado("antonio","perez","30225696q","123","25","juanma@gmail",1350.50)
e3 = empleado("pepe","diaz","30225696q","123","25","juanma@gmail",800)
e4 = empleado("luis","postigo","30225696q","123","25","juanma@gmail",725)


d = departamento("Empresa",123)
d.aniadir_empleado(e1)
d.aniadir_empleado(e2)
d.aniadir_empleado(e3)
d.aniadir_empleado(e4)

d.get_salario_total()
'''