def verificarTriangulo(A,B,C):
    if A<=B+C and B<=A+C and C<=A+B:
        return 1
    return 0

def tipoTriangulo(A,B,C):
    if verificarTriangulo(1, 1, 1) == 1:
        if A==B and B==C:
            print("Triangulo Equilateral")
        else:
            if A!=B and A!=C and B!=C:
                print("Triangulo Escaleno")
            else:
                print("Triangulo Isosceles")
    else:
        print("Não é um trangulo")








