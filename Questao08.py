
def calcularPotencia(num, den):
    print("-"*25)
    print(f"{num} ELEVADO A {den} = {num**den}")
    print("-" * 25)


print("-"*25)
numer = int(input("INFORME NUMERADOR: "))
denom = int(input("INFORME DENOMINADOR: "))

calcularPotencia(numer, denom)
