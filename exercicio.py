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

# Prática seis, gerar um programa que conte a quantidade de palavras em uma string.

def contar_palavras(texto):
    return len(texto.split())
    # Essa função conta a quantidade de palavras em uma string
   texto = input("Digite a frase que deseja contar: ")
    print("A frase '{}' tem {} palavras".format(texto, contar_palavras(texto)))
'''
'''Exercício 1: Divisão
Escreva um programa que:
1. Solicite ao usuário dois números inteiros.   
2. Realize a divisão do primeiro número pelo segundo.
3. Exiba o resultado da divisão.
4. Use  para exibir a mensagem "Fim da operação".

x =0
y = 0
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
try:
    resultado = x / y
    print("O resultado da divisão de {} por {} é: {}".format(x, y, resultado))
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
finally:
    print("Fim da operação")'''

'''Exercício 2: Arquivo
Crie um programa que:
Tente abrir um arquivo chamado dados.txt. usando try
Use  para tratar o erro caso o arquivo não exista.
Utilize  para ler e imprimir o conteúdo do arquivo se ele for encontrado.
Adicione um bloco  para fechar o arquivo ou exibir uma mensagem de encerramento.

try:
    with open("dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo 'dados.txt' não foi encontrado.")
else:
    print("Arquivo lido com sucesso.")
finally:
    print("Fim da operação")'''
'''
Exercício 3: Conversão de tipos
Escreva um código que:
Solicite ao usuário que insira um número
Use  para converter o valor fornecido para um número inteiro.
Use  para exibir uma mensagem de erro se o valor não for numérico
Utilize  para dizer ao usuário que a conversão foi bem-sucedida.
Adicione  para exibir uma mensagem como "Processo finalizado"

valor = (input("Digite um número: "))
try:
    valor = int(valor)
except ValueError:
    print("Erro: O valor fornecido não é um número.")
else:
    print("Conversão bem-sucedida! O número é:", valor)
finally:
    print("Processo finalizado.")'''

# **Exercícios de Prática com as Bibliotecas `math` e `random`**
'''
1. **Cálculo da Hipotenusa**
   - Escreva um programa que solicita ao usuário os valores dos catetos de um triângulo e calcule a hipotenusa usando a função **`math.sqrt`** e o teorema de Pitágoras.

2. **Área de um Círculo**
   - Solicite ao usuário o raio de um círculo e calcule sua área utilizando **`math.pi`** e a fórmula \( \text{Área} = \pi \cdot r^2 \).

3. **Cálculos Trigonométricos**
   - Peça ao usuário um ângulo em graus e:
     - Converta-o para radianos com **`math.radians`**.
     - Calcule o seno, cosseno e tangente utilizando **`math.sin`**, **`math.cos`** e **`math.tan`**.

4. **Arredondamento e Fatoriais**
   - Escreva um programa que:
     - Solicite um número decimal e arredonde-o para cima e para baixo usando **`math.ceil`** e **`math.floor`**.
     - Solicite um número inteiro e calcule seu fatorial com **`math.factorial`**.



### **Exercícios com a biblioteca `random`**

1. **Números Aleatórios**
   - Gere 10 números aleatórios entre 1 e 100 usando **`random.randint`** e exiba-os na tela.

2. **Simulação de Dado**
   - Simule o lançamento de um dado de 6 lados. Use **`random.randint`** para gerar números entre 1 e 6 e pergunte ao usuário se ele deseja continuar lançando o dado.

3. **Aleatorização de Listas**
   - Escreva um programa que receba uma lista de nomes e os embaralhe usando **`random.shuffle`**.

4. **Jogo de Adivinhação**
   - Crie um jogo onde o programa escolhe um número entre 1 e 50 com **`random.randint`** e o usuário deve adivinhar. O programa deve fornecer feedback se o palpite foi muito alto ou muito baixo, até que o número correto seja encontrado.

5. **Loteria Simples**
   - Gere 6 números aleatórios distintos entre 1 e 60, simulando um bilhete de loteria, utilizando **`random.sample`**.
 '''