numero = int(input("Digite um número: "))
soma_divisores = 0
i = 1

while i < numero:
    if numero % i == 0:
        soma_divisores += i
    i += 1

if soma_divisores == numero:
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")
