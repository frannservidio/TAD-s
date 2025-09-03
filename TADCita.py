###### TAD SIMPLE CITA ######
# Estructura interna: [DNI, Nombre, Obra Social, Teléfono, Fecha, Hora]

cita = [0, "", "", "", "", ""] # DNI, Nombre, Obra Social, Teléfono, Fecha, Hora

def crearCita():
    # Crea una cita vacia
    cita = [0, "", "", "", "", ""]
    return cita

def cargarCita(cita, dni, nombre, obraSocial, telefono, fecha, hora):
    # Carga los datos de la cita
    cita[0] = dni
    cita[1] = nombre
    cita[2] = obraSocial
    cita[3] = telefono
    cita[4] = fecha
    cita[5] = hora

def verDNI(cita):
    #Retorna el DNI del paciente.
    return cita[0]

def verNombre(cita):
    #Retorna el nombre del paciente 
    return cita[1]

def verObraSocial(cita):
    # Retorna la obra social del paciente
    return cita[2]

def verTelefono(cita):
    # Retorna el teléfono del paciente
    return cita[3]

def verFecha(cita):
    # Retorna la fecha de la cita.
    return cita[4]

def verHora(cita):
    # Retorna la hora de la cita.
    return cita[5]

def modDNI(cita, nuevoDNI):
    # Modifica el DNI del paciente
    cita[0] = nuevoDNI

def modNombre(cita, nuevoNombre):
    # Modifica el nombre del paciente
    cita[1] = nuevoNombre

def modObraSocial(cita, nuevaObraSocial):
    # Modifica la obra social del paciente
    cita[2] = nuevaObraSocial

def modTelefono(cita, nuevoTelefono):
    # Modifica el teléfono del paciente
    cita[3] = nuevoTelefono

def modFecha(cita, nuevaFecha):
    # Modifica la fecha de la cita
    cita[4] = nuevaFecha

def modHora(cita, nuevaHora):
    # Modifica la hora de la cita
    cita[5] = nuevaHora

def copiarCita(cita1, cita2):
    # Copia los datos de la cita 1 a la cita 2
    cita1[0] = cita2[0]
    cita1[1] = cita2[1]
    cita1[2] = cita2[2]
    cita1[3] = cita2[3]
    cita1[4] = cita2[4]
    cita1[5] = cita2[5]