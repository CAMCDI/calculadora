def calculadora():
    while True:
        print("\nCalculadora Básica")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '5':
            print("Saliendo de la calculadora...")
            break
        
        if opcion not in ('1', '2', '3', '4'):
            print("Opción inválida, intente de nuevo.")
            continue
        
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada inválida, por favor ingrese números válidos.")
            continue
        
        if opcion == '1':
            print(f"Resultado: {num1 + num2}")
        elif opcion == '2':
            print(f"Resultado: {num1 - num2}")
        elif opcion == '3':
            print(f"Resultado: {num1 * num2}")
        elif opcion == '4':
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                print(f"Resultado: {num1 / num2}")

calculadora()