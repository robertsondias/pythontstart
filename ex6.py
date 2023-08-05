idade = int(input("Digite sua idade: "))
peso = int(input("Digite seu peso: "))
dormiu = int(input("Quantas hora dormiu nas ultimas 24 horas? "))

if (idade > 15 and idade < 70 and peso > 50 and dormiu > 6):
    print ("Você pode doar sangue. ")
else:
    print ("Você não pode doar sangue. ")