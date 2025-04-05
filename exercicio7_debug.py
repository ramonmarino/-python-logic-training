# TREINO PARA DEBUG, ENCONTRAR ERROS, TENTAR ENCONTRAR SOLUÇÕES

def calcular_media(notas):
    soma = 0

    for nota in notas:
        soma += nota
    return soma / len(notas)


notas = [7.5, 8.0, 6.5]
media = calcular_media(notas)
print("Média final:", media)

def buscar_nome(nomes, indice):
    return len(nomes[indice])


lista_de_nomes = ["Ana", "Carlos", "Maria"]

nome = buscar_nome(lista_de_nomes,1)

print("Nome encontrado:", nome)

def mostrar_nome(nome,indice):
    return nome[indice]

lista = ["Ana", "Carlos", "Maria"]

nome_passado = mostrar_nome(lista,2)

print(f" O nome da posição é: {nome_passado}")


def dividir(n1, n2):
    if n2 == 0:
         return print("Divisão por zero!")
    resultado = n1 / n2
    return resultado


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print("Resultado da divisão é:", dividir(a, b))


def somar(a, b):
    resultado = a + b
    return resultado

x = int(input("Digite o número 1: "))
y = int(input("Digite o número 2: "))

# Breakpoint aqui
print("Soma:", somar(x, y))
