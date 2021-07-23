import random

def separador_de_letras(palavra):
    letras = list(palavra)
    return letras

def serteio(valor,separador):
    valor1 = valor.split(separador)
    random.shuffle(valor1)
    return valor1[1]
