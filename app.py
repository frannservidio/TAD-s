# ===================== Enunciado 3 ====================
# Integrantes: 
#    - DON Antu
#    - GÓMEZ Santiago
#    - GIANELLI Pilar
#    - SERVIDIO Francisco Gabriel

# ===================== LIBRERÍAS ======================
from TADAgenda import *
from TADCita import *
from TADCola import *
from datetime import date, time 

# ===================== VALIDACIONES ===================
def pedir_dni():
    # Valida que el DNI tenga exactamente 8 dígitos numéricos
    while True:
        dni_input = input("Ingrese DNI del paciente (sin puntos): ").strip()
        try:
            dni = int(dni_input)
            if len(dni_input) == 8 and dni > 0:
                return dni
            else:
                print(">>> El DNI debe tener exactamente 8 dígitos y ser un número positivo.")
        except ValueError:
            print(">>> DNI inválido. Ingrese solo números.")

def pedir_telefono():
    # Valida que el teléfono telefónico tenga entre 10 y 13 dígitos
    while True:
        telefono_input = input("Ingrese teléfono del paciente (sin guiones): ").strip()
        try:
            telefono = int(telefono_input)
            if 10 <= len(telefono_input) <= 13 and telefono > 0:
                return telefono
            else:
                print(">>> El teléfono debe tener entre 10 y 13 dígitos")
        except ValueError:
            print(">>> Número inválido. Ingrese solo números.")  

def pedir_fecha(mensaje):   
    # Valida que la fecha esté en formato AAAA-MM-DD        
    while True:
        try:
            fecha_input = input(mensaje).strip()
            return date.fromisoformat(fecha_input)
        except ValueError:
            print(">>> Formato de fecha inválido. Use AAAA-MM-DD.")

def pedir_hora():
    # Valida que la hora esté en formato HH:MM
    while True:
        hora_input = input("Ingrese hora de la cita (HH:MM): ").strip()
        try:
            time.fromisoformat(hora_input)
            return hora_input
        except ValueError:
            print(">>> Hora inválida. Use el formato HH:MM.")

def pedir_nombre():
    # Valida que el nombre no esté vacío y no contenga solo números
    while True:
        try:
            nombre = input("Ingrese nombre del paciente: ").strip()
            if nombre and not nombre.replace(" ", "").isnumeric():
                return " ".join(p.capitalize() for p in nombre.split())
            print(">>> El nombre no puede estar vacío ni ser numérico.")
        except Exception as e:
            print(f">>> Error al ingresar el nombre: {e}")

def pedir_obra_social():
    # Valida que la obra social no esté vacía y no contenga solo números
    while True:
        try:
            obra = input("Ingrese obra social del paciente: ").strip()
            if obra and not obra.replace(" ", "").isnumeric():
                return obra.capitalize()
            print(">>> La obra social no puede estar vacía ni ser numérica.")
        except Exception as e:
            print(f">>> Error al ingresar la obra social: {e}")

# ===================== INICIALIZACIÓN =================
a = crearAgenda()  # Agenda médica
c = crearCola()    # Cola para opción 7
op = 0             # Variable para controlar el menú

