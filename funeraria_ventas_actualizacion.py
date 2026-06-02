# sistema de ventas funeraria los angeles
# ahora con registro de usuarios y modificaciones!!
# =============================================
# BLOQUE 1 - base de datos, crear cuenta y login
# menu con while True para iniciar sesion,
# registrarse, modificar usuario o salir
#
# FUNCIONES DE ESTE BLOQUE:
# - opcion 1: iniciar sesion con usuario y clave
# - opcion 2: registrar cuenta nueva
# - opcion 3: modificar usuario (nombre, clave o ambos)
# - opcion 4: salir del sistema
# =============================================

usuarios = {
    "Jose": "2026"   # Jose puede entrar sin registrarse
}

print("Bienvenido al Sistema de ventas 'Funeraria Los Angeles'")
print("------------------------------------------------------")
print("Sistema de acceso restringido.\n")

usuario_activo = ""   # aqui guardo quien entro al sistema

while True:
    print("""
========= FUNERARIA LOS ANGELES =========
        1. INICIAR SESION
        2. REGISTRARSE
        3. MODIFICAR USUARIO
        4. SALIR
==========================================""")

    opcion = input("Seleccione una opcion: ").strip()

    # ---- opcion 1: iniciar sesion ----
    # busca el usuario en el diccionario y compara la clave
    # si coincide guarda el nombre en usuario_activo y rompe el while con break
    if opcion == "1":
        print("\n---INICIO DE SESION---")
        usuario = input("Ingrese su usuario: ").strip()
        clave = input("Ingrese la contraseña: ").strip()

        if usuario in usuarios and usuarios[usuario] == clave:
            print(f"\nAcceso Permitido!! Bienvenido {usuario}")
            usuario_activo = usuario
            break   # sale del while y entra al menu principal
        else:
            print("Usuario o contraseña incorrectos, intenta de nuevo")

    # ---- opcion 2: registrarse ----
    # verifica que el nombre no exista antes de guardarlo
    # si ya existe avisa, si no existe lo agrega al diccionario usuarios
    elif opcion == "2":
        print("\n---REGISTRO DE USUARIO---")
        nuevo_usuario = input("Cree su nombre de usuario: ").strip()

        if nuevo_usuario in usuarios:
            print(f"El usuario '{nuevo_usuario}' ya existe, intenta con otro nombre")
        else:
            nueva_clave = input("Cree su contraseña: ").strip()
            usuarios[nuevo_usuario] = nueva_clave   # guardo la cuenta nueva en el diccionario
            print("Registro completado con exito! Ya puedes iniciar sesion")

    # ---- opcion 3: modificar usuario ----
    # permite cambiar nombre (a), contraseña (b) o ambos (c)
    # pide el nombre y clave del usuario como verificacion de seguridad
    # para cambiar nombre: borra el registro viejo con del y crea uno nuevo
    # nombre_buscar se actualiza cuando se elige c para que el cambio de
    #   contraseña apunte al nombre nuevo y no falle
    elif opcion == "3":
        print("\n---MODIFICAR USUARIO---")
        nombre_buscar = input("Ingresa el usuario que deseas modificar: ").strip()

        if nombre_buscar not in usuarios:
            print(f"El usuario '{nombre_buscar}' no existe")
        else:
            clave_confirm = input("Ingresa la contraseña del usuario: ").strip()

            if clave_confirm != usuarios[nombre_buscar]:
                print("Contraseña incorrecta, no se puede modificar")
            else:
                print(f"\nUsuario encontrado: {nombre_buscar}")
                print("Que deseas modificar?")
                print("  a - Cambiar nombre de usuario")
                print("  b - Cambiar contraseña")
                print("  c - Ambos")

                cambio = input("Opcion: ").strip().lower()

                # cambia el nombre: borra el registro viejo y crea uno nuevo con la misma clave
                if cambio == "a" or cambio == "c":
                    nuevo_nombre = input("Nuevo nombre de usuario: ").strip()

                    if nuevo_nombre in usuarios:
                        print(f"El usuario '{nuevo_nombre}' ya existe, elige otro nombre")
                    else:
                        clave_guardada = usuarios[nombre_buscar]   # guardo la clave antes de borrar
                        del usuarios[nombre_buscar]                # elimino el registro viejo
                        usuarios[nuevo_nombre] = clave_guardada    # creo el registro con nombre nuevo
                        nombre_buscar = nuevo_nombre               # actualizo para que opcion b funcione si es c
                        print(f"Nombre cambiado a '{nuevo_nombre}' correctamente!")

                # cambia la contraseña: reemplaza la clave en el diccionario
                if cambio == "b" or cambio == "c":
                    nueva_clave = input("Nueva contraseña: ").strip()
                    usuarios[nombre_buscar] = nueva_clave   # reemplazo la clave en el diccionario
                    print("Contraseña cambiada correctamente!")

                if cambio not in ("a", "b", "c"):
                    print("Opcion invalida, no se hizo ningun cambio")

    # ---- opcion 4: salir ----
    # exit() cierra el programa completo desde el menu de acceso
    elif opcion == "4":
        print("Saliendo del sistema...")
        exit()

    else:
        print("Opcion incorrecta, intente nuevamente")


