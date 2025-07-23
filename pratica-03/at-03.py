def converter_temperatura(valor, origem, destino):
    origem = origem.lower()
    destino = destino.lower()

    if origem == "fahrenheit":
        celsius = (valor - 32) * 5/9
    elif origem == "kelvin":
        celsius = valor - 273.15
    elif origem == "celsius":
        celsius = valor
    else:
        return "Unidade de origem inválida."

    if destino == "celsius":
        return celsius
    elif destino == "fahrenheit":
        return (celsius * 9/5) + 32
    elif destino == "kelvin":
        return celsius + 273.15
    else:
        return "Unidade de destino inválida."

valor = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (Celsius, Fahrenheit ou Kelvin): ")
destino = input("Digite a unidade de destino (Celsius, Fahrenheit ou Kelvin): ")

resultado = converter_temperatura(valor, origem, destino)

if isinstance(resultado, str):
    print("Erro:", resultado)
else:
    print(f"{valor} {origem.capitalize()} equivale a {resultado:.2f} {destino.capitalize()}")
