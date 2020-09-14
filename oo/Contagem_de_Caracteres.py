def contar_caracteres(s):
    """"Função que contar os caracteres de uma string

    Ex:
    >>> contar_caracteres('Rosemedjina')
    a:1
    d:1
    e:2
    i:1
    j:1
    m:1
    R:1
    S:1
    >>> contar_caracteres('banana')
    a:3
    b:1
    n:2
    : param s: string ser conatada
    """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}:{contagem}')
            caracter_anterior = caracter
            contagem =1
            

    print(f'{caracter_anterior}:{contagem}')

if __name__ == '__main__':
    contar_caracteres('Rosemedjina')
    print()
    contar_caracteres('banana')



