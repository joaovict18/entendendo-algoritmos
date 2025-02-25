def maior(arr):
    if not arr:
        return 0
    else:
        maior_elemento = arr[0]
        resto_lista = maior(arr[1:])

        if resto_lista > maior_elemento:
            maior_elemento = resto_lista
    
    return maior_elemento

print(maior([2, 4, 6]))