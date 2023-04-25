import time
import random

class Node:
    # Element kolejki niech będzie obiektem klasy, której atrybutami będą __dane i __priorytet.
    # Ta klasa powinna mieć zdefiniowane 'magiczne' metody pozwalające na użycie na jej obiektach operatorów
    # < i >  (metody __lt__ i __gt__) oraz wypisanie ich print-em (__str__) w postaci
    # priorytet : dane.
    # Dzięki zastosowaniu operatorów < i > atrybuty __dane i  __priorytet mogą (i powinny być) prywatne.
    def __init__(self, priorytet, dane = None) -> None:
        self.__dane = dane
        self.__priorytet = priorytet
    
    def __gt__(self, other):
        if other == None:
           return True
        return self.__priorytet > other.__priorytet
    
    def __lt__(self, other):
        if other == None:
            return False
        return self.__priorytet < other.__priorytet

    def __str__(self) -> str:
        return str(self.__priorytet) + " : " + str(self.__dane)



class Kopiec:
    # konstruktor tworzący pustą kolejkę
    def __init__(self, tab2sort: list = None) -> None:
        self.tree_size = 0
        self.tab_size = 0
        if tab2sort == None:
            self.tab = []
        else:
            self.tab_size = len(tab2sort)
            self.tree_size = self.tab_size
            self.tab = tab2sort
            for i in range(self.tab_size, -1, -1):
                self._sort_down(i)

    def sort(self):
        for i in range(len(self.tab)-1, -1, -1):
            self.tab[i] = self.dequeue()        


    
    # is_empty - zwracająca True jeżeli kolejka jest pusta
    def is_empty(self):
        if self.tree_size == 0:
            return True
        else:
            return False
        

    # Dodatkowo, aby usprawnić poruszanie się po kopcu, proszę napisać metody left i right,
    # które otrzymawszy indeks węzła zwracają indeks odpowiednio lewego i prawego potomka,
    # oraz metodę parent, która na podstawie indeksu węzła zwraca indeks jego rodzica.
    def parent(self, index: int):
        parent = (index-1)//2
        if parent < 0:
            return 0
        else:
            return parent
        
    def right(self, index: int):
        right = index*2 + 1
        return right
    
    def left(self, index: int):
        left = index*2 + 2
        return left 
    
    # peek - zwracająca None jeżeli kolejka jest pusta lub element kolejki o najwyższym priorytecie (czyli największej wartości atrybutu __priorytet)
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0]

    

    def _sort_down(self, index):
        #self.print_tree()
        if index < self.tree_size:
            if self.left(index) < self.tree_size and self.tab[self.left(index)] > self.tab[self.right(index)]:
                child_i = self.left(index) 
                #print("Lefe bigger")
            elif self.right(index) < self.tree_size:
                child_i = self.right(index)
                #print("right bigger")
            else:
                return None
            if self.tab[index] < self.tab[child_i]:
                self.tab[index], self.tab[child_i] = self.tab[child_i], self.tab[index]
            self._sort_down(child_i)
    
        pass

    # dequeue - zwracająca None jeżeli kolejka jest pusta lub element kolejki o najwyższym priorytecie 
    # (zdejmując go z wierzchołka kopca)
    def dequeue(self):
        if self.is_empty():
            return None
        ret_value = self.peek()
        self.tab[0] = self.tab[self.tree_size-1]
        self.tree_size -= 1
        self._sort_down(0)
        
        return ret_value
    
        
    # enqueue - otrzymująca dane do wstawienia do kolejki (kopca)  - tym razem będzie to cały obiekt klasy implementującej element kolejki.
    #  UWAGA - element początkowo jest dokładany na koniec KOPCA, więc:
    #   jeżeli rozmiar kopca bedzie taki jak rozmiar tablicy, to będzie oznaczało append,
    #   a jeżeli będzie mniejszy to będzie to oznaczało zastąpienie istniejącego elementu tablicy. 
    def enqueue(self, element2insert):
        self.tab.append(element2insert)
        self.tree_size += 1
        self.tab_size += 1
        parent_index = self.parent(self.tree_size-1)
        child_index = self.tree_size-1
        if self.tree_size == 1:
            return
        while (self.tab[parent_index] is None or self.tab[parent_index] < self.tab[child_index]) and child_index != 0:
            self.tab[parent_index], self.tab[child_index] = self.tab[child_index], self.tab[parent_index]
            child_index = parent_index
            parent_index = self.parent(child_index)
            


    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.tab_size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx = 0, lvl = 0):
        print("==================")
        self._print_tree(idx, lvl)
        print("==================")

    def _print_tree(self, idx, lvl):
        if idx<self.tree_size:           
            self._print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self._print_tree(self.left(idx), lvl+1)



def wybier_sort(lst:list):
    for i in range(len(lst)):
        m = i
        for j in range(i, len(lst)):
            if lst[m] > lst[j]:
                m = j
        lst[m], lst[i] = lst[i], lst[m]
    return lst


if __name__ == "__main__":
    param =  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    lst = []
    for elem in param:
        lst.append(Node(elem[0], elem[1]))
    kopiec = Kopiec(lst)
    kopiec.print_tree()
    kopiec.print_tab()
    kopiec.sort()
    print("Posortowane:")
    kopiec.print_tab()
    print("Sortowanie niestabilne")


#Drugi test: Wygeneruj losowo 10000 liczb w przedziale od 0 do 99 i wpisz je do tablicy. 
# Posortuj tę tablicę przez stworzenie i rozebranie kopca. Wypisz czas sortowania takiej tablicy. 
# W celu realizacji tego zadania  należy zaimportować moduły random i time.  
# Do generowania liczb można wykorzystać zapis int(random.random() * 100) 
# powodujący wylosowanie liczby całkowitej z zakresu 0-99, natomiast do pomiaru czasu można zaadaptować kod:

    lst = []
    for i in range(10000):
        lst.append(int(random.random() * 100))

    t_start = time.perf_counter()
    kopiec = Kopiec(lst)
    kopiec.sort()    
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    #kopiec.print_tab()
    print()

    lst = []
    param =  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    for elem in param:
        lst.append(Node(elem[0], elem[1]))
    wybier_sort(lst)
    for elem in lst:
        print("(", elem, ")", end = ' ')
    print()
    print("Sortowanie niestabilne")
    
    lst = []
    for i in range(10000):
        lst.append(int(random.random() * 100))

    t_start = time.perf_counter()
    wybier_sort(lst)   
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))   
    #print(lst)
