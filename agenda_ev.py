listaev = []
class AgendaEventos :
    def __init__(self, eventos):
        self.eventos = eventos
        
    def adicionar_ev(self, evento):
        listaev.append(evento)
        print('Evento ', evento, " adicionado!")

    def editar_ev(self, evento,  novo_evento):
        listaev.append(novo_evento)
        listaev.remove(evento)
        print('Lista de eventos atualizada: ')
        print(listaev)

    def remover_ev(self, evento):
        print("Eventos removidos: ", evento)
        listaev.remove(evento)

    def listar_ev(self):
        print('Lista de Eventos cadastrados: ')
        print(listaev)

        
ev01 = AgendaEventos('Festa')
ev02 = AgendaEventos('Premiação')
AgendaEventos.adicionar_ev(ev02, 'Premiação')
AgendaEventos.adicionar_ev(ev01, 'Festa')
print('')
AgendaEventos.editar_ev(ev01, 'Festa', 'Comemoração')
print('')
AgendaEventos.remover_ev(ev01, 'Comemoração')
AgendaEventos.listar_ev(ev01)