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

    def find_leftest(self, prev = None):
        if self.left_desc_ is None:
            prev: Node = prev
            return self, prev
        else:
            return self.left_desc_.find_leftest(prev = self)
        
    def find_rightest(self, prev = None):
        if self.right_desc_ is None:
            prev: Node = prev
            return self, prev
        else:
            return self.right_desc_.find_rightest(prev = self)


    def delete(self, prev):
        #print(self)
        prev: Node = prev
        if self.left_desc_ is None and self.right_desc_ is None:
            if prev.key_ < self.key_:
                prev.left_desc_ = None
            else:
                prev.right_desc_ = None
        elif self.left_desc_ is not None and self.right_desc_ is None:
            if prev.key_ < self.key_:
                prev.left_desc_ = self.left_desc_
            else:
                prev.right_desc_ = self.left_desc_
        elif self.left_desc_ is None and self.right_desc_ is not None:
            if prev.key_ < self.key_:
                prev.left_desc_ = self.right_desc_
            else:
                prev.right_desc_ = self.right_desc_
        else:
            if prev.key_ < self.key_:
                node2ins, prevnode2ins = self.right_desc_.find_leftest(self)
                prevnode2ins.left_desc_ = None      #usuwanie obiektu do podstawienia ze starej pozycji
                node2append, prevnode2append = node2ins.find_rightest(node2ins)   #znalezienie najmniejszego potomka obiektu do podstawienia
                node2append.right_desc_ = self.right_desc_       
                node2ins.left_desc_ = self.left_desc_       #podpięcie wszystkich lewych potomków do obiektu dpodst który nie może mieć swoich lewych bo jest najbardziej lewy
                prev.left_desc_ = node2ins
            else:
                # 24-37-20-24-
                selfrightdesc = self.right_desc_
                node2ins, prevnode2ins = self.left_desc_.find_rightest(self)
                prevnode2ins.right_desc_ = None      #usuwanie obiektu do podstawienia ze starej pozycji
                node2append, prevnode2append = node2ins.find_leftest(node2ins)   #znalezienie najmniejszego potomka obiektu do podstawienia
                if prevnode2append !=node2ins:
                    node2append.left_desc_ = self.left_desc_       
                node2ins.right_desc_ = selfrightdesc       #podpięcie wszystkich prawych potomków do obiektu dpodst który nie może mieć swoich lewych bo jest najbardziej lewy
                prev.right_desc_ = node2ins


            
                

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

    def __str__(self):
        return str(self.key_) + " : " + str(self.value_)

        

class BST:
    def __init__(self, root: Node = None) -> None:
        self.root_: Node = root

    def search(self, key):
        if self.root_ is not None:
            x = self.root_.search(key, self.root_)
            if x == None:
                print("Not found: " + str(key))
                return None
            return x[0].value_
        else: 
            return None
        
    def insert(self, key, value):
        if self.root_ is not None:
            self.root_.insert(key, value)
        else:
            self.root_ = Node(key, value)

    def delete(self, key):
        x = self.root_.search(key, self.root_)
        if x == None:
            print("Not found: " + str(key))
            return None
        node, prev = x
        if key == self.root_.key_:
            node2ins, prevnode2ins = self.root_.left_desc_.find_rightest(self.root_)
            prevnode2ins.right_desc_ = None      #usuwanie obiektu do podstawienia ze starej pozycji
            node2ins.right_desc_ = self.root_.right_desc_
            node2ins.left_desc_ = self.root_.left_desc_
            self.root_ = node2ins
        else:
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
    tree.delete(62)
    # dodaj element 59:N
    tree.insert(59, "N")
    # dodaj element 100:P
    tree.insert(100, "P")
    # usuń element o kluczu 8
    tree.delete(8)
    # usuń element o kluczu 15
    tree.delete(15)
    # 24-37-20-24-
    # wstaw element 55:R
    tree.insert(55, "r")
    # usuń element o kluczu 50
    tree.delete(50)
    # # usuń element o kluczu 5
    tree.delete(5)
    # usuń element o kluczu 24
    tree.delete(24)
    # wypisz wysokość drzewa
    print(tree.height())
    # wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość
    tree.print()
    # wyświetl drzewo 2D\
    tree.print_tree()
