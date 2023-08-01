# =============================================== TRABALHO DE GRUPO EDA ================================================
# ISCTE-IUL
# 1º ano | Licenciatura em Ciência de Dados
# Trabalho de Grupo Final | U.C. Estruturas de Dados e Algoritmos
# André Silvestre Nº104532 | Diogo Catarino Nº104745 | Francisco Gomes Nº104944
# ======================================================================================================================

# ----------------- Imports -----------------
import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import csv
import pandas as pd
pd.options.mode.chained_assignment = None
matplotlib.use('Qt5Agg')
# -------------------------------------------

# ========
#  FASE 1
# ========

# ================================================ [CLASS VERTEX] ================================================


class Vertex:  # Classe Vértice - User do Facebook

    # [Construtor] - só tem um atributo/id que guarda o objeto que pretendemos guardar nesse vértice
    def __init__(self, x):
        self._id = x

    # [id] - Devolve o id neste vértice
    @property
    def id(self):
        return self._id

    # [__eq__] - Função booleana que diz se um Vértice de id X é igual ao Vértice em que estamos (o do self)
    #            É obrigatório definir a função __eq__ quando se define a função __hash__
    def __eq__(self, x):
        return x == self._id  # x é um objeto- quero saber com esta função
        # se é igual ao objeto/item que está guadado no self._id

    # [__hash__] - Getter para obter a identificação de um Vértice feito chamando as funções hash() e id() do Python
    #              Devolve um inteiro que identifica este vértice como uma chave num dicionário
    def __hash__(self):
        return hash(self._id)

    # [__str__] - Função que devolve o objeto guardado no Vértice em string
    def __str__(self):
        return '{0}'.format(self._id)


# ------------------------------------------------ [TESTE VERTEX] -------------------------------------------------
if __name__ == "__main__":
    # [Teste do Vertex]
    v1 = Vertex(10)
    print("------- [VERTEX 1] -------\n", "Vértice ->", v1)
    print("Hash ->", v1.__hash__())

    v2 = Vertex(20)
    print("\n------- [VERTEX 2] -------\n", "Vértice ->", v2)
    print("Hash ->", v2.__hash__())

    v3 = Vertex(10)
    print("\n------- [VERTEX 3] -------\n", "Vértice ->", v3)
    print("Hash ->", v3.__hash__())

    print("\n[COMPARAÇÃO ENTRE V1 E V2 - __eq__] -> ", v1 == v2)
    print("[COMPARAÇÃO ENTRE V1 E V3 - __eq__] -> ", v1 == v3)
    print("[COMPARAÇÃO ENTRE V2 E V3 - __eq__] -> ", v2 == v3)
    print("---------------------------------------------------------------\n")


# ================================================ [CLASS EDGE] ================================================


class Edge:  # Classe Aresta - Conecção entre Users
    """Estrutura de Aresta - (origem, destino), com peso - para um grafo"""

    # [Contrutor] - Inicializa os atributos vértice de origem, vértice de destino e peso
    def __init__(self, u, v, p):
        """A aresta será inserida no no Grafo usando insert_edge(u,v,x)"""
        self._origem = u
        self._destino = v
        self._peso = p

    # [origem] - Devolve o Vértice Origem
    @property
    def origem(self):
        return self._origem

    # [destino] - Devolve o Vértice destino
    @property
    def destino(self):
        return self._destino

    # [peso] - Devolve o Peso da Aresta
    @property
    def peso(self):
        return self._peso

    # [endpoints] - Função que devolve num tuple os dois vértices associados à aresta
    @property
    def endpoints(self):
        return self._origem, self._destino

    # [opposite] - Dado um vértice v (que pode ser origem ou destino desta aresta) devolve o vértice que está na
    #              outra ponta da aresta
    def opposite(self, v):
        # O if - else compacto lê-se -> se v é o vértice origem da aresta, a função devolve o vértice destino
        # Caso contrário devolve o vértice origem
        return self._destino if v is self._origem else self._origem

    # [__eq__] - Função booleana que compara duas Arestas.
    #           É obrigatório definir a função __eq__ quando se define a função __hash__
    def __eq__(self, other):
        return self._origem == other.origem and self._destino == other.destino

    # [__hash__] - Função que devolve um identificador único para a edge/aresta usando a função hash() do
    #              Python sobre o tuplo (vértice origem, vértice destino)
    def __hash__(self):
        return hash((self._origem, self._destino))

    # [__str__] -Função que devolve a informação(origem, destino) em string
    def __str__(self):
        return '({0},{1} | {2})'.format(self._origem, self._destino, self._peso)


