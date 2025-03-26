# Crie uma função que recebe uma lista de números e retorna um dicionário
# com a frequência de cada número.

def lista():
    sequencia_numeros = [1, 2, 2, 3, 3, 4, 5]  # lista
    frequencia = {}  # dicionário

    for i in sequencia_numeros:
        if i in frequencia:
            frequencia[i] += 1
        else:
            frequencia[i] = 1

    return frequencia


print("Exercicio1: ", lista())
print("---------------------------------------------------------------------")

# Exercício 2: Contar números negativos, positivos e zeros em uma lista
# Você tem uma lista de números e precisa contar quantos números positivos,
# negativos e zeros existem nela.

sequencia = [-5, 0, 7, -3, 2, 0, -8, 1]

quantidade_positivos = 0
quantidade_negativos = 0
quantidade_zeros = 0

for i in sequencia:  # percorri a lista para saber quais os números
    if i > 0:  # verifiquei se é positivo
        quantidade_positivos += 1  # somei os positivos
    elif i < 0:
        quantidade_negativos += 1
    else:
        quantidade_zeros += 1
print("Exercicio 2: ")
print(f"Quantidade de números Positivos na lista: {quantidade_positivos} ")
print(f"Quantidade de números Negativos na lista: {quantidade_negativos} ")
print(f"Quantidade de números 0 na lista: {quantidade_zeros} ")

print("---------------------------------------------------------------------")


# Exercício 3: Contar a quantidade de pares e ímpares em uma lista
# Você tem uma lista de números e precisa contar quantos números pares e ímpares existem nela.
# Desafio:
# Crie uma função que percorre uma lista de números.
# Verifique se o número é par ou ímpar.
# Conte a quantidade de números pares e ímpares e retorne os resultados.
# A lógica seria:
# Um número é par se for divisível por 2 (n % 2 == 0).
# Um número é ímpar se não for divisível por 2 (n % 2 != 0).


def lista_numeros():
    sequencia2 = [5, 8, 12, 33, 45, 10, 22, 17]
    cont = 0
    cont_impar = 0

    for i in sequencia2:
        if i % 2 == 0:  # sabendo se o número é par
            cont += 1

        elif i % 2 != 0:
            cont_impar += 1

    return cont, cont_impar


print(f"A quantidade de números pares é: {lista_numeros()[0]} e números ímpares: {lista_numeros()[1]}")
