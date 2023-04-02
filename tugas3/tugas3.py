#Nama: Muhammad Alif Taufiqurahman
#Nim: 210511127
#Kelas: R3(C) Teknik Informatika



print("Tugas 3 bagian 1")
from playsound import playsound

class hewan:
    def __init__(self, hewan):
        self.hewan = hewan
    def bersuara(self):
        print(f'{self.hewan} bersuara ....')

class kucing(hewan):
    def __init__(self, hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara...')
        playsound('C:\\Users\\ACER\\Documents\\semester 4\\pertemuan3_polynorism\\kucing.mp3')

class kuda(hewan):
    def __init__(self, hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara...')
        playsound('C:\\Users\\ACER\\Documents\\semester 4\\pertemuan3_polynorism\\kuda.mp3')

class gajah(hewan):
    def __init__(self, hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara...')
        playsound('C:\\Users\\ACER\\Documents\\semester 4\\pertemuan3_polynorism\\gajah.mp3')

def hewan_bersuara(hewan):
    hewan.bersuara()

hewan1 = hewan('hewan')
hewan2 = kucing('kucing')
hewan3 = kuda('kuda')
hewan4 = gajah('gajah')


hewan_bersuara(hewan1)
hewan_bersuara(hewan2)
hewan_bersuara(hewan3)
hewan_bersuara(hewan4)