# ------------------------------------------------ [TESTE EDGE] -------------------------------------------------
if __name__ == "__main__":
    # [Teste da Edge]
    print("------- [EDGE 1] -------")
    e1 = Edge(1, 3, 1)  # Edge que liga o vértice 1 e 3 com peso 1
    print("Aresta ->", e1)
    print("Hash ->", e1.__hash__())

    print("\n------- [EDGE 2] -------")
    e2 = Edge(4, 5, 20)  # Edge que liga o vértice 4 e 5 com peso 20
    print("Aresta ->", e2)
    print("Hash ->", e2.__hash__(), "\n")

    print("\n------- [EDGE 3] -------")
    e3 = Edge(1, 3, 1)  # = ao Edge 1
    print("Aresta ->", e3)
    print("Hash ->", e3.__hash__(), "\n")

    print("\n[COMPARAÇÃO ENTRE E1 E E2 - __eq__] -> ", e1 == e2)
    print("[COMPARAÇÃO ENTRE E1 E E3 - __eq__] -> ", e1 == e3)
    print("[COMPARAÇÃO ENTRE E2 E E3 - __eq__] -> ", e2 == e3)
    print("---------------------------------------------------------------\n")


# ================================================ [CLASS GRAFO] ================================================
class Graph:
    """Representação de um grafo usando mapas de adjacências (associações)"""

    # [Construtor do Grafo] - Inicializa os atributos directed, number e vertices
    def __init__(self, directed=False):
        """Cria um grafo vazio (contentor _vertices); é orientado se o parâmetro directed tiver o valor True"""
        self._directed = directed  # indica se o grafo é dirigido (valor True) ou não (valor False)
        self._number = 0  # quantidade de nós
        self._vertices = {}  # dicionário com os vários vértices como chaves e em que o valor
        # associado a cada vértice é o dicionário de adjacências desse vértice
        # (associação: outro_vértice -> aresta que os liga)

    # [insert_vertex] - Insere e devolve um novo vértice com o id x
    def insert_vertex(self, x):
        v = Vertex(x)  # Criar um vértice chamando o seu construtor e passando o objeto x a guardar no vértice
        if v not in self._vertices.keys():
            self._vertices[v] = {}  # Inicializar o dicionário/mapa de adjacências correspondente ao vértice v a vazio
            self._number += 1
        return v

    # [insert_edge] - Insere e devolve uma nova aresta entre u e v com peso x
    def insert_edge(self, u, v, x=None):
        e = Edge(u, v, x)
        self._vertices[u][v] = e  # vai colocar nas incidências de u
        self._vertices[v][u] = e  # e nas incidências de v (para facilitar a procura de todos os arcos incidentes)
        return e

    # [is_directed] - Indica se o grafo é Direcionado ou Não Direcionado
    @property
    def is_directed(self):
        return self._directed

    # [vertex_count] - Devolve a quantidade de vértices no grafo
    @property
    def vertex_count(self):
        return self._number

    # [vertices] - Devolve um iterável sobre todos os vértices do Grafo
    @property
    def vertices(self):
        return self._vertices.keys()

    # [edge_count] - Devolve a quantidade de arestas do Grafo
    @property
    def edge_count(self):
        total = sum(len(self._vertices[v]) for v in self._vertices)
        # Para grafos não direcionados, certificar que não vai contar duas vezes as arestas
        return total if self._directed else total // 2

    # [edges] - Devolve o conjunto de todas as arestas do Grafo
    @property
    def edges(self):
        result = set()
        for secondary_map in self._vertices.values():
            result.update(secondary_map.values())
        return result

    # [incident_edges] - Gera todas as arestas apartir de um dado vértice v
    def incident_edges(self, v, outgoing=True):
        """Gerador: indica todas as arestas (outgoing) incidentes em v
        Se for um grafo dirigido e outgoing for False, devolve as arestas em incoming
        """
        for edge in self._vertices[v].values():  # para todas as arestas relativas a v:
            if not self._directed:
                yield edge
            else:  # senão deve ir procurar em todas as arestas para saber quais entram ou saiem
                x, y = edge.endpoints()
                if (outgoing and x == v) or (not outgoing and y == v):
                    yield edge

    # [get_edge] - Devolve a aresta que liga u e v ou None se não forem adjacentes
    def get_edge(self, u, v):
        edge = self._vertices[u].get(v)  # returns None se não existir aresta alguma entre u e v
        if edge != None and self._directed:  # se é dirigido
            _, x = edge.endpoints  # vai confirmar se é u --> v
            if x != v:
                edge = None
        return edge

    # [degree] - Devolve a quantidade de arestas incidentes no vértice v
    def degree(self, v, outgoing=True):
        """Se for Dirigido, conta apenas as arestas Outcoming ou em Incoming, de acordo com o valor de Outgoing"""
        adj = self._vertices
        if not self._directed:
            count = len(adj[v])
        else:
            count = 0
            for edge in adj[v].values():
                x, y = edge.endpoints()
                if (outgoing and x == v) or (not outgoing and y == v):
                    count += 1
        return count

    # [remove_edge] - Remove a aresta entre u e v
    def remove_edge(self, u, v):
        if u in self._vertices.keys() and v in self._vertices[u].keys():
            del self._vertices[u][v]
            del self._vertices[v][u]

    # [remove_vertex] - Remove o vértice v
    def remove_vertex(self, v):
        # remover todas as arestas de [v]
        # remover todas as arestas com v noutros vertices
        # remover o vértice
        lst = [i for i in self.incident_edges(v)]
        for i in lst:
            x, y = i.endpoints()
            self.remove_edge(x, y)
        del self._vertices[v]
        return v

    # ============================================= [MST] =====================================================
    # [FUNÇÕES AUXILIARES] - ALGORITMO DE KRUSKAL
    conjunto = {}
    rank = {}

    # [MakeSet (v)] - Criar um conjunto singular com um vértice v
    def MakeSet(self, vertice):
        if not isinstance(vertice, Vertex):
            raise TypeError("O objeto inserido não é um Vertex!")
        self.conjunto[vertice] = vertice
        self.rank[vertice] = 0

    # [Find(v)] - Devolve o vértice v do conjunto
    def Find(self, v):
        if not isinstance(v, Vertex):
            raise TypeError("O objeto inserido não é um Vertex!")
        if self.conjunto[v] == v:
            return v
        else:
            return self.Find(self.conjunto[v])

    # [Union(A,B)] - Substitui os conjuntos A e B por um único conjunto contendo a sua união
    def Union(self, vertice1, vertice2):
        vertice1 = self.Find(vertice1)
        vertice2 = self.Find(vertice2)
        if self.rank[vertice1] < self.rank[vertice2]:
            self.conjunto[vertice1] = vertice2
        elif self.rank[vertice1] > self.rank[vertice2]:
            self.conjunto[vertice2] = vertice1
        else:
            self.conjunto[vertice2] = vertice1
            self.rank[vertice1] += 1

    # [b] - Implementação do Algoritmo de Kruskal
    @property
    def Kruskal(self):
        # Inicialização de n conjuntos com todos os vértices do Grafo
        for vertice in self.vertices:
            self.MakeSet(vertice)

        # Cria uma lista de arestas
        lista_de_arestas = []
        peso_s_kruskal = 0
        for edge in self.edges:
            lista_de_arestas.append(edge)
            peso_s_kruskal += int(edge.peso)

        # Ordena as arestas pelo peso
        lista_de_arestas.sort(key=lambda x: int(x.peso))

        # Cria a Árvore de Cobertura Mínima
        MST = Graph()

        for edge in lista_de_arestas:
            if self.Find(edge.origem) != self.Find(edge.destino):
                self.Union(edge.origem, edge.destino)

                v1 = MST.insert_vertex(edge.origem.id)
                v2 = MST.insert_vertex(edge.destino.id)

                MST.insert_edge(v1, v2, int(edge.peso))

        return MST


