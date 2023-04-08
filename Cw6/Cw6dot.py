class Node:
    def __init__(self, max_children):
        self.tab_ = [None]*(max_children-1)
        self.children: Node = [None]*(max_children)
        self.max_children = max_children

    def nononetab(self):
        return [i for i in self.tab_ if i is not None]
    def __len__(self):
        return len(self.nononetab())

    
    def append_forNone(self, data):
        #print("append")
        i =0 
        if self.tab_[0] is not None:
            while self.tab_[i] is not None:
                i+=1
        self.tab_[i] = data

    def insert2tab(self, data, index):
        #print("index < cap")
        if self.tab_[index] is None:
            self.tab_[index] = data
            #print("zastap None")
        else:
            self.tab_ = self.tab_[:index] + [data] + self.tab_[index:]
            #print("wstaw i rozson")
            if self.tab_[-1] is None:
                #print("usun None")
                self.tab_.pop()

    def delete_overflow(self):
        #Przed dodaniem rozsuwania wszystko było o wiele bardziej
        if len(self.tab_) > self.max_children:
            self.divide()


    def divide(self):
        tabl: list= [None for _ in range(self.max_children)]
        if self.tab_[:self.max_children//2] is not None:
            for i in range(len(self.tab_[:self.max_children//2])):
                tabl[i] = self.tab_[:self.max_children//2][i]
        self.tab_ = tabl
        

    def insert(self, data, index: int):
        """wstawiająca daną w miejscu wskazanym przez podany indeks, przesuwając istniejące elementy w prawo;
        jeżeli tablica elementu w którym ma nastąpić wstawienie jest pełna to do listy dokładany jest nowy element, 
        połowa zapełnionej tablicy jest przenoszona do nowego elementu i wstawienie danej 
        zachodzi albo w opróżnianym elemencie albo we wstawianym (w zależności gdzie 'wypada' miejsce wskazane przez indeks). 
        Podanie indeksu większego od aktualnej liczby elementów listy skutkuje dodaniem elementu na końcu listy."""
        #print("Inserting")
        if index < len(self):
            #print("index < capacity and index < len(self)")
            self.insert2tab(data, index)
        elif self.tab_[-1] is None and self.next_ is None:
            #print("Append")
            self.append_forNone(data)
        elif index > len(self):
            if self.next_ is None:
                #print("Simple append")
                self.tab_.append(data)
            else:
                self.next_.insert(data, index-len(self))

        self.delete_overflow()

        


        # if len(self.keys) >= self.max_children-1:
        #     mid = self.max_children//2 #MOŻNA ZMIENIĆ
        #     self.keys = [self.keys[mid]]

        print(self.tab_)
            
        

    


class BTree:
    def __init__(self, max_children):
        self.max_children = max_children
        self.root = Node(max_children)
    
    def insert(self, key):
        self.root.insert(key)
    
    # def print_tree(self):
    #     print("==============")
    #     self._print_tree(self.root, 0)
    #     print("==============")
    
    # def _print_tree(self, node: Node, lvl):
    #     if node is not None:
    #         for i in range(node.size+1):                    
    #             self._print_tree(node.children[i], lvl+1)
    #             if i<node.size:
    #                 print(lvl*'  ', node.keys[i])


    
if __name__ == "__main__":
    #utwórz puste drzewo o maksymalnej liczbie potomków równej 4
    btree = BTree(max_children = 4)
    # dodaj do niego elementy (będące jednocześnie kluczami) po kolei z listy: [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    keys = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    for key in keys:
        btree.insert(key)
    # wyświetl drzewo
    # btree.print_tree()
    # utwórz drugie puste drzewo, dodaj do niego 20 kolejnych liczb od 0 do 19 (będą to te same liczby co w liście ale dodane w kolejności rosnącej)
    # btree2 = BTree(4)
    # for i in range(20):
    #     btree2.insert(i)
    # # wyświetl stworzone drzewo (zauważ jak różni się od poprzedniego)
    # btree2.print_tree()
    # dodaj do drugiego drzewa kolejne liczby od 20 do 199, wyświetl drzewo (zauważ jak wzrosła jego wysokość)
    # utwórz trzecie puste drzewo o maksymalnej liczbie potomków równej 6, dodaj do niego te same liczby co do drugiego drzewa (od 0 do 199) i wyświetl go (zauważ jak zmalała jego wysokość)