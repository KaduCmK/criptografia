# decodificador numerico -> alfabeto

# info sobre a criptografia no codificador.py

import string

entrada = str(input('Entre com o código: \n'))
codigo = entrada.split('.')

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

print(decodificador(codigo))