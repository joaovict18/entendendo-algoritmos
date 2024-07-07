def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) / 2
        chute = lista[meio]

        if chute == item:
            return meio
        
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    
    return None

# Exercícios - Respostas
# 1.1 ) O número máximo de etapas seria igual a quantidade de items, seguindo o padrão de pesquisa linear, assim sendo 128 etapas.
# 1.2 ) Duplicando a quantidade de items presentes na lista, o número de etapas continuaria sendo igual a quantidade de items, sendo assim, 256 etapas.