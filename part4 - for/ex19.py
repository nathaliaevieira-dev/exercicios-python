numero = int(input("Digite um número: "))
fator = 1

for i in range(1, numero + 1):
    fator *= i

print("Fatorial é ", fator)