# ======================================================================================================================

# ================================================ [GRAFO TESTE] ================================================
def construir_grafo_teste(filename):
    print('[Início] - Construir um grafo...')

    # Inicialização da Classe Graph
    g = Graph()

    # Importar os valores do CSV
    f = open(filename, 'r')
    print(f'\nReading... [Origem, Destino, Peso]')

    i = 0
    for row in f:
        Origem, Destino, Peso = row.strip(" ").strip("\n").split(",")
        print(i, " ----- ", Origem, Destino, Peso)

        v1 = g.insert_vertex(Origem)
        v2 = g.insert_vertex(Destino)

        g.insert_edge(v1, v2, Peso)

        i += 1
    return g


if __name__ == "__main__":
    g = construir_grafo_teste('Grafo_Teste.csv')

    # Criação do Grafo da Biblioteca NetworkX e Carregamento das Arestas
    print(f'\nNetworkX Graph Without Kruskal...')
    nx_graph = nx.Graph()
    for e in g.edges:
        nx_graph.add_edge(str(e.origem.id), str(e.destino.id), weight=int(e.peso))

    # Representação do Grafo
    print(f'\nDrawing NetworkX Graph...')
    nx.draw(nx_graph, node_size=500, with_labels=True, font_size=15, edge_color="#525252", font_weight='bold',
            node_color="#43b3ae", font_color="black", node_shape="o", alpha=0.7, linewidths=4)
    plt.show()
    # ------------------------------------------------------------------------------------------------------------------

    print(f'\nNetworkX Graph With Kruskal...')
    nx_graph_Kruskal = nx.Graph()
    for e in g.Kruskal.edges:
        nx_graph_Kruskal.add_edge(str(e.origem.id), str(e.destino.id), weight=int(e.peso))

    # Representação
    print(f'\nDrawing NetworkX Graph...')
    nx.draw(nx_graph_Kruskal, node_size=500, with_labels=True, font_size=15, edge_color="#525252", font_weight='bold',
            node_color="#43b3ae", font_color="black", node_shape="o", alpha=0.7, linewidths=4)
    plt.show()
    # ------------------------------------------------------------------------------------------------------------------


