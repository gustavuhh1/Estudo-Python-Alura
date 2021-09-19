from cpf_cnpj import Documento
from TelefonesBr import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco
import requests

print("++++++++++++++ViaCepAPI++++++++++++++++")

# CEP

cep = '60822610'
b = BuscaEndereco(cep)
print(b.acessa_viacep())


print("++++++++++++++DateTime++++++++++++++++")

# DateTime and TimeDelta
cadastro = DatasBr()
print(cadastro)

print("++++++++++++++TelefoneBr++++++++++++++")

# TELEFONE BR
telefone = "5585996103234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

print('++++++++++++++CPF_e_CNPJ++++++++++++++')

# CPF E CNPJ
exemplo_cnpj = "04165814000137"
exemplo_cpf = "41831775026"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento, ':Cpf')
documento2 = Documento.cria_documento(exemplo_cpf)
print(documento2, ':Cnpj')
