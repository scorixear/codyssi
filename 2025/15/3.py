import os, sys
import time

class Node:
    def __init__(self, code: str, id: int):
        self.code = code
        self.id = id
        self.left = None
        self.right = None
        self.parent = None
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None
    def is_root(self) -> bool:
        return self.parent is None
    def add_child(self, child: "Node"):
        if child.id > self.id:
            if self.right is None:
                self.right = child
                child.parent = self
            else:
                self.right.add_child(child)
        else:
            if self.left is None:
                self.left = child
                child.parent = self
            else:
                self.left.add_child(child)
    def traverse(self, nodes: list["Node"]):
        if self.parent is not None:
            nodes.append(self.parent)
            return self.parent.traverse(nodes)
        return nodes

    def __repr__(self):
        return f"Node(code={self.code}, id={self.id})"
    def __str__(self):
        return f"Node {self.id} ({self.code})"
    def __eq__(self, other: 'Node'):
        return self.id == other.id and self.code == other.code
    def __hash__(self):
        return hash((self.id, self.code))

class Tree:
    def __init__(self):
        self.root = None
    def insert_node(self, node: Node):
        if self.root is None:
            self.root = node
        else:
            self.root.add_child(node)
    def get_layer_ids(self):
        if self.root is None:
            return []
        layers = []
        queue = [(self.root, 0)]
        while queue:
            node, layer = queue.pop(0)
            if len(layers) <= layer:
                layers.append(0)
            layers[layer] += node.id
            if node.left is not None:
                queue.append((node.left, layer + 1))
            if node.right is not None:
                queue.append((node.right, layer + 1))
        return layers

        

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    nodes = {}
    tree = Tree()
    mode = 0
    path1 = None
    path2 = None
    for line in lines:
        if mode == 0 and line == "":
            mode = 1
            continue
        if mode == 0:
            code, id = line.split(" | ")
            id = int(id)
            node = Node(code, id)
            nodes[node.code] = node
            tree.insert_node(node)
        else:
            code, id = line.split(" | ")
            id = int(id)
            node = nodes[code]
            if path1 is None:
                path1 = node.traverse([])
                path1.reverse()
            elif path2 is None:
                path2 = node.traverse([])
                path2.reverse()
    index = 0
    common = None
    while True:
        if index >= len(path1) or index >= len(path2):
            break
        if path1[index] == path2[index]:
            common = path1[index]
            index += 1
        else:
            break
    if common is None:
        print("No common ancestor found")
        return
    print(common)


    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
