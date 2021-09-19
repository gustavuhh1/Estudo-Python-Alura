import requests


class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido")

    def __str__(self):
        return self.cep_mask()

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def cep_mask(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_viacep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
