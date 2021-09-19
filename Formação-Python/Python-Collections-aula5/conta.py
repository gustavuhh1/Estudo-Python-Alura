class ContaCorrente:
    def __init__(self, titular, codigo, saldo):
        self.titular = str(titular)
        self.codigo = codigo
        self.saldo = saldo

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return ">>> Titular: {} Codigo: {} Saldo: {} <<<".format(self.titular, self.codigo, self.saldo)


conta_do_gui = ContaCorrente("Guilherme", 132, 300)
conta_do_gui.deposita(300)

conta_da_dani = ContaCorrente("Daniela", 231, 500)
conta_da_dani.deposita(200)

contas = (conta_da_dani, conta_do_gui)
for conta in contas:
    print(conta)

# Segunda representação
gustavo = ("Gustavo", 16)
carlos = ("Carlos", 32)

usuarios = [gustavo, carlos]
print(usuarios)

roberta = ("Roberta", 21)
usuarios.append(roberta)
print(usuarios)

