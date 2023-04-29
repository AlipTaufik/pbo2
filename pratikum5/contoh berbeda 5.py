list_angka = ["anggur", "pisang", "pepaya"]
try:
    value = list_angka[5]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")