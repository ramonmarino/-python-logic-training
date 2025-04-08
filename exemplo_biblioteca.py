# 1. Importar bibliotecas
import pandas as pd
from sklearn.linear_model import LinearRegression


# 2. Dados de exemplo (anos de experiência e salários)
dados = {
    'experiencia': [1, 2, 3, 4, 5],
    'salario': [2500, 3000, 3500, 4000, 4500]
}
df = pd.DataFrame(dados)

# 3. Separar variáveis (X e y)
X = df[['experiencia']]  # entrada
y = df['salario']        # saída

# 4. Criar e treinar o modelo
modelo = LinearRegression()
modelo.fit(X, y)

# 5. Fazer uma previsão
experiencia_nova = [[7]]  # 7 anos de experiência
salario_previsto = modelo.predict(experiencia_nova)

print(f"Salário previsto para 7 anos de experiência: R$ {salario_previsto[0]:.2f}")

# 6. Visualizar com gráfico
plt.scatter(X, y, color='blue')  # pontos reais
plt.plot(X, modelo.predict(X), color='red')  # linha da regressão
plt.xlabel("Anos de Experiência")
plt.ylabel("Salário")
plt.title("Experiência vs Salário")
plt.show()
