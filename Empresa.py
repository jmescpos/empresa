__author__ = 'Juanma'

class Empresa():
    """Clase empleado de una empresa"""
    def __init__(self, nombre_empresa, cif, razon_social):
        """Metodo constructor de la clase empresa

        Este metodo se encarga de inicializar los diferentes atributos de un objeto empresa
        ademas de crear una lista de departamentos vacia.

        :param nombre_empresa: Es el nombre que tendra la empresa.
        :param cif: Es el identificador fiscal de la empresa(CIF).
        :param razon_social: Es un nombre por el que se conoce a una empresa la publico en general.
        :type nombre_empresa: String.
        :type cif: String.
        :type razon_social: String.
        """
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.listaDepartamentos = []

