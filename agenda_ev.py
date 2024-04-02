lista_eventos = []

class AgendaEventos :

    def adicionar_ev():
        novo_ev = input("Adicionar eventos: ")
        print (novo_ev)
        lista_eventos.append(novo_ev)

    def editar_ev():
        edit_ev = input("Digite o evento que deseja editar: ")
        print(edit_ev)
        novo_edit = input("Digite as alterações: ")
        print ("evento editado: ", novo_edit)

    def remover_ev():
        remo_ev = print ("Digite o evento que deseja remover: ")
        print("Eventos removidos: ", remo_ev)
        lista_eventos.remove(remo_ev)