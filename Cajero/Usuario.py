intentos_restantes = 3  # Número de intentos permitidos para ingresar la contraseña

# usuarios: contraseña, saldo inicial y historial de transacciones
usuarios = {"Wilfredo": {"contraseña": "128900", "saldo": 3000, "historial": []},
            "Pedro": {"contraseña": "458379", "saldo": 5200, "historial": []}}  

print("cajero automático")

# Bucle principal para solicitar el nombre de usuario
while intentos_restantes > 0:
    usuario = input("Ingrese su nombre de usuario: ")  # Solicita el nombre de usuario
    if usuario in usuarios:  # Verificar si el usuario existe 

        # Bucle para solicitar la contraseña
        while intentos_restantes > 0:
            contraseña = input("Ingrese su contraseña: ")  # Solicita la contraseña
            if contraseña == usuarios[usuario]["contraseña"]:  # Verificar si la contraseña es correcta
                print("Inicio de sesión exitoso.")
                # Bucle de opciones del cajero automático
                while True:
                    # Mostrar opciones al usuario
                    print("\n1. Retirar")
                    print("2. Depositar")
                    print("3. Realizar una transferencia")
                    print("4. Estado de la cuenta")
                    print("5. Salir")
                    opcion = input("Seleccione una opción: ")  # Solicita opción al usuario
                    
                    # Muestra la opción 1: Retirar dinero
                    if opcion == "1":
                        print("\nOpciones de retiro:")
                        print("1) Q100")
                        print("2) Q300")
                        print("3) Q500")
                        print("4) Otra cantidad")
                        print("5) Consultar saldo")
                        retiro_opcion = input("Seleccione una opción de retiro: ")
                        
                        if retiro_opcion == "1":
                            monto = 100
                        elif retiro_opcion == "2":
                            monto = 300
                        elif retiro_opcion == "3":
                            monto = 500
                        elif retiro_opcion == "4":
                            monto = float(input("Ingrese la cantidad a retirar: "))
                            if monto > usuarios[usuario]["saldo"]:
                                print("La cantidad ingresada es mayor que su saldo.")
                                print("Su saldo es de:", usuarios[usuario]["saldo"])
                                continue
                        elif retiro_opcion == "5":
                            print("Saldo actual:", usuarios[usuario]["saldo"])
                            continue
                        else:
                            print("Opción no válida.")
                            continue
                        
                        if monto <= usuarios[usuario]["saldo"]:  # Verifica si el saldo es suficiente
                            usuarios[usuario]["saldo"] -= monto  # Actualiza el  saldo
                            usuarios[usuario]["historial"].append(f"Retiro: -Q{monto}")  # Registra la transacción en el historial
                            print("Retiro exitoso.")  # Muestra el  mensaje de retiro exitoso
                        else:
                            print("Saldo insuficiente.")
                    
                    #Muestra la  opción 2: Depositar dinero
                    elif opcion == "2":
                        destinatario = input("Ingrese el nombre de usuario al que desea depositar: ")
                        if destinatario in usuarios:  # Verifica si el destinatario existe
                            monto = float(input(f"Ingrese el monto a depositar en la cuenta de {destinatario}: "))  # Solicita monto a depositar
                            usuarios[destinatario]["saldo"] += monto  # Actualiza el  saldo del destinatario
                            usuarios[destinatario]["historial"].append(f"Depósito: +Q{monto}")  # Registra la transacción en el historial del destinatario
                            print(f"Depósito exitoso en la cuenta de {destinatario}.")  # Muestra el  mensaje de depósito exitoso
                        else:
                            print("Usuario destinatario no encontrado.")  # Muestra el  mensaje de destinatario no encontrado
                    
                    #Muestra la opción 3: Realizar una transferencia
                    elif opcion == "3":
                        destinatario = input("Ingrese el nombre de usuario del destinatario: ")  # Solicita al destinatario
                        if destinatario in usuarios:  # Verifica si el destinatario existe
                            monto = float(input("Ingrese el monto a transferir: "))  # Solicita el monto a transferir
                            if monto <= usuarios[usuario]["saldo"]:  # Verifica si el saldo es suficiente
                                usuarios[usuario]["saldo"] -= monto  # Actualiza el saldo del remitente
                                usuarios[destinatario]["saldo"] += monto  # Actualiza el saldo del destinatario
                                usuarios[usuario]["historial"].append(f"Transferencia: -Q{monto} hacia {destinatario}")  # Registra la transacción en el historial del remitente
                                usuarios[destinatario]["historial"].append(f"Transferencia: +Q{monto} desde {usuario}")  # Registra la transacción en el historial del destinatario
                                print("Transferencia exitosa.")  #Muestra el mensaje de transferencia exitosa
                            else:
                                print("Saldo insuficiente.")  #Muestra el  mensaje de saldo insuficiente
                        else:
                            print("Usuario destinatario no encontrado.")  # Muestra el  mensaje de destinatario no encontrado
                    
                    #Muestra la  opción 4: Estado de la cuenta
                    elif opcion == "4":
                        print("Saldo actual:", usuarios[usuario]["saldo"])  # Muestra el saldo actual del usuario
                        print("Historial de transacciones:")
                        for transaccion in usuarios[usuario]["historial"]:  # Muestra el historial de transacciones del usuario
                            print(transaccion)
                    
                    # Muestra la opción 5: Salir
                    elif opcion == "5":
                        print("Gracias por utilizar nuestro cajero automático.")  # Muestra el mensaje de despedida
                        break  # Sale del bucle de opciones del cajero automático
                    
                    else:
                        print("Opción no válida. Inténtelo de nuevo.")  # Muestra el mensaje de opción no válida
                break  # Sale del bucle para solicitar la contraseña
            else:
                print("Contraseña incorrecta.")
                intentos_restantes -= 1
                if intentos_restantes == 0:
                    print("Se han agotado los intentos. Se ha bloqueado la cuenta")
                    break  # Sale del bucle para solicitar la contraseña
    else:
        print("Usuario no encontrado.")
        intentos_restantes -= 1
        if intentos_restantes == 0:
            print("Se han agotado los intentos. Por favor, vuelva a intentarlo más tarde.")
            break  # Sale del bucle principal