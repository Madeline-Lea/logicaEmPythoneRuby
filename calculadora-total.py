"""
Programa de calculo de operações
Autor: Leonardo Miguel
Data: 20/03/2022
Descrição:
	Apenas um exercício com a intenção de fazer um calculo,
e exibir o resultado para o usuário que estiver utili-
zando este programa, assim mostrando o resultados das
operações aritiméticas básicas.
"""

# Às variáveis (num1 e num2) tem a função de armazenar os digitos pelo o usuário.
num1 = int(input("Digite um número para o resultado de todas às operações  "))
num2 = int(input("Digite outro numero: "))    

"""
 As variáveis (soma, subtracao, multiplicacao, divisao)
 tem o trabalho de fazer de fato a operação das variáveis (num1 e num2).
"""
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 
    
# Esse print demonstra ao usuário os resultados de todas operações feitas.
print(f"""
A adição dos números é: {soma}
A subtração dos números é: {subtracao}
A multiplicação dos números é: {multiplicacao}
A divisão dos numeros é: {divisao}
""")