# Esta será la función principal desde donde se llamará a las demás funciones mediante la importación de las mismas
from suma import suma
from resta import resta
from producto import producto
from division import division

#   Declaramos una variable global resultado
resultado = None    #   Le puse None por el momento ya que no se que tipo de dato almacenará aún

#   A continuación definimos/declaramos la función principal
def calculadora() -> None:
    # Usamos -> None como type hint porque la función calculadora()
    # no devuelve ningún valor con return.
    # Reglas generales de type hints en funciones:
    # 1) Si una función retorna un valor específico, indicamos el tipo de dato.
    # 2) Si una función no devuelve nada (solo ejecuta acciones como imprimir o modificar variables globales), se usa -> None
    global resultado    #   Indicamos que escribiremos sobre la variable global resultado
    
    print('Operaciones disponibles: suma, resta, producto, division.')
    operacion = input('Ingrese la operación a realizar:').strip().lower()
    
    try:
        num1 = float(input('Igresa el primer número: '))
        num2 = float(input('Ingresa el segndo número: '))
        
        if  operacion == 'suma':
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
        
        # Evaluamos si el resultado devuelto es totalmente decimal para imprimirlo como decimal
        # o si es un entero lo imprimimos como entero 
        if resultado % 1 == 0:  
            resultado = int(resultado)  # Si no tiene parte decimal, lo convertimos a entero
        else:
            resultado = resultado  # Si tiene decimales, lo dejamos igual
        # Mostramos el resultado dentro de la función
        print(f'Resultado= {resultado}')

    except ValueError as e:
        print(f'Obtuvimos un error de tipo: {e}')

if __name__ == '__main__':
    calculadora()
    # Una línea a continuación solamete para mostrar el uso de la variable global en la función principal
    print(f'Último resultado almacenado en la variable resultado dentro de la "memoria" de la calculadora: {resultado}')
