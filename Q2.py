import heapq as hq

# é criada a lista de prioridade
list_car = [(4, 'F(N) = 2 ^ N'), (1, 'H(N) = Nlog(N)'), (3, 'S(N) = N ^ log(N)'), (2, 'G(N) = N ^ log(N)')]
# heapify transforma a lista em uma lista de prioridade
hq.heapify(list_car)

print('The order of presentation is: ')
# a lista é impressa na ordem de prioridadeö
for i in list_car:
    print(i[0], ':', i[1])