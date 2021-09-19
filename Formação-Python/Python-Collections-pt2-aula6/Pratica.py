from collections import defaultdict
from collections import Counter
texto1 = "Fria e calculista’. É dessa forma que a Polícia Civil de Mato Grosso classificou Ana Cláudia Flor, viúva do empresário Toni da Silva Flor, de 37 anos, morto há pouco mais de um ano em Cuiabá.De acordo com o delegado responsável pela investigação, Marcel Gomes de Oliveira, a mulher, que chegou a liderar uma mobilização na cidade pedindo justiça pelo assassinato do marido, é apontada como a mandante do crime, que teria sido planejado por motivação financeira."

texto2 = "Jimmy, baterista do grupo Molejo, e sua mulher, Cristiane Sales, denunciaram à Polícia Civil que o filho do casal, George, que tem apenas 7 anos, foi vítima de preconceito por ser autista. Segundo eles, uma vizinha da família, que mora em um condomínio na Zona Oeste do Rio de Janeiro, afirmou: depois que autismo virou moda, retardado tinha mudado de nome."


def analisa_frequncia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcao = [(letra, frequencia / total_de_caracteres)
                 for letra, frequencia in aparicoes.items()]
    proporcao = Counter(dict(proporcao))
    mais_comuns = proporcao.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("´{}´ => {:.2f}%".format(caractere, proporcao*100))


analisa_frequncia_de_letras(texto2)
analisa_frequncia_de_letras(texto1)
