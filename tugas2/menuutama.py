import tkinter as tk
from tkinter import Menu,Label
from frmbuku import *
from frmanggota import *
from frmkategori import *
from frmpeminjaman import *


# root window
root = tk.Tk()
root.title('Kelompok 6 R3')
root.geometry("900x400")

Label(text='Kelompok 6 Kelas R3').grid(row=0, column=0, sticky=W,padx=10,pady=10,)
Label(text='MUHAMMAD ALIF TAUFIQURAHMAN 210511127').grid(row=1, column=0, sticky=W,padx=10,pady=10,)
Label(text='MOHAMMAD MAOLANA 210511121').grid(row=2, column=0, sticky=W,padx=10,pady=10,)
Label(text='TITO FEBRI ANGGARA 210511126').grid(row=3, column=0, sticky=W,padx=10,pady=10,)

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
buku_menu = Menu(menubar)
anggota_menu = Menu(menubar)
kategori_menu = Menu(menubar)
peminjaman_menu = Menu(menubar)




def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="Buku",command= lambda: new_window("Buku", Frmbuku)
)
menubar.add_cascade(
    label="Anggota",command= lambda: new_window("Anggota", Frmanggota)
)
menubar.add_cascade(
    label="Kategori",command= lambda: new_window("Kategori", Frmkategori)
)
menubar.add_cascade(
    label="Peminjaman", command= lambda: new_window("Peminjaman", Frmpeminjaman)
)

  
root.mainloop()