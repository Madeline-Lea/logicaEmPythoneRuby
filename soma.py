"""
Programa de somar números
Autor: Leonardo Miguel
Data: 20/03/2022
Descrição:
	Apenas um exercício com a intenção de fazer uma soma,
e exibir o resultado para o usuário que estiver utili-
zando este programa.
"""

# Às variáveis (num1 e num2) tem a função de armazenar os digitos pelo o usuário.
num1 = int(input("Digite um número para soma:  "))
num2 = int(input("Digite outro numero para soma: "))    

# A variável (soma) tem o trabalho de fazer de fato a adição das variáveis (num1 e num2).
soma = num1 + num2

    
print(f'A soma dos números é: {soma}')