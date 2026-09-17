user = "sesi"
codigo = "sesi123"

while True:
    usuario = input("Escreva o seu usuário: ")
    senha = input("Escreva sua senha: ")

    if usuario == user and senha == codigo:
        print("Acesso Liberado")
        break
    else:
        print("Acesso Negado, Tente novamente")