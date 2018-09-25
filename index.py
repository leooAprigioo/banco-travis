class Banco():
    saldo = 0
    def deposito(self, valor):
        self.saldo += valor
        return True

    def saque(self, valor):
        if (valor > self.saldo):
            print("Digite um valor menor que o saldo atual")
            return False
        self.saldo -= valor
        return True

    def exibirSaldo(self):
        print(str(self.saldo))
