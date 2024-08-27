def eh_palindromo(s):
    s = s.lower().replace(" ", "") 
    return s == s[::-1]
palavras = ["radar", "level", "python", "ana", "madam", "palavra", "arara", "meive"]
for palavra in palavras:
    resultado = eh_palindromo(palavra)
    print(f"A string '{palavra}' é um palíndromo? {resultado}")