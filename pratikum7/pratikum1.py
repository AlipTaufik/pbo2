#Nama : Muhammad Alif Taufiqurahman
#Nim : 210511127
#Kelas : R3 / TI21C

class TabungMeta(type): 
    def __init__(cls, name, bases, attrs): 
        super().__init__(name, bases, attrs) 
        
        # Tambahkan method untuk menghitung luas dan volume tabung
        def luas(cls, jari): 
            return 3.14 *jari * jari
        cls.luas = classmethod(luas) 
        
        def volume(cls, jari, tinggi): 
            return 3.14 *jari * jari * tinggi
        cls.volume = classmethod(volume) 
        
class Tabung(metaclass=TabungMeta): 
    pass 

s = Tabung() 
# Menghitung luas permukaan tabung dengan jari=5
luas_tabung = Tabung.luas(5) 
print("Luas Tabung:", luas_tabung) 

# Menghitung volume tabung dengan jari=5 dan tinggi=10
volume_tabung = Tabung.volume(5, 10) 
print("Volume Tabung:", volume_tabung)