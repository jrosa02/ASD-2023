class element:
    def __init__(self, data, next) -> None:
        self.data_ = data
        self.next_ = next

    def __str__(self):
        return " -> " + str(self.data_) + "\n"

class linked_list:
    def __init__(self) -> None:
        self.head_: element = None

    def destroy(self):
        """usunięcie/zniszczenie całej listy - tu też jest łatwo - wystarczy ustawić head na None, a Python sam zwolni pamięć :)"""
        self.head_ = None

    def is_empty(self) -> bool:
        """metoda zwracająca True dla pustej listy"""
        if self.head_ is None:
            return True
        return False
    
    def __len__(self) -> int:
        i: int = 0
        if self.is_empty():
            return i
        i += 1
        el = self.head_
        while not el.next_ is None:
            i += 1
            el = el.next_
        return i
    
    def get(self):
        if not self.is_empty():
            return self.head_.data_

    def __add__(self, data):
        """metoda dodająca na początek listy (jako argument ma dostać dane, które wstawi do pola data tworzonego przez tę funkcję elementu listy)"""
        self.head_ = element(data, self.head_)

    def append(self, data):
        """metoda dodająca na koniec listy (argument taki sam jak w add)"""
        el_2_app2 = element(data, None)
        if not self.is_empty():
            el: element = self.head_
            while(el.next_ != None):
                el = el.next_
            el.next_ = el_2_app2
        else:
            self.head_ = el_2_app2
        

    def remove(self):
        """metoda usuwająca element z początku listy"""
        if self.is_empty():
            return
        if self.head_.next_ is None:
            self.head_ = None
        else:
            self.head_ = self.head_.next_

    def remove_end(self):
        """metoda usuwająca element z końca listy"""
        if self.is_empty():
            return None
        if self.head_.next_ is None:
            self.head_ = None
            return None
        el: element = self.head_
        while(el.next_.next_ != None):
            el = el.next_
        el.next_ = None



    def __str__(self) -> str:
        if not self.is_empty():
            strink = str(self.head_)
            el: element = self.head_
            while(not el.next_ is  None):
                strink += str(el.next_)
                el = el.next_
            return strink
        else:
            return "empty"
    
if __name__ == "__main__":
    prot = [('AGH', 'Kraków', 1919),
        ('UJ', 'Kraków', 1364),
        ('PW', 'Warszawa', 1915),
        ('UW', 'Warszawa', 1915),
        ('UP', 'Poznań', 1919),
        ('PG', 'Gdańsk', 1945)]
    
    uczelnie = linked_list()
    for elem in prot:
        uczelnie.__add__(elem)
    print(uczelnie)
    print(len(uczelnie))
    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.remove_end()
