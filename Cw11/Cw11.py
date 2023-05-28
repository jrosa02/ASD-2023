import numpy as np
import copy

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
        return str(self.key)


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
        elif vertex in self.index_dict.keys():
            return None
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
        return list(self.prox_matrix[vertex_idx])
    
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
                        lst.append((self.getVertex(row).key, self.getVertex(col).key))
        return lst
    
    def __repr__(self) -> str:
        return str(self.prox_matrix)
    
def ullman_rek1(row, M:np.ndarray, usedcolls: set, mat_P, mat_G, ret_val: list = [], no_rec:int = 0) -> int:
    no_rec += 1
    if row == M.shape[0]:
        if not (mat_P - M@(M@mat_G).T).any():
            #print(M)
            ret_val.append(M)
        return no_rec
    
    for col in range(M.shape[1]):
        if not col in usedcolls:
            usedcolls.add(col)
            for col1 in range(M.shape[1]):
                M[row, col1] = 0
            M[row, col] = 1
            no_rec = ullman_rek1(row+1, M.copy(), usedcolls, mat_P, mat_G, ret_val, no_rec)
            usedcolls.discard(col)
    return no_rec
    
def find_fitting1(mgraf_G: matGraf, mgraf_P: matGraf):
    print("\tUlmann 1.0")
    mx_P = mgraf_P.prox_matrix.astype(int)
    mx_G =mgraf_G.prox_matrix.astype(int)
    M = np.zeros((mgraf_P.prox_matrix.shape[0], mgraf_G.prox_matrix.shape[1]))
    for i in range(M.shape[0]):
        degvi = np.count_nonzero(mx_P[i, :])
        for j in range(M.shape[0]):
            degvj = np.count_nonzero(mx_G[j, :])
    Ms = list()
    no_rec = ullman_rek1(0, M, set(), mgraf_P.prox_matrix, mgraf_G.prox_matrix, Ms, 0)
    print(f"Ilość rekurencji: {no_rec}, Znalezione izomorfizmy: {len(Ms)}")
    


def ullman_rek2(row, M:np.ndarray, usedcolls: list, mat_P, mat_G, ret_val: list = [], no_rec:int = 0, M0 = None) -> int:
    M0 = M0 if M0 is not None else M
    no_rec += 1
    if row == M.shape[0]:
        if not (mat_P - M@(M@mat_G).T).any():
            #print(M)
            ret_val.append(M)
        return no_rec

    for col in range(M.shape[1]):
        if not col in usedcolls:
            if M0[row, col]:
                usedcolls.append(col)
                for col1 in range(M.shape[1]):
                    M[row, col1] = 0
                M[row, col] = 1
                no_rec = ullman_rek2(row+1, M.copy(), usedcolls, mat_P, mat_G, ret_val, no_rec, M0)
                usedcolls.remove(col)
    return no_rec
    
def find_fitting2(mgraf_G: matGraf, mgraf_P: matGraf):
    print("\tUlmann 2.0")
    mx_P = mgraf_P.prox_matrix.astype(int)
    mx_G =mgraf_G.prox_matrix.astype(int)
    M = np.zeros((mgraf_P.prox_matrix.shape[0], mgraf_G.prox_matrix.shape[1]))
    M0 = np.zeros((mgraf_P.prox_matrix.shape[0], mgraf_G.prox_matrix.shape[1]))
    for i in range(M.shape[0]):
        degvi = np.count_nonzero(mx_P[i, :])
        for j in range(M.shape[1]):
            degvj = np.count_nonzero(mx_G[j, :])
            M0[i][j] = 1 if degvi <= degvj else 0
    Ms = list()
    no_rec = ullman_rek2(0, M, [], mgraf_P.prox_matrix, mgraf_G.prox_matrix, Ms, 0, M0)
    print(f"Ilość rekurencji: {no_rec}, Znalezione izomorfizmy: {len(Ms)}")

def prune(M:np.ndarray ,P: np.ndarray, G:np.ndarray):
    M = M.astype(int)
    change = True
    while change:
        change = False
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if M[i, j]:
                    nnnnx = False
                    for x in range(P.shape[1]):
                        for y in range(G.shape[1]):
                            if M[x, y]:
                                nnnnx = True
                                break
                        if nnnnx:
                            break
                    if not nnnnx:
                        M[i, j] = 0
                        change = True
                        break

    return M

def ullman_rek3(row, M:np.ndarray, usedcolls: list, mat_P, mat_G, ret_val: list = [], no_rec:int = 0, M0 = None) -> int:
    M0 = M0 if M0 is not None else M
    no_rec += 1
    if row == M.shape[0]:
        if not (mat_P - M@(M@mat_G).T).any():
            #print(M)
            ret_val.append(M)
        return no_rec

    M = prune(M, mat_P, mat_G)
    
    for col in range(M.shape[1]):
        if not col in usedcolls:
            if M0[row, col]:
                usedcolls.append(col)
                for col1 in range(M.shape[1]):
                    M[row, col1] = 0
                M[row, col] = 1
                no_rec = ullman_rek3(row+1, M.copy(), usedcolls, mat_P, mat_G, ret_val, no_rec, M0)
                usedcolls.remove(col)
    return no_rec
    
def find_fitting3(mgraf_G: matGraf, mgraf_P: matGraf):
    print("\tUlmann 3.0")
    mx_P = mgraf_P.prox_matrix.astype(int)
    mx_G =mgraf_G.prox_matrix.astype(int)
    M = np.zeros((mgraf_P.prox_matrix.shape[0], mgraf_G.prox_matrix.shape[1]))
    M0 = np.zeros((mgraf_P.prox_matrix.shape[0], mgraf_G.prox_matrix.shape[1]))
    for i in range(M.shape[0]):
        degvi = np.count_nonzero(mx_P[i, :])
        for j in range(M.shape[1]):
            degvj = np.count_nonzero(mx_G[j, :])
            M0[i][j] = 1 if degvi <= degvj else 0
    Ms = list()
    no_rec = ullman_rek3(0, M, [], mgraf_P.prox_matrix, mgraf_G.prox_matrix, Ms, 0, M0)
    print(f"Ilość rekurencji: {no_rec}, Znalezione izomorfizmy: {len(Ms)}")


def main():
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]
    matrixgraf_G = matGraf()
    matrixgraf_P = matGraf()

    for woj in "ABCDEF":
        x = Vertex(woj, "")
        matrixgraf_G.insertVertex(x)
    for woj in graph_G:
        matrixgraf_G.insertEdge(Vertex(woj[0], ""), Vertex(woj[1], ""), woj[2])
        matrixgraf_G.insertEdge(Vertex(woj[1], ""), Vertex(woj[0], ""), woj[2])

    for woj in "ABC":
        y = Vertex(woj, "")
        matrixgraf_P.insertVertex(y)
    for woj in graph_P:
        matrixgraf_P.insertEdge(Vertex(woj[0], ""), Vertex(woj[1], ""), woj[2])
        matrixgraf_P.insertEdge(Vertex(woj[1], ""), Vertex(woj[0], ""), woj[2])

    #print(matrixgraf_P)
    #print(matrixgraf_G)

    find_fitting1(matrixgraf_G, matrixgraf_P)
    find_fitting2(matrixgraf_G, matrixgraf_P)
    find_fitting3(matrixgraf_G, matrixgraf_P)


if __name__ == "__main__":
    main()