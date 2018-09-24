from django.db import models

from bancoTravis.menu import Menu
from bancoTravis.banco import Banco

class Main(models.Model):
    
    menu = Menu()
    banco = Banco()
    opcoesMenu = ["1. DEPÓSITO","2. RETIRADA","3. EXTRATO","4. FIM"]

    def principal(self):
        self.banco.setMenu(self.menu)
        self.menu.apagaTela()
        flag = True
        saldo = float(input("Digite seu saldo: "))
        while (flag):
            self.menu.apagaTela()
            self.menu.exibirMenu(self.opcoesMenu)
            print("Seu saldo é de: " + str(saldo))
            opcao = int(input("Digite o numero da operação: "))
            while not(1 <= opcao <= 4):
                print("Operação invalida")
                opcao = int(input("Digite o numero da operação: "))
            if (opcao == 1):
                self.menu.apagaTela()
                saldo = self.banco.deposito(saldo)
            elif(opcao == 2):
                self.menu.apagaTela()
                saldo = self.banco.retirada(saldo)
            elif(opcao == 3):
                self.menu.apagaTela()
                self.banco.extrato(saldo)
            else:
                self.menu.apagaTela()
                self.banco.fim(saldo)
                flag = False