
salario=float(input("INFORME SEU SALÁRIO: "))
contsal=salario + (10/100*salario)


def aumentosalario(consal):
    print(f"SEU NOVO SALÁRIO FICA {contsal:.2f}R$ COM OS 10% DE AUMENTO")


aumentosalario(consal=salario)