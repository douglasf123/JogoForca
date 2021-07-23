import manipulando_variaveis
import texto_menu
import valida_entradas
import os

#variaveis globais
erros = 0
letras_digitadas=""

while True:
    os.system("cls")
    texto_menu.menu_inicial()
    opcao = int(input ("Escolha uma opção: "))
    if(valida_entradas.opcao_primeiro_menu(opcao)):
        nomes = input()
        if(valida_entradas.valida_numero_de_jogadores(nomes)):
            jogador = manipulando_variaveis.serteio(nomes,",")
            print(jogador,"\n")
            palavra = input("digite uma palavra: ").lower()
            tema = input("digite o tema referente a palavra: ")
            #palavra = manipulando_variaveis.separador_de_letras(palavra)
            forca = manipulando_variaveis.formar_lacuna(palavra)
            while erros < 15:
                os.system("cls")
                texto_menu.tela_jogo(tema,len(palavra),erros,letras_digitadas,forca)
                tentativa = input("Digite uma palavra ou uma letra: ").lower()

                if(valida_entradas.letra_ou_palavra(tentativa) == "letra"):
                   letras_digitadas = letras_digitadas + tentativa + "-"
                   if(palavra.find(tentativa) > -1 ):
                       forca = manipulando_variaveis.tem_letra(tentativa,forca,palavra)
                   else:
                       erros = erros + 1

                elif(valida_entradas.letra_ou_palavra(tentativa) == "palavra"):
                    print("tentativa ")

                elif(valida_entradas.letra_ou_palavra(tentativa) == "vazio"):
                    print("nada foi digitado")

            print("#######LOSER####\n\n \t\tFIM DE JOGO")