capacity = 0


class element:
    def __init__(self, next = None, datalist: list = None) -> None:
        print("Eleme init")
        self.tab_: list= [None for _ in range(capacity)]
        if datalist is not None:
            for i in range(len(datalist)):
                self.tab_[i] = datalist[i]
        self.next_: element = next
        print(self.tab_)

    def __len__(self):
        return len([i for i in self.tab_ if i is not None])
            
    def get(self, index: int):
        elem = self
        while index >= len(elem) and elem.next_ is not None:
            index -= len(elem)
            elem = elem.next_
        if elem is not None:
            return elem.tab_[index]
        
    def append_forNone(self, data):
        print("append")
        i =0 
        if self.tab_[0] is not None:
            while self.tab_[i] is not None:
                i+=1
        self.tab_[i] = data

    def insert2tab(self, data, index):
        print("index < cap")
        if self.tab_[index] is None:
            self.tab_[index] = data
            print("zastap None")
        else:
            self.tab_ = self.tab_[:index] + [data] + self.tab_[index:]
            print("wstaw i rozson")
            if self.tab_[-1] is None:
                print("usun None")
                self.tab_.pop()

    def delete_overflow(self):
        #Przed dodaniem rozsuwania wszystko było o wiele bardziej
        if len(self.tab_) > capacity:
            self.divide()


    def divide(self):
        elems: element = element(next=self.next_, datalist= self.tab_[capacity//2:])
        tabl: list= [None for _ in range(capacity)]
        if self.tab_[:capacity//2] is not None:
            for i in range(len(self.tab_[:capacity//2])):
                tabl[i] = self.tab_[:capacity//2][i]
        self.tab_ = tabl
        self.next_ = elems
        

    def insert(self, data, index: int):
        """wstawiająca daną w miejscu wskazanym przez podany indeks, przesuwając istniejące elementy w prawo;
        jeżeli tablica elementu w którym ma nastąpić wstawienie jest pełna to do listy dokładany jest nowy element, 
        połowa zapełnionej tablicy jest przenoszona do nowego elementu i wstawienie danej 
        zachodzi albo w opróżnianym elemencie albo we wstawianym (w zależności gdzie 'wypada' miejsce wskazane przez indeks). 
        Podanie indeksu większego od aktualnej liczby elementów listy skutkuje dodaniem elementu na końcu listy."""
        print("Inserting")
        if index < len(self):
            print("index < capacity and index < len(self)")
            self.insert2tab(data, index)
        elif self.tab_[-1] is None and self.next_ is None and index < capacity:
            print("Append")
            self.append_forNone(data)
        elif index > len(self):
            if self.next_ is None:
                self.tab_.append(data)
            else:
                self.next_.insert(data, index-len(self))


        


        
            
        self.delete_overflow()

    def insert_old(self, data, index: int):
        """wstawiająca daną w miejscu wskazanym przez podany indeks, przesuwając istniejące elementy w prawo;
        jeżeli tablica elementu w którym ma nastąpić wstawienie jest pełna to do listy dokładany jest nowy element, 
        połowa zapełnionej tablicy jest przenoszona do nowego elementu i wstawienie danej 
        zachodzi albo w opróżnianym elemencie albo we wstawianym (w zależności gdzie 'wypada' miejsce wskazane przez indeks). 
        Podanie indeksu większego od aktualnej liczby elementów listy skutkuje dodaniem elementu na końcu listy."""

        print("Inserting")
        if index < capacity:
            print("index < cap")
            if self.tab_[index] is None:
                self.tab_[index] = data
                print("zastap None")
            else:
                self.tab_ = self.tab_[:index] + [data] + self.tab_[index:]
                print("wstaw i rozson")
                if self.tab_[-1] is None:
                    print("usun None")
                    self.tab_.pop()
        elif self.tab_[-1] is None and self.next_ is None:
                print("append")
                i =0 
                if self.tab_[0] is not None:
                    while self.tab_[i] is not None:
                        i+=1
                self.tab_[i] = data
        if index >= capacity:
            print("To next elem")
            if self.next_ is None:
                print("nowy element")
                lst = [data]
                self.next_ = element(next= None, datalist=[data])
            elif self.next_ is not None:
                self.next_.insert(data, index-len(self.tab_))

        self.delete_overflow()

    def delete(self, index: int):
        pass

    def __str__(self):
        out = "-----------------------------------\n"
        out += str(self.tab_) + "\n"
        elem = self
        while elem.next_ is not None:
            elem = elem.next_
            out += "->" + str(elem.tab_) + "\n"
        out += ("-----------------------------------")
        return out

    def debug(self):
        print(self)


class unrolledlinkedlist():
    def __init__(self, head:element = None) -> None:
        if head is None:
            self.head_ = element()
        else: self.head_ = head

    def get(self, index: int):
        if self.head_ is not None:
            return self.head_.get(index)
        else:
            return None

    def insert(self, data, index: int):
        if self.head_ is not None:
            self.head_.insert(data =data, index = index)

    def delete(self, index: int):
        if self.head_ is not None:
            self.head_.delete(index)

    def __str__(self) -> str:
        if self.head_ is not None:
            return self.head_.__str__()
        else:
            return "[]"
    
    def debug(self):
        if self.head_ is not None:
            return self.head_.debug()
        else:
            return "[]"


    

if __name__ == "__main__":
    capacity = 6
    elem = unrolledlinkedlist()
    elem.debug()
    print("Inserting")
    for i in range(0,10):
        elem.insert(data = i, index = i)
        elem.debug()
    print("Getting [4]: " + str(elem.get(4)))
    print("Random insert (10,1),(11,8)")
    elem.insert(10,1)
    elem.insert(11,8)

    elem.debug()
    elem.delete(1)
    elem.delete(2)
    print("Deleting")
    elem.debug()
