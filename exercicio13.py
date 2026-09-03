#declaraçao de variaveis
quilos: float = 0
gramas_ao_dia: float = 0

#inicio
quilos = float(input("Digite a quantidade de quilos de alimento: "))
gramas_ao_dia = float(input("Digite a quantidade de gramas de alimento consumida por dia: "))
gramas_ao_dia = gramas_ao_dia / 1000  # Converter para quilos
dias = (quilos / gramas_ao_dia)
print(f"A quantidade de dias que o alimento durara e: {dias}")
#fim