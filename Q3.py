def soma_nums(numList):
    soma = 0
    for num in numList:
        soma += num
    return soma


num_pares = [2, 4, 6, 8, 10]
print(soma_nums(num_pares))
