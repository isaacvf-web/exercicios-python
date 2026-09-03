#declaraçao de variaveis
cateto1: float = 0
cateto2: float = 0

#inicio
cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))
hipotenusa = (cateto1 ** 2 + cateto2 ** 2)
print(f"O valor da hipotenusa e: {hipotenusa}")
#fim