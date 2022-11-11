import networkx as nx
import matplotlib.pyplot as plt

# Cria o grafo
G = nx.Graph()

# Cria os vértices do grafo
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')

# Cria as arestas do grafo
G.add_edge('B', 'A')
G.add_edge('B', 'D')
G.add_edge('B', 'C')
G.add_edge('D', 'C')
G.add_edge('D', 'E')

# Mostra os vértices do grafo
print('Lista de vértices: ')
print(G.nodes())


print('Preenchendo os vértices')
for v in G.nodes():
    print(v)

# Mostra as arestas do grafo
print('Lista de arestas: ')
print(G.edges())


print('Percorrendo as arestas')
for e in G.edges():
    print(e)


print('Percorrendo de graus de G')
print(G.degree())


print('O grau de vértice B é %d' %G.degree()['B'])
print()

# Mostra a lista de adjacência do grafo
print('Grafo como lista de adjacências')
print(G['A'])
print(G['B'])
print(G['C'])
print(G['D'])
print(G['E'])

# Mosta a matriz binária de adjacência do grafo
print('Matriz de adjacência de G')
A = nx.adjacency_matrix(G)
print(A.todense())

# Define o peso de cada aresta do grafo
G['B']['A']['peso'] = 1
G['B']['D']['peso'] = 2
G['B']['C']['peso'] = 2
G['D']['C']['peso'] = 3
G['D']['E']['peso'] = 1

# Adiciona o peso de cada aresta no grafo
print('Adicionando pesos às arestas')
for edge in G.edges():
    u = edge[0]
v = edge[1]
print('O peso da aresta', edge, 'vale', G[u][v]['peso'])
# Uso do método draw do networkx para desenhar o grafo e plota ele com o matplotlib
print('Plotando o grafo como imagem...')
plt.figure(1)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()

