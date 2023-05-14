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
    
    def vertexes(self):
        return set(self.index_dict.keys())

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
                #MST.insertEdge(graph.getVertex(new_v), graph.getVertex(parent[new_v]), min(potnewV.keys()))
                sum += min(potnewV.keys())
            v = new_v
    return MST, sum

graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]

class UnionFind():
    def __init__(self) -> None:
        self.parent = []
        self.size = []
        self.n = 0

    def append(self, x: int):
        self.parent.append(x)
        self.size.append(-1)
        self.n += 1

    def find(self, x):
        if x != self.parent[x]:
            return self.find(self.parent[x])
        return x
    
    def union_sets(self, s1, s2):
        root_1 = self.find(s1)
        root_2 = self.find(s2)
        if  root_1 == root_2:
            return
        if self.size[root_1] > self.size[root_2]:
            self.parent[root_2] = root_1
            self.size[root_2] += 1
        else:
            self.parent[root_1] = root_2
            self.size[root_1] += 1

    def same_components(self, s1, s2):
        return self.find(s1) == self.find(s2)
    
    def ret_edges(self):
        lst = []
        for i in range(len(self.parent)):
            lst.append((chr(self.parent[i] + 65), chr(i + 65)))
        return lst
    

if __name__ == "__main__":
    

    listgraf = lstGraf()
    for woj in graf:
        x = Vertex(woj[0], "")
        y = Vertex(woj[1], "")
        val = woj[2]
        listgraf.insertVertex(x)
        listgraf.insertVertex(y)
        listgraf.insertEdge(x, y, val)
        listgraf.insertEdge(y, x, val)

    edges = listgraf.edges()
    edges.sort(key= lambda el: el[2])
    print(edges)

    unfnd = UnionFind()
    for i in range(listgraf.order()):
        unfnd.append(i)

    for edge in edges:
        if not unfnd.same_components(ord(edge[0]) - 65, ord(edge[1]) - 65):
            unfnd.union_sets(ord(edge[0]) - 65, ord(edge[1]) - 65)
            
    print(unfnd.same_components(0, 1))
    unionedges = unfnd.ret_edges()
    edgedict = {(elem[0], elem[1]): elem[2] for elem in edges}
    print(unionedges)
    outedges = []
    summm = 0
    for unionedge in unionedges:
        print(unionedge)
        outedges.append((unionedge[0], unionedge[1], edgedict[unionedge]))
        summm += edgedict[unionedge]


        
    
    outlistgraf = lstGraf()
    for woj in graf:
        x = Vertex(woj[0], "")
        y = Vertex(woj[1], "")
        outlistgraf.insertVertex(x)
        outlistgraf.insertVertex(y)

    for woj in outedges:
        x = Vertex(woj[0], "")
        y = Vertex(woj[1], "")
        outlistgraf.insertEdge(x, y, woj[2])

    printGraph(outlistgraf)
    print("Summ = ",summm)