# ===================== MENÚ PRINCIPAL ==================
while (op != 8):
    print("""
    === MENÚ DE GESTIÓN DE AGENDA MÉDICA ===
    1 - Registrar nueva cita
    2 - Modificar fecha y hora de una cita por DNI
    3 - Eliminar una cita por DNI
    4 - Mostrar todas las citas
    5 - Mover todas las citas de una fecha a otra
    6 - Eliminar todas las citas por obra social
    7 - Mostrar citas de un día específico
    8 - Salir
    """)

    # Validación de entrada del menú
    try:
        op = int(input("Seleccione una opción: "))
    except ValueError:
        print(">>> Ingrese un número válido.")
        continue

     # ===== OPCIÓN 1: ALTA DE CITA =====
    if (op == 1):
        s = 'S'
        while (s == 'S'):
            cita = crearCita()
            dni = pedir_dni()
            decision = 'S'
            
            # Buscar si ya existe una cita con ese DNI
            datos_encontrados = False
            for i in range(1, tamanioAgenda(a) + 1):
                cita_existente = recuperarCita(a, i)
                if verDNI(cita_existente) == dni:
                    nombre = verNombre(cita_existente)
                    obraSocial = verObraSocial(cita_existente)
                    telefono = verTelefono(cita_existente)
                    datos_encontrados = True
                    print(f"Ya existe una cita registrada para el DNI {dni}:\nNombre: {nombre}\nObra Social: {obraSocial}\nTeléfono: {telefono}")
                    decision = input("¿Desea agregar una nueva cita para este paciente? (S/N): ").strip().upper()
                    break
            
            # Si el usuario no desea agregar una nueva cita, preguntar si desea agregar más
            if decision != 'S':
                print(">>> Operación cancelada. No se registró nueva cita.")
                s = input("¿Desea agregar más citas? (S/N): ").strip().upper()
                continue  
                    
            # Si no se encontró, solicitar los datos
            if not datos_encontrados:
                nombre = pedir_nombre()
                obraSocial = pedir_obra_social()
                telefono = pedir_telefono()

            # Validar fecha y hora sin superponer citas
            while True:
                fecha = pedir_fecha("Ingrese fecha de la cita (AAAA-MM-DD): ")
                hora = pedir_hora()
                existe_conflicto = False

                # Verificar si ya existe una cita con la misma fecha y hora
                for i in range(1, tamanioAgenda(a) + 1):
                    cita_existente = recuperarCita(a, i)
                    if verFecha(cita_existente) == fecha and verHora(cita_existente) == hora:
                        existe_conflicto = True
                        break

                # Si existe conflicto, pedir otra fecha y hora
                if existe_conflicto:
                    print(f">>> Ya existe una cita registrada para la fecha {fecha} y hora {hora}. Ingrese otra.")
                else:
                    break
            
            # Registrar la cita
            cargarCita(cita, dni, nombre, obraSocial, telefono, fecha, hora)
            agregarCita(a, cita)
            print(">>> Cita registrada correctamente.")
            s = input("¿Desea agregar más citas? (S/N):  ").upper()

    # ===== OPCIÓN 2: MODIFICAR CITA =====
    elif (op == 2):
        print("=== MODIFICAR FECHA Y HORA DE UNA CITA ===")
        # Validar si hay citas registradas
        if tamanioAgenda(a) == 0:
            print(">>> No hay citas registradas.")
            continue
        dni = pedir_dni()
        cantidad = 0
        print(f"\nCitas registradas para el DNI {dni}:")
        for i in range(1, tamanioAgenda(a)+1):
            cita = recuperarCita(a, i)
            if verDNI(cita) == dni:
                cantidad += 1
                print(f"{cantidad}) Fecha: {verFecha(cita)} - Hora: {verHora(cita)}")
            
        if cantidad == 0:
            print(">>> No se encontraron citas para ese DNI.")
            continue

        # Seleccionar cuál cita modificar    
        while True:
                try:
                    seleccion = int(input("Seleccione el número de cita que desea modificar: "))
                    if 1 <= seleccion <= cantidad:
                        break
                    else:
                        print(">>> Número de cita inválido. Intente nuevamente.")
                except ValueError:
                    print(">>> Entrada inválida. Ingrese un número.")
        
        contador = 0
        cita_modificar = None
        for i in range(1, tamanioAgenda(a) + 1):
            cita = recuperarCita(a, i)
            if verDNI(cita) == dni:
                contador += 1
                if contador == seleccion:
                    cita_modificar = cita
                    break
        
        # Preguntar qué desea modificar
        while True:
            print("1- Modificar fecha\n2- Modificar hora\n3- Modificar ambas\n0- Cancelar")
            opcion = input("Seleccione una opción: ")

            # Modificar solo la fecha
            if (opcion == "1"):
                nuevaFecha = pedir_fecha("Nueva fecha (AAAA-MM-DD): ")
                conflicto = False
                for i in range(1, tamanioAgenda(a) + 1):
                    otra_cita = recuperarCita(a, i)
                    if otra_cita != cita_modificar and verFecha(otra_cita) == nuevaFecha and verHora(otra_cita) == verHora(cita_modificar):
                        conflicto = True
                        break
                if conflicto:
                    print(">>> Ya existe una cita registrada para esa fecha y hora.")
                else:
                    modFecha(cita_modificar, nuevaFecha)
                    print(">>> Fecha modificada correctamente.")

            # Modificar solo la hora   
            elif opcion == "2":
                nueva_hora = pedir_hora()
                conflicto = False
                for i in range(1, tamanioAgenda(a) + 1):
                    otra_cita = recuperarCita(a, i)
                    if otra_cita != cita_modificar and verFecha(otra_cita) == verFecha(cita_modificar) and verHora(otra_cita) == nueva_hora:
                        conflicto = True
                        break
                if conflicto:
                    print(">>> Ya existe una cita en esa fecha y hora.")
                else:
                    modHora(cita_modificar, nueva_hora)
                    print(">>> Hora modificada correctamente.")

            # Modificar ambas
            elif opcion == "3":
                nueva_fecha = pedir_fecha("Ingrese nueva fecha (AAAA-MM-DD): ")
                nueva_hora = pedir_hora()
                conflicto = False
                for i in range(1, tamanioAgenda(a) + 1):
                    otra_cita = recuperarCita(a, i)
                    if otra_cita != cita_modificar and verFecha(otra_cita) == nueva_fecha and verHora(otra_cita) == nueva_hora:
                        conflicto = True
                        break
                if conflicto:
                    print(">>> Ya existe una cita en esa fecha y hora.")
                else:
                    modFecha(cita_modificar, nueva_fecha)
                    modHora(cita_modificar, nueva_hora)
                    print(">>> Fecha y hora modificadas correctamente.")

            # Cancelar modificación
            elif opcion == "0":
                print(">>> Modificación cancelada.")
                break

            # Opción inválida
            else:
                print(">>> Opción inválida. Intente nuevamente.")

    # ===== OPCIÓN 3: ELIMINAR CITA POR DNI =====
    elif (op == 3):
        print("==== ELIMINAR CITA POR DNI ====")

        if tamanioAgenda(a) == 0:
            print(">>> No hay citas registradas.")
            continue
        
        # Preguntar si desea eliminar una cita
        resp = input("¿Está seguro que desea eliminar una cita? (S/N): ").strip().upper()
        while resp == 'S':
            dni = pedir_dni()
            cantidad = 0

            # Mostrar citas asociadas al DNI
            print(f"\n==== Citas registradas para el DNI {dni}: ====")
            for i in range(1, tamanioAgenda(a) + 1):
                cita = recuperarCita(a, i)
                if verDNI(cita) == dni:
                    cantidad += 1
                    print(f"{cantidad}) Fecha: {verFecha(cita)} - Hora: {verHora(cita)}")

            # Si no hay citas, preguntar si desea intentar con otro DNI
            if cantidad == 0:
                print(">>> No se encontraron citas para ese DNI.")
                resp = input("¿Desea intentar con otro DNI? (S/N): ").strip().upper()
                continue

            # Seleccionar cuál cita eliminar
            while True:
                try:
                    seleccion = int(input("Seleccione el número de la cita que desea eliminar: "))
                    if 1 <= seleccion <= cantidad:
                        break
                    else:
                        print(">>> Número fuera de rango.")
                except ValueError:
                    print(">>> Entrada inválida. Ingrese un número válido.")

            # Recorrer de nuevo para encontrar y eliminar la cita seleccionada
            contador = 0
            for i in range(1, tamanioAgenda(a) + 1):
                cita = recuperarCita(a, i)
                if verDNI(cita) == dni:
                    contador += 1
                    if contador == seleccion:
                        eliminarCita(a, cita)
                        print(">>> Cita eliminada correctamente.")
                        break

            # Preguntar si desea eliminar otra
            resp = input("¿Desea eliminar otra cita? (S/N): ").strip().upper()
    
    # ===== OPCIÓN 4: MOSTRAR TODAS LAS CITAS =====
    elif (op == 4):

        # Validar si hay citas registradas
        if tamanioAgenda(a) == 0:
            print(">>> No hay citas registradas.")
            continue

        # Mostrar todas las citas
        print("========== LISTADO DE CITAS ==========")
        for i in range(1, tamanioAgenda(a)+1):
            rec = recuperarCita(a,i)
            print(f"DNI: {verDNI(rec)}\nNombre: {verNombre(rec)}\nObra Social: {verObraSocial(rec)}\nTeléfono: {verTelefono(rec)}\nFecha: {verFecha(rec)}\nHora: {verHora(rec)}")
            print("===================================")

    # ===== OPCIÓN 5: TRASLADO DE CITAS ENTRE FECHAS =====
    elif (op == 5):            
        print("=== TRASLADO DE CITAS DE UN DÍA A OTRO ===")

        # Validar si hay citas registradas
        if tamanioAgenda(a) == 0:
            print(">>> No hay citas registradas.")
            continue

        # Pedir fecha de origen y destino, asegurando que no sean iguales
        fecha_origen = pedir_fecha("Ingrese la FECHA ORIGINAL de las citas (AAAA-MM-DD): ")
        while True:
            fecha_destino = pedir_fecha("Ingrese la NUEVA FECHA a la que desea trasladar las citas (AAAA-MM-DD): ")
            if fecha_destino != fecha_origen:
                break
            print(">>> La nueva fecha no puede ser igual a la original.")

        # Registrar horas ocupadas en la fecha destino
        horas_ocupadas_destino = []
        for i in range(1, tamanioAgenda(a) + 1):
            cita = recuperarCita(a, i)
            if verFecha(cita) == fecha_destino:
                horas_ocupadas_destino.append(verHora(cita))

        # Recorrer citas en fecha origen e intentar trasladar si no hay conflicto
        trasladadas = 0
        conflictos = []
        for i in range(1, tamanioAgenda(a) + 1):
            cita = recuperarCita(a, i)
            if verFecha(cita) == fecha_origen:
                hora = verHora(cita)
                if hora in horas_ocupadas_destino:
                    conflictos.append((verDNI(cita), hora))
                else:
                    modFecha(cita, fecha_destino)
                    trasladadas += 1
                    horas_ocupadas_destino.append(hora)

        # Mostrar resultados
        if trasladadas > 0:
            print(f"\n{trasladadas} citas fueron trasladadas correctamente de {fecha_origen} a {fecha_destino}.")
        if conflictos:
            print("\n No se trasladaron las siguientes citas por conflicto de horario:")
            for dni, hora in conflictos:
                print(f" - DNI: {dni}, Hora: {hora}")
        if trasladadas == 0 and not conflictos:
            print("\n No se encontraron citas en la fecha original.")
        
    # ===== OPCIÓN 6: ELIMINAR POR OBRA SOCIAL =====
    elif (op == 6):

        # Validar si hay citas registradas
        if tamanioAgenda(a) == 0:
            print(">>> No hay citas registradas.")
            continue
        
        # Pedir obra social y confirmar eliminación
        ob_social = input("Ingrese obra social de las citas a eliminar: ").strip().capitalize()

        confirmar = input(f"¿Está seguro que desea eliminar TODAS las citas con obra social '{ob_social}'? (S/N): ").strip().upper()
        if confirmar != 'S':
            print("Operación cancelada.")
            continue
        
        # Recorrer la agenda y eliminar citas con la obra social indicada
        i = 1
        encontrado = False
        while i <= tamanioAgenda(a):
            rec = recuperarCita(a, i)
            if verObraSocial(rec).capitalize() == ob_social:
                eliminarCita(a, rec)
                encontrado = True
            else:
                i += 1

        # Mostrar resultado de la eliminación
        if not encontrado:
            print(f">>> No se encontraron citas con la obra social '{ob_social}'.")
        else:
            print(f">>> Todas las citas con obra social '{ob_social}' fueron eliminadas.")

    # ===== OPCIÓN 7: MOSTRAR CITAS DE UN DÍA =====
    elif (op == 7):

        # Validar si hay citas registradas
        if tamanioAgenda(a) == 0:
            print(">>> No hay citas registradas.")
            continue

        # Pedir fecha y mostrar citas
        fecha = pedir_fecha("Ingrese fecha de las citas a mostrar (AAAA-MM-DD): ")
        for i in range(1, tamanioAgenda(a)+1):
            rec = recuperarCita(a, i)
            if verFecha(rec) == fecha:
                encolar(c, rec)
        if not esVacia(c):
            print("========== LISTADO DE CITAS ==========")
            while not esVacia(c):
                rec = desencolar(c)
                print(f"Nombre: {verNombre(rec)}\nObra Social: {verObraSocial(rec)}")
                print("======================================")
        else:
            print(">>> No hay citas registradas para esa fecha.")
    
    # ===== OPCIÓN 8: SALIR =====
    elif (op == 8):
        print(">>> Saliendo del sistema...")

    # ===== OPCIÓN INVÁLIDA =====
    else:
        print(">>> Opción inválida. Intente nuevamente.")

# ===================== FIN DEL PROGRAMA ======================
