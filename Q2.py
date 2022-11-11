import heapq as hq
# é criada a lista de prioridade, com o indice de prioridade e o valor
list_func = [(4, 'F(N) = 2 ^ N'), (1, 'H(N) = Nlog(N)'), (3, 'S(N) = N ^ log(N)'), (2, 'G(N) = N ^ 3/2')]
# heapify transforma a lista em uma lista de prioridade, ordenando ela conforme o indice de cada elemento
hq.heapify(list_func)

print('The order of presentation is: ')
# a lista é impressa na ordem de prioridade
for i in list_func:
    print(i[0], ':', i[1])