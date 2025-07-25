while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ").strip()

    if senha.lower() == "sair":
        print("Encerrando o programa.")
        break

    tem_8_caracteres = len(senha) >= 8

    contem_numero = any(char.isdigit() for char in senha)

    if tem_8_caracteres and contem_numero:
        print("Senha forte. ✅")
        break
    else:
        print("Senha fraca. ❌ A senha deve ter pelo menos 8 caracteres e conter ao menos um número.\n")
