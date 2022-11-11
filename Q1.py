import heapq as hq
# é criada a lista de prioridade, com o indice de prioridade e o valor
list_car = [(4, 'conforto'), (1, 'eletronica'), (3, 'transmisssao'), (2, 'frenagem'), (5, 'retrovisor')]
# heapify transforma a lista em uma lista de prioridade, ordenando ela conforme o indice de cada elemento
hq.heapify(list_car)

print('The order of presentation is: ')
# a lista é impressa na ordem de prioridade
for i in list_car:
    print(i[0], ':', i[1])
