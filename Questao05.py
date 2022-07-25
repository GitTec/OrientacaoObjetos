
salario=float(input("INFORME SEU SALÁRIO: "))


def aumentosalario(sal):
    contsal = sal + (10 / 100 * sal)
    print(f"SEU NOVO SALÁRIO FICA {contsal:.2f}R$ COM OS 10% DE AUMENTO")


aumentosalario(sal=salario)