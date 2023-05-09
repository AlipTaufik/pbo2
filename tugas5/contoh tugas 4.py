dictionary = {"merek": "supra", "model": 2312, "tahun": 2003}
try:
    value = dictionary["Harga"]
except KeyError:
    print("Key yang diminta tidak ditemukan pada dictionary!")