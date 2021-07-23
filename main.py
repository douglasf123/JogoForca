import manipulando_variaveis
import texto_menu
import valida_entradas

#variaveis globais
erros = 0
letras_digitadas=""

while True:
    texto_menu.menu_inicial()
    opcao = int(input ("Escolha uma opção: "))
    if(valida_entradas.opcao_primeiro_menu(opcao)):
        nomes = input()
        if(valida_entradas.valida_numero_de_jogadores(nomes)):
            jogador = manipulando_variaveis.serteio(nomes,",")
            print(jogador,"\n")
            palavra = input("digite uma palavra: ").lower()
            tema = input("digite o tema referente a palavra: ")
            palavra = manipulando_variaveis.separador_de_letras(palavra)
            while True:
                texto_menu.tela_jogo(tema,len(palavra),erros,letras_digitadas)
                tentativa = input("Digite uma palavra ou uma letra: ").lower()

                if(valida_entradas.letra_ou_palavra(tentativa) == "letra"):
                   list(letras_digitadas).append(tentativa)
                   print(letras_digitadas)
                   print(tentativa)

                elif(valida_entradas.letra_ou_palavra(tentativa) == "palavra"):
                    print("tentativa ")

                elif(valida_entradas.letra_ou_palavra(tentativa) == "vazio"):
                    print("nada foi digitado")

