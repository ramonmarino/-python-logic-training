# Escreva uma função que recebe um número inteiro positivo n
# e retorna a soma de todos os números ímpares de 1 até n.
# Conceito: Laços de repetição, operadores aritméticos e condições.
# Dica: Um número é ímpar quando numero % 2 != 0.


def numero_positivo(n):
    soma = 0
    lista_numero_impares = []  # lista vazia
    for i in range(n):
        if i % 2 != 0:
            lista_numero_impares.append(i)
            soma += i  # i +=, === i + i

    print(f"Os números ímpares São: {lista_numero_impares}")
    return soma


print(f"A Soma dos números ímpares é: {numero_positivo(20)}")

print("------------------------------------------------------------------------")


# Crie uma função que receba uma lista de números e retorne o maior número da lista.
# Dicas para pensar na solução:
# Como percorrer todos os números da lista?
# Como armazenar o maior valor encontrado até agora?
# O que fazer se um número maior for encontrado?

def lista_maior_numero(lista):
    maior_numero = lista[0]

    for i in lista:
        if i > maior_numero:
            maior_numero = i
    return maior_numero


listas_para_testar = [
    [-10, -5, 0, 5, 10, 15, 20],  # Lista com números negativos e positivos
    [-100, -50, -20, -5, -1],  # Lista com apenas negativos
    [42],  # Lista com um único número
    [7, 7, 7, 7, 7, 7],  # Lista com todos os números iguais
    [99, 1, 250, 3, 150, 400, 0]  # Lista desordenada
]

for lista in listas_para_testar:
    print(f"Lista: {lista} Maior número: {lista_maior_numero(lista)}")

print("---------------------------------------------------------------------------")


# Objetivo: Criar uma função que recebe uma string (frase) e retorna
# um dicionário com a contagem de cada palavra na frase.
# Dicas:
# Você pode usar um dicionário para armazenar a contagem de palavras.
# Use .split() para dividir a string em palavras.
# Considere transformar tudo para minúsculas (.lower()) para evitar contagens duplicadas
# devido a diferenças de capitalização.
print()
def palavra():
    contagem_palavras = {} # dicionário chave e valor
    frase = "Ramon ramon ramon de seu melhor!"
    texto = frase.lower().split() # divide a frase e deixa tudo minúsculas
    for i in texto:
        if i in contagem_palavras:
            contagem_palavras[i] += 1
        else:
            contagem_palavras[i] = 1
    return contagem_palavras

print(palavra())