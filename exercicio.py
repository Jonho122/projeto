#Prática um, gerar um programa que conte a quantidade de vogais em uma string.
def contar_vogais(texto):
    simples = texto.lower()  
    vogais = "aeiou"
    contador = 0  

    for letra in simples:  
        if letra in vogais:  
            contador += 1  

    print("A palavra '{}' tem {} vogais".format(texto, contador))
    return contador  

# Exemplo de uso
contar_vogais("Olá Mundo!")
