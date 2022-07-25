ano = int(input("INFORME O ANO ATUAL: "))


def anoAtual(infano):
    print("-" * 25)
    print(f"VOCÊ INFORMOU O ANO {infano}")
    print("-" * 25)


def anoBissexto():
    if (ano % 4 == 0) or (ano % 100 != 0) or (ano % 400 == 0):
        print("O ANO É BISSEXTO")
    else:
        print("O ANO NÃO É BISSEXTO!!!!!")


anoAtual(ano)
anoBissexto()
