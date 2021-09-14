idades = [15, 87, 32, 65, 56, 32, 49, 37]


for i in range(len(idades)):
    print("posição:", i+1, "idade:", idades[i])
# ou melhor
# for indice, idade in enumerate(idades):
    #print(indice, "x", idade)


usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979),
]
# Crio variaveis para os valores de usuarios
# for nome, idade, ano in usuarios:
#print(nome , idade, ano)
# So quero a variavel nome
# for nome, _, _ in usuarios:
# print(nome)
