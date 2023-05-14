import numpy as np
import cv2
import matplotlib.pyplot as plt

import numpy as np

class Vertex():
    def __init__(self, key, data) -> None:
        self.key = key
        self.data = data

    def __eq__(self, __value: object) -> bool:
        """__eq__ (porównującą węzły wg klucza - czyli wybranego pola identyfikującego węzeł)"""
        return self.key == __value.key
    
    def __hash__(self) -> int:
        """__hash__ (wykorzystywaną przez słownik, zwracająca klucz)."""
        return hash(self.key)
    
    def __str__(self) -> str:
        return str(self.key) + ": " + str(self.data)


class lstGraf():
    def __init__(self):
        """konstruktor - tworzący pusty graf"""
        self.prox_list = []
        self.index_dict = dict()

    # isEmpty( ) - zwracająca True jeżeli graf jest pusty
    def isEmpty(self):
        if not len(self.index_dict):
            return True
        return False
    
    def insertVertex(self, vertex):
        """insertVertex(vertex)    - wstawia do grafu  podany węzeł"""
        if vertex not in self.index_dict.keys():
            self.index_dict[vertex] = len(self.prox_list)
            self.prox_list.append([])
        else:
            x = self.index_dict[vertex]
            del(self.index_dict[vertex])
            self.index_dict[vertex] = x

    
    def insertEdge(self, vertex1, vertex2, edge = 1):
        """insertEdge(vertex1, vertex2, egde) - wstawia do grafu krawędź pomiędzy podane węzły"""
        if (vertex2, edge) in set(self.prox_list[self.index_dict[vertex1]]):
            self.prox_list[self.index_dict[vertex1]] = (vertex2, edge)
        else:
            self.prox_list[self.index_dict[vertex1]].append((self.index_dict[vertex2], edge))

    # deleteVertex(vertex) - usuwa podany węzeł
    def deleteVertex(self, vertex):
        index = self.index_dict.pop(vertex)
        self.prox_list.pop(index)
        for vtx in self.index_dict:
            if self.index_dict[vtx] > index:
                self.index_dict[vtx] -= 1
        for i in range(len(self.prox_list)):
            self.prox_list[i] = list(filter(lambda a: a[0] != index, self.prox_list[i]))
            for j in range(len(self.prox_list[i])):
                self.prox_list[i][j][0] -= 1 if self.prox_list[i][j][0] > index else 0

    
    # deleteEdge(vertex1, vertex2) - usuwa krawędź pomiędzy podanymi węzłami
    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        
        #print(self.prox_list[idx1])
        if self.prox_list[idx1] is not None:
            idx2 = [x[0] for x in self.prox_list[idx1]].index(idx2)
            self.prox_list[idx1].pop(idx2)

    # Dodatkowo przydatne będą metody metody:
    def getVertexIdx(self, vertex) -> int:
        """getVertexIdx(vertex) - zwraca indeks węzła (wykorzystując metodę indeks lub wspomniany słownik)"""
        return self.index_dict[vertex]
    
    def getVertex(self, vertex_idx) -> Vertex:
        """getVertex(vertex_idx)    - zwraca węzeł o podanym indeksie (niejako odwrotność powyższej metody)"""
        value: list[Vertex] = [i for i in self.index_dict if self.index_dict[i]==vertex_idx]
        if value == []:
            print(self.order())
            print(vertex_idx)
            print(value)
            pass
        return value[0]

    
    # neighboursIdx(vertex_idx) - zwraca listę indeksów węzłów przyległych do węzła o podanym indeksie (połączenia wyjściowe) LUB
    def neighboursIdx(self, vertex_idx):
        return [x[0] for x in self.prox_list[vertex_idx]]
    
    def neighboursIdxnW(self, vertex_idx):
        return list(self.prox_list[vertex_idx])
    
    # neighbours(vertex_idx) - zwraca listę węzłów przyległych do węzła o podanym indeksie (połączenia wyjściowe)
    def neighbours(self, vertex_idx):
        return list([(self.getVertex(indx), self.prox_list[indx]) for indx in self.neighboursIdx(vertex_idx)])
    
    def order(self):
        """order() - zwraca rząd grafu (liczbę węzłów)"""
        return len(self.index_dict)
    
    def size(self, directed: bool = False):
        """size() - zwraca rozmiar grafu (liczbę krawędzi)"""
        raise NotImplementedError()
     
    def edges(self, directed: bool = False):
        """edges() - zwracająca wszystkie krawędzie grafu w postaci listy par: (klucz_węzła_początkowego, klucz_węzła_końcowego) 
        - będzie potrzebna do wyrysowania grafu."""
        lst = list()
        if not directed:
            for i in range(len(self.prox_list)):
                for somsiad_idx in self.prox_list[i]:
                        if self.getVertex(i).key == 856:
                            print(somsiad_idx)
                        lst.append((self.getVertex(i).key, self.getVertex(somsiad_idx[0]).key, somsiad_idx[1]))
        return lst
    
    def neigh_edges(self, indx):
        return self.prox_list[indx]
    

