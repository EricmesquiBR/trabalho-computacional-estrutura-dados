import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('v1')
G.add_node('v2')
G.add_node('v3')
G.add_node('v4')
G.add_node('v5')

G.add_edge('v1', 'v2')
G.add_edge('v1', 'v3')
G.add_edge('v2', 'v4')
G.add_edge('v3', 'v4')
G.add_edge('v5', 'v1')
G.add_edge('v4', 'v5')
G.add_edge('v2', 'v4')

print('Lista de vértices: ')
print(G.nodes())


print('Preenchendo os vértices')
for v in G.nodes():
    print(v)


print('Lista de arestas: ')
print(G.edges())


print('Percorrendo as arestas')
for e in G.edges():
    print(e)


print('Percorrendo de graus de G')
print(G.degree())


print('O grau de vértice v2 é %d' %G.degree()['v2'])
print()

print('Grafo como lista de adjacências')
print(G['v1'])
print(G['v2'])
print(G['v3'])
print(G['v4'])
print(G['v5'])


print('Matriz de adjacência de G')
A = nx.adjacency_matrix(G)
print(A.todense())

G['v1']['v2']['peso'] = 5
G['v2']['v3']['peso'] = 10
G['v3']['v4']['peso'] = 2
G['v4']['v5']['peso'] = 7
G['v5']['v1']['peso'] = 4
G['v2']['v4']['peso'] = 8

print('Adicionando pesos às arestas')
for edge in G.edges():
    u = edge[0]
v = edge[1]
print('O peso da aresta', edge, 'vale', G[u][v]['peso'])
print('Plotando o grafo como imagem...')
plt.figure(1)
nx.draw_network(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()

