class Sendal:
    def __init__(self, merek, model):
        self.merek = merek
        self.model = model
sandal = Sendal("Carvil", 2043)
try:
    print(sandal.harga)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")