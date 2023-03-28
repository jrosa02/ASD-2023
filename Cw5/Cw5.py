class Node:
    def __init__(self, key, value = None, left_desc = None, right_desc = None) -> None:
        self.key_ = key
        self.value_ = value
        self.left_desc_: Node = left_desc
        self.right_desc_: Node = right_desc

    def search(self, key):
        if self.key_ == key:
            return self
        elif self.key_ < key and self.left_desc_ is not None:
            self.left_desc_.search(key)
        elif self.key_ > key and self.right_desc_ is not None:
            self.right_desc_.search(key)
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

    def delete(self):
        pass

    def height(self) -> int:
        pass

class BST:
    def __init__(self, root: Node = None) -> None:
        self.root_: Node = root

    def search(self, key):
        if self.root_ is not None:
            self.root_.search(key).value_

    def insert(self, key, value):
        if self.root_ is not None:
            self.root_.insert(key, value)
        else:
            self.root_ = Node(key, value)

    def delete(self, key):
        self.root_.search(key).delete()

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
    keyvalue = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    tree = BST()
    for key in keyvalue:
        tree.insert(key, keyvalue[key])
    tree.print_tree()
