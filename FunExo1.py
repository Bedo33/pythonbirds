# def verificarTriangulo(A,B,C):
#     if A<=B+C and B<=A+C and C<=A+B:
#         print("É um triangulao")
#     else:
#         print("Não é um triangulo")
#
# verificarTriangulo("15","10","4")

def verificarTriangulo(A,B,C):
    if A<=B+C and B<=A+C and C<=A+B:
        return 1
    return 0
if verificarTriangulo(1,1,1) == 1:
    print("É um triangulo")
else:
    print("Não é um triangulo")