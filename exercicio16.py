#declaraçao de variaveis
horas_trabalhadas: float = 0
valor_hora: float = 0
percentual_desconto: float = 0
dependentes: int = 0

#inicio
horas_trabalhadas = float(input("Digite o numero de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
dependentes = int(input("Digite o numero de dependentes: "))
salario_bruto = horas_trabalhadas * valor_hora
salario_liquido = salario_bruto - (salario_bruto * percentual_desconto / 100)
salario_a_receber = salario_liquido + (dependentes * 100)
print(f"O salario a receber e: R$ {salario_a_receber:.2f}")
##fim