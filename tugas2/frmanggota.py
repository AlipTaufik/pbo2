import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from anggota import anggota

class Frmanggota:
    
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
        Label(mainFrame, text='Kodeanggota:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='nama:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='alamat:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='jenis kelamin:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        
        # Textbox
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIM.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtnama = Entry(mainFrame) 
        self.txtnama.grid(row=1, column=1, padx=5, pady=5) 

        self.txtalamat = Entry(mainFrame) 
        self.txtalamat.grid(row=2, column=1, padx=5, pady=5)

# Radio Button
        self.txtJK = StringVar()
        self.L = Radiobutton(mainFrame, text='Laki-laki', value='L', variable=self.txtJK)
        self.L.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        self.L.select() # set pilihan yg pertama
        self.P = Radiobutton(mainFrame, text='Perempuan', value='P', variable=self.txtJK)
        self.P.grid(row=3, column=2, padx=5, pady=5, sticky=W)
    
        
    
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=7, column=0, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=7, column=1, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=7, column=2, padx=5, pady=5)

        # define columns
        columns = ('idanggota', 'kodeanggota', 'nama','jk','alamat')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idanggota', text='ID')
        self.tree.column('idanggota', width="20")
        self.tree.heading('kodeanggota', text='Kodeanggota')
        self.tree.column('kodeanggota', width="100")
        self.tree.heading('nama', text='nama')
        self.tree.column('nama', width="200")
        self.tree.heading('jk', text='jk')
        self.tree.column('jk', width="20")
        self.tree.heading('alamat', text='alamat')
        self.tree.column('alamat', width="150")
        # set tree position
        self.tree.place(x=0, y=300)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,"")
        self.txtnama.delete(0,END)
        self.txtnama.insert(END,"")       
        self.txtalamat.delete(0,END)
        self.txtalamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mhs = anggota()
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
        mhs = anggota()
        res = mhs.getByNIDD(nim)
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtnama.focus()
        return res
        
    def TampilkanData(self, event=None):
        nim = self.txtNIM.get()
        mhs = anggota()
        res = mhs.getByNIDD(nim)
        self.txtnama.delete(0,END)
        self.txtnama.insert(END,mhs.nama)
        self.txtalamat.delete(0,END)
        self.txtalamat.insert(END,mhs.alamat)
           
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        ka = self.txtNIM.get()
        namaa = self.txtnama.get()
        jkk = self.txtJK.get()
        alamat = self.txtalamat.get()
        
        mhs = anggota()
        mhs.kodeanggota = ka
        mhs.nama = namaa
        mhs.jk = jkk
        mhs.alamat = alamat
        if(self.ditemukan==True):
            res = mhs.updateBykodee(ka)
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
        mhs = anggota()
        mhs.kodeanggota = nim
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
    aplikasi = Frmanggota(root2, "Aplikasi Data Mahasiswa")
    root2.mainloop()