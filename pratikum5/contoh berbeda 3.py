try:
    with open("file naga.txt") as file:
        data = file.write(saffa)
except FileNotFoundError:
    print("File yang diminta tidak ditemukan!")
