#declaraçao de variaveis
deposito: float = 0
meses: int = 0

#inicio
deposito = float(input("Digite o valor do deposito: "))
meses = int(input("Digite o numero de meses: "))
valor_final = deposito * (1.013 ** meses)
print("O valor final do deposito e: ", round(valor_final, 2))
#fim