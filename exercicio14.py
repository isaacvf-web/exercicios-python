#declaraçao de variaveis
angulo1: float = 0
angulo2: float = 0
angulo3: float = 0

#inicio
angulo1 = float(input("Digite o primeiro angulo do triangulo: "))
angulo2 = float(input("Digite o segundo angulo do triangulo: "))
angulo3 = 180 - (angulo1 + angulo2)
print(f"O terceiro angulo do triangulo e: {angulo3}")
#fim