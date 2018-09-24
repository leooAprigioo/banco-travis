from django.db import models
from bancoTravis.banco import Banco

class Menu (models.Model):
    
    tamanhoMenu = 50

    def apagaTela(self):
        print("\n"*100)

    def exibirMenu(self, menu = "", opcao = False):
        if not menu:
            menu = self.definirMenu()
        elif (opcao):
            menu = self.definirMenu(menu)
        metadeMenu = self.tamanhoMenu // 2
        print("+" + "-" * self.tamanhoMenu + "+")
        for i in range (0, len(menu), 1):
            print ("|" + " "* (metadeMenu - 5) + menu[i] + " " * (metadeMenu - len(menu[i]) + 5) + "|")
        print("+" + "-" * self.tamanhoMenu + "+")
    
    def definirMenu(self, opcao = ""):
        if not opcao:
            opcao = []
            contador = 0
            quantidadeOpcao = int(input("Digite o numero de opcões que terá: "))
            while (quantidadeOpcao < 1):
                print("O menu precisa ter pelo menos 1 opção")
                quantidadeOpcao = int(input("Digite o numero de opcões que terá: "))
            for i in range (1, quantidadeOpcao + 1, 1):
                itemMenu = input("Digite o nome do " + str(i) + "º item do menu: ")
                print("+" + "-" * self.tamanhoMenu + "+")
                print("|" + " " * 15 + "Torna-lo uma opção?" + " " * 16 + "|")
                print("+" + "-" * self.tamanhoMenu + "+")
                resposta = input("Digite S/N: ").upper()
                while not("S" in resposta or "N" in resposta):
                    print("Digite 'S' para 'Sim' ou 'N' para 'Não': ")
                    resposta = input("Digite S/N: ").upper()
                if (resposta == "S"):
                    contador += 1
                    itemMenu = str(contador) + ". " + itemMenu
                    opcao.append(itemMenu)
                else:
                    opcao.append(itemMenu)
            return(opcao)
        else:
            itemMenu = ""
            contador = 0
            for i in range (0, len(opcao), 1):
                print("+" + "-" * self.tamanhoMenu + "+")
                print("|" + " " * 15 + "Torna-lo uma opção?" + " " * 16 + "|")
                if (len(opcao[i]) % 2 == 0):
                    print("|" + " " * ((self.tamanhoMenu//2) - (len(opcao[i]) // 2)) + opcao[i] + " " * ((self.tamanhoMenu//2) - (len(opcao[i]) // 2)) + "|")
                else:
                    print("|" + " " * ((self.tamanhoMenu//2) - (len(opcao[i]) // 2)) + opcao[i] + " " * ((self.tamanhoMenu//2) - (len(opcao[i]) // 2) - 1) + "|")
                print("+" + "-" * self.tamanhoMenu + "+")
                resposta = input("Digite S/N: ").upper()
                while not("S" in resposta or "N" in resposta):
                    print("Digite 'S' para 'Sim' ou 'N' para 'Não': ")
                    resposta = input("Digite S/N: ").upper()
                if (resposta == "S"):
                    contador += 1
                    itemMenu = str(contador) + ". " + opcao[i]
                    opcao[i] = itemMenu
            return opcao
    
    