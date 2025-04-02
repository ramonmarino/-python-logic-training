# Estudo Classes e objetos

'''Classes são a definição de um novo tipo de dados que associa dados e operações em uma
só estrutura, Um objeto por ser entendido como uma variável cujo o tipo é uma classe.'''

''' Métodos nada mais são que funções associadas a uma classe.'''


class televisao:  # classe
    def __init__(self):  # construtor/ manipula as informação
        self.ligada = False
        self.canal = 2
        self.marca = "LG"
        self.tamanho = "45 polegadas"

    def mudar_canal_para_cima(self):
        self.canal += 1

    def mudar_canal_para_baixo(self):
        self.canal -= 1


print("TV 1\n")
tv = televisao()
print(tv.ligada)  # metodo
print(tv.canal)
print(tv.marca)
print(tv.tamanho)

print("------------------------------")
print("TV 2 \n")
tv_sala = televisao()
tv_sala.ligada = True
tv.canal = 10
tv.marca = "sansung"
tv.tamanho = "60 polegadas"

print(tv_sala.ligada)  # metodo
print(tv.canal)
print(tv.marca)
print(tv.tamanho)
tv.mudar_canal_para_baixo() # mudando o canal
print(tv.canal)
