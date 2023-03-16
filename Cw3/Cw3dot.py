size = 0

class element:
    def __init__(self, next = None, datalist: list = None) -> None:
        self.tab_: list= [None for _ in range(size)]
        if datalist is not None:
            for i in range(len(datalist)):
                self.tab_[i] = datalist[i]
        self.next_: element = next
            
    def get(self, index: int):
        elem = self
        while index >= len(elem.tab_) and elem.next_ is not None:
            index -= len(elem.tab_)
            elem = elem.next_
        if elem is not None:
            return elem.tab_[index]

    def insert(self, data, index: int):
        """wstawiająca daną w miejscu wskazanym przez podany indeks, przesuwając istniejące elementy w prawo;
        jeżeli tablica elementu w którym ma nastąpić wstawienie jest pełna to do listy dokładany jest nowy element, 
        połowa zapełnionej tablicy jest przenoszona do nowego elementu i wstawienie danej 
        zachodzi albo w opróżnianym elemencie albo we wstawianym (w zależności gdzie 'wypada' miejsce wskazane przez indeks). 
        Podanie indeksu większego od aktualnej liczby elementów listy skutkuje dodaniem elementu na końcu listy."""

        print("Inserting")
        print(index)
        if index < size:
            print("index < size")
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
        if index >= size:
            print("To next elem")
            if self.next_ is None:
                print("nowy element")
                lst = [data]
                self.next_ = element(next= None, datalist=[data])
            elif self.next_ is not None:
                self.next_.insert(data, index-len(self.tab_))


        #Przed dodaniem rozsuwania wszystko było o wiele bardziej
        if len(self.tab_) > size:
            elems: element = element(next=self.next_, datalist= self.tab_[size//2:])
            tabl: list= [None for _ in range(size)]
            if self.tab_[:size//2] is not None:
                for i in range(len(self.tab_[:size//2])):
                    tabl[i] = self.tab_[:size//2][i]
            self.tab_ = tabl
            self.next_ = elems

            

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



if __name__ == "__main__":
    size = 6
    elem = element()
    elem.debug()
    print("Inserting")
    for i in range(0,10):
        elem.insert(data = i, index = i)
        elem.debug()
    print("Getting: " + str(elem.get(4)))
    elem.insert(10,1)
    elem.insert(11,8)
    print("Random insert")
    elem.debug()
    elem.delete(1)
    elem.delete(2)
    print("Deleting")
    elem.debug()
