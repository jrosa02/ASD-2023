

class Elem:
    def __init__(self, key, value) -> None:
        self.key_ = key
        self.value_ = value

    def __str__(self) -> str:
        return "(" + str(self.key_) + " -> " + str(self.value_) + ")\n" 
    

class Hashmap:
    def __init__(self, size: int, c1: int = 1, c2: int = 0) -> None:
        self.tab_ :list[Elem] = [None for _ in range(size)]
        self.size_ = size
        self.c1_ = c1
        self.c2_  = c2
        
    def __len__(self) -> int:
        return self.size_

    def hash(self, key) -> int:
        if isinstance(key, str):
            sums = 0
            for letter in key:
                sums += ord(letter)
            return sums % len(self)
        elif isinstance(key, int):
            #print("hash ->" + str(len(self)))
            return key % len(self)
        
    def solve_collision(self, key) -> int:
        default_index = self.hash(key) + 1
        i = 0
        while True:
            new_index = (default_index + self.c1_*i + self.c2_ * i**2) % len(self)
            if new_index == default_index:
                return None
            if self.tab_[new_index] is None or self.tab_[new_index].key_ == key:
                return new_index
            

            i += 1
            if i >= len(self):
                i = 0 

    def search(self, key):
        default_index = self.hash(key)
        if self.tab_[default_index] is not None and self.tab_[default_index].key_ == key:
            #print("default search")
            return self.tab_[default_index].value_
        else:
            if self.c1_ == 1 and self.c2_ == 0:
                i = default_index + 1
                while True:
                    if i == default_index:
                        return None
                    
                    if self.tab_[i].key_ == key:
                        return self.tab_[i].value_
                    
                    i += 1
                    if i >= len(self):
                        i = 0       
                return None      

    def insert(self, elem: Elem) -> bool:
        """wstawiająca daną wg podanego klucza, jeżeli element o takim kluczu istnieje, jego wartość powinna zostać nadpisana"""
        default_index = self.hash(elem.key_)
        if self.tab_[default_index] is None or self.tab_[default_index].key_ == elem.key_:
            self.tab_[default_index] = elem
            return True
        else:
            if self.c1_ == 1 and self.c2_ == 0:
                i = default_index + 1
                while True:
                    if i == default_index:
                        return None
                    if self.tab_[i] is None or self.tab_[i].key_ == elem.key_:
                        self.tab_[i] = elem
                        return True
                    
                    i += 1
                    if i >= len(self):
                        i = 0
                return None

    def remove(self, key):
        default_index = self.hash(key)
        if self.tab_[default_index] is None or self.tab_[default_index].key_ == key:
            self.tab_[default_index] = None
            return True
        else:
            if self.c1_ == 1 and self.c2_ == 0:
                i = default_index + 1
                while True:
                    if i == default_index:
                        return None
                    if self.tab_[i] is None or self.tab_[i].key_ == key:
                        self.tab_[i] = None
                        return True
                    
                    i += 1
                    if i >= len(self):
                        i = 0
                return None

    def __str__(self):
        outstr: str = "--Hashmap--\n"
        for elem in self.tab_:
            if elem is None:
                outstr += "(None)\n"
            else:
                outstr += str(elem)
        return outstr + "----------" 



if __name__ =="__main__":
    mapa = Hashmap(size = 13)
    keys = [1, 2, 3, 4, 5, 18, 31, 8, 9, 10, 11, 12, 13, 14, 15]
    values = "ABCDEFGHIJKLMNOPRSTUWXYZ"
    for i in range(len(keys)):
        mapa.insert(Elem(keys[i], values[i]))
    print(mapa)
    print(mapa.search(5))
    print(mapa.search(14))
    mapa.insert(Elem(5, "Z"))
    print(mapa.search(5))
    mapa.remove(5)
    print(mapa)
    print(mapa.search(31))
    mapa.insert(Elem('test', "W"))
    print(mapa)

    mapa2 = Hashmap(13)
    for i in range(1,14):
        mapa2.insert(Elem(13*i, values[i-1]))
    print(mapa2)