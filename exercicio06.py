#declaraçao de variaveis
x: float = 0
y: float = 0
aux: float = 0

#inicio
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
aux = x
x = y
y = aux
print("O valor de x e:", x)
print("O valor de y e:", y)
#fim