n1 = float(input("Digite a 1º nota: "))
n2 = float(input("Digite a 2º nota: "))
n3 = float(input("Digite a 3º nota: "))

media = (n1 + n2 + n3) / 3

if media >= 6:
    print(f"Você está aprovado, com sua média sendo: {media:.1f}")

elif media < 6 and media >= 4:
    print(f"Vocês está em recuperação, com sua média sendo: {media:.1f}")

elif media < 4:
    print(f"Você está reprovado, com sua média sendo: {media:.1f}")