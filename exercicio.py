# Prática um, gerar um programa que conte a quantidade de vogais em uma string.
'''def contar_vogais(texto):
    simples = texto.lower()
    vogais = "aeiou"
    contador = 0

    for letra in simples:
        if letra in vogais:
            contador += 1

    print("A palavra '{}' tem {} vogais".format(texto, contador))
    return contador

# Exemplo de uso


# Prática dois, gerar um programa que inverta uma string.
contar_vogais("Olá Mundo!")


def inverter_texto(texto):
    return texto[::-1]
    # Essa sintaxe fatia cada string da frase e a coloca ao contrario

# Pratica três, gerar um programa que capitaliza as palavras de uma string.


def capitalizar_palavras(texto):
    return texto.title()

# Pratica quatro, gerar um programa que apague strings especificas.abs


def apagar_palavras(texto, palavra, quantidade):
    return texto.replace(palavra, "", quantidade)
    # Essa função substitui a palavra desejada por um espaço vazio
    texto = input("Digite a frase que deseja apagar: ")
    palavra = input("Digite a palavra que deseja apagar: ")
    quantidade = int(input("Digite a quantidade de vezes que deseja apagar: "))
    texto = apagar_palavras(texto, palavra, quantidade)
    print (texto)


#Prática cinco, gerar um programa que verifique se uma string é um palíndromo.
def verificar_palindromo(texto):
    simples = texto.lower().replace(" ", "")
    return simples == simples[::-1]
    texto = input("Digite a frase que deseja verificar: ")
    if verificar_palindromo(texto):
    print("A frase '{}' é um palíndromo".format(texto))
    else:
    print("A frase '{}' não é um palíndromo".format(texto))
'''
# Prática seis, gerar um programa que conte a quantidade de palavras em uma string.