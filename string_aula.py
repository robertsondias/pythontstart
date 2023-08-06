frase = "Python é incrível"
primeiro_nome = "Robertson"
segundo_nome = "Dias"

#concatenar strigs
nome_completo = primeiro_nome + " " + segundo_nome
print(nome_completo)

#imprimir pulando caracteres
nome = nome_completo[0:14:2]
print(nome)

#find --> localiza o primeiro indice da substring em um string
print(frase.find("incrível"))

#upper ---> frase em maiúsculo
print (frase.upper())

#lower ---> frase em minusculo
print (frase.lower())

#replace ---> substituir string
print (frase.replace(" ", "-----"))