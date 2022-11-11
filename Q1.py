import heapq as hq

# é criada a lista de prioridade
list_car = [(4, 'conforto'), (1, 'eletronica'), (3, 'transmisssao'), (2, 'frenagem'), (5, 'retrovisar')]
# heapify transforma a lista em uma lista de prioridade
hq.heapify(list_car)

print('The order of presentation is: ')
# a lista é impressa na ordem de prioridadeö
for i in list_car:
    print(i[0], ':', i[1])
