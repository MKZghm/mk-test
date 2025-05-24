velocidade_maxima = int(input("Digite a velocidade máxima permitida (km/h): "))
velocidade_registrada = int(input("Digite a velocidade registrada do veículo (km/h): "))

if velocidade_registrada <= velocidade_maxima:
    print("Velocidade dentro do limite. Dirija com segurança.")
else:
    excesso = velocidade_registrada - velocidade_maxima
    multa = excesso * 5.00
    print(f"Você ultrapassou o limite em {excesso} km/h.")
    print(f"Valor da multa: R$ {multa:.2f}")