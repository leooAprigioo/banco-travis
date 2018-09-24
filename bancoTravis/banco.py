from django.db import models

class Banco (models.Model):

    historico = []
    menu = object()

    def setMenu(self, menu):
        self.menu = menu

    def deposito(self, saldo):
        self.menu.exibirMenu(["DEPOSITO"])
        valor = float(input("Digite o valor a ser depositado: "))
        while (valor < 0):
            print("O valor nao pode ser negativo")
            valor = float(input("Digite o valor a ser depositado: "))
        saldo += valor
        self.historico.append("CREDITO +" + str(valor))
        print("Deposito efetuado com sucesso")
        print("Pressione ENTER para voltar")
        input()
        return saldo

    def retirada(self, saldo):
        self.menu.exibirMenu(["RETIRADA"])
        valor = float(input("Digite o valor a ser retirado: "))
        while (valor < 0):
            print("O valor nao pode ser negativo")
            valor = float(input("Digite o valor a ser retirado: "))
        saldo -= valor
        self.historico.append("DEBITO  -" + str(valor))
        print("Retirada efetuada com sucesso")
        print("pressione ENTER para voltar")
        input()
        return saldo
    
    def extrato(self, saldo):
        self.menu.exibirMenu(["EXTRATO"])
        statusSaldo = []
        statusSaldo.append("SALDO ATUAL: " + str(saldo))
        if (saldo > 0):
            statusSaldo.append("CONTA PREFERENCIAL")
        elif(saldo == 0):
            statusSaldo.append("CONTA ZERADA")
        else:
            statusSaldo.append("CONTA ESTOURADA")
        if not self.historico:
            self.menu.exibirMenu(["NÃO HÁ LANÇAMENTOS"])
        else:
            self.menu.exibirMenu(self.historico)
        self.menu.exibirMenu(statusSaldo)
        print("pressione ENTER para voltar")
        input()
    
    def fim(self, saldo):
        statusSaldo = []
        statusSaldo.append("SALDO ATUAL: " + str(saldo))
        if (saldo > 0):
            statusSaldo.append("CONTA PREFERENCIAL")
        elif(saldo == 0):
            statusSaldo.append("CONTA ZERADA")
        else:
            statusSaldo.append("CONTA ESTOURADA")
        self.menu.exibirMenu(statusSaldo)

