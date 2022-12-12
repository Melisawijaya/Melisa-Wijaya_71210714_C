class Graph:
    def __init__(self):
        self._data = {}

    def addVertex(self, key):
        if key not in self._data:
            self._data[key] = set()

    def vertex(self):
        print("\nSeluruh Node = ", end = "")
        for key, value in self._data.items():
            print(key, end = " ")
        print()

    
    def edge(self):
        listEdge = set()
        for key,value in self._data.items():
            for item in self._data[key]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
                    
        print("Seluruh Edge = ", end = "")
        for item in listEdge:
            print(item, end = " ")
        print()


    def addEdge(self, x, y):
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x) #hanya digunakan jika graph tidak berarah

    def bfs(self, node):
        visited = []
        listQueue = []
        visited.append(node)
        listQueue.append(node)
        
        print("Tranversing BFS =", end = " ")
        while listQueue:
            print(listQueue[0], end = " ")
            for child in self._data[listQueue[0]]:
                if child not in visited:
                    visited.append(child)
                    listQueue.append(child)
            del listQueue[0]
        print("\n")


graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')

graph.addEdge('a', 'b')
graph.addEdge('b','c')
graph.addEdge('b', 'd')
graph.addEdge('c', 'e')
graph.addEdge('c','g')
graph.addEdge('d', 'e')
graph.addEdge('e', 'f')

# jangan ubah bagian di bawah 
graph.vertex()
graph.edge()
graph.bfs("a")