class  PriorityQueueSortedList:
    def __init__(self):
        self._data = []
        self._size = 0
    
    def __len__(self):
        return len(self._data)
        
    def is_empty(self):
        return len(self._data) == 0
    
    def add(self, data, priority):
        if self.is_empty():
            self._data.append([data, priority])
        elif self._size == 1:
            if self._data[0][1] > priority:
                self._data.insert(0,[data, priority])
            else:
                self._data.append([data, priority])
        else:
            if self._data[0][1] > priority:
                self._data.insert(0,[data, priority])
            elif self._data[-1][1] <= priority:
                self._data.append([data, priority])
            else:
                posisi = 0
                bantu = self._data[posisi]
                while bantu[1] < priority:
                    posisi += 1
                self._data.append([data, priority])
    
    def update(self, prioBaru, dataBaru):
        posisi = 0
        bantu = self._data[posisi]
        while bantu[1] == prioBaru:
            bantu[0] == dataBaru
            
    def remove(self):
        if self.isEmpty():
            print("Priority Queue is empty")
        self._data[0].pop()
        self._size -= 1
    
    def removeWithPrio(self, prio):
        if self.isEmpty():
            print("Priority Queue is empty")
        else:
            posisi = 0
            bantu = self._data[posisi]
            while bantu[1] == prio:
                bantu.pop()
        
    def printIsiQueue(self):
        if self.is_empty():
            print("Priority Queue is empty")
        else:
            for i in range(0, len(self._data)):
                print(self._data[i], end=" ")
            print()


sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
# sortedList.update(4, "Karin")
# sortedList.update(3, "Rafi")
# sortedList.remove()
# sortedList.removePriority(4)
# sortedList.peek()
sortedList.printIsiQueue()
