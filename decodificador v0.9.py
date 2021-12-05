# decodificador numerico -> alfabeto

# info sobre a criptografia no codificador.py

import string
import random
import numpy as np

entrada = str(input('Entre com o código: \n'))
codigo = entrada.split('.')
ent_chave = input('Chave: ')
c= ent_chave.split(', ')
chave = []
for i in range(len(c)):
    chave.append(int(c[i]))

print(chave)
print(len(chave))
input()

def decodificador(codigo):
    output = []
    numerais = list(range(27))
    alfabeto = list(string.ascii_lowercase)
    especiais = list(string.punctuation)

    for i in range(len(codigo)):
        if codigo[i] == '.':
            output.append('')
        elif codigo[i] == ' ':
            output.append(' ')
        elif codigo[i] in str(numerais):
            for j in range(len(numerais)):
                if codigo[i] == str(numerais[j]):
                    output.append(alfabeto[j]) 
        elif codigo[i] in alfabeto:
            for j in range(len(alfabeto)):
                if codigo[i] == alfabeto[j]:
                    output.append(str(numerais[j]))
        elif codigo[i] in especiais:
            for j in range(len(especiais)):
                if codigo[i] == especiais[j]:
                    output.append(especiais[j])

    return ''.join(output)


def unshuffle(l, order):
    l_out = [0] * len(l)
    for i, j in enumerate(order):
        l_out[j] = l[i]
    return l_out

print('=============================')
print('Sua mensagem decodificada:')
print(decodificador(unshuffle(codigo, chave)))
input('pressione qualquer tecla para sair')
