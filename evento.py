class Evento:
    def __init__(self, titulo, data, hora, local):
        self.titulo = titulo
        self.data = data 
        self.hora = hora
        self.local = local

    def __str__(self):
        print('Nome do Evento: {}'.format(self.titulo))
        print('Data: {}'.format(self.data))
        print('Hora: {}'.format(self.hora))
        print('Local: {}'.format(self.local))

ev01 = Evento('Festa', '2024-04-01', '17:25', 'Escola' )
Evento.__str__(ev01)