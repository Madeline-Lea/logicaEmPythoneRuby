# Início do algoritmo

# Importação da biblioteca CMath
from cmath import sqrt

# Declaração de Variáveis
a = 0
b = 0
c = 0
delta = 0
x1 = round(0)
x2 = round(0)

# Inputs que pergunta ao usuário quais números ele irá utilizar para o cálculo.
a = float(input("Digite o número A: "))
b = float(input("Digite o número B: "))
c = float(input("Digite o número C: "))

# A realização da equação de segundo grau.
delta = float(  b** - (4 * a * c))

# Verifica se delta é menor do que zero.
# Else realiza as raizes.
if(delta < 0):
    print("Não existe raizes possíveis.")
else:
    x1 = -b + sqrt(delta) / (2 * a)
    x2 = -b - sqrt(delta) / (2 * a)
    print(f"A raiz 1 é = {x1}, \n A raiz 2 é = {x2}" )

#Fim do algoritmo.