valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro

valor_em_dolar = round(valor_em_dolar, 2)
valor_em_euro = round(valor_em_euro, 2)

print(f"Valor em reais: R$ {valor_em_reais}")
print(f"Convertido em dólares: US$ {valor_em_dolar}")
print(f"Convertido em euros: € {valor_em_euro}")