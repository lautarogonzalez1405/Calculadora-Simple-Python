print('Bienvenido a este prototipo de calculadora simple.')
print('Puedes realizar operaciones básicas como suma, resta, multiplicación y división.')
print('Por favor, ingresa la operación que deseas realizar en el formato: número1 operador número2')
print('Por ejemplo: 3 + 4 o 10 / 2')

def calculadora():

    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else None,
    }

    while True:
        operacion = input('Ingresa tu opearacion (o escribe "salir" para salir de la calculadora): ')
        
        if operacion.lower() == 'salir':
            print("Gracias por usar la calculadora, hasta luego")
            break

        try:
            partes = operacion.split()
            if len(partes) != 3:
                print("Formato invalido. Use: numerador operador numerador")
                continue
            num1, op, num2 = float(partes[0]), partes[1], float(partes[2])

            if op not in operadores:
                print(f"Operador invalido. Usa: {', '.join(operadores.keys())}")
                continue

            resultado = operadores[op](num1, num2)
            if resultado is None:
                print("Error: no se puede dividir entre cero")
            else:
                print(f"Resultado: {resultado}")

        except ValueError:
            print("Error: debes ingresar numeros validos")

if __name__ == "__main__":
    calculadora()