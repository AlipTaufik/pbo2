import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from kategori import kategori

class Frmkategori:
    
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
        Label(mainFrame, text='Kodekategori:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='nama_kategori:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        
        # Textbox
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIM.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtnama_kategori = Entry(mainFrame) 
        self.txtnama_kategori.grid(row=1, column=1, padx=5, pady=5) 


    
        
    
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=7, column=0, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=7, column=1, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=7, column=2, padx=5, pady=5)

        # define columns
        columns = ('idkategori', 'kodekategori', 'nama_kategori')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idkategori', text='ID')
        self.tree.column('idkategori', width="20")
        self.tree.heading('kodekategori', text='Kodekategori')
        self.tree.column('kodekategori', width="100")
        self.tree.heading('nama_kategori', text='nama_kategori')
        self.tree.column('nama_kategori', width="100")
        # set tree position
        self.tree.place(x=0, y=100)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,"")
        self.txtnama_kategori.delete(0,END)
        self.txtnama_kategori.insert(END,"")       
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mhs = kategori()
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
        mhs = kategori()
        res = mhs.getByNIK(nim)
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtnama_kategori.focus()
        return res
        
    def TampilkanData(self, event=None):
        nim = self.txtNIM.get()
        mhs = kategori()
        res = mhs.getByNIK(nim)
        self.txtnama_kategori.delete(0,END)
        self.txtnama_kategori.insert(END,mhs.nama_kategori)
           
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kp = self.txtNIM.get()
        nk = self.txtnama_kategori.get()
        
        mhs = kategori()
        mhs.kodekategori = kp
        mhs.nama_kategori = nk
        if(self.ditemukan==True):
            res = mhs.updateBykodee(kp)
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
        mhs = kategori()
        mhs.kodekategori = nim
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
    aplikasi = Frmkategori(root2, "Aplikasi Data Mahasiswa")
    root2.mainloop()