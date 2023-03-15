size = 0

class element:
    def __init__(self, next = None, data: list = None) -> None:
        self.tab_: list= []
        self.next_: element = next
        if not data is None:
            self.tab_ = data
            
    def get(self, index: int):
        elem = self
        while index >= len(elem.tab_) and elem.next_ is not None:
            index -= len(elem.tab_)
            elem = elem.next_
        if elem is not None:
            return elem.tab_[index]

    def insert(self, data, index: int):
        if len(self.tab_) < size:
            if index >= len(self.tab_):
                self.tab_.append(data)
            elif index < len(self.tab_):
                self.tab_ = self.tab_[:index] + [data] + self.tab_[index:]
        elif len(self.tab_) >= size:
            if self.next_ is None:
                self.next_ = element(next= None, data= self.tab_[size//2:])
                self.tab_ = self.tab_[:size//2]
        
            

    def delete(self, index: int):
        pass

    def debug(self):
        print(self.tab_)



if __name__ == "__main__":
    size = 6
    elem = element()
    elem.debug()
    print()
    for i in range(0,10):
        elem.insert(data = i, index = i)
        elem.debug()
    print(elem.get(4))
    elem.insert(10,1)
    elem.insert(11,8)
    elem.debug()
    elem.delete(1)
    elem.delete(2)
    elem.debug()