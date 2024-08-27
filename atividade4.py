def ordenacao_por_insercao(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

numeros = [5, 2, 9, 1, 5, 6, 8, 3, 7, 4, 13, 10, 12]

ordenacao_por_insercao(numeros)
print(f"Lista ordenada: {numeros}")