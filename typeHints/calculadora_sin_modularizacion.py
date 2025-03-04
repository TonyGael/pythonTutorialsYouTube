# Calculadora con las operaciones: suma, resta, producto y división

# Función para sumar dos números
def suma(num1: float, num2: float) -> float:
    '''Recibe dos números y retorna su suma.'''
    resultado = num1 + num2
    return resultado

# Función para restar dos números
def resta(num1: float, num2: float) -> float:
    '''Recibe dos números y retorna su resta.'''
    resultado = num1 - num2
    return resultado

# Función para multiplicar dos números
def producto(num1: float, num2: float) -> float:
    '''Recibe dos números y retorna su producto.'''
    resultado = num1 * num2
    return resultado

# Función para dividir dos números
def division(num1: float, num2: float) -> float:
    '''Recibe dos números y retorna su división. Maneja división por cero.'''
    if num2 == 0:
        print('No se puede realizar división por cero.')
        return 0

    resultado = num1 / num2

    # Comprobamos si el resultado es un número entero o decimal
    return int(resultado) if resultado.is_integer() else resultado

# Variable global para almacenar el último resultado
resultado = None

# Función principal de la calculadora
def calculadora() -> None:
    '''Función principal que gestiona la calculadora.''' 
    global resultado

    print('Operaciones disponibles: suma, resta, producto, división.')
    operacion = input('Ingrese la operación a realizar: ').strip().lower()

    try:
        num1 = float(input('Ingresa el primer número: '))
        num2 = float(input('Ingresa el segundo número: '))

        if operacion == 'suma':
            resultado = suma(num1, num2)
        elif operacion == 'resta':
            resultado = resta(num1, num2)
        elif operacion == 'producto':
            resultado = producto(num1, num2)
        elif operacion == 'division':
            resultado = division(num1, num2)
        else:
            print('Operación no válida!')
            return

        # Imprimimos el resultado, adaptando el formato si es un entero
        print(f'Resultado = {resultado}')

    except ValueError as e:
        print(f'Error de entrada: {e}')

if __name__ == '__main__':
    calculadora()
    print(f'Último resultado almacenado en memoria: {resultado}')
