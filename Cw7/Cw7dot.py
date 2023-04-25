import polska as pl

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
        return str(self.key) + " -> " + str(self.data)


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
        self.index_dict[vertex] = len(self.prox_list)
        self.prox_list.append([])
        #edges = self.edges()
    
    def insertEdge(self, vertex1, vertex2, edge = 1):
        """insertEdge(vertex1, vertex2, egde) - wstawia do grafu krawędź pomiędzy podane węzły"""
        self.prox_list[self.index_dict[vertex1]].append(self.index_dict[vertex2])

    # deleteVertex(vertex) - usuwa podany węzeł
    def deleteVertex(self, vertex):
        index = self.index_dict.pop(vertex)
        self.prox_list.pop(index)
        for vtx in self.index_dict:
            if self.index_dict[vtx] > index:
                self.index_dict[vtx] -= 1
        for i in range(len(self.prox_list)):
            self.prox_list[i] = list(filter(lambda a: a!= index, self.prox_list[i]))
            for j in range(len(self.prox_list[i])):
                self.prox_list[i][j] -= 1 if self.prox_list[i][j] > index else 0

    
    # deleteEdge(vertex1, vertex2) - usuwa krawędź pomiędzy podanymi węzłami
    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        
        if self.prox_list[idx1] is not None:
            idx2 = self.prox_list[idx1].index(idx2)
            self.prox_list[idx1].pop(idx2)

    # Dodatkowo przydatne będą metody metody:
    def getVertexIdx(self, vertex) -> int:
        """getVertexIdx(vertex) - zwraca indeks węzła (wykorzystując metodę indeks lub wspomniany słownik)"""
        return self.index_dict[vertex]
    
    def getVertex(self, vertex_idx) -> Vertex:
        """getVertex(vertex_idx)    - zwraca węzeł o podanym indeksie (niejako odwrotność powyższej metody)"""
        value = [i for i in self.index_dict if self.index_dict[i]==vertex_idx]
        if value == None:
            print(vertex_idx)
        return value[0]
    
    # neighboursIdx(vertex_idx) - zwraca listę indeksów węzłów przyległych do węzła o podanym indeksie (połączenia wyjściowe) LUB
    def neighboursIdx(self, vertex_idx):
        return list(self.prox_list[vertex_idx])
    
    # neighbours(vertex_idx) - zwraca listę węzłów przyległych do węzła o podanym indeksie (połączenia wyjściowe)
    def neighbours(self, vertex_idx):
        raise NotImplementedError()
    
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
                        lst.append((self.getVertex(i).key, self.getVertex(somsiad_idx).key))
        return lst
    

def choose_color(graf: lstGraf, index, kolory):
    neigh_colors = []
    for neigh_idx in graf.neighboursIdx(index):
        if neigh_idx in kolory:
            neigh_colors.append(kolory[neigh_idx])
    neigh_colors = set(neigh_colors)
    i = 0
    while i in neigh_colors:
        i+=1
    kolory[index] = i
    
def koloruj_graf(graf: lstGraf, DFS: bool = False) -> dict:
    kolory = dict()
    kolejka = []
    met = set()
    kolejka.append(0)
    while len(kolejka):
        node_idx = kolejka.pop() if DFS else kolejka.pop(0)
        met.add(node_idx)
        choose_color(graf, node_idx, kolory)
        for neigh_idx in graf.neighboursIdx(node_idx):
            if neigh_idx not in met:
                kolejka.append(neigh_idx)
    return kolory


if __name__ == "__main__":
    matrixgraf = lstGraf()
    for woj in pl.slownik:
        x = Vertex(woj, pl.slownik[woj])
        matrixgraf.insertVertex(x)
    for woj in pl.graf:
        matrixgraf.insertEdge(Vertex(woj[0], pl.slownik[woj[0]]), Vertex(woj[1], pl.slownik[woj[1]]))
    
    print("Maksymalna liczba kolorów to 4 w obu przypadkach")

    kolory = koloruj_graf(matrixgraf, False)
    kolory = [(matrixgraf.getVertex(k).key, v) for k, v in kolory.items()]
    edges = matrixgraf.edges()
    pl.draw_map(edges, kolory)

    kolory = koloruj_graf(matrixgraf, True)
    kolory = [(matrixgraf.getVertex(k).key, v) for k, v in kolory.items()]
    edges = matrixgraf.edges()
    pl.draw_map(edges, kolory)

    