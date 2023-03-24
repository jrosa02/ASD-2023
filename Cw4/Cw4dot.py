import random
from typing import List

class Element:
    """Elementy listy również powinny być zaimplementowane jako klasa z atrybutami przechowującymi:
      klucz,  wartość (jakąś daną), liczbę poziomów oraz listę (tablicę) ze wskazaniami na następny element o rozmiarze równym liczbie poziomów."""
    def __init__(self, key, value, maxLevel:int = 4, nr_lvl = None) -> None:
        self.key_ = key
        self.value_ = value
        self.nr_lvl_ = self.randomLevel(maxLevel) if nr_lvl is None else nr_lvl
        self.next_: List[Element] = [None for _ in range(self.nr_lvl_)]
        self.maxLevel = maxLevel
        pass

    def randomLevel(self, maxLevel, p = 0.5):
        random.seed(int(random.random()*10000))
        return int(random.random()*maxLevel)+1
    
    def compare_next_keys(self, key):
        index = 0
        for i in range(len(self.next_)):
            if self.next_[i] is None: return None
            if self.next_[i].key_ < key: index = i
        return index
    
    def __str__(self) -> str:
        outstr: str = '\t'
        for i in reversed(range(self.maxLevel)):
            if i >= self.nr_lvl_:
                outstr += "|\t"
            elif self.next_[i] is not None: 
                outstr += "\/" + str(self.next_[i].value_) +"\t"
            else:
                outstr += "N\t"
        outstr += str(self.key_) + "\t" + str(self.value_) + '\n'
        return outstr
    
    

    



class Listjuping:
    def __init__(self, maxLevel:int = 4) -> None:
        """konstruktor z parametrem określającym maksymalną 'wysokość' elementu listy - powinien tworzyć pusty element listy,
          którego tablica wskazań na następne elementy będzie reprezentowała tablicę głów list na poszczególnych poziomach, ten element ma zostać przypisany do atrybutu head"""
        self.head_: Element = Element(0, None, maxLevel=maxLevel, nr_lvl=maxLevel)
        self.maxLevel_ = maxLevel

    def __str__(self) -> str:
        i = 0
        outstr:str = "HEAD" + str(self.head_)
        elem = self.head_
        while elem is not None and elem.next_[0] is not None:
            i+=1
            elem = elem.next_[0]
            outstr += str(i) + "->" + str(elem)
        return outstr
        
    
    def find_last_smaller_key(self, elem2insert: Element, depth: int, startpoint: Element = None) -> Element:
        if startpoint is None: startpoint  = self.head_
        elem = self.head_
        i = 0
        while elem.next_[depth] is not None and elem.next_[depth].key_ <= elem2insert.key_:
            #print(elem)
            elem = elem.next_[depth]
            i += 1
        return elem
        


    def search():
        """wyszukująca i zwracająca wartość odpowiadającą podanemu kluczowi (lub None)"""
        pass

    def insert(self, elem2insert: Element):
        """wstawiająca daną wg podanego klucza - podczas szukania miejsca 
        do wstawienia klucza powinna tu być tworzona lista  (tablica) zawierająca poprzedniki  znalezionego elementu  na każdym poziomie 
        (znaleziony element to ten, którego klucz jest większy od klucza wstawianego elementu);
        dla poziomów, których znaleziony element nie posiada  w tablicy poprzedników powinna być wpisana głowa listy (np. head)."""
        if self.head_.next_[0] is None:
            for i in range(min([len(elem2insert.next_), len(self.head_.next_)])):
                self.head_.next_[i] = elem2insert
                elem = self.head_
        else:
            elem = self.find_last_smaller_key(elem2insert, 0)
            if elem.key_ == elem2insert.key_:
                elem.value_ = elem2insert.value_
            else:
                for i in range(min([len(elem2insert.next_), len(elem.next_)])):
                    elem2insert.next_[i] = elem.next_[i]
                    elem.next_[i]=elem2insert


        

    def remove(self, key):
        """usuwająca daną o podanym kluczu"""
        pass






if __name__ == "__main__":
# utworzenie pustej listy
    pustalista = Listjuping()
# użycie insert do wpisana do niej 15 danych (niech kluczami będą  kolejne liczby od 1, a wartościami - kolejne litery),
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    values = "ABCDEFGHIJKLMNOPRSTUWXYZ"
    for i in range(10):
        pustalista.insert(Element(keys[i], values[i]))
# wypisanie listy
    print(pustalista)
# użycie search do wyszukania (i wypisania) danej o kluczu 2
# użycie insert do nadpisania wartości dla klucza 2 literą 'Z'
    pustalista.insert(Element(2, "Z"))
# użycie search do wyszukania (i wypisania) danej o kluczu 2
# użycie delete do usunięcia danych o kluczach 5, 6, 7
# wypisanie tablicy
    print(pustalista)
# użycie insert do wstawienia  danej 'W' o kluczu 6
# wypisanie tablicy