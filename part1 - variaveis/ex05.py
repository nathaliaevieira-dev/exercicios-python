preco = input(print("Coloque o preço do produto: "))
quantidade = input(print("Digite a quantidade de produto comprada: "))

total = float(preco) * float(quantidade)
print ("O valor total da compra foi de: "), print(f"{total:.2f}")

