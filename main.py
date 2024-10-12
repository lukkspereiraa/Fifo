import random

def criar_referencia(qtd_paginas, valor_maximo=9):
    return [random.randint(0, valor_maximo) for _ in range(qtd_paginas)]

def fifo_substituicao(lista_paginas, tamanho_quadros):
    quadros_memoria = []
    falhas_pagina = 0
    
    for pagina in lista_paginas:
        if pagina not in quadros_memoria:
            falhas_pagina += 1
            if len(quadros_memoria) < tamanho_quadros:
                quadros_memoria.append(pagina)
            else:
                quadros_memoria.pop(0)
                quadros_memoria.append(pagina)
    
    return falhas_pagina

def lru_substituicao(lista_paginas, tamanho_quadros):
    quadros_memoria = []
    falhas_pagina = 0
    ultima_utilizacao = {}
    
    for tempo, pagina in enumerate(lista_paginas):
        if pagina not in quadros_memoria:
            falhas_pagina += 1
            if len(quadros_memoria) < tamanho_quadros:
                quadros_memoria.append(pagina)
            else:
                menos_usada = min(quadros_memoria, key=lambda p: ultima_utilizacao[p])
                quadros_memoria.remove(menos_usada)
                quadros_memoria.append(pagina)
        ultima_utilizacao[pagina] = tempo 
    
    return falhas_pagina

def testar_algoritmos(paginas_acessadas, max_quadros):
    print(f"Referência de páginas: {paginas_acessadas}")
    
    for qtd_quadros in range(1, max_quadros + 1):
        falhas_fifo = fifo_substituicao(paginas_acessadas, qtd_quadros)
        falhas_lru = lru_substituicao(paginas_acessadas, qtd_quadros)
        
        print(f"\nNúmero de quadros: {qtd_quadros}")
        print(f"FIFO - Falhas: {falhas_fifo}")
        print(f"LRU  - Falhas: {falhas_lru}")
            
        if falhas_fifo < falhas_lru:
            print("FIFO teve menos falhas.")
        elif falhas_fifo > falhas_lru:
            print("LRU teve menos falhas.")
        else:
            print("Ambos os algoritmos tiveram a mesma quantidade de falhas.")

quantidade_paginas = 20
max_quadros = 5
lista_paginas = criar_referencia(quantidade_paginas)
testar_algoritmos(lista_paginas, max_quadros)