def soma(arr):
    if not arr:
        return 0
    else:
        return arr[0] + soma(arr[1:]) 

print(soma([2, 4, 6]))

# caso-base: a soma dos elementos no array assume apenas o único elemento existente no array, caso exista
# caso recursivo: caso-base acrescido a própria função aplicada no restante dos elementos do array
# soma([2, 4, 6)] => 2 + soma([4, 6]) => 4 + soma([6]) => [6] => 6