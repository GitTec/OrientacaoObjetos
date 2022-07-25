ano = int(input("INFORME O ANO ATUAL: "))


def anoAtual(infano):
    print("-" * 25)
    print(f"VOCÊ INFORMOU O ANO {infano}")
    print("-" * 25)


def anoBissexto(anobi):
    if (anobi % 4 == 0 and anobi % 100 != 0) or (anobi % 400 == 0):
        print("O ANO É BISSEXTO")
    else:
        print("O ANO NÃO É BISSEXTO!!!!!")


anoAtual(ano)
anoBissexto(anobi=ano)
