from abc import ABC, abstractmethod

class Vertex():
    def __init__(self, key, data) -> None:
        self.key = key
        self.data = data

    def __eq__(self, __value: object) -> bool:
        """__eq__ (porównującą węzły wg klucza - czyli wybranego pola identyfikującego węzeł)"""
        return self.data == __value.data
    
    def __hash__(self) -> int:
        """__hash__ (wykorzystywaną przez słownik, zwracająca klucz)."""
        return hash(self.key)

class Graf(ABC):
    def __init__(self):
        """konstruktor - tworzący pusty graf"""
        super.__init__()

    # isEmpty( ) - zwracająca True jeżeli graf jest pusty
    @abstractmethod
    def isEmpty(self):
        raise NotImplementedError()
    
    # insertVertex(vertex)    - wstawia do grafu  podany węzeł
    @abstractmethod
    def insertVertex(self, vertex):
        raise NotImplementedError()
    
    # insertEdge(vertex1, vertex2, egde) - wstawia do grafu krawędź pomiędzy podane węzły
    @abstractmethod
    def insertEdge(self, vertex1, vertex2, edge):
        raise NotImplementedError()
    
    # deleteVertex(vertex) - usuwa podany węzeł
    @abstractmethod
    def deleteVertex(self, vertex):
        raise NotImplementedError()
    
    # deleteEdge(vertex1, vertex2) - usuwa krawędź pomiędzy podanymi węzłami
    @abstractmethod
    def deleteEdge(self, vertex):
        raise NotImplementedError()      

    # Dodatkowo przydatne będą metody metody:
    # getVertexIdx(vertex)      - zwraca indeks węzła (wykorzystując metodę indeks lub wspomniany słownik)
    @abstractmethod
    def getVertexIdx(self, vertex) -> int:
        raise NotImplementedError()
    
    @abstractmethod
    def getVertex(self, vertex_idx):
        """getVertex(vertex_idx)    - zwraca węzeł o podanym indeksie (niejako odwrotność powyższej metody)"""
        raise NotImplementedError()
    
    # neighboursIdx(vertex_idx) - zwraca listę indeksów węzłów przyległych do węzła o podanym indeksie (połączenia wyjściowe) LUB
    @abstractmethod
    def neighboursIdx(self, vertex_idx):
        raise NotImplementedError()
    
    # neighbours(vertex_idx) - zwraca listę węzłów przyległych do węzła o podanym indeksie (połączenia wyjściowe)
    @abstractmethod
    def neighbours(self, vertex_idx):
        raise NotImplementedError()
    
    @abstractmethod
    def order(self):
        """order() - zwraca rząd grafu (liczbę węzłów)"""
        raise NotImplementedError()
    
    @abstractmethod
    def size(self):
        """size() - zwraca rozmiar grafu (liczbę krawędzi)"""
        raise NotImplementedError()
     
    @abstractmethod
    def edges(self):
        """edges() - zwracająca wszystkie krawędzie grafu w postaci listy par: (klucz_węzła_początkowego, klucz_węzła_końcowego) 
        - będzie potrzebna do wyrysowania grafu."""
        raise NotImplementedError()