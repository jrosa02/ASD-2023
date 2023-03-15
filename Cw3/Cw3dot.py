size = 0

class element:
    def __init__(self, next, data = None) -> None:
        self.tab_: list= [None for _ in range(size)]
        self.next = next
        if not data is None:
            

    def get(self, index: int):
        return self.tab_[index]
    
    def insert(self, data, index: int):
        if len(self.tab_) == size:

        if index < len(self.tab_):
            self.tab_.append(data)

    def delete():
        pass

    def debug(self):
        print(self.tab_)


if __name__ == "__main__":
    size = 6
    elem = element(None)
    elem.debug()
    for i in range(0,10):
        elem.insert(data = i, index = i)
        elem.debug()
    elem.get(4)