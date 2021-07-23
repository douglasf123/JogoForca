import random

def separador_de_letras(palavra):
    letras = list(palavra)
    return letras

def serteio(valor,separador):
    valor1 = valor.split(separador)
    random.shuffle(valor1)
    return valor1[1]

def formar_lacuna(palavra):
    forca = ""
    for i in palavra:
        forca = forca + " _"
    return(forca)

def tem_letra(tentativa,forca,palavra):

    forca_nova = forca.split()
    i = palavra.find(tentativa)

    forca_nova
    "".join(forca_nova)

    return(str(forca_nova).strip('[],/'))