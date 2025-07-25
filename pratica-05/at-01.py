valor_conta = float(input("Informe o valor da conta (R$): "))

porcentagem_gorjeta = float(input("Informe a porcentagem da gorjeta (ex: 10 para 10%): "))

valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)

print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
