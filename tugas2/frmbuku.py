import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from buku import buku

class Frmbuku:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kodebuku:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Judul:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Pengarang:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Penerbit:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tahun:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Kodekategori:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        # Textbox
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIM.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtBuku = Entry(mainFrame) 
        self.txtBuku.grid(row=1, column=1, padx=5, pady=5) 

        self.txtpengarang = Entry(mainFrame) 
        self.txtpengarang.grid(row=2, column=1, padx=5, pady=5)

        self.txtpenerbit = Entry(mainFrame) 
        self.txtpenerbit.grid(row=3, column=1, padx=5, pady=5)

        self.txttahun = Entry(mainFrame) 
        self.txttahun.grid(row=4, column=1, padx=5, pady=5)

        self.txtKodeKategori = Entry(mainFrame) 
        self.txtKodeKategori.grid(row=5, column=1, padx=5, pady=5)
        
        
    
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=7, column=0, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=7, column=1, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=7, column=2, padx=5, pady=5)

        # define columns
        columns = ('idbuku', 'kodebuku', 'judul','pengarang','penerbit', 'tahun', 'kodekategori')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idbuku', text='ID')
        self.tree.column('idbuku', width="30")
        self.tree.heading('kodebuku', text='KodeBuku')
        self.tree.column('kodebuku', width="80")
        self.tree.heading('judul', text='Judul')
        self.tree.column('judul', width="80")
        self.tree.heading('pengarang', text='Pengarang')
        self.tree.column('pengarang', width="200")
        self.tree.heading('penerbit', text='Penerbit')
        self.tree.column('penerbit', width="100")
        self.tree.heading('tahun', text='tahun')
        self.tree.column('tahun', width="60")
        self.tree.heading('kodekategori', text='kodekategori')
        self.tree.column('kodekategori', width="100")
        # set tree position
        self.tree.place(x=0, y=300)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,"")
        self.txtBuku.delete(0,END)
        self.txtBuku.insert(END,"")       
        self.txtpengarang.insert(END,"")
        self.txtpenerbit.insert(END,"")
        self.txttahun.insert(END,"")
        self.txtKodeKategori.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mhs = buku()
        result = mhs.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        nim = self.txtNIM.get()
        mhs = buku()
        res = mhs.getByNID(nim)
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtBuku.focus()
        return res
        
    def TampilkanData(self, event=None):
        nim = self.txtNIM.get()
        mhs = buku()
        res = mhs.getByNID(nim)
        self.txtBuku.delete(0,END)
        self.txtBuku.insert(END,mhs.judul)
        self.txtpengarang.delete(0,END)
        self.txtpengarang.insert(END,mhs.pengarang)
        self.txtpenerbit.delete(0,END)
        self.txtpenerbit.insert(END,mhs.penerbit)
        self.txttahun.delete(0,END)
        self.txttahun.insert(END,mhs.tahun)
        self.txtKodeKategori.delete(0,END)
        self.txtKodeKategori.insert(END,mhs.kodekategori)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kb = self.txtNIM.get()
        judull = self.txtBuku.get()
        jk = self.txtpengarang.get()
        penerbit = self.txtpenerbit.get()
        tahunn = self.txttahun.get()
        kategori = self.txtKodeKategori.get()
        
        mhs = buku()
        mhs.kodebuku = kb
        mhs.judul = judull
        mhs.pengarang = jk
        mhs.penerbit = penerbit
        mhs.tahun = tahunn
        mhs.kodekategori = kategori
        if(self.ditemukan==True):
            res = mhs.updateBykode(kb)
            ket = 'Diperbarui'
        else:
            res = mhs.simpan()
            ket = 'Disimpan'
            
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nim = self.txtNIM.get()
        mhs = buku()
        mhs.kodebuku = nim
        if(self.ditemukan==True):
            res = mhs.deleteByNID(nim)
            rec = mhs.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = Frmbuku(root2, "Aplikasi Data Mahasiswa")
    root2.mainloop()