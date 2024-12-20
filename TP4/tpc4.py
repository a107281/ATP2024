# Solução do TPC4

def Menu():
    print("---------------- MENU -------------------")
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procurar um elemento")
    print("(0) Sair")
    print("-----------------------------------------")

def Criar_Lista():
    import random
    
    N = int(input("Introduza o número máximo de elementos que deseja ter na sua lista."))
    lista = []
    i = 0
    while i < N:
        num = random.randint(1,100)
        lista.append(num)
        i = i + 1
    return lista


def Ler_Lista():
    lista = []
    x = input("Digite um número para a sua lista. Quando não desejar introduzir mais números, escreva 'fim'. ")
    while x != "fim":
        y = int(x)
        lista.append(y)
        x = input("Digite um número para a sua lista. Quando não desejar introduzir mais números, escreva 'fim'.")
    return lista


def Soma_Lista(lista):
    i = 0
    soma = 0
    while i < len(lista):
        soma = soma + lista[i]
        i = i + 1
    return soma


def Media_Lista(lista):
    media = 0
    soma = Soma_Lista(lista)

    if len(lista) != 0:
        media = soma / len(lista)
    return media


def Maior_Lista(lista):
    i = 1
    maior = lista[0]

    while i < len(lista):
        if lista[i] > maior:
            maior = lista[i]
        i = i + 1
    return maior


def Menor_Lista(lista):
    i = 1
    menor = lista[0]

    while i < len(lista):
        if lista[i] < menor:
            menor = lista[i]
        i = i + 1
    return menor


def Esta_Ordenada_Por_Ordem_Crescente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return "Não"
    return "Sim"


def Esta_Ordenada_Por_Ordem_Decrescente(lista):
    for i in range(len(lista) - 1):
        if lista[i] < lista[i + 1]:
            return "Não"
    return "Sim"


def Procurar_Elemento(lista):
    x = int(input("Que elemento deseja encontrar na lista?"))
    if x in (lista):
        return lista.index(x)
    else: 
        return "-1"
    

def Main():
    lista = []
    cond = True

    while cond:
        Menu()
        opcao = input("Insira a opção pretendida.")
    
        if opcao == "1":
            lista = Criar_Lista()
            print(lista)

        elif opcao == "2":
            lista = Ler_Lista()
            print(lista)

        elif opcao == "3":
            res = Soma_Lista(lista)
            print(res)

        elif opcao == "4":
            res = Media_Lista(lista)
            print(res)

        elif opcao == "5":
            res = Maior_Lista(lista)
            print(res)

        elif opcao == "6":
            res = Menor_Lista(lista)
            print(res)

        elif opcao == "7":
            res = Esta_Ordenada_Por_Ordem_Crescente(lista)
            print(res)

        elif opcao == "8":
            res = Esta_Ordenada_Por_Ordem_Decrescente(lista)
            print(res)

        elif opcao == "9":
            res = Procurar_Elemento(lista)
            print(res)

        elif opcao == "0":
            cond = False
            print("Até à próxima!")


Main()