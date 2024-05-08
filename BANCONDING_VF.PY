
# ----V4.2
# crear Cdt -> En progreso
# Se agregaron funciones - ganancia, impuestom ganancia_final para rellenar cdt
# ----V4.3
# Menu Admin. (Completado)
# Monto total de todas las cuentas de ahorros. (Completado)
# Total ganancias CDT.(Falta)
# estado cdt ->(completado) (muestra la lista de cdts-> se le puede meter cariño)

# El menu tiene un while ahora hay que darle salir-> (Completado)

# ---v4.4
# imprimirle al admin  la suma de todos los cdts-> (FALTA)
# se creo la opcion salir para romper el codigo-> (LISTO)
# hacer el sistema de transferencias-> (FALTA)
# al crear un usuario se esta mostrando un mensaje de verificacion-> (LISTO)
# si no tengo un cdt debe ,ostrar un mensaje advirtiendo que este usuario no tie3nen ningun cdt-> (FALTA)
# si el usuario ingresa un numero que no esta entre las opciones se le advierte con un mensaje-> (LISTO)

# ---v4.5
# Hacer el sistema de transferencias-> (FALTA)


# Crear nuevo cdt -> ()
#       -> linea 265 "plazo" si se pone un numero diferente se rompe el codigo(FALTA)
#       -> Verificar que tiene el saldo para hacerlo para que no quede en numero negativo(LISTO)
#       -> Tiene que tener minimo 500000 de saldo para dejarle hacer el cdt(LISTO)
#       -> Monto para crear CDT 500.000 (LISTO)
# Ahora se puede ver la cantidad de cdts ->(LISTO) (Agrege un contador a el diccionario/objeto json para contar cada vez que se agrege un cdt)
# imprimirle al admin  la suma de todos los cdts-> (LISTO)
# menu admin cualquier opción daba mensaje de que "opción no valida" (CORREGIDO)
# Simular CDT tiene que ser minimo de 500000 (CORREGIDO)
# si no tengo un cdt debe ,ostrar un mensaje advirtiendo que este usuario no tie3nen ningun cdt-> (LISTO)
# ---v4.9
# Hacer el sistema de transferencias-> (LISTO)
# Ya no se rompe en el inicio (CORREGIDO)
# En la parte de crear cdt en la parte donde se escoje el plazo se rompe si se escoje otra opción(CORREGIDO)

import random


def cdt_simulador(f_monto, f_plazo):

    if f_plazo == 1:
        interes = 1.063
        meses = 3
    elif f_plazo == 2:
        interes = 1.085
        meses = 6
    elif f_plazo == 3:
        interes = 1.113
        meses = 9
    elif f_plazo == 4:
        interes = 1.149
        meses = 12

    resultado1 = f_monto*interes
    resultado2 = resultado1-f_monto
    resultado3 = (resultado2*meses)/12
    resultado4 = resultado3*0.04
    resultado5 = resultado3-resultado4
    return print(f"Cantidad de meses: {meses} Ganancia Neta:{resultado3}$ , impuesto de {resultado4}  ==> Ganancia final: {resultado5}$")


def cdt_ganancia_neta(f_monto, f_plazo):

    if f_plazo == 1:
        interes = 1.063
        meses = 3
    elif f_plazo == 2:
        interes = 1.085
        meses = 6
    elif f_plazo == 3:
        interes = 1.113
        meses = 9
    elif f_plazo == 4:
        interes = 1.149
        meses = 12

    resultado1 = f_monto*interes
    resultado2 = resultado1-f_monto
    resultado3 = (resultado2*meses)/12
    return resultado3


def cdt_ganancia_final(f_monto, f_plazo):

    if f_plazo == 1:
        interes = 1.063
        meses = 3
    elif f_plazo == 2:
        interes = 1.085
        meses = 6
    elif f_plazo == 3:
        interes = 1.113
        meses = 9
    elif f_plazo == 4:
        interes = 1.149
        meses = 12

    resultado1 = f_monto*interes
    resultado2 = resultado1-f_monto
    resultado3 = (resultado2*meses)/12
    resultado4 = resultado3*0.04
    resultado5 = resultado3-resultado4
    return resultado5


def cdt_retencion_fuente(f_monto, f_plazo):

    if f_plazo == 1:
        interes = 1.063
        meses = 3
    elif f_plazo == 2:
        interes = 1.085
        meses = 6
    elif f_plazo == 3:
        interes = 1.113
        meses = 9
    elif f_plazo == 4:
        interes = 1.149
        meses = 12

    resultado1 = f_monto*interes
    resultado2 = resultado1-f_monto
    resultado3 = (resultado2*meses)/12
    resultado4 = resultado3*0.04
    return resultado4


