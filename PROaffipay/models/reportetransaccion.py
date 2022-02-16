

class reportetransaccion():

    def __init__(self, id_transaccion, nombre_titular, tarjeta_origen, cvv_origen, monto, tarjeta_destino, evento, respuesta_evento, fecha_hora, email):
        self.id_transaccion = id_transaccion
        self.nombre_titular = nombre_titular
        self.tarjeta_origen = tarjeta_origen
        self.cvv_origen = cvv_origen
        self.monto = monto
        self.tarjeta_destino = tarjeta_destino
        self.evento = evento
        self.respuesta_evento = respuesta_evento
        self.fecha_hora = fecha_hora
        self.email = email