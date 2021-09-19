endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Regular Expression -- ReqEx

# 5 Dígitos + hifen (opcional) + 3 dígitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) # Match
if busca:
    cep = busca.group()
    print(cep)

