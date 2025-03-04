def division(num1: float, num2: float) -> float | int:
    resultado = 0     #   resultado sería una variable loval a la función
    if num2 == 0:
        print('No se puede realizar división por cero.')
    
    resultado = num1 / num2
    
    #   A continuación comprobamos si el resultado es un número entero o decimal para devolver en el formato y tipo adecuado
    if resultado % 1 == 0:
        return int(resultado)   #   Usamos el operador de modulo % para verificar si el resto es 1 o 0.
    else:
        return resultado
