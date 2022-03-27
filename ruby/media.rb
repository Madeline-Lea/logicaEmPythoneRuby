$num = 0

$i = 3

$totalNum = 4

for $i in 0..$i
    puts("Digite um número para calcular a média: ")
    $num += Integer(gets)
end

$media = $num / $totalNum

puts("Á média é: #{$media}")