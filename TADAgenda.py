###### TAD COMPUESTO AGENDA ######
# agenda = []

def crearAgenda():
    # Crea y retorna una agenda vacia
    agenda = []
    return agenda

def agregarCita(agenda, cita):
    # Agrega una cita a la agenda
    agenda.append(cita)

def eliminarCita(agenda, cita):
    # Elimina una cita de la agenda
    agenda.remove(cita)

def recuperarCita(agenda, i):
    # Recupera la cita de la agenda de la posición iesima
    return agenda[i-1]

def tamanioAgenda(agenda):
    # Retorna la cantidad de citas en la agenda
    return len(agenda)