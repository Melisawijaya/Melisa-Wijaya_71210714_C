class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None
        
class SLNC: #single linked list non circular
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def insert_head(self, no_rekening, nama, saldo):
        baru = NodeTabungan(no_rekening, nama, saldo)
        if self._size == 0:
            self._head = baru
            self._tail = baru
        else:
            baru._next = self._head
            self._head = baru
        self._size += 1
        
    def print(self):
        bantu = self._head
        while bantu != None:
            print(bantu.no_rekening, end = " ")
            # print(bantu.nama, end = " ")
            # print(bantu.saldo, end = " ")
            bantu = bantu._next
        print()

    def deleteHead(self):
        if self.isEmpty() == False:
            if self._size == 1:
                self._head = None
                self._tail = None
            else:
                hapus = self._head
                self._head = self._head._next
                del hapus
            self._size -= 1
            
    def deleteTail(self):
        if self.isEmpty() == False:
            if self._size == 1:
                self._head = None
                self._tail = None
            else:
                bantu = self._head
                while bantu._next != self._tail:
                    bantu = bantu._next
                hapus = self._tail
                self._tail = bantu
                self._tail._next = None
                del hapus
            self._size -= 1

    def delete(self, posisi):
        if self._size == 0:
            return False
        elif posisi == 0:
            self.deleteHead()
        elif posisi + 1 >= self._size:
            self.deleteTail()
        else:
            hapus = self._head
            for i in range (posisi):
                hapus = hapus._next
            bantu = self._head
            while bantu._next != hapus:
                bantu = bantu._next
            bantu._next = hapus._next
        del hapus
        self._size -= 1



slnc=SLNC()
slnc.insert_head(201,"Hanif", 250000)
slnc.print()