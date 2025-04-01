# Desafio 1: Soma de Dígitos
# Escreva uma função que recebe um número inteiro positivo e retorna a soma dos seus dígitos.

def soma_valores(numero):
    return sum(int(digito) for digito in str(numero))


print(soma_valores(555))  # 5 + 5 + 5

print("-------------------------------------------------------------")


# Um palíndromo é uma palavra, número ou frase que se lê da mesma forma
# de frente para trás e vice-versa.
# Crie uma função que recebe uma string e retorna True se for um palíndromo e False caso contrário.

def palindromo(texto):
    if texto == texto[::-1]:  # vira a palavra ao contrário
        return print("É palíndromo")
    else:
        return print("Não é palíndromo")


palindromo("radar")

print("-----------------------------------------------------------------------")


# Dado uma lista de números inteiros, crie uma função
# que retorne uma nova lista contendo apenas os números únicos
# ou seja, que aparecem exatamente uma vez.


def numeros_unicos():
    lista = [1, 1, 2, 2, 3, 4, 5, 5, 8]
    mesmo_numeros = {}
    for i in lista:
        mesmo_numeros[i] = mesmo_numeros.get(i, 0) + 1
        # se o número existir no dicionário inicializa com 0

        numeros_unicos = [num for num, cont in mesmo_numeros.items() if  cont == 1]

    return numeros_unicos


print(numeros_unicos())