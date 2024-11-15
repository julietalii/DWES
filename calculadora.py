from operaciones import suma, resta, multiplicacion, division


while True:
    # Solicita dos números al usuario
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    # Solicita el tipo de operación
    print("\nSelecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = input("Introduce el número de la operación deseada: ")

    # Realiza la operación seleccionada
    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultado:", division(num1, num2))
    else:
        print("Opción no válida.")

    # Pregunta si el usuario quiere continuar
    continuar = input("\n¿Quieres realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
        print("Gracias por usar la calculadora.")
        break

