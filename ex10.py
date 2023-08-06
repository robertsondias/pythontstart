# MODO ARCÁICO
# compra01 = int(input("Digite o valor da primeira compra"))
# compra02 = int(input("Digite o valor da segunda compra"))
# compra03 = int(input("Digite o valor da terceira compra"))

# valortotal = compra01 + compra02 + compra03

# valortotal = valortotal + valortotal * 0.20

# print("O valor total com impostos é " +str(valortotal))

total = 0
imposto = 0.1

while True:
    valor_item = input("Digite o valor do produto ou pressione S para sair ")
    if valor_item == 'S':
        break
    total = total + float(valor_item)
    
total = total * imposto + total
    
print("O valor total com impostos é:", total)
    