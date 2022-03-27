# Declaração de variáveis 


=begin
    
    Nessa parte há puts para que o usuário identifique que ele
tem que colocar números nos (gets);
    E nos gets de fato são nossas variáveis que irão pegar os 
números que forem digitados pelo o usuário.
    
=end
puts "Insira um número para a soma: "
num1 = gets
puts "Insira outro número: "
num2 = gets


=begin


=end

soma = Integer(num1) + Integer(num2)

puts "A soma dos números é: #{soma}!"