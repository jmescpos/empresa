from unittest import TestCase
from mockito import *
from Empleado import *
from Departamento import *

__author__ = 'Juanma'


class TestDepartamento(TestCase):
    def test_get_salario_total(self):

        e1 = mock(empleado)
        e2 = mock(empleado)
        e3 = mock(empleado)

        when(e1).get_salario().thenReturn(700)
        when(e2).get_salario().thenReturn(800)
        when(e3).get_salario().thenReturn(1200)

        d = departamento("Informatica",1)

        d.aniadir_empleado(e1)
        d.aniadir_empleado(e2)
        d.aniadir_empleado(e3)

        totalSalario = d.get_salario_total()

        self.assertNotEquals(totalSalario,2700)
        self.assertEqual(totalSalario, 2700)
        self.assertGreater(totalSalario, 1)
        self.assertLess(totalSalario, 1)