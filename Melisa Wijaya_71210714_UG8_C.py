class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3
    def __init__(self): #konstruktor
        pass
        self.data = []
        self.capacity = Kasir.DEFAULT_CAPACITY
       
    def __len__(self): #mengembalikan ukuran Queue
        pass
        return len(self.data)

    def is_empty(self): #mengecek apakah Queue kosong ?
        pass
        return len(self.data) == 0

    def dequeue(self): #menghapus data paling depan (front)
        pass
        data = self.data[0]
        self.data.remove(data)
        print("### Pelanggan", data, "Selesai Membayar ###")

    def enqueue(self, namaPelanggan): #menambah data ke list
        pass
        self.data.append(namaPelanggan)

    def resize(self, cap): #mengubah ukuran queue pada list
        pass
        print()
        print("### Melakukan Resize ###")
        self.DEFAULT_CAPACITY = self.DEFAULT_CAPACITY * cap
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        pass
        if self.capacity == len(self.data):
            self.resize(2)
            print()
            print("=== Kasir ===")
            kapasitas = len(self.data)-1
            nomer = 1
            for i in range(0, (self.capacity)):            
                if i <= kapasitas:
                    print(nomer,".",self.data[i], end=' ')
                    print()
                else:
                    print(nomer,". Kosong")
                nomer += 1
        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()
