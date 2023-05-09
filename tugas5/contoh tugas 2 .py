try:
    x = int(input("masukan angka:"))
    y = x / 0
except ZeroDivisionError:
    print("Terjadi kesalahan pembagian dengan nol!")