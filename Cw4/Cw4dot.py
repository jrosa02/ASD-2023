import random
from typing import List

class Element:
    """Elementy listy również powinny być zaimplementowane jako klasa z atrybutami przechowującymi:
      klucz,  wartość (jakąś daną), liczbę poziomów oraz listę (tablicę) ze wskazaniami na następny element o rozmiarze równym liczbie poziomów."""
    def __init__(self, key, value = None, maxLevel:int = 4, nr_lvl = None) -> None:
        self.key_ = key
        self.value_ = value
        self.maxLevel_: int = maxLevel
        self.nr_lvl_: int = self.randomLevel() if nr_lvl is None else nr_lvl
        self.next_: List[Element] = [None for _ in range(self.maxLevel_)]
        pass

    def randomLevel(self, p = 0.5):
        lvl = 1   
        while random.random() < p and lvl < self.maxLevel_:
              lvl = lvl + 1
        return lvl
    
    def compare_next_keys(self, key):
        index = 0
        for i in range(len(self.next_)):
            if self.next_[i] is None: return None
            if self.next_[i].key_ < key: index = i
        return index
    
    def __str__(self) -> str:
        outstr: str = '\t'
        for i in reversed(range(self.maxLevel_)):
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
        
    
    def find_all_prev(self, elem2insert: Element) -> List[Element]:
        curr_elem = self.head_
        prev_elems = [None for _ in range(elem2insert.maxLevel_)]
        for level in reversed(range(elem2insert.maxLevel_)):
            while curr_elem.next_[level] is not None and curr_elem.next_[level].key_ < elem2insert.key_:
                curr_elem = curr_elem.next_[level]
            prev_elems[level] = curr_elem
        return prev_elems
        


    def search(self, key):
        """wyszukująca i zwracająca wartość odpowiadającą podanemu kluczowi (lub None)"""
        prev_elems = self.find_all_prev(Element(key, None, self.maxLevel_))
        if prev_elems[0].next_ is not None and prev_elems[0].next_[0].key_ == key:
            return prev_elems[0].next_[0].value_
        else:
            return None

    def insert(self, elem2insert: Element):
        """wstawiająca daną wg podanego klucza - podczas szukania miejsca 
        do wstawienia klucza powinna tu być tworzona lista  (tablica) zawierająca poprzedniki  znalezionego elementu  na każdym poziomie 
        (znaleziony element to ten, którego klucz jest większy od klucza wstawianego elementu);
        dla poziomów, których znaleziony element nie posiada  w tablicy poprzedników powinna być wpisana głowa listy (np. head)."""
        #find all elements on all levels(present in elem2insert) which keys are smaller descending from highest
        prev_elems = self.find_all_prev(elem2insert)
        curr_elem = prev_elems[0]
        post_current_elem = curr_elem.next_[0] #Element with higher or same key elem2insert
        if post_current_elem is None: #is last
            for level in range(elem2insert.nr_lvl_):
                prev_elems[level].next_[level] = elem2insert
        elif prev_elems[0].next_[0].key_ == elem2insert.key_:
            prev_elems[0].next_[0].value_ = elem2insert.value_     
        else:
            for level in range(elem2insert.nr_lvl_):
                elem2insert.next_[level] = prev_elems[level].next_[level]
                prev_elems[level].next_[level] = elem2insert
        


        

    def remove(self, key):
        """usuwająca daną o podanym kluczu"""
        prev_elems = self.find_all_prev(Element(key, None))
        curr_elem = prev_elems[0]
        post_current_elem = curr_elem.next_[0] #Element with higher or same key elem2insert
        for level in range(len(prev_elems)):
            if prev_elems[level].next_[level] is not None and prev_elems[level].next_[level].key_ == key:
                prev_elems[level].next_[level] = prev_elems[level].next_[level].next_[level]


    def displayList_(self):
        #Do debugu moja lepsza ;-)
        node = self.head_.next_[0]  # pierwszy element na poziomie 0
        keys = []                           # lista kluczy na tym poziomie
        while(node != None):
            keys.append(node.key_)
            node = node.next_[0]

        for lvl in range(self.maxLevel_-1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head_.next_[lvl]
            idx = 0
            while(node != None):                
                while node.key_>keys[idx]:
                    print("  ", end=" ")
                    idx+=1
                idx+=1
                print("{:2d}".format(node.key_), end=" ")     
                node = node.next_[lvl]    
            print("")
        print()






if __name__ == "__main__":
# utworzenie pustej listy
    pustalista = Listjuping()
# użycie insert do wpisana do niej 15 danych (niech kluczami będą  kolejne liczby od 1, a wartościami - kolejne litery),
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    values = "ABCDEFGHIJKLMNOPRSTUWXYZ"
    for i in range(15):
        pustalista.insert(Element(keys[i], values[i]))
# wypisanie listy
    #print(pustalista)
    pustalista.displayList_()
# użycie search do wyszukania (i wypisania) danej o kluczu 2
    print(pustalista.search(2))
# użycie insert do nadpisania wartości dla klucza 2 literą 'Z'
    pustalista.insert(Element(2, "Z"))
# użycie search do wyszukania (i wypisania) danej o kluczu 2
    print(pustalista.search(2))
# użycie delete do usunięcia danych o kluczach 5, 6, 7
    pustalista.remove(5)
    pustalista.remove(6)
    pustalista.remove(7)
# wypisanie tablicy
    #print(pustalista)
    pustalista.displayList_()
# użycie insert do wstawienia  danej 'W' o kluczu 6
    pustalista.insert(Element(6, "W"))
# wypisanie tablicy
    #print(pustalista)
    pustalista.displayList_()