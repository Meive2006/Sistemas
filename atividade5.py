def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma

# Testando a função com uma lista diferente
nova_lista = [10, 15, 22, 33, 42, 55, 60, 73, 88, 91, 66, 70, 73, 52]
resultado = soma_pares(nova_lista)
print(f"A soma dos números pares é: {resultado}")