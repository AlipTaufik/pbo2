#Nama : Muhammad Alif Taufiqurahman
#Nim : 210511127
#Kelas : R3 / TI21C

class Penulis:
    def __init__(self, nama, judul):
        self.nama = nama
        self.judul = judul

class Buku:
    def __init__(self, penulis, genre):
        self.genre = genre
        self.penulis = penulis

    def daftar_buku(self):
        for penulis in self.penulis:
            print("Penulis :",penulis.nama,",Judul :", penulis.judul, ",Genre =",self.genre)

penulis1 = Penulis("J K rowlin", "Princess Java")
penulis2 = Penulis("Alexander", "Harry Potta")

buku = Buku([penulis1, penulis2], "Scient Fiction")
buku.daftar_buku()