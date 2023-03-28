import copy


class Node:
    def __init__(self, key, value = None, left_desc = None, right_desc = None) -> None:
        self.key_ = key
        self.value_ = value
        self.left_desc_: Node = left_desc
        self.right_desc_: Node = right_desc

    def __str__(self) -> str:
        return str(self.key_) + "-" + str(self.value_)

    def search(self, key, prev):
        if self.key_ == key:
            return self, prev
        elif self.key_ < key and self.left_desc_ is not None:
            return(self.left_desc_.search(key, self))
        elif self.key_ > key and self.right_desc_ is not None:
            return(self.right_desc_.search(key, self))
        else:
            return None
        

    def insert(self, key, value):
        if self.key_ == key:
            self.value_ = value
        elif self.key_ < key:
            if self.left_desc_ is not None:
                self.left_desc_.insert(key, value)
            else:
                self.left_desc_ = Node(key, value)
        elif self.key_ > key:
            if self.right_desc_ is not None:
                self.right_desc_.insert(key, value)
            else:
                self.right_desc_ = Node(key, value)

    def delete(self, prev):
        prev: Node = prev
        if self.left_desc_ is None and self.right_desc_ is None:
            if prev.key_ < self.key_:
                prev.left_desc_ = None
            else:
                prev.right_desc_ = None
        elif self.left_desc_ is not None:
            if prev.key_ < self.key_:
                prev.left_desc_ = self.left_desc_
            else:
                prev.right_desc_ = self.left_desc_
        elif self.right_desc_ is not None:
            if prev.key_ < self.key_:
                prev.left_desc_ = self.right_desc_
            else:
                prev.right_desc_ = self.right_desc_
        else:
            pass


    def height(self) -> int:
        llvl = 1
        rlvl = 1
        if self.right_desc_ is not None:
            rlvl = self.right_desc_.height() + 1
        if self.left_desc_ is not None:
            llvl = self.left_desc_.height() + 1
        
        return max(rlvl, llvl)
    
    def tolist(self, lst:list):
        if self is not None:
            if self.right_desc_ is not None:
                self.right_desc_.tolist(lst)
            lst.append((self.key_, self.value_))
            if self.left_desc_ is not None:
                self.left_desc_.tolist(lst)

        

class BST:
    def __init__(self, root: Node = None) -> None:
        self.root_: Node = root

    def search(self, key):
        if self.root_ is not None:
            return self.root_.search(key, self.root_)[0].value_
        else: 
            return None
        
    def insert(self, key, value):
        if self.root_ is not None:
            self.root_.insert(key, value)
        else:
            self.root_ = Node(key, value)

    def delete(self, key):
        node, prev = self.root_.search(key, self.root_)
        node.delete(prev)

    def height(self) -> int:
        return self.root_.height()
    
    def print(self) -> str:
        lst = []
        self.root_.tolist(lst)
        print(lst)

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root_, 0)
        print("==============")

    def __print_tree(self, node: Node, lvl: int):
        if node!=None:
            self.__print_tree(node.right_desc_, lvl+5)

            print()
            print(lvl*" ", node.key_, node.value_)
     
            self.__print_tree(node.left_desc_, lvl+5)


if __name__ == "__main__":
    # utworzenie pustego drzewa BST
    tree = BST()
    # dodanie kolejno elementy klucz:wartość -- {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}, tworząc drzewo o podanej strukturze, jak na rysunku: 
    keyvalue = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for key in keyvalue:
        tree.insert(key, keyvalue[key])
    # wypis drzewo 2D (funkcją print_tree)
    tree.print_tree()
    # wyświetl zawartość drzewa jako listę elementów ułożonych od najmniejszego do największego klucza wypisanych w postaci klucz wartość - przykładowo powyższe drzewo powinno być wypisane tak:
    # 3 H,5 D,8 I,15 B,20 E,24 L,37 J,50 A,58 F,60 K,62 C,91 G,
    tree.print()
    # # znajdź klucz 24 i wypisz wartość
    print(tree.search(24))
    # zaktualizuj wartość "AA" dla klucza 20
    tree.insert(20, "AA")
    # dodaj element 6:M
    tree.insert(6, "M")
    # usuń element o kluczu 62
    # dodaj element 59:N
    # dodaj element 100:P
    # usuń element o kluczu 8
    # usuń element o kluczu 15
    # wstaw element 55:R
    # usuń element o kluczu 50
    # usuń element o kluczu 5
    # usuń element o kluczu 24
    # wypisz wysokość drzewa
    # wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość
    # wyświetl drzewo 2D
