#declaraçao de variaveis
salario: float = 0.0
salarioNovo: float = 0.0

#inicio
salario = float(input("digite o salario do funcionario:"))
salarioNovo = (salario * 1.15)
print (f"O salario novo do funcionario com o reajuste e: {salarioNovo: .2f}")
#fim