'''
http://www.bytebank.com.br/cambio





'''
# http://www.bytebank.com.br/cambio
import re

url = 'www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A url nao é valida.")
