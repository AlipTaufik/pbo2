#Nama : Muhammad Alif Taufiqurahman
#Nim : 210511127
#Kelas : R3 / TI21C

class Mahasiswa:
    def __init__(self, nama, prodi):
        self.nama = nama
        self.prodi = prodi
    
class KelompokKKM:
    def __init__(self, tempat, mahasiswa):
        self.tempat = tempat
        self.mahasiswa = mahasiswa

    def daftar_kelompokKKM(self):
        for mahasiswa in self.mahasiswa:
            print("Nama Mhs :",mahasiswa.nama,", Prodi :", mahasiswa.prodi,", Tempat KKM :", self.tempat)

mahasiswa1 = Mahasiswa("Ahmad", "Teknik Industri")
mahasiswa2 = Mahasiswa("Abdul", "Sastra Indonesia")
mahasiswa3 = Mahasiswa("Maharani", "Farmasi")
mahasiswa4 = Mahasiswa("Wati", "Sastra Prancis")
mahasiswa5 = Mahasiswa("Pranowo", "Teknik Kebun")
mahasiswa6 = Mahasiswa("Joko", "Elektro Mesin")

KKM = KelompokKKM("desa gaungan", [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4, mahasiswa5,mahasiswa6])
KKM.daftar_kelompokKKM()