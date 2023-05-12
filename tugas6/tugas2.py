import threading
import time

def hitung_jumlah(angka):
    jumlah = 0
    for i in range(angka):
        jumlah += i
    return jumlah

if __name__ == '__main__':
    angka_list = [1000000, 2000000, 3000000, 4000000, 5000000]
    threads = []
    start_time = time.time()
    for angka in angka_list:
        thread = threading.Thread(target=hitung_jumlah, args=(angka,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Waktu total perhitungan: {end_time - start_time:.2f} detik")