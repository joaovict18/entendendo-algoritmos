def contar(arr):
    contagem = 0
    if not arr:
        return 0
    else:
        contagem = 1 + contar(arr[1:])
        return contagem


# caso-base: o tamanho do array será apenas 1 caso ele seja composto de apenas 1 elemento
# caso recursivo: caso-base acrescido da própria função com a contagem do restante do array

print(contar([2, 4, 6, 9]))