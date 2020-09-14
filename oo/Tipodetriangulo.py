A= float(input())
B= float(input())
C= float(input())
N1= float(1)
N2= float(1)
N3= float(1)

if A>=B and A>=C:
    N1=A
    if B>=C:
        N2=B
        N3=C
    else:
        N2=C
        N3=B

if B>=A and B>=C:
    N1=B
    if A>=C:
        N2=A
        N3=C
    else:
        N2=C
        N3=A
if C>=A and C>=B:
    N1=C
    if A>=B:
        N2=A
        N3=B
    else:
        N2=B
        N3=A
if A==B and B==C:
    N1=A
    N2=B
    N3=C
    A=N1
    B=N2
    C=N3

if  A >= B+C:
    print("NAO FORMA TRIANGULO")
elif A**2 == B**2 + C**2:
    print("TRIANGULO RETANGULO")
elif A**2 > B**2 + C**2:
    print("TRIANGULO OBTUSANGULO")
elif A**2 < B**2 + C**2:
    print("TRIANGULO ACUTANGULO")
elif A==B and B==C:
    print("TRIANGULO EQUILATERO")
elif A==B or A==C or B==C:
    print("TRIANGULO ISOSCELES")



