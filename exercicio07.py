#declaraça de variaveis
comprimento: float = 0
largura: float = 0
altura: float = 0

#inicio
comprimento = float(input("Digite o comprimento do paralelepipedo: "))
largura = float(input("Digite a largura do paralelepipedo: "))
altura = float(input("Digite a altura do paralelepipedo: "))
volume = comprimento * largura * altura
print("O volume do paralelepipedo e:", volume)
#fim