__author__ = 'Juanma'


class Empleado():
    """Clase empleado de una empresa"""

    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """Constructor clase empleado.

        Este metodo se encarga de inicializar los diferentes atributos de un objeto empleado
        con los paramatros que se le pasan al llamar al constructor y crear el objeto.

        :param nombre: Nombre del empleado.
        :param apellidos: Apellidos del empleado.
        :param dni: Documento nacional de identificacion del empleado.
        :param direccion: Direccion del empleado.
        :param edad: Edad del empleado.
        :param email: Correo electronico del empleado.
        :param salario: Sueldo del empleado.
        """
        self.nombre = nombre
        self.apellido = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario


    def get_salario(self):
        """Metodo get del atributo salario.

        Este metodo devuelve el salario del empleado que lo invoca.
        :return salario: Devuelve la cantidad en euros del salario del empleado.
        :rtype salario: Float.
        """
        return self.salario

    def get_dni(self):
        """Metodo get del atributo dni.

        Este metodo devuelve el dni del empleado que lo invoca.
        :return dni: Devuelve el documento nacional de identidad del empleado.
        :rtype dni: String."""
        return self.dni

    def get_nombre_apellidos(self):
        """Metodo get que devuelve el atributo nombre y apellido.

        Este metodo devuelve el atributo nombre y apellido concatenados del objeto empleado que lo invoca.Para
        ello se introduce un espacio en blanco en ambos atributos.
        :return nombre_apellido: Devuelve la concatenacion del nombre y el apellido.
        :rtype nombre_apellidos: String."""
        return self.nombre + ' ' + self.apellidos

    def get_edad(self):
        """Metodo get del atributo edad.

        Este metodo devuelve la edad del empleado que lo invoca.
        :return edad: Devuelve la edad del empleado.
        :rtype edad: Int."""
        return self.edad

    def get_email(self):
        """Metodo get del atributo email.

        Este metodo devuelve el email del empleado que lo invoca.
        :return edad: Devuelve el email del empleado.
        :rtype edad: String."""
        return self.email

    def get_direccion(self):
        """Metodo get del atributo direccion.

        Este metodo devuelve la direccion del empleado que lo invoca.
        :return edad: Devuelve la direccion del empleado.
        :rtype edad: String."""
        return self.direccion

    def get_salario_mensual(self):
        """Metodo que devuelve el salario anual.

        Este metodo devuelve el salario mensual multiplicado por 12, es decir lo que
        ganaria el empleado en un anio.
        :return self.salario: Devuelve el salario anual del empleado.
        :rtype self.salario: Float."""
        return self.salario * 12