def printGraph(g: lstGraf):
    n = g.order()
    print("---------GRAPH---------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighboursIdxnW(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end="; ")
        print()
    print("------------------------")


def PrimaDżewo(graph: lstGraf, start: int=None):
    if start is None:
        start = 0
    intree = [False for _ in range(graph.order())]
    distance = [np.float64('inf') for _ in range(graph.order())]
    parent = [-1 for _ in range(graph.order())]

    MST = lstGraf()
    for i in range(graph.order()):
        MST.insertVertex(graph.getVertex(i))
    v = start
    sum = 0
    while(not intree[v]):
        intree[v] = True

        for indx, wei in graph.neigh_edges(v):
            if wei < distance[indx] and not intree[indx]:
                distance[indx] = wei
                parent[indx] = v

        potnewV ={distance[indx] : indx  for indx in range(graph.order()) if not intree[indx]}
        if potnewV:
            new_v = potnewV[min(potnewV.keys())]
            if parent[new_v] >= 0:
                MST.insertEdge(graph.getVertex(parent[new_v]), graph.getVertex(new_v), min(potnewV.keys()))
                MST.insertEdge(graph.getVertex(new_v), graph.getVertex(parent[new_v]), min(potnewV.keys()))
                sum += min(potnewV.keys())
            v = new_v
    return MST, sum


I = cv2.imread("download.png",cv2.IMREAD_GRAYSCALE)
print(np.max(I), np.min(I))
graph = lstGraf()

for row in range(I.shape[0]):
    for col in range(I.shape[1]):
        graph.insertVertex(Vertex(I.shape[1] * row + col, I[row, col]))
for row in range(1, I.shape[0]-1):
    for col in range(1, I.shape[1]-1):
        for i in range(3):
            for j in range(3):
                if i!=1 or j!=1:
                    graph.insertEdge(Vertex(I.shape[1] * row + col, I[row, col]),
                                    Vertex(I.shape[1] * (row - 1 + i) + (col-1 + j), I[row - 1 + i, col-1 + j]),
                                    np.abs(np.int64(I[row, col]) - np.int64(I[row-1 + i, col-1 + j])))
                    
        
                    
primagraf, suma = PrimaDżewo(graph)

edgess = primagraf.edges()
edges = sorted(edgess, key = lambda el: el[2], reverse=True)
primagraf.deleteEdge(Vertex(edges[0][0], ""), Vertex(edges[0][1], ""))
primagraf.deleteEdge(Vertex(edges[0][1], ""), Vertex(edges[0][0], ""))

IS = np.zeros(I.shape)
# implementujemy prostą trawersację grafu - np. z wykorzystaniem stosu, kolejki lub rekurencyjną  (nie ma to większego znaczenia w tym przypadku),
def traverse(graphh: lstGraf, point, fn, val, img):
    visited = set([point])
    stos = [point]
    while len(stos):
        current = stos.pop()
        #print((current//I.shape[0], current%I.shape[0]))
        fn(graphh, current, val, img)
        visited.add(current)
        neighs = graphh.neighboursIdx(current)
        for neigh in neighs:
            if neigh not in visited:
                stos.append(neigh)

def color(graphh, indx, val, img):
    vertex = graphh.getVertex(indx)
    vertex.data = val
    img[vertex.key//img.shape[1], vertex.key%img.shape[1]] = vertex.data
    return img

img = np.zeros(I.shape, dtype=np.uint8)
# uruchamiamy przejścia po obu drzewach - zaczynamy od wierzchołków, które łączyła usunięta krawędź. Niech każde przeszukanie 'pokoloruje' piksele odpowiadające odwiedzanym wierzchołkom jednym 'kolorem' (proszę jako 'kolor' ustalić dwa poziomy szarości - np. 100 i 200)
traverse(primagraf, edges[0][0], color, 200, img)
print("-------------------------")
traverse(primagraf, edges[0][1], color, 100, img)
# z “napotkanych” wierzchołków odczytujemy współrzędne piksela (y = klucz//XX, x = klucz % XX) i pod te współrzędne wpisujemy "kolor" do obrazu wyjściowego

# obraz wyświetlamy (przykładowo: cv2.imshow("Wynik",IS) oraz cv2.waitKey() )
cv2.imshow("Wynik", img)
cv2.waitKey()