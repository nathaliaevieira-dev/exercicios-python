numero = 1
par = 0

while True:
    numero = input(print("Escreva um número: "))
    if int(numero) == 0:
        break
    else: 
        if (int(numero) % 2 == 0):
         par = par + 1

print("Quantos números foram positivos na operação: ", par)