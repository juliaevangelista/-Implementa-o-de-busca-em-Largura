from node import Node
from collections import deque
class Tree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        position = self.root
        previous = None
        while position is not None:
            previous = position
            if value < position.value:
                position = position.childLeft
            else:
                position = position.childRight
        if self.root is None:
            self.root = Node(value)
        elif value < previous.value:
            previous.childLeft = Node(value)
        else:
            previous.childRight = Node(value)

    def _deleteByMerging(self, node: Node):
        tmp = node
        if node is not None:
            if node.childRight is None:
                node = node.childLeft
            elif node.childLeft is None:
                node = node.childRight
            else:
                tmp = node.childLeft
                while tmp.childRight is not None:
                    tmp = tmp.childRight
                tmp.childRight = node.childRight
                node.value = node.childLeft.value
                node.childRight = node.childLeft.childRight
                node.childLeft = node.childLeft.childLeft

    def findAndDeleteByMerging(self, value):
        position = self.root
        previous = None
        while position is not None:
            if position.value == value:
                break
            previous = position
            if value < position.value:
                position = position.childLeft
            else:
                position = position.childRight
        if position is not None and position.value == value:
            if position.childLeft is None and position.childRight is None:
                if position == self.root:
                    self.root = None
                elif position == previous.childLeft:
                    previous.childLeft = None
                else:
                    previous.childRight = None
            else:
                self._deleteByMerging(position)
        elif self.root is not None:
            print(f"Elemento {value} não está na árvore")
        else:
            print("Árvore está vazia")

    def dfs(self, node=None):
        if node is None:
            node = self.root

        if node is not None and not node.visited:
            print(node.value)
            node.visited = True 
            self.dfs(node.childLeft)
            self.dfs(node.childRight)
    def bfs(self, valor):
        fila = deque()
        if self.root is not None:
            fila.append(self.root)

        while len(fila) > 0:
            node_atual = fila.popleft()
            if node_atual.value == valor:
                return node_atual
            else:
                if node_atual.childLeft is not None:
                    fila.append(node_atual.childLeft)
                if node_atual.childRight is not None:
                    fila.append(node_atual.childRight)
    
    def __str__(self):
        return f"{self.root}"

    def __repr__(self):
        return f"{self}"




