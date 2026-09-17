print("Digite dois números para saber qual é o maior ou se são iguais")

num1 = input("Digite o primeiro número:")
num2 = input("Digite o segundo número:")

if float(num1) > float(num2):
    print(f"O maior número é: {num1}")

elif float (num1) < float(num2):
    print(f"O maior número é: {num2}")

elif float(num1) == float(num2):
    print("Os 2 números são iguais")