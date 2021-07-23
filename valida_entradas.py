import texto_menu


def opcao_primeiro_menu(opcao):
    if (opcao > 3 or opcao < 1):
        print("\n Opção inexistente")
        return (False)
    elif (opcao == 3):
        exit()
    elif(opcao == 1):
        return (texto_menu.partida_iniciada())
    elif(opcao==2):
        return (texto_menu.mostra_regras())

def valida_numero_de_jogadores(nomes):
    jogadores = nomes.split(",")
    if(len(jogadores) < 2):
        print("O jogo precisa de 2 ou mais jogadores ")
        return False
    else:
        return True

def letra_ou_palavra(entrada):
    list(entrada)
    if(len(entrada) > 1):
        return ("palavra")
    elif(len(entrada) == 1):
        return ("letra")
    elif(len(entrada) < 1 ):
        return ("vazio")

