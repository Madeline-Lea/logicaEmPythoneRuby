"""
Programa de calculos aritiméticos
Autor: Leonardo Miguel
Data: 20/03/2022
Descrição:
    Esse programa tem o proposito de calcular
médias aritiméticas inseridas pelo o usuário.

"""

# Declaração das variáveis 
# Essa variável é o nosso contador para poder fazer a nossa repetição com for.
somas = 0


#  Esse for tem a função de rodar 4 vezes e pegar os números inseridos pelo o usuário.

for i in range(4):
    somas += float(input("Digite um número de 1 a 10 para calcular a média: "))

# A variável média tem a função de calcular a soma e a divisão.
soma = somas
media = 4
# Aqui em si fica nossa variável de resolução das operações.
resultados = float((soma + int(media)) / float(media))
print("...")

print(" ")

print(f'A média total é: {resultados}')

