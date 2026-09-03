#declaraçao de variaveis
tempo_percurso: float = 0
velocidade_media: float = 0

#inicio
tempo_percurso = float(input("Digite o tempo de percurso em horas: "))
velocidade_media = float(input("Digite a velocidade media em km/h: "))
distancia_percorrida = tempo_percurso * velocidade_media
litros_combustivel = distancia_percorrida / 12
print(f"A quantidade de litros de combustivel consumidos e: {litros_combustivel:.2f}")
#fim