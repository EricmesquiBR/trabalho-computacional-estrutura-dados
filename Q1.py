import heapq as hq

list_car = [(3, 'transmisssao'), (1, 'eletronica'), (5, 'retrovisar'), (2 , 'frenagem'), (4, 'conforto')]
hq.heapify(list_car)

print('The order of presentation is: ')

for i in list_car:
    print(i[0], ':', i[1])