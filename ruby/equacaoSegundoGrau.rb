#Início do algoritmo

# Declaração de variáveis
=begin
a = REAL
b = REAL 
c = REAL
delta = REAL 
x1 = REAL 
x2 = REAL
=end

# Importação da biblioteca cmath
require 'cmath' 

# Aqui será pego todos os números digitados pelo o usuário.
puts('Digite o número de A: ')
a = Float(gets)
puts('Digite o número de B: ')
b = Float(gets)
puts('Digite o número de C: ')
c = Float(gets)

# Aqui será feito o calculo para achar o DELTA.
delta = b** -(4 * a * c)

# Verificação caso DELTA for menor do que 0, exibir ao usuário que não possui raizes reais. 
if delta < 0
    puts("Não possui raizes reais.")
else
    # Aqui é feito o calculo final de Bhaskara, fazendo em si a divisão e a multiplicação para achar a raiz quadrada.
    x1 = (-b + CMath.sqrt(delta)) / (2 * a)
    x2 = (-b - CMath.sqrt(delta)) / (2 * a)
    # O final de tudo, aqui mostra ao usuário à raiz de A e a raiz de B.
    puts("""
        A raiz 1 é = #{x1},
        A raiz 2 é = #{x2}
    """) 
end

# Fim do Algoritmo 