def id_random():
    lista_r = []
    for r in range(0, 1):
        lista_r.append(random.randrange(1000, 9999))
    return sum(lista_r)


def transferir(origen, destino, monto, personas):
    cuenta_origen = None
    cuenta_destino = None

    # Buscar las cuentas de origen y destino en la lista de personas.
    for usuario in personas:
        if usuario["id"] == origen:
            cuenta_origen = usuario
        elif usuario["id"] == destino:
            cuenta_destino = usuario

    # Verificar que se encontraron ambas cuentas.
    if cuenta_origen is None:
        print("La cuenta de origen no existe.")
        # con este return estoy rompiendo la funcion
        return
    elif cuenta_destino is None:
        print("\n\n⚠ No existe una cuenta registrada con este ID  ⚠\n\n")
        # con este return estoy rompiendo la funcion
        return

    # Verificar que hay suficiente saldo en la cuenta de origen.
    if cuenta_origen["saldo_cuenta"] < monto:
        print("\n\n⚠ Usted no posee fondos suficientes para realizar esta acción ⚠\n\n")
        return

    # Realizar la transferencia.
    cuenta_origen["saldo_cuenta"] -= monto
    cuenta_destino["saldo_cuenta"] += monto

    print(f"\n\nTRANSFERENCIA REALIZADA CON EXITO!\n\nMonto transferido: {monto}$\n\n")


usuarios = [
    {
        "nombre": "nombre",
        "edad": 20,
        "usuario": "1",
        'contrasena': "2",
        "id": 0000,
        'saldo_cuenta': 999.0,
        'contador_cdt': 1,
        'cdt': [{
            'monto': 500000.0,
            'plazo': "3 Meses",
            'tasa': "6.3% EA",
            'ganancia_neta': 7875.0,
            'retencion_fuente': 315.0,
            'ganancia_final': 7560.0,
        }]
    },
    {
        'nombre': 'Sebastian M.',
        "edad": 30,
        'usuario': 'sebas',
        'contrasena': 'sebas326',
        "id": 3030,
        'saldo_cuenta': 500000.0,
        'contador_cdt': 1,
        'cdt': [{
            'monto': 500000.0,
            'plazo': "3 Meses",
            'tasa': "6.3% EA",
            'ganancia_neta': 7875.0,
            'retencion_fuente': 315.0,
            'ganancia_final': 7560.0,
        }]
    },
    {
        'nombre': 'Andres',
        "edad": 30,
        'usuario': 'andres326',
        'contrasena': 'andres326',
        "id": 5050,
        'saldo_cuenta': 10000000.0,
        'contador_cdt': 0,
        'cdt': []
    },
    {
        'nombre': 'Jonathan',
        "edad": 30,
        'usuario': 'jona326',
        'contrasena': 'jona326',
        "id": 4050,
        'saldo_cuenta': 500000.0,
        'contador_cdt': 0,
        'cdt': []
    },
    {
        'nombre': 'Mauricio',
        "edad": 30,
        'usuario': 'mauricio326',
        'contrasena': 'mauro326',
        "id": 9090,
        'saldo_cuenta': 1000000.0,
        'contador_cdt': 0,
        'cdt': []

    }
]


