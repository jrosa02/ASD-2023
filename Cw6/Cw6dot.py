class BTreeNode:
    def __init__(self, max_children):
        self.keys = [None]*(max_children)
        self.children = [None]*(max_children+1)
        self.size = 0
    
    def is_full(self):
        return self.size == len(self.children)-1
    
    def insert_in_node(self, key, child=None):
        if self.is_full():
            return self.split_node(key, child)
        
        i = self.size-1
        while i>=0 and self.keys[i]>key:
            self.keys[i+1] = self.keys[i]
            self.children[i+2] = self.children[i+1]
            i -= 1
        
        self.keys[i+1] = key
        self.children[i+2] = child
        self.size += 1
    
    def split_node(self, key, child=None):
        mid = self.size//2

        new_node = BTreeNode(len(self.children)-1)
        new_node.keys = self.keys[mid+1:]
        new_node.children = self.children[mid+1:]
        new_node.size = self.size - mid - 1

        self.keys = self.keys[:mid]
        self.children = self.children[:mid+1]
        self.size = mid
        key_to_parent = self.keys[-1]

        if child is not None:
            if child.keys[0] < key_to_parent:
                self.insert_in_node(child.keys[0], child.children[0])
                new_node.children[0] = child.children[1]
            else:
                new_node.insert_in_node(child.keys[0], child.children[0])
                self.children[-1] = child.children[1]

        return key_to_parent, new_node


class BTree:
    def __init__(self, max_children):
        self.max_children = max_children
        self.root = BTreeNode(max_children)
    
    def insert(self, key):
        new_node = self._insert(self.root, key)
        if new_node is not None:
            new_root = BTreeNode(self.max_children)
            new_root.keys[0] = new_node[0]
            new_root.children[0] = self.root
            new_root.children[1] = new_node[1]
            self.root = new_root
        
    def _insert(self, node: BTreeNode, key):
        if node.children[0] is None:
            node.insert_in_node(key)
            if node.is_full():
                return node.split_node(None)
            else:
                return None
            
        i = node.size-1
        while i>=0 and node.keys[i]>key:
            i -= 1
            
        new_node = self._insert(node.children[i+1], key)
        if new_node is None:
            return None
        
        node.insert_in_node(new_node[0], new_node[1])
        if node.is_full():
            return node.split_node(None)
        else:
            return None
        
        i = node.size-1
        while i>=0 and node.keys[i]>key:
            i -= 1
        
        new_node = self._insert(node.children[i+1], key)
        if new_node is None:
            return None
        
        node.insert_in_node(new_node[0], new_node[1])
        return node.split_node(None, new_node[1])
    
    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")
    
    def _print_tree(self, node: BTreeNode, lvl):
        if node is not None:
            for i in range(node.size+1):                    
                self._print_tree(node.children[i], lvl+1)
                if i<node.size:
                    print(lvl*'  ', node.keys[i])


    
if __name__ == "__main__":
    #utwórz puste drzewo o maksymalnej liczbie potomków równej 4
    btree = BTree(max_children = 4)
    # dodaj do niego elementy (będące jednocześnie kluczami) po kolei z listy: [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    keys = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    for key in keys:
        btree.insert(key)
    # wyświetl drzewo
    btree.print_tree()
    # utwórz drugie puste drzewo, dodaj do niego 20 kolejnych liczb od 0 do 19 (będą to te same liczby co w liście ale dodane w kolejności rosnącej)
    # btree2 = BTree(4)
    # for i in range(20):
    #     btree2.insert(i)
    # # wyświetl stworzone drzewo (zauważ jak różni się od poprzedniego)
    # btree2.print_tree()
    # dodaj do drugiego drzewa kolejne liczby od 20 do 199, wyświetl drzewo (zauważ jak wzrosła jego wysokość)
    # utwórz trzecie puste drzewo o maksymalnej liczbie potomków równej 6, dodaj do niego te same liczby co do drugiego drzewa (od 0 do 199) i wyświetl go (zauważ jak zmalała jego wysokość)