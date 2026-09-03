#declaraçao de variaveis
import math
A: float = 0
B: float = 0
C: float = 0
delta: float = 0
x1: float = 0
x2: float = 0

#inicio
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
delta = B*B - 4*A*C
#se o delta for menor que 0, nao existe raiz real
if delta < 0:
    print("Nao existe raiz real")
    #se o delta for igual ou maior a 0, existe raiz real
else: 
    x1 = (-B + math.sqrt(delta)) / (2*A)
    x2 = (-B - math.sqrt(delta)) / (2*A)
    print("O valor de x1 e:", x1)
    print("O valor de x2 e:", x2)
#fim