# Exercício 3
# Escreva uma função que peça ao usuário para digitar um número inteiro positivo.
# O programa deve continuar pedindo até que o usuário insira um número válido.
# Se o usuário inserir um número negativo ou zero, deve mostrar uma mensagem de erro e pedir novamente.
# Quando um número válido for inserido, o programa deve imprimir "Número válido inserido: X" e encerrar.


def numeros():
    escolha_numero = int(input("Digite um número: "))

    while escolha_numero <= 0:
        print("Por favor insira um número válido!")
        escolha_numero = int(input("Digite um número: "))

    if escolha_numero > 0:
        print(f"Número Válido inserido: {escolha_numero} ")


numeros()

print("---------------------------------------------------------------------")


# Crie uma função chamada verifica_par_impar() que receba um número do usuário e,
# utilizando um loop while continue pedindo ao usuário para inserir um número
# até que ele insira um número válido (diferente de 0).
# Se o número for par, informe que o número é par, e se for ímpar, informe que o número é ímpar.
# Caso o número seja 0,
# o loop continuará pedindo ao usuário para inserir um número válido.

def verfica_par_impar():
    escolha_numero2 = int(input("Escolha um número: "))
    while escolha_numero2 <= 0:
        print("Por favor insera um número válido maior que 0.")
        escolha_numero2 = int(input("Digite o Número válido: "))
    if escolha_numero2 % 2 == 0:
        print(f"Número é par: {escolha_numero2} ")
    else:
        print("O número é ímpar!")


verfica_par_impar()

print("----------------------------------------------------------")

# Exercício 3
# Crie uma função que receba uma lista de números inteiros
# e imprima a quantidade de números positivos, negativos e zeros na lista.
# Utilize um while para percorrer a lista e contar as ocorrências.
numero_positivos = 0
numero_negativo = 0
numero_zero = 0


def lista():
    global numero_positivos, numero_negativo, numero_zero
    lista = [1, 2, 3, 4, 5, 6, 7, -3, -4, 0]

    while lista:
        numero = lista.pop()  # remove o ultimo numero da lista

        if numero > 0:
            numero_positivos += 1
        elif numero < 0:
            numero_negativo += 1
        else:
            numero_zero += 1

    print(f"Números positivos: {numero_positivos}")
    print(f"Números negativos: {numero_negativo}")
    print(f"Números zero: {numero_zero}")

lista()
