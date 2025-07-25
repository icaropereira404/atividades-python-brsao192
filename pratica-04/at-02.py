notas = []

while True:
    entrada = input("Digite a nota (ou 'fim' para encerrar): ").strip().lower()

    if entrada == "fim":
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Erro: a nota deve estar entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim' para encerrar.")

# Exibe resultado final
if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f}")
    print(f"Total de notas válidas registradas: {len(notas)}")
else:
    print("\nNenhuma nota válida foi registrada.")
