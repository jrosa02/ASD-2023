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
        return self.__priorytet > other.__priorytet
    
    def __lt__(self, other):
        return self.__priorytet < other.__priorytet

    def __str__(self) -> str:
        return str(self.__priorytet) + " : " + str(self.__dane)



class Kopiec:
    # konstruktor tworzący pustą kolejkę
    def __init__(self) -> None:
        self.tab = []
        self.size = 0
        self.heap_size = 0
    
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
    # dequeue - zwracająca None jeżeli kolejka jest pusta lub element kolejki o najwyższym priorytecie 
    # (zdejmując go z wierzchołka kopca)
    def dequeue(self):
        if self.is_empty():
            return None
        elem2ret = self.tab[0]
        self.tab[0] = None
        parent_index = 0
        left_child_idx = self.left(parent_index)
        right_child_idx = self.right(parent_index)
        if self.tab[left_child_idx] > self.tab[right_child_idx]:
            child_idx = left_child_idx
        else:
            child_idx = right_child_idx
        while child_idx < self.heap_size:
            self.tab[parent_index], self.tab[child_idx] = self.tab[child_idx], self.tab[parent_index]
            parent_index = child_idx
            left_child_idx = self.left(parent_index)
            right_child_idx = self.right(parent_index)
            if left_child_idx < self.size and right_child_idx < self.size and self.tab[left_child_idx] > self.tab[right_child_idx]:
                child_idx = left_child_idx
            else:
                child_idx = right_child_idx
        
        self.heap_size -= 1
        return elem2ret
        
            


        
    # enqueue - otrzymująca dane do wstawienia do kolejki (kopca)  - tym razem będzie to cały obiekt klasy implementującej element kolejki.
    #  UWAGA - element początkowo jest dokładany na koniec KOPCA, więc:
    #   jeżeli rozmiar kopca bedzie taki jak rozmiar tablicy, to będzie oznaczało append,
    #   a jeżeli będzie mniejszy to będzie to oznaczało zastąpienie istniejącego elementu tablicy. 
    def enqueue(self, element2insert):
        self.tab.append(element2insert)
        self.size += 1
        self.heap_size += 1
        parent_index = self.parent(self.size-1)
        child_index = self.size-1
        if self.size == 1:
            return
        while self.tab[parent_index] <= self.tab[child_index] and child_index != 0:
            self.tab[parent_index], self.tab[child_index] = self.tab[child_index], self.tab[parent_index]
            child_index = parent_index
            parent_index = self.parent(child_index)
            


    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        print("==================")
        self._print_tree(idx, lvl)
        print("==================")

    def _print_tree(self, idx, lvl):
        if idx<self.size:           
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
    elem = kopiec.dequeue()
    # użycie  peek do odczytu i wypisania kolejnej  danej
    print(kopiec.peek())
    # wypisanie aktualnego stanu kolejki w postaci tablicy
    kopiec.print_tab()
    # wypisanie zapamiętanej, usuniętej pierwszej danej z kolejki
    print(elem)
    # opróżnienie kolejki z wypisaniem usuwanych danych (użycie dequeue w pętli dopóki w kolejce będą dane)
    while not kopiec.is_empty():
        print(kopiec.dequeue())
    # wypisanie opróżnionej kolejki w postaci tablicy (powinno się wypisać { } )
