pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").strip()

    if entrada.lower() == "fim":
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim' para encerrar.")

print("\nResumo:")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
