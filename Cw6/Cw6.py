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
    def __init__(self) -> None:
        self.tab = []
        self.tree_size = 0
        self.tab_size = 0
    
    # is_empty - zwracająca True jeżeli kolejka jest pusta
    def is_empty(self):
        if len(self.tab) == 0:
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
        
    def is_smaller(self, a, b):
        if a is None and b is None:
            return False
        elif a is None:
            return False
        elif b is None:
            return True
        else:
            return a > b

    

    def _dequeue(self, index):
        left_child_i = self.left(index)
        right_child_i = self.right(index)
        if self.is_smaller(left_child_i, right_child_i):
            child_i = left_child_i
        else:
            child_i = right_child_i
        if child_i > self.tab_size:
            return None
        self.tab[child_i], self.tab[index] = self.tab[index], self.tab[child_i]
        print(child_i)
        self._dequeue(child_i)
        return None
    

    # dequeue - zwracająca None jeżeli kolejka jest pusta lub element kolejki o najwyższym priorytecie 
    # (zdejmując go z wierzchołka kopca)
    def dequeue(self):
        if self.is_empty():
            return None
        ret_value = self.peek()
        self.tab[0] = None
        self._dequeue(0)
        self.tree_size -= 1
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
        while (self.tab[parent_index] is None or self.tab[parent_index] <= self.tab[child_index]) and child_index != 0:
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


if __name__ == "__main__":
    # utworzenie pustej kolejki
    kopiec = Kopiec()
    # użycie w pętli enqueue do wpisana do niej elementów których priorytety będą brane z listy [7, 5, 1, 2, 5, 3, 4, 8, 9], a odpowiadające im wartości będą kolejnymi literami z napisu "GRYMOTYLA"
    priorytety = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    for priorytet in priorytety:
        kopiec.enqueue(priorytet)
    # wypisanie aktualnego stanu kolejki w postaci kopca
    kopiec.print_tree(0, 0)
    # wypisanie aktualnego stanu kolejki w postaci tablicy
    kopiec.print_tab()
    # użycie dequeue do odczytu  pierwszej  danej z kolejki, proszę ją zapamiętać
    kopiec.print_tree()
    elem = kopiec.dequeue()
    kopiec.print_tree()
    # użycie  peek do odczytu i wypisania kolejnej  danej
    print(kopiec.peek())
    # wypisanie aktualnego stanu kolejki w postaci tablicy
    kopiec.print_tab()
    # wypisanie zapamiętanej, usuniętej pierwszej danej z kolejki
    print(elem)
    # opróżnienie kolejki z wypisaniem usuwanych danych (użycie dequeue w pętli dopóki w kolejce będą dane)
    #while not kopiec.is_empty():
    #    kopiec.dequeue()
    # wypisanie opróżnionej kolejki w postaci tablicy (powinno się wypisać { } )
