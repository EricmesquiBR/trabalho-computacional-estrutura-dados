# função recursiva conforme o slide 10 da aula 7 que soma os números
def soma_nums(numList):
    # variável que armazena a soma
    soma = 0
    # loop para somar os números
    for num in numList:
        soma += num
    #retorna a soma
    return soma

# array com os 5 primeiros números pares não nulos
num_pares = [2, 4, 6, 8, 10]
# print para a soma dos números
print(soma_nums(num_pares))