# =============================================== [DATASET FACEBOOK] ===============================================
def limpar_dataset():
    data = pd.read_csv(r'Data_Facebook_Excel.csv')

    print(data)

    i = 0

    while i < len(data):
        print(i)
        j = 1
        while j < len(data):
            if data['X'][i] == data['Y'][j] and data['X'][j] == data['Y'][i]:

                print("i=", i, data['X'][i], data['Y'][i], data['Interactions'][i], '|',
                      "j=", j, data['X'][j], data['Y'][j], data['Interactions'][j])

                data['Interactions'][i] += int(data['Interactions'][j])
                print(data.Interactions[i])

                data = data.drop(labels=j, axis=0)
                data = data.reset_index(drop=True)
                j += 1
            else:
                j += 1
        i += 1

    return data.to_csv("Data_Facebook_Alterado.csv")


# if __name__ == "__main__":
#     limpar_dataset()


def construir_grafo_Facebook(filename):
    print('[Início] - Construir um grafo...')

    # Inicialização da Classe Graph
    g = Graph()

    # Importar os valores do CSV - [VÉRTICES]
    f = open(filename, 'r')
    data = csv.reader(f, delimiter=',')
    headers = next(data)
    print(f'\nReading... {headers}')

    i = 1
    for row in data:
        user_follower, user_followed, interactions = row[1], row[2], row[3]

        print(i, '-----', user_follower, user_followed, interactions)

        v1 = g.insert_vertex(str(user_follower))
        v2 = g.insert_vertex(str(user_followed))

        g.insert_edge(v1, v2, int(interactions))

        i += 1
    f.close()

    return g


