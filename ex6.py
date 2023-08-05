idade = input("Digite sua idade: ")
peso = input("Digite seu peso: ")
dormiu = input("Quantas hora dormiu nas ultimas 24 horas? ")

idade = int (idade)
peso = int (peso)
dormiu = int (dormiu)

if (idade > 15 and idade < 70 and peso > 50 and dormiu > 6):
    print ("Você pode doar sangue. ")
else:
    print ("Você não pode doar sangue. ")