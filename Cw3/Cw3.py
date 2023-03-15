def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]

class Kolejka:
    def __init__(self) -> None:
        self.size = 5
        self.tab_ = [None for _ in range(self.size)]
        self.write_idx_ = 0
        self.read_idx_ = 0
    
    def is_empty(self):
        if self.write_idx_ == self.read_idx_:
            return True
        else:
            return False
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab_[self.read_idx_]
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            a = self.peek()
            if self.read_idx_ == self.size-1:
                self.read_idx_ = 0
            else:
                self.read_idx_ += 1
            return a
        
    def enqueue(self, data):
        self.tab_[self.write_idx_] = data
        if self.write_idx_ == self.size-1:
            self.write_idx_ = 0
        else:
            self.write_idx_ += 1
        if self.is_empty():
            realloc(self.tab_, self.size * 2)
            self.tab_= [self.tab_[i] for i in range(self.write_idx_)] + [None for _ in range(self.size)] + [self.tab_[i] for i in range(self.write_idx_, self.size)]
            self.read_idx_ += self.size
            self.size = len(self.tab_)


    def __str__(self):
        if self.is_empty():
            return "[]"
        output = "[ "
        if self.read_idx_ < self.write_idx_:
            for i in range(self.read_idx_, self.write_idx_):
                output += str(self.tab_[i]) + " "
        else:
            for i in range(self.read_idx_, self.size):
                output += str(self.tab_[i]) + " "
            for i in range(self.write_idx_):
                output += str(self.tab_[i]) + " "
        output += "]"
        return output
    
    def debug(self):
        print(str(self.tab_) + "Wrt-> " + str(self.write_idx_) + " Rd->" +str(self.read_idx_))
            
            


if __name__ == "__main__":
    kolej = Kolejka()
    for i in range(4):
        kolej.enqueue(i+1)
    print(kolej.dequeue())
    print(kolej.peek())
    print(kolej)
    for i in range(4):
        kolej.debug()
        kolej.enqueue(i+5)
    kolej.debug()
    while( not kolej.is_empty()):
        print(kolej.dequeue())
    print(kolej)
    #kolej.debug()