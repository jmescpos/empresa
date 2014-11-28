from unittest import TestCase

from mockito import *

from Empleado import *
from Departamento import *


__author__ = 'Juanma'


class TestDepartamento(TestCase):
    """Clase de testeo para los metodos de la clase departamento"""

    def test_get_salario_total_mensual(self):
        """Metodo que comprueba si el salario total de los empleados funciona correctamente.

        Este metodo crea tre objetos mockitos de tipo empleado, inicializa sus atributos de salario y crea unu departamento.
        A continuacion anyade los empleados creados al departamento con el metodo aniadir empleado, y por ultimo utiliza
        el metodo get_salario_total_mensual para calcular el salario total.

        :return self.assertEquals: Devuelve el resultado de la comprobacion entre el metodo total_salario_mensual y el segundo parametro.
        :raise  self.assertEquals: Puede devolver una excepcion si el metodo no hace correctamente el calculo.
        """

        e1 = mock(Empleado)
        e2 = mock(Empleado)
        e3 = mock(Empleado)

        when(e1).get_salario_mensual().thenReturn(1000)
        when(e2).get_salario_mensual().thenReturn(1000)
        when(e3).get_salario_mensual().thenReturn(1000)

        d = Departamento("Informatica", 1)

        d.aniadir_empleado(e1)
        d.aniadir_empleado(e2)
        d.aniadir_empleado(e3)

        total_salario_mensual = d.get_salario_total_mensual()

        self.assertEquals(total_salario_mensual, 36001)