i = 0
while i == 0:
    print(" ---------------------------------------------")
    print(f" ========== BIENVENIDO A BANCODING ===========\n           Programamos tus finanzas")
    print(" ---------------------------------------------")
    try:
        login = int(input(
            "Ingrese el numero correspondiente a la opción  que desea elegir por favor:\n1=> Iniciar sesión  en su perfil\n2=> Crear un perfil\n3=> Salir\n "))

        if login == 1:
            usuario_perfil = input("Ingrese su usuario por favor: ").lower()
            contrasena_perfil = input(
                "Ingrese su contraseña por favor: ").lower()
            contrasena_true = False
            usuario_true = False
            admin_valor = 1

            if usuario_perfil == "admin" and contrasena_perfil == "0000":
                # Menu del Admin
                while admin_valor == 1:
                    print("---- ADMIN ----")
                    menu_admin = int(
                        input(f"1=> Total cuentas ahorros\n2=> Total ganancias CDT \n3=> Salir\n=>"))

                    if menu_admin == 1:
                        acumulador_saldos = 0
                        for saldo in usuarios:
                            acumulador_saldos += saldo['saldo_cuenta']
                        print(
                            f"{usuarios}\n\nLa suma total de los saldos de las cuentas de ahorros es de: {acumulador_saldos}$\n\n")

                    elif menu_admin == 2:
                        acumulador_cdts = 0
                        for usuario in usuarios:
                            for cdts in usuario["cdt"]:
                                acumulador_cdts += cdts["ganancia_final"]

                        print("\n\nTotal ganancias CDT", acumulador_cdts, "$\n\n")

                    elif menu_admin == 3:
                        break

                    elif 0 < menu_admin > 4:
                        print("\n\n⚠ Ingrese una opción  válida por favor: \n\n")

            elif usuario_perfil != "admin":
                for usuario in usuarios:
                    if usuario["usuario"] == usuario_perfil:
                        contrasena_true = True
                        usuario_true = True

                        if usuario["contrasena"] == contrasena_perfil:
                            contrasena_true = False
                            menu_perfil_on = 1

                            while menu_perfil_on == 1:
                                print(
                                    " -------------------------------------------------------")
                                print(
                                    "Bienvenido ", usuario["nombre"], "- Número de cuenta: ", usuario["id"])
                                print("Saldo: ", usuario["saldo_cuenta"], "$")
                                print(
                                    " -------------------------------------------------------")
                                menu_perfil = int(input(
                                    "1=> Transferir dinero\n2=> Estado CDTS\n3=> Crear CDT\n4=> Simular CDT\n5=> Salir\n:"))

                                if menu_perfil == 1:
                                    x = usuario["id"]
                                    aquient = int(
                                        input("Ingrese por favor el ID al que desea realizar  la transferencia: "))
                                    cuanto = float(
                                        input("Ingrese la cantidad de dinero que desea transferir: "))
                                    transferencia = transferir(
                                        x, aquient, cuanto, usuarios)

                                elif menu_perfil == 2:
                                    print(
                                        f"\nCantidad de CDTs actual: {usuario['contador_cdt']}")
                                    if usuario['contador_cdt'] > 0:
                                        for cdt in usuario["cdt"]:
                                            print(cdt, "\n")
                                    elif usuario['contador_cdt'] <= 0:
                                        print(
                                            "\n\n⚠ Este usuario no tiene ningún  CDT ⚠\n\n ")

                                elif menu_perfil == 3:

                                    if usuario["saldo_cuenta"] < 500000:
                                        print(
                                            "\n\n⚠ Saldo mínimo   para crear un CDT es de 500.000$ ⚠\n\n")

                                    elif usuario["saldo_cuenta"] >= 500000:
                                        monto_transaccion = float(
                                            input("Ingrese el monto de la inversión  que desea realizar en BANCODING: "))
                                        if monto_transaccion < 500000:
                                            print(
                                                "\n\n⚠ Mínimo  para crear un CDT es de 500.000$⚠\n\n")

                                        elif monto_transaccion >= 500000:
                                            if usuario["saldo_cuenta"] >= monto_transaccion:
                                                x = usuario["saldo_cuenta"] - \
                                                    monto_transaccion
                                                usuario.update(
                                                    {"saldo_cuenta": x})
                                                while True:
                                                    try:
                                                        plazo = int(input("Ingrese el plazo en el cual desea realizar el CDT:\n1=> 3 Meses - 6.3% EA\n2=> 6 Meses - 8.5% EA\n3=> 9 Meses - 11.3% EA\n4=> 12 Meses - 14.9% EA\n"))
                                                        if plazo in [1,2,3,4]:
                                                            break
                                                        else:
                                                            print("\n\n⚠ Opción no válida, intente de nuevo ⚠\n\n")
                                                    except ValueError:
                                                        print("\n\n⚠ Opción no válida, intente de nuevo ⚠\n\n")


                                                if plazo == 1:
                                                    plazo_cdt = "3 Meses"
                                                    ea_taza = "6.3% EA"
                                                elif plazo == 2:
                                                    plazo_cdt = "6 Meses"
                                                    ea_taza = "8.5% EA"
                                                elif plazo == 3:
                                                    plazo_cdt = "9 Meses"
                                                    ea_taza = "11.3% EA"
                                                elif plazo == 4:
                                                    plazo_cdt = "12 Meses"
                                                    ea_taza = "14.9% EA"

                                                ganancia_neta_1 = cdt_ganancia_neta(
                                                    monto_transaccion, plazo)
                                                retencion_fuente_1 = cdt_retencion_fuente(
                                                    monto_transaccion, plazo)
                                                ganancia_final_1 = cdt_ganancia_final(
                                                    monto_transaccion, plazo)

                                                nuevo_cdt = {
                                                    'monto': monto_transaccion,
                                                    'plazo': plazo_cdt,
                                                    'tasa': ea_taza,
                                                    'ganancia_neta': ganancia_neta_1,
                                                    'retencion_fuente': retencion_fuente_1,
                                                    'ganancia_final': ganancia_final_1,
                                                }
                                                usuario["cdt"].append(
                                                    nuevo_cdt)
                                                usuario['contador_cdt'] += 1
                                                print(
                                                    "\n\nCDT creado correctamente!\n\n")

                                                for cdt in usuario["cdt"]:
                                                    print(
                                                        f"Monto: {cdt['monto']}$,Plazo: {cdt['plazo']}, Tasa: {cdt['tasa']},Ganancia final: {cdt['ganancia_final']}$")

                                            elif usuario["saldo_cuenta"] < monto_transaccion:
                                                print(
                                                    "\n⚠ Saldo insuficiente para realizar esta operación ⚠\n")

                                elif menu_perfil == 4:
                                    monto = float(
                                        input("Ingrese el monto con el cual desea simular el CDT: "))
                                    if monto < 500000:
                                        print(
                                            "\n\n⚠ Monto mínimo  para simular un CDT es de 500.000$ ⚠\n\n")
                                    elif monto >= 500000:
                                        simulacion1 = cdt_simulador(monto, 1)
                                        simulacion2 = cdt_simulador(monto, 2)
                                        simulacion3 = cdt_simulador(monto, 3)
                                        simulacion4 = cdt_simulador(monto, 4)
                                elif menu_perfil == 5:
                                    break
                                else:
                                    print(
                                        "\n\n⚠ Ingrese una opción  válida por favor ⚠\n\n")

                if contrasena_true == True:
                    print("\n\n⚠ Contraseña incorrecta ⚠\n\n")
                if usuario_true == False:
                    print("\n\n⚠ El usuario no existe ⚠\n\n")

        elif login == 2:
            nombre = input("Ingrese su nombre por favor: ").lower()
            edad = int(input("Ingrese su edad por favor: "))
            nombre_usuario = input(
                "Ingrese un nombre de usuario por favor: ").lower()
            contrasena = input("Ingrese una contraseña por favor: ").lower()
            monto_inicial = float(
                input("ingrese el monto con el que desea abrir su cuenta(min.$1'000.000):"))
            funcion_id_usuario = id_random()
            id_usuario = int(funcion_id_usuario)
            encontrado_usuario = False

            if monto_inicial < 1000000:
                print("El monto minimo  es : $1'000.000")
                encontrado_usuario = True
            if edad < 18:
                print(" \n\n⚠ Debes de ser mayor de edad para crear un perfil ⚠\n\n")
                encontrado_usuario = True
            elif edad >= 18:
                for usuario in usuarios:
                    if usuario["id"] == id_usuario:
                        funcion_id_usuario = id_random()
                        id_usuario = int(funcion_id_usuario)
                        print("Hay otro usuario con la misma id")
                        encontrado_usuario = True
                        break
                    if usuario["usuario"] == nombre_usuario:
                        print("\n\n ⚠ Este nombre de usuario ya existe ⚠\n\n")
                        encontrado_usuario = True
                        break
            if encontrado_usuario == False:
                usuarios.append(
                    {
                        "nombre": nombre,
                        "edad": edad,
                        "usuario": nombre_usuario,
                        'contrasena': contrasena,
                        "id": id_usuario,
                        'saldo_cuenta': monto_inicial,
                        'contador_cdt': 0,
                        'cdt': []
                    }
                )
                print("\n\nUsuario creado correctamente!\n\n")
        elif login == 3:
            print("┌──────────────────────────────────────────────────────────────────────────────────────────────────┐")
            print("│  Gracias por utilizar la APP de BANCODING, tu banco de confianza donde programamos tus finanzas. │")
            print("└──────────────────────────────────────────────────────────────────────────────────────────────────┘")
            i = 1
        else:
            print("\n\n⚠ Ingrese una opción  válida por favor: \n\n")
    except ValueError:
        print("\n\n⚠ Ingrese un número válido por favor ⚠\n\n")
