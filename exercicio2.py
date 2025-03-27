# Exercício 1: Classificação de Números
# Peça ao usuário para inserir um número e verifique:
# Se for positivo, exiba "Número positivo".
# Se for negativo, exiba "Número negativo".
# Se for zero, exiba "Número neutro".


def valores_numeros():
    escolha_numero = int(input("Escolha um número por favor: "))

    match escolha_numero:
        case _ if escolha_numero > 0:
            print("O Número é positivo, maior que zero!")
        case _ if escolha_numero < 0:
            print(" O Número é negativo, menor que zero!")
        case 0:
            print("Número Neutro!")


valores_numeros()

print("-------------------------------------------------------------")


# Exercício 2: Contar números positivos, negativos e zeros
# Você tem uma lista de números e precisa contar quantos números positivos,
# negativos e zeros existem nela.
# Instruções:
# Crie uma função que receba uma lista de números.
# A função deve contar quantos números são positivos, negativos e quantos são zeros.
# Imprimir a quantidade de números positivos, negativos e zeros.


def lista_numeros():
    lista = [-5, 0, 7, -3, 2, 0, -8, 1]
    cont_positivo = 0
    cont_negativo = 0
    cont_zero = 0

    for i in lista:
        if i > 0:
            cont_positivo += 1
        elif i < 0:
            cont_negativo += 1
        else:
            cont_zero += 1

    print(f"A quantidade de números positivos {cont_positivo}")
    print(f"A quantidade de números negativos {cont_negativo}")
    print(f"A quantidade de números zeros {cont_zero}")


lista_numeros()

print("---------------------------------------------------------------------")

# Exercício 3:
# Enunciado:
# Você tem uma lista de números e precisa identificar os números maiores, menores ou iguais
# a um número chave fornecido pelo usuário. O número chave será dado pelo usuário e a tarefa é separar os números que são maiores, menores ou iguais ao número chave.
# Exemplo:
# Para a lista [1, 5, 9, 12, 3, 7] e a chave 6, o programa deve dividir os números em três grupos:
# Maiores que 6: [9, 12, 7]
# Menores que 6: [1, 5, 3]
# Iguais a 6: []

lista = [1, 5, 9, 12, 3, 7]
maiores = []
menores = []
iguais = []

escolha_usuario = int(input("Escolha seu número: "))

for i in lista:
    if i > escolha_usuario:
        maiores.append(i)


    elif i < escolha_usuario:
        menores.append(i)

    else:
        iguais.append(i)


print(f"Os maiores números são: {maiores}")
print(f"Os menores números são: {menores}")
print(f"Os números são iguais:  {iguais}")