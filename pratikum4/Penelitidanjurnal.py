#Nama : Muhammad Alif Taufiqurahman
#Nim : 210511127
#Kelas : R3 / TI21C

class Peneliti:
    def __init__(self, nama, judul):
        self.nama = nama
        self.judul = judul

class Jurnal:
    def __init__(self, tahun, peneliti):
        self.tahun = tahun
        self.peneliti = peneliti

    def daftar_jurnal(self):
        for peneliti in self.peneliti:
            print("Peneliti :",peneliti.nama,", Judul :", peneliti.judul,", Terbit :", self.tahun)

peneliti1 = Peneliti("Ahmad", "Laut Biru")
peneliti2 = Peneliti("Fulan", "Bukit Hijau")

jurnal = Jurnal("2003", [peneliti1, peneliti2])
jurnal.daftar_jurnal()