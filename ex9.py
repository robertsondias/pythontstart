numero = 20
while True:
    palpite = int(input("Digite um numero: "))
    if numero == palpite:
        print("Numero correto")
        break
    if palpite > numero:
        print("tente novamente. Dica: O numero é menor")
    else:
        print("tente novamente. Dica: O numero é maior")