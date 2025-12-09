'''
Implementa una calculadora con las operaciones de suma(+), resta(-), multiplicación(*) y division(/).
El programa ofrecera un menu con las operaciones disponibles y pedira al usuario que introduzca
una opcion. A continuacion, pedira dos numeros y efectuara la operacion requerida.
'''


class Calculadora:
    """Clase que implementa las operaciones básicas de una calculadora"""
    
    def suma(self, num1, num2):
        """
        Realiza la suma de dos números
        
        Args:
            num1 (float): Primer número
            num2 (float): Segundo número
        
        Returns:
            float: Resultado de la suma
        """
        return num1 + num2
    
    def resta(self, num1, num2):
        """
        Realiza la resta de dos números
        
        Args:
            num1 (float): Primer número
            num2 (float): Segundo número
        
        Returns:
            float: Resultado de la resta
        """
        return num1 - num2
    
    def multiplicacion(self, num1, num2):
        """
        Realiza la multiplicación de dos números
        
        Args:
            num1 (float): Primer número
            num2 (float): Segundo número
        
        Returns:
            float: Resultado de la multiplicación
        """
        return num1 * num2
    
    def division(self, num1, num2):
        """
        Realiza la división de dos números
        
        Args:
            num1 (float): Primer número (dividendo)
            num2 (float): Segundo número (divisor)
        
        Returns:
            float: Resultado de la división
        
        Raises:
            ZeroDivisionError: Si el divisor es cero
        """
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return num1 / num2