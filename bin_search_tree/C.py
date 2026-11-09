from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if key < current.data:
                current = current.left
            elif key > current.data:
                current = current.right
            else:
                return

        if key < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node


    def search(self, key):
        if self.root is None:
            return
        found = False
        current = self.root
        while current is not None and not found:
            if key < current.data:
                current = current.left
            elif key == current.data:
                found = True
            else:
                current = current.right
        return found

    def max_node(self, node):
        parent = node
        current = node.left
        while current.right is not None:
            parent = current
            current = current.right
        return current, parent

    def delete(self, key):
        if self.root is None:
            return
            
        current = self.root
        parent = None
        
        while current is not None and current.data != key:
            parent = current
            if key < current.data:
                current = current.left
            else:
                current = current.right
                
        if current is None:
            return

        if current.left is None or current.right is None:
            if current.left is not None:
                child = current.left
            else:
                child = current.right
                
            if parent is None:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child

        else:
            maxe_node, parent_maxe_node = self.max_node(current)
            
            max_value = maxe_node.data
            if parent_maxe_node.right == maxe_node:
                parent_maxe_node.right = maxe_node.left
            else:
                parent_maxe_node.left = maxe_node.left
                
            current.data = max_value

    def print_tree(self, p, level=0):
        if p is None:
            return
            
        self.print_tree(p.left, level + 1)
        
        print('.' * level + str(p.data))
        
        self.print_tree(p.right, level + 1)

    def __str__(self):
        if self.root is None:
            return "Дерево пустое"
        
        lines = []
        
        def build_tree_string(node, level=0):
            if node is not None:
                build_tree_string(node.right, level + 1)
                
                indent = "    " * level
                lines.append(f"{indent}── {node.data}")
                
                build_tree_string(node.left, level + 1)
                
        build_tree_string(self.root)
        return "\n".join(lines)


    def height(self):
        if self.root is None:
            return 0
            
        queue = [self.root]
        height = 0
        
        while len(queue) > 0:
            height += 1
            
            level_size = len(queue)
            
            for _ in range(level_size):
                current = queue.pop(0)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
                    
        return height

    def size(self):
        if self.root is None:
            return 0
        queue = deque()
        queue.append(self.root)
        size = 0
        while len(queue) > 0:
            level_size = len(queue)
            size += level_size    
            for _ in range(level_size):
                current = queue.popleft()
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
        return size

tree = BinarySearchTree()
for num in list(map(int, input().split()))[:-1]:
    tree.insert(num)

print(tree.size())  