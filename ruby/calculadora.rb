=begin
    
Programa para saber o calculo de todas as
operações.

Autor: Leonardo Miguel 
Data: 27/03/2022

Descrição:
    Esse programa foi feito para realizar calculos
e mostrar ao usuário todas as operações de ariti_
mética básica como adição, subtração, mulitplicação
e divisão.

=end


# Início do algoritmo 
puts "Programa de calculos"

=begin

    Aqui fica a declaração das variáveis


=end
puts "Insira um número para calcular: "
num1 = gets

puts "Insira outro número: "
num2 = gets 

adicao = Integer(num1) + Integer(num2)
subtracao  =  Integer(num1) - Integer(num2)
multiplicacao =  Integer(num1) * Integer(num2)
divisao =  Integer(num1) / Integer(num2)
puts (" ")

puts("==== Resultados ====")

puts ("""
O resultado da adição foi: #{adicao}
O resultado da subtração foi: #{subtracao}
O resultado da multiplicação foi: #{multiplicacao}
O resultado da divisão foi: #{divisao}
""")
