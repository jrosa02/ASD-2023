class Node:
    def __init__(self, key, value = None, left_desc = None, right_desc = None) -> None:
        self.key_ = key
        self.value_ = value
        self.left_desc_: Node = left_desc
        self.right_desc_: Node = right_desc

    def __str__(self) -> str:
        return str(self.key_) + " " + str(self.value_) + " =" + str(self.imbalance())

    def search(self, key, prev):
        if self.key_ == key:
            return self, prev
        elif self.key_ < key and self.left_desc_ is not None:
            return(self.left_desc_.search(key, self))
        elif self.key_ > key and self.right_desc_ is not None:
            return(self.right_desc_.search(key, self))
        else:
            return None
        
    def imbalance(self):
        if self.left_desc_ is None:
            left_h = 0
        else:
            left_h = self.left_desc_.height()
        if self.right_desc_ is None:
            right_h = 0
        else:
            right_h = self.right_desc_.height()
        return left_h-right_h

        

    def insert(self, key, value, prev, tree):
        if self.key_ == key:
            self.value_ = value
        elif self.key_ < key:
            if self.left_desc_ is not None:
                self.left_desc_.insert(key, value, self, tree)
            else:
                self.left_desc_ = Node(key, value)
        elif self.key_ > key:
            if self.right_desc_ is not None:
                self.right_desc_.insert(key, value, self, tree)
            else:
                self.right_desc_ = Node(key, value)
        self.balance(prev, tree)

        #Balancing
    def balance(self, prev, tree = None):
        prev:Node = prev
        if self.imbalance() > 1:
            #print("RR rot")
            #self.print_subtree()
            self.RR(prev,  tree)

        if self.imbalance() < -1:
            # print("LL rot")
            #self.print_subtree()
            self.LL(prev, tree)



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


    def delete(self, prev, tree):
        print("self ", self)
        print("prev ", prev)
        prev :Node = prev
        if self.left_desc_ is None:
            if prev.key_ > self.key_:
                prev.left_desc_ = self.right_desc_
            else:
                prev.right_desc_ = self.right_desc_
        elif self.right_desc_ is None:
            if prev.key_ > self.key_:
                prev.left_desc_ = self.left_desc_
            else:
                prev.right_desc_ = self.left_desc_
        else:
            rightleftest, prevrleftest = self.right_desc_.find_leftest(self)
            print()
            self.key_ = rightleftest.key_
            self.value_ = rightleftest.value_
            rightleftest = None
            print()

        

        

    def LL(self, prev, tree = None):
        prev: Node = prev
        tree: BST = tree
        if self == tree.root_:
            tree.root_ = self.right_desc_
        if prev.right_desc_ == self:
            prev.right_desc_ = self.right_desc_
        elif prev.left_desc_ == self:
            prev.left_desc_ = self.right_desc_
        self.right_desc_.left_desc_, self.right_desc_ = self, self.right_desc_.left_desc_

    def RR(self,prev, tree = None):
        prev: Node = prev
        tree: BST = tree
        if self == tree.root_:
            tree.root_ = self.left_desc_
        if prev.right_desc_ == self:
            prev.right_desc_ = self.left_desc_
        elif prev.left_desc_ == self:
            prev.left_desc_ = self.left_desc_ 
        self.left_desc_.right_desc_, self.left_desc_ = self, self.left_desc_.right_desc_

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

    def print_subtree(self):
        print("Subtree====")
        self.__print_subtree()
        print("===========")

    def __print_subtree(self, lvl: int = 0):
        if self.right_desc_ is not None:
            self.right_desc_.__print_subtree(lvl+5)

        print(lvl*" ", self)

        if self.left_desc_ is not None:
            self.left_desc_.__print_subtree(lvl+5)

        

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
        
    def insert(self, key, value = None):
        if self.root_ is not None:
            self.root_.insert(key, value, self.root_, self)
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
            self.root_.balance(self.root_, self)
        else:
            node.delete(prev, self)

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

            print(lvl*" ", node)

            self.__print_tree(node.left_desc_, lvl+5)




if __name__ == "__main__":
    # utworzenie pustego drzewa BST
    dżewo = BST()
    # dodanie kolejno elementy klucz:wartość -- {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'} 
    # tworząc drzewo o podanej strukturze, jak na rysunku: 
    słownik = {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}
    for key in słownik:
        dżewo.insert(key, słownik[key])
        #dżewo.print_tree()
    # wyświetl drzewo 2D
    dżewo.print_tree()
    # wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość
    dżewo.print()
    # wyszukaj element o kluczu 10 i wypisz wartość
    print(dżewo.search(10))
    # usuń element o kluczu 50
    dżewo.delete(50)
    # usuń element o kluczu 52
    dżewo.print_tree()
    dżewo.delete(52)
    dżewo.print_tree()
    # usuń element o kluczu 11
    dżewo.delete(11)
    # usuń element o kluczu 57
    dżewo.delete(57)
    # usuń element o kluczu 1
    dżewo.delete(1)
    # usuń element o kluczu 12
    dżewo.delete(12)
    # dodaj element o kluczu 3:AA
    dżewo.insert(3, "AA")
    # dodaj element o kluczu 4:BB
    dżewo.insert(4, "BB")
    # usuń element o kluczu 7
    dżewo.delete(7)
    # usuń element o kluczu 8
    dżewo.delete(8)
    # wyświetl drzewo 2D
    dżewo.print_tree()
    # wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość