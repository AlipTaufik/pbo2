import multiprocessing
import time

def hitung_jumlah(angka):
    jumlah = 0
    for i in range(angka):
        jumlah += i
    return jumlah

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    angka_list = [1000000, 2000000, 3000000, 4000000, 5000000]
    start_time = time.time()
    hasil = pool.map(hitung_jumlah, angka_list)
    end_time = time.time()
    print(f"Hasil perhitungan: {hasil}")
    print(f"Waktu total perhitungan: {end_time - start_time:.2f} detik")