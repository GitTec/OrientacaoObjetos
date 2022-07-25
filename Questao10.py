import math


def areaTriangulo(ba, al):
    print("-"*25)
    print(f"A ÁREA DO TRIÂNGULO É {ba * al}")
    print("-" * 25)


def diagonal(al, ba):
    diag = math.sqrt(pow(al, 2) + pow(ba, 2))
    print(f"A DIAGONAL DO TRIÂNGULO É {diag:.2f}")


base = int(input("INFORME A BASE: "))
altura = int(input("INFORME A ALTURA: "))


areaTriangulo(ba=base, al=altura)
diagonal(al=altura, ba=base)