# =============================================
# BLOQUE 2 - menu principal con while True
# el menu no se cierra hasta que escribas SALIR
#
# OPCIONES DEL MENU PRINCIPAL:
# - opcion 1: registrar venta nueva
# - opcion 2: ver todas las ventas del dia
# - opcion 3: ver reporte y total recaudado
# - opcion 4: modificar una venta existente
# - opcion 5: modificar usuario ya dentro del sistema
# - SALIR: cerrar el programa
# =============================================

ventas = []  # lista vacia donde voy a guardar las ventas
total = 0    # empieza en 0 porque todavia no hay ventas

while True:

    print("\n=== MENU PRINCIPAL ===")
    print("1 - Registrar venta")
    print("2 - Ver ventas del dia")
    print("3 - Ver total recaudado")
    print("4 - Modificar venta")
    print("5 - Modificar mi usuario")
    print("SALIR - cerrar el programa")

    # BLOQUE 3 - limpieza de datos
    # .strip() quita espacios al inicio y al final
    # .lower() convierte a minusculas para evitar errores por mayusculas
    opcion = input("\nQue deseas hacer?: ").strip().lower()


    # BLOQUE 4 - registrar venta
    # pide nombre del cliente, servicio y precio
    # guarda cada venta como diccionario dentro de la lista ventas
    # append() agrega el diccionario al final de la lista
    # try/except atrapa el error si el precio no es numero
    # += suma el precio nuevo al total acumulado
    if opcion == "1":
        cliente = input("Nombre del cliente: ").strip()
        servicio = input("Servicio vendido: ").strip()

        try:
            precio = int(input("Precio del servicio: $"))

            # cada venta es un diccionario con tres datos: cliente, servicio y precio
            ventas.append({"cliente": cliente, "servicio": servicio, "precio": precio})

            total += precio  # sumo el precio al total acumulado
            print("Venta registrada correctamente!!")

        except ValueError:
            # esto pasa si el usuario escribe letras donde va un numero
            print("El precio debe ser un numero, intentalo de nuevo")


    # BLOQUE 5 - ver ventas del dia
    # recorre la lista ventas con for y muestra cada registro
    # enumerate() agrega un contador desde 1 para numerar las ventas
    # slicing [:10] recorta el nombre del cliente si es muy largo
    elif opcion == "2":

        if len(ventas) == 0:
            print("No hay ventas registradas todavia")

        else:
            print("\n-- Ventas del dia --")
            for i, v in enumerate(ventas, 1):
                nombre = v["cliente"][:10]  # slicing: solo los primeros 10 caracteres
                print(f"  {i}. {nombre} | {v['servicio']} | ${v['precio']}")


    # BLOQUE 6 - ver total recaudado
    # muestra un reporte con datos del usuario activo y todas las ventas
    # ventas[-1] accede al ultimo elemento de la lista
    # .replace() cambia los guiones por espacios en el nombre del servicio
    # comillas triples permiten escribir el reporte en varias lineas
    elif opcion == "3":

        ultimo = "ninguno"
        if len(ventas) > 0:
            ultimo = ventas[-1]["servicio"].replace("-", " ")  # cambia guiones por espacios

        reporte = f"""
==============================
   REPORTE DE VENTAS
   Usuario:           {usuario_activo}
   Ventas realizadas: {len(ventas)}
   Ultimo servicio:   {ultimo}
   Total recaudado:   ${total}
=============================="""
        print(reporte)


    # BLOQUE 7 - modificar venta
    # muestra la lista numerada para elegir cual venta tocar
    # permite cambiar el servicio (a), el precio (b) o ambos (c)
    # venta = ventas[num - 1] guarda una referencia directa al diccionario
    #   entonces modificar venta["precio"] cambia el dato dentro de la lista
    # al cambiar precio usa total - precio_viejo + nuevo_precio
    #   para recalcular sin descuadrar el acumulado
    elif opcion == "4":

        if len(ventas) == 0:
            print("No hay ventas registradas todavia")

        else:
            print("\n-- Selecciona la venta a modificar --")
            for i, v in enumerate(ventas, 1):
                nombre = v["cliente"][:10]
                print(f"  {i}. {nombre} | {v['servicio']} | ${v['precio']}")

            try:
                num = int(input("\nNumero de venta a modificar: "))

                # verifico que el numero este dentro del rango valido de la lista
                if num < 1 or num > len(ventas):
                    print("Numero invalido, intenta de nuevo")

                else:
                    venta = ventas[num - 1]  # -1 porque las listas empiezan en indice 0

                    print(f"\nVenta actual: {venta['cliente']} | {venta['servicio']} | ${venta['precio']}")
                    print("Que deseas modificar?")
                    print("  a - Nombre del servicio")
                    print("  b - Precio")
                    print("  c - Ambos")

                    cambio = input("Opcion: ").strip().lower()

                    # si elige a o c modifica el nombre del servicio en el diccionario
                    if cambio == "a" or cambio == "c":
                        nuevo_servicio = input("Nuevo nombre del servicio: ").strip()
                        venta["servicio"] = nuevo_servicio

                    # si elige b o c modifica el precio y recalcula el total
                    if cambio == "b" or cambio == "c":
                        try:
                            precio_viejo = venta["precio"]   # guardo el precio anterior para restar del total
                            nuevo_precio = int(input("Nuevo precio: $"))
                            venta["precio"] = nuevo_precio
                            total = total - precio_viejo + nuevo_precio  # recalculo sin descuadrar el total
                        except ValueError:
                            print("El precio debe ser un numero")

                    if cambio in ("a", "b", "c"):
                        print("Venta modificada correctamente!")
                    else:
                        print("Opcion invalida, no se hizo ningun cambio")

            except ValueError:
                print("Debes escribir un numero")


    # BLOQUE 8 - modificar usuario dentro del menu principal
    # permite cambiar nombre (a), contraseña (b) o ambos (c) estando ya dentro
    # para cambiar nombre: borra el registro viejo con del y crea uno nuevo
    #   luego actualiza usuario_activo para que el reporte muestre el nombre correcto
    # para cambiar contraseña: pide la clave actual como verificacion de seguridad
    #   si no coincide no realiza ningun cambio
    # nombre_buscar se actualiza al cambiar nombre para que opcion c no falle
    elif opcion == "5":

        print(f"\n--- MODIFICAR USUARIO ---")
        print(f"Usuario actual: {usuario_activo}")
        print("Que deseas modificar?")
        print("  a - Cambiar nombre de usuario")
        print("  b - Cambiar contraseña")
        print("  c - Ambos")

        cambio_usuario = input("Opcion: ").strip().lower()

        # cambia el nombre: borra el registro viejo y crea uno nuevo con la misma clave
        if cambio_usuario == "a" or cambio_usuario == "c":
            nuevo_nombre = input("Nuevo nombre de usuario: ").strip()

            if nuevo_nombre in usuarios:
                print(f"El usuario '{nuevo_nombre}' ya existe, elige otro nombre")
            else:
                clave_actual = usuarios[usuario_activo]   # guardo la clave antes de borrar
                del usuarios[usuario_activo]              # elimino el registro viejo del diccionario
                usuarios[nuevo_nombre] = clave_actual     # creo el registro nuevo con el nombre cambiado
                usuario_activo = nuevo_nombre             # actualizo la variable con el nombre nuevo
                print(f"Nombre cambiado correctamente! Ahora eres '{usuario_activo}'")

        # cambia la contraseña: verifica la clave actual antes de permitir el cambio
        if cambio_usuario == "b" or cambio_usuario == "c":
            clave_verificacion = input("Ingresa tu contraseña actual para confirmar: ").strip()

            if clave_verificacion != usuarios[usuario_activo]:
                print("Contraseña incorrecta, no se realizaron cambios")
            else:
                nueva_clave = input("Nueva contraseña: ").strip()
                usuarios[usuario_activo] = nueva_clave   # reemplazo la clave en el diccionario
                print("Contraseña cambiada correctamente!")

        if cambio_usuario not in ("a", "b", "c"):
            print("Opcion invalida, no se hizo ningun cambio")


    # BLOQUE 9 - salir del programa
    # break rompe el while True y termina el programa mostrando despedida
    elif opcion == "salir":
        print(f"\nHasta luego {usuario_activo}! - Funeraria Los Angeles")
        break

    else:
        print("Opcion incorrecta, escribe 1, 2, 3, 4, 5 o SALIR")

# fin del programa :)

