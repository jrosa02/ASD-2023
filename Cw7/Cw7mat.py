import numpy as np
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


class matGraf():
    def __init__(self):
        """konstruktor - tworzący pusty graf"""
        self.prox_matrix:np.ndarray = np.ndarray((0,0))
        self.index_dict = dict()

    # isEmpty( ) - zwracająca True jeżeli graf jest pusty
    def isEmpty(self):
        if not len(self.index_dict):
            return True
        return False
    
    def insertVertex(self, vertex):
        """insertVertex(vertex)    - wstawia do grafu  podany węzeł"""
        if self.prox_matrix.shape == (0, 0):
            self.prox_matrix = np.zeros((1, 1))
            self.index_dict[vertex] = 0
        else:
            self.index_dict[vertex] = self.prox_matrix.shape[0]
            self.prox_matrix = np.concatenate([self.prox_matrix, np.zeros((1, self.prox_matrix.shape[1]))])
            self.prox_matrix = np.concatenate([self.prox_matrix, np.zeros((self.prox_matrix.shape[0], 1))], axis=1)
    
    def insertEdge(self, vertex1, vertex2, edge = 1):
        """insertEdge(vertex1, vertex2, egde) - wstawia do grafu krawędź pomiędzy podane węzły"""
        self.prox_matrix[self.index_dict[vertex1], self.index_dict[vertex2]] = edge

    # deleteVertex(vertex) - usuwa podany węzeł
    def deleteVertex(self, vertex):
        index = self.index_dict.pop(vertex)
        self.prox_matrix = np.delete(self.prox_matrix, index, 0)
        self.prox_matrix = np.delete(self.prox_matrix, index, 1)
        for vtx in self.index_dict:
            if self.index_dict[vtx] > index:
                self.index_dict[vtx] -= 1
    
    # deleteEdge(vertex1, vertex2) - usuwa krawędź pomiędzy podanymi węzłami
    def deleteEdge(self, vertex1, vertex2):
        self.insertEdge(vertex1, vertex2, 0)

    # Dodatkowo przydatne będą metody metody:
    def getVertexIdx(self, vertex) -> int:
        """getVertexIdx(vertex) - zwraca indeks węzła (wykorzystując metodę indeks lub wspomniany słownik)"""
        raise NotImplementedError()
    
    def getVertex(self, vertex_idx) -> Vertex:
        """getVertex(vertex_idx)    - zwraca węzeł o podanym indeksie (niejako odwrotność powyższej metody)"""
        value = [i for i in self.index_dict if self.index_dict[i]==vertex_idx]
        if value == None:
            print(vertex_idx)
        return value[0]
    
    # neighboursIdx(vertex_idx) - zwraca listę indeksów węzłów przyległych do węzła o podanym indeksie (połączenia wyjściowe) LUB
    def neighboursIdx(self, vertex_idx):
        raise NotImplementedError()
    
    # neighbours(vertex_idx) - zwraca listę węzłów przyległych do węzła o podanym indeksie (połączenia wyjściowe)
    def neighbours(self, vertex_idx):
        raise NotImplementedError()
    
    def order(self):
        """order() - zwraca rząd grafu (liczbę węzłów)"""
        return len(self.index_dict)
    
    def size(self, directed: bool = False):
        """size() - zwraca rozmiar grafu (liczbę krawędzi)"""
        size = 0
        for row in range(self.prox_matrix.shape[0]):
            for col in range(self.prox_matrix.shape[0]):
                if row != col and self.prox_matrix[row, col] != 0:
                    size += 1
        if directed:
            size /= 2
        return size
     
    def edges(self, directed: bool = False):
        """edges() - zwracająca wszystkie krawędzie grafu w postaci listy par: (klucz_węzła_początkowego, klucz_węzła_końcowego) 
        - będzie potrzebna do wyrysowania grafu."""
        lst = list()
        if not directed:
            for row in range(self.prox_matrix.shape[0]):
                for col in range(row):
                    if row != col and self.prox_matrix[row, col] != 0:
                        lst.append((self.getVertex(row).data, self.getVertex(col).data))
        return lst
    

if __name__ == "__main__":
    print(Vertex('K', pl.slownik['K']) == Vertex('Z', pl.slownik['Z']))
    matrixgraf = matGraf()
    for woj in pl.slownik:
        x = Vertex(woj, pl.slownik[woj])
        matrixgraf.insertVertex(x)
    for woj in pl.graf:
        matrixgraf.insertEdge(Vertex(woj[0], pl.slownik[woj[0]]), Vertex(woj[1], pl.slownik[woj[1]]))
    matrixgraf.deleteVertex(Vertex('K', pl.slownik['K']))
    edges = matrixgraf.edges()
    pl.draw_map(edges)