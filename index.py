# Grupos de até 4 alunos
# AC7 e AC8 de Lógica de Programação
# Prof. Dr. Alexandre l. Rangel
# Nome; Turma
# Aluno1: LEONARDO APRIGIO DA SILVA; SI 1B 
# Aluno2: 
# Aluno3:
# Aluno4:

tamanhoMenu = 50
opcoesMenu = ["1. DEPÓSITO","2. RETIRADA","3. EXTRATO","4. FIM"]
historico = []
# Esta função espaciona o Shell para deixa-lo limpo de informações desnecessarias

def apagaTela():
    print("\n"*100)

# Esta função exibe um menu, independente das opções passadas
# @menu é um parametro opcional que recebe uma lista de opções para o menu ser exibido. Caso vazio, usa a função @definirMenu() para gerar as opções
# @opcao é um parametro opcional que recebe um valor booleano onde é usado para definir se a lista informada em @menu será transformada em opções ou não

def exibirMenu(menu = "", opcao = False):
    if not menu:
        menu = definirMenu()
    elif (opcao):
        menu = definirMenu(menu)
    metadeMenu = tamanhoMenu // 2
    print("+" + "-" * tamanhoMenu + "+")
    for i in range (0, len(menu), 1):
        print ("|" + " "* (metadeMenu - 5) + menu[i] + " " * (metadeMenu - len(menu[i]) + 5) + "|")
    print("+" + "-" * tamanhoMenu + "+")       

# Esta função gera um lista de opções para ser usada em um menu
# @opcao é um parametro opcional onde recebe como valor uma lista de menu ja gerada, transformando-a em opcões. Caso vazio, gera uma lista de opções
# @return retorna a lista de opções criada

def definirMenu(opcao = ""):
    if not opcao:
        opcao = []
        contador = 0
        quantidadeOpcao = int(input("Digite o numero de opcões que terá: "))
        while (quantidadeOpcao < 1):
            print("O menu precisa ter pelo menos 1 opção")
            quantidadeOpcao = int(input("Digite o numero de opcões que terá: "))
        for i in range (1, quantidadeOpcao + 1, 1):
            itemMenu = input("Digite o nome do " + str(i) + "º item do menu: ")
            print("+" + "-" * tamanhoMenu + "+")
            print("|" + " " * 15 + "Torna-lo uma opção?" + " " * 16 + "|")
            print("+" + "-" * tamanhoMenu + "+")
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
            print("+" + "-" * tamanhoMenu + "+")
            print("|" + " " * 15 + "Torna-lo uma opção?" + " " * 16 + "|")
            if (len(opcao[i]) % 2 == 0):
                print("|" + " " * ((tamanhoMenu//2) - (len(opcao[i]) // 2)) + opcao[i] + " " * ((tamanhoMenu//2) - (len(opcao[i]) // 2)) + "|")
            else:
                print("|" + " " * ((tamanhoMenu//2) - (len(opcao[i]) // 2)) + opcao[i] + " " * ((tamanhoMenu//2) - (len(opcao[i]) // 2) - 1) + "|")
            print("+" + "-" * tamanhoMenu + "+")
            resposta = input("Digite S/N: ").upper()
            while not("S" in resposta or "N" in resposta):
                print("Digite 'S' para 'Sim' ou 'N' para 'Não': ")
                resposta = input("Digite S/N: ").upper()
            if (resposta == "S"):
                contador += 1
                itemMenu = str(contador) + ". " + opcao[i]
                opcao[i] = itemMenu
        return opcao

# Esta função adiciona um valor ao saldo do usuario
# @saldo recebe o saldo para calculo do valor
# @return retorna o saldo ja calculado

def deposito(saldo):
    exibirMenu(["DEPOSITO"])
    valor = float(input("Digite o valor a ser depositado: "))
    while (valor < 0):
        print("O valor nao pode ser negativo")
        valor = float(input("Digite o valor a ser depositado: "))
    saldo += valor
    historico.append("CREDITO +" + str(valor))
    print("Deposito efetuado com sucesso")
    print("Pressione ENTER para voltar")
    input()
    return saldo

# Esta função retira um valor do saldo do usuario
# @saldo recebe o saldo para calculo do valor
# @return retorna o saldo ja calculado

def retirada(saldo):
    exibirMenu(["RETIRADA"])
    valor = float(input("Digite o valor a ser retirado: "))
    while (valor < 0):
        print("O valor nao pode ser negativo")
        valor = float(input("Digite o valor a ser retirado: "))
    saldo -= valor
    historico.append("DEBITO  -" + str(valor))
    print("Retirada efetuada com sucesso")
    print("pressione ENTER para voltar")
    input()
    return saldo

# Esta função retorna o historico de todas as operações efetuadas
# @saldo recebe o valor do saldo atual para exibição

def extrato(saldo):
    exibirMenu(["EXTRATO"])
    statusSaldo = []
    statusSaldo.append("SALDO ATUAL: " + str(saldo))
    if (saldo > 0):
        statusSaldo.append("CONTA PREFERENCIAL")
    elif(saldo == 0):
        statusSaldo.append("CONTA ZERADA")
    else:
        statusSaldo.append("CONTA ESTOURADA")
    if not historico:
        exibirMenu(["NÃO HÁ LANÇAMENTOS"])
    else:
        exibirMenu(historico)
    exibirMenu(statusSaldo)
    print("pressione ENTER para voltar")
    input()

# Esta função exibe o saldo final para termino das operações
# @saldo recebe o saldo atual para exibição

def fim(saldo):
    statusSaldo = []
    statusSaldo.append("SALDO ATUAL: " + str(saldo))
    if (saldo > 0):
        statusSaldo.append("CONTA PREFERENCIAL")
    elif(saldo == 0):
        statusSaldo.append("CONTA ZERADA")
    else:
        statusSaldo.append("CONTA ESTOURADA")
    exibirMenu(statusSaldo)

# Função de entrada

def principal():
    apagaTela()
    flag = True
    saldo = float(input("Digite seu saldo: "))
    while (flag):
        apagaTela()
        exibirMenu(opcoesMenu)
        print("Seu saldo é de: " + str(saldo))
        opcao = int(input("Digite o numero da operação: "))
        while not(1 <= opcao <= 4):
            print("Operação invalida")
            opcao = int(input("Digite o numero da operação: "))
        if (opcao == 1):
            apagaTela()
            saldo = deposito(saldo)
        elif(opcao == 2):
            apagaTela()
            saldo = retirada(saldo)
        elif(opcao == 3):
            apagaTela()
            extrato(saldo)
        else:
            apagaTela()
            fim(saldo)
            flag = False
        
principal()