if __name__ == "__main__":
    g = construir_grafo_Facebook('Data_Facebook_Alterado_SemNConexos.csv')

    print(f'\nNetworkX Graph Without Kruskal...')
    nx_graph = nx.Graph()
    for e in g.edges:
        nx_graph.add_edge(str(e.origem.id), str(e.destino.id), weight=int(e.peso))

    nx.draw(nx_graph, node_size=250, node_color='#1778F2', linewidths=4, with_labels=False, font_size=6,
            edge_color="#525252", font_color="black", node_shape="o", alpha=0.7)
    plt.show()

    print(f'\nNetworkX Graph With Kruskal...')
    nx_graph_Kruskal = nx.Graph()
    for e in g.Kruskal.edges:
        nx_graph_Kruskal.add_edge(str(e.origem.id), str(e.destino.id), weight=int(e.peso))

    # Representação
    print(f'\nDrawing NetworkX Graph...')
    nx.draw(nx_graph_Kruskal, node_size=250, node_color='#1778F2', linewidths=4, with_labels=False, font_size=10,
            edge_color="#525252", font_color="black", node_shape="o", alpha=0.7)
    plt.show()

    print("  ** END ** ")

# ==================================================================================================================

# ========
#  FASE 2
# ========


def Cluster_Hierarquico(grafo, k):
    assert isinstance(grafo, Graph), "O objeto inserido não é do tipo Grafo!"

    # Cria uma lista de arestas
    lista_de_arestas = []
    for edge in grafo.Kruskal.edges:
        lista_de_arestas.append(edge)

    # Ordena as arestas pelo peso
    lista_de_arestas.sort(key=lambda x: x.peso)

    # Cria a Árvore de Cobertura Mínima
    MST = grafo.Kruskal

    # Remover k-1 arestas com MAIOR Peso
    for i in range(k - 1):
        print(lista_de_arestas[-1])
        MST.remove_edge(lista_de_arestas[-1].origem, lista_de_arestas[-1].destino)
        lista_de_arestas.remove(lista_de_arestas[-1])

    return MST


if __name__ == "__main__":
    # ------------------------------------------- [GRAFO TESTE] --------------------------------------------------------
    G_Agrupado = Cluster_Hierarquico(construir_grafo_teste('Grafo_Teste.csv'), k=5)

    # Representação
    nx_graph_Agrupado = nx.Graph()
    for v in G_Agrupado.vertices:
        nx_graph_Agrupado.add_node(v.id)
    for e in G_Agrupado.edges:
        nx_graph_Agrupado.add_edge(str(e.origem.id), str(e.destino.id), weight=int(e.peso))

    print(f'\nDrawing NetworkX Graph...')
    nx.draw(nx_graph_Agrupado, node_size=500, with_labels=True, font_size=15, edge_color="#525252", font_weight='bold',
            node_color="#43b3ae", node_shape="o", alpha=0.7, linewidths=4)
    plt.show()

    # ------------------------------------------- [GRAFO FACEBOOK] -----------------------------------------------------
    G_Agrupado = Cluster_Hierarquico(construir_grafo_Facebook('Data_Facebook_Alterado_SemNConexos.csv'), k=200)

    # Representação
    nx_graph_Agrupado = nx.Graph()
    for v in G_Agrupado.vertices:
        nx_graph_Agrupado.add_node(str(v.id))
    for e in G_Agrupado.edges:
        nx_graph_Agrupado.add_edge(str(e.origem.id), str(e.destino.id), weight=int(e.peso))

    print(f'\nDrawing NetworkX Graph...')
    nx.draw(nx_graph_Agrupado, node_size=250, with_labels=False, edge_color="#525252", node_color='#1778F2',
            node_shape="o", alpha=0.7, linewidths=4)
    plt.show()


