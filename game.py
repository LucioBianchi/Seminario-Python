from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "/", "*"]
# Cantidad de cuentas a resolver
times = 5
# Inicializo cantidad de resultados correctos
cant_correct = 0
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    # En caso de que se ingrese un valor no numérico, se cuenta como incorrecto y se informa
    try:
        result = float(input("resultado: "))
    except ValueError:
        print("Valor no permitido. ", end = '')
    # Imprime si el resultado es correcto
    match operator:
        case "+": 
            correct_result = number_1 + number_2
        case "-": 
            correct_result = number_1 - number_2
        case "*": 
            correct_result = number_1 * number_2
        case "/": 
            if number_2 != 0:
                correct_result = number_1 / number_2
            else:
                print("No es posible la división por cero")
                
    # Imprimo si es correcto o incorrecto
    # Convierto resul, que era un string, a float
    if (result) == (correct_result):
        print("El resultado es correcto")
        # Cuento los casos correctos
        cant_correct += 1
    else: 
        print("El resultado es incorrecto")

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
# Imprime la cantidad de resultados correctos e incorrectos
print(f"Cantidad de resultados correctos: {cant_correct}")
print(f"Cantidad de resultados incorrectos: {times - cant_correct}")
