# esse é um parâmetro. O parâmetro é a VARIÁVEL "OPERAÇÃO". Parametro é quando modera a função

nome = "python"
def soma_multiplicacao(valor1, valor2, operacao):
    if operacao == "somar":
        resultado = valor1 + valor2
    if operacao == "multiplicar":
        resultado = valor1 * valor2
    return resultado
print(nome)

    
valor_1 = float(input("passe o primeiro valor: "))
valor_2 = float(input("passe o segunto valor: "))
opcao = input("Qual operação será feita?")
resultado = soma_multiplicacao(valor_1, valor_2, opcao)
print(resultado, "opcao escolhida é", opcao)

# def soma(a,b):  # é argumentos, pois foram informações utilizadas para geradar resultado. 
#É quando insere informações p/ ajudar na função.

#     resultado = a + b
#     return resultado

# print(soma(4,10))

# soma_lados = (soma(40,10))
# print("A soma dos lados é: ", soma_lados)