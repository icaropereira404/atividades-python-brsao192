import unicodedata
import string

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def limpar_texto(texto):
    texto = texto.lower()  
    texto = remover_acentos(texto)  
    texto = ''.join(c for c in texto if c not in string.punctuation and not c.isspace())  
    return texto

frase = input("Digite uma palavra ou frase: ")

texto_limpo = limpar_texto(frase)

if texto_limpo == texto_limpo[::-1]:
    print("Sim")
else:
    print("Não")
