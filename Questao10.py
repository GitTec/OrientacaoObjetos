import math


def areaTriangulo(ba, al):
    print("-"*25)
    print(f"A ÁREA DO TRIÂNGULO É {base * altura}")
    print("-" * 25)


def diagonal():
    diag = math.sqrt(pow(altura, 2) + pow(base, 2))
    print(f"A DIAGONAL DO TRIÂNGULO É {diag:.2f}")


base = int(input("INFORME A BASE: "))
altura = int(input("INFORME A ALTURA: "))


areaTriangulo(base, altura)
diagonal()