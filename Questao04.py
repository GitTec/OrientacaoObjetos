def mensagem():
    print("-"*20)

def tiponumero(number):
    if num < 0:
        mensagem()
        print(f"NÚMERO {number} É NEGATIVO")
        mensagem()
    elif num > 0:
        mensagem()
        print(f"NÚMERO {number} É POSITIVO")
        mensagem()
    else:
        mensagem()
        print("NUMERO É 0")
        mensagem()

num = int(input("INFORME UM NÚMERO: "))
tiponumero(num)