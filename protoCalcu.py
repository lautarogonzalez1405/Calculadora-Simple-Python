from colorama import Fore, Style

print('Bienvenido a este prototipo de calculadora simple.')


def calculadora():
    
    historial = []

    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else None,
        '%': lambda a, b: a * b / 100,
    }

    while True:
        print(Fore.RED + "ATENCION: Si es tu primera vez usando la calculadora, selecciona la opcion de Instrucciones")
        print(Fore.MAGENTA + """
            ======== MENU DE CALCULADORA =========
            1. Realizar operaciones
            2. Instrucciones
            3. Historial
            4. Salir
            ======================================""" + Style.RESET_ALL)

        opcion = input("Elija una opcion: ").strip()

        if opcion == '1':

            print('Modo operaciones activado. Escribe "atras" para volver al menu.')

            while True:
                operacion = input('Ingresa tu opearacion: ')

                if operacion.lower() == 'atras':
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
                        historial.append(f'{operacion} = {resultado}')

                except ValueError:
                    print("Error: debes ingresar numeros validos")
        
        elif opcion == '2':
            print("En este prototipo de calculadora podras realizar operaciones como: Suma, Resta, Multiplicacion, Division y Porcentaje")
            print("\nLa forma de realizar una operacion es: 'numero' 'operador' 'numero'")
            print("CUIDADO: Si no respetas la formalizacion o introducis un operador no valido se mostrara un error en pantalla\n")
            print("Si deseas calcular un porcentaje tambien es de la misma forma, siendo el primer numero la base y el segundo numero la cantidad de porcentaje deseada")
        
        elif opcion == '3':
            print('Mostrando el historial de operaciones: ')
            for o in historial:
                print(o)

        elif opcion == '4':
            print("Gracias por usar la calculadora, hasta luego")
            break
        
        else:
            print(Fore.RED + "Opcion invalida. Intente de nuevo." + Style.RESET_ALL)
if __name__ == "__main__":
    calculadora()