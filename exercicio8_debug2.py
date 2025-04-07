def dividir(a, b):
    if b == 0:
       return  "Erro de divisão por zero, rode novamente!"

    else:
        resultado = a / b


        return f"A divisão dos valores é: {resultado}"


print(dividir(20, 0))

print("---------------------------------------------")


def validar_usuario(nome, idade):
    if not nome:
        return "Erro: nome não pode estar vazio."

    if idade < 18:
        return "Erro: o usuário deve ter pelo menos 18 anos."

    return f"Usuário {nome} com {idade} anos cadastrado com sucesso!"


print(validar_usuario("Ramon", 25))       # nome vazio
print(validar_usuario("Ana", 15))    # idade abaixo
print(validar_usuario("Lucas", 30))  # tudo certo

