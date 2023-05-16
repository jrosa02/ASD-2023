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
    
class Edge():
    def __init__(self, capacity, isresidual) -> None:
        self.capacity: float = capacity
        self.flow: float = 0.0
        self.residual: float = 0.0 if isresidual else capacity
        self.isResidual: bool = isresidual

    def __repr__(self) -> str:
        return str(self.capacity) + " " + str(self.flow) + " " + str(self.residual) + " " + str(self.isResidual)


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

    
    def insertEdge(self, vertex1, vertex2, edge: Edge):
        """insertEdge(vertex1, vertex2, egde) - wstawia do grafu krawędź pomiędzy podane węzły"""
        if (vertex2, edge) in set(self.prox_list[self.index_dict[vertex1]]):
            self.prox_list[self.index_dict[vertex1]] = (vertex2, edge)
            self.prox_list[self.index_dict[vertex2]] = (vertex1, Edge(edge.capacity, True))
        else:
            self.prox_list[self.index_dict[vertex1]].append((self.index_dict[vertex2], edge))
            self.prox_list[self.index_dict[vertex2]].append((self.index_dict[vertex1], Edge(edge.capacity, True)))

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


def traverse(graf: lstGraf, start_idx):
    kolejka = []
    met = set([start_idx])
    parent = [None for x in range(graf.order())]
    kolejka.append(start_idx)

    while len(kolejka):
        node_idx = kolejka.pop()

        for neigh_idx_idx in range(len(graf.neighboursIdx(node_idx))):
            neigh_true_idx = graf.neighboursIdx(node_idx)[neigh_idx_idx]

            if neigh_true_idx not in met and graf.prox_list[node_idx][neigh_idx_idx][1].residual > 0:
                kolejka.append(neigh_true_idx)
                met.add(neigh_true_idx)
                parent[neigh_true_idx] = node_idx
                
    return parent

def min_cap(graf: lstGraf, start_idx, stop_idx, parent):
    current_idx = stop_idx
    min_cap = float('inf')
    if parent[current_idx] != current_idx:
        return 0
    while current_idx != start_idx:
        x = 0
        for neigh_idx, edge in graf.prox_list[parent[current_idx]]:
            if neigh_idx == current_idx and not edge.isResidual:
                x = (current_idx, edge)
                break
        min_cap = min([x[1].residual, min_cap])
        current_idx = parent[current_idx]
    return min_cap
                

if __name__ == "__main__":
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]

    listgraf = lstGraf()
    lst_rdges = []
    for woj in graf_1:
        x = Vertex(woj[0], "")
        y = Vertex(woj[1], "")
        val = woj[2]
        listgraf.insertVertex(x)
        listgraf.insertVertex(y)
        listgraf.insertEdge(x, y, Edge(val, False))

    parent = traverse(listgraf, 0)
    print(parent)
    mincp = min_cap(listgraf, 0, 4, parent)
    print(mincp)
    