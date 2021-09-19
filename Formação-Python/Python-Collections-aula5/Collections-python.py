# Lista
idades = [39, 30, 27, 18]
# Imprime o primero valor [0] da lista
print(f'Imprimindo a idade no lugar [0]: {idades[0]}')
# Adiciona a idade 15 em idades no final da lista
idades.append(15)
idades.append(15)
# Adiciona idade 23 em uma certa posição
idades.insert(0, 23)
# Remover a idade 15 em idades (ele tira apenas uma unidade)
idades.remove(15)
# Remove todos os Elementos
# >>> idades.clear()
# Pegunta se possui um elemento na lista (in)
if 15 in idades:
    print(f'idade 15 esta na lista')
else:
    print(f'idade 15 não esta na lista')
# fazer uma lista Idades no proximo ano
idades_no_proximo_ano = []
for idade in idades:
    idades_no_proximo_ano.append(idade+1)
# ou
idades_no_proximo_ano = [(idade+1) for idade in idades]
# com condição
idades_no_proximo_ano = [(idade) for idade in idades if idade > 21]


print(idades, " 2020")
print(idades_no_proximo_ano, " 2021")