# ----------------------------------------------[MÉTRICAS PARA OS GRAFOS]----------------------------------------------
# [Fontes] https://networkx.org/documentation/stable/_downloads/networkx_reference.pdf
#          https://github.com/miladfa7/Social-Network-Analysis-in-Python/blob/master/Social-Network-Analysis-in-Python.ipynb
# ----------------------------------------------------------------------------------------------------------------------

def NetworkX_Degree_Centrality(Grafo):
    assert isinstance(Grafo, Graph), "O objeto inserido não é do tipo Grafo!"

    nx_graph = nx.Graph()
    for e in Grafo.edges:
        nx_graph.add_edge(str(e.origem.id), str(e.destino.id), weight=int(e.peso))

    pos = nx.spring_layout(nx_graph)
    degCent = nx.degree_centrality(nx_graph)
    node_size = [v * 100000 for v in degCent.values()]
    nx.draw_networkx(nx_graph, pos=pos, with_labels=False, node_color='#1778F2', linewidths=4,
                     edge_color="#525252", node_shape="o", alpha=0.7, node_size=node_size)

    plt.axis('off')
    plt.show()

    print("Degree Centrality ->", degCent)
    print("Degree Centrality Ordenado ->", sorted(degCent.items(), key=lambda item: item[1], reverse=True), "\n")

# ----------------------------------------------------------------------------------------------------------------------


def NetworkX_Closeness_Centrality(Grafo):
    assert isinstance(Grafo, Graph), "O objeto inserido não é do tipo Grafo!"

    nx_graph = nx.Graph()
    for e in Grafo.edges:
        nx_graph.add_edge(str(e.origem.id), str(e.destino.id), weight=int(e.peso))

    pos = nx.spring_layout(nx_graph)
    cloCent = nx.closeness_centrality(nx_graph)
    node_size = [v * 10000 for v in cloCent.values()]
    nx.draw_networkx(nx_graph, pos=pos, with_labels=False, node_color='#1778F2', linewidths=4,
                     edge_color="#525252", node_shape="o", alpha=0.7, node_size=node_size)
    plt.axis('off')
    plt.show()

    print("Closeness Centrality ->", cloCent)
    print("Closeness Centrality Ordenado ->", sorted(cloCent.items(), key=lambda item: item[1], reverse=True), "\n")

# ----------------------------------------------------------------------------------------------------------------------


def NetworkX_Betweenness_Centrality(Grafo):
    assert isinstance(Grafo, Graph), "O objeto inserido não é do tipo Grafo!"

    nx_graph = nx.Graph()
    for e in Grafo.edges:
        nx_graph.add_edge(str(e.origem.id), str(e.destino.id), weight=int(e.peso))

    pos = nx.spring_layout(nx_graph)
    betCent = nx.betweenness_centrality(nx_graph, normalized=True, endpoints=True)
    node_size = [v * 10000 for v in betCent.values()]
    nx.draw_networkx(nx_graph, pos=pos, with_labels=False, node_color='#1778F2', linewidths=4,
                     edge_color="#525252", node_shape="o", alpha=0.7, node_size=node_size)
    plt.axis('off')
    plt.show()

    print("Betweenness Centrality ->", betCent)
    print("Betweenness Centrality Ordenado ->", sorted(betCent.items(), key=lambda item: item[1], reverse=True), "\n")


if __name__ == "__main__":
    G = Cluster_Hierarquico(construir_grafo_Facebook('Data_Facebook_Alterado_SemNConexos.csv'), k=1)
    NetworkX_Degree_Centrality(G)
    NetworkX_Closeness_Centrality(G)
    NetworkX_Betweenness_Centrality(G)
