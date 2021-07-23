def menu_inicial():
    print("Jogo da Forca\n"
          "---------------------\n"
          "[1] Iniciar partida\n"
          "[2] Regras do jogo\n"
          "[3] sair\n"
          "------------------\n"
          )
def mostra_regras():
    print("Regras\n\n "
          "Ddois ou mais Players\n"
          "Um dos player da a palavra e tema\n"
          "Deve ser ter dica de Nº letras e tema\n"
          "15 chances de acertar a palavra ou letras\n"
          "O jogo termina quando a palavra é completada ou se esgotas a chances\n"
          "O player pode digitar uma letra ou a palavra\n"
          "Se o player tentar a palavra, acertando ou errando a roda se encerran\n"
          "Então troca a posição dos players e o jogo se reinician\n")
    input()
    return ()

def partida_iniciada():
    print("Digite os nomes dos jogadores separados por (,)\n")
    return (True)

def tela_jogo(tema,total_letras,erros,letras_digitadas):
    print("Descubra a palavra\n\nTema: ",tema,"\tTotal de letras: ", total_letras,"\tErrou:",erros)
    print("\n\n Letras Digitadas: ",letras_digitadas)
