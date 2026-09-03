#declaraçao de variaveis
ano_de_nascimento: int = 0
ano_atual: int = 0
idade_atual: int = 0
idade_futura: int = 0

#inicio
ano_de_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade_atual = ano_atual - ano_de_nascimento
idade_futura = idade_atual + 17
print(f"A idade futura da pessoa daqui a 17 anos sera: {idade_futura}")
#fim