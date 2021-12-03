# Codificador alfabeto - > numérico

# Cada letra é traduzida pela sua posição numérica no alfabeto, dividida entre pontos
# exemplo: abc -> 1 2 3

# Números seguem o caminho contrario e sao convertidos em suas respectivas letras
# ex: 1 2 3 -> abc

# Caracteres especiais não são criptografados

# Letras com acento (á, ã, ç) NÃO SÃO ACEITAS!

import string

frase = input('Escreva a frase a ser codificada: \n')

def codificador(frase):
    output = []
    numerais = list(range(27))
    alfabeto = list(string.ascii_lowercase)
    especiais = list(string.punctuation)

    for i in range(len(frase)):
        if frase[i] == ' ':
            output.append(' ')
        elif frase[i] in alfabeto:
            for j in range(len(alfabeto)):
                if frase[i] == alfabeto[j]:
                    output.append(str(numerais[j]))
        elif frase[i] in str(numerais):
            for h in range(len(numerais)):
                if frase[i] == str(numerais[h]):
                    output.append(alfabeto[h])
        elif frase[i] in especiais:
            for k in range(len(especiais)):
                if frase[i] == especiais[k]:
                    output.append(especiais[k])

    return '.'.join(output)

print(codificador(frase))