#declaraçao de variaveis
celsius: float = 0.0
fahrenheit: float = 0.0

#inicio
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (9*celsius + 160) / 5
print (f"A temperatura em Fahrenheit e: {fahrenheit: .2f}")
#fim