import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from peminjaman import peminjaman

class Frmpeminjaman:
    
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
        Label(mainFrame, text='nomorbukti:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='tgl_pinjam:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='kodeanggota:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='kodebuku1:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='kodebuku2:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='tglhrsdikembali:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='tgl_dikembalikan:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='status_pinjam:').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIM.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtnb = Entry(mainFrame) 
        self.txtnb.grid(row=1, column=1, padx=5, pady=5) 

        self.txttgl_pinjam = Entry(mainFrame) 
        self.txttgl_pinjam.grid(row=2, column=1, padx=5, pady=5)

        self.txtka = Entry(mainFrame) 
        self.txtka.grid(row=3, column=1, padx=5, pady=5)

        self.txtkb1 = Entry(mainFrame) 
        self.txtkb1.grid(row=4, column=1, padx=5, pady=5)

        self.txtkb2 = Entry(mainFrame) 
        self.txtkb2.grid(row=5, column=1, padx=5, pady=5)

        self.txttgl1 = Entry(mainFrame) 
        self.txttgl1.grid(row=6, column=1, padx=5, pady=5)


        self.txttgl2 = StringVar()
        Cbo = ttk.Combobox(mainFrame, width = 27, textvariable = self.txttgl2) 
        Cbo.grid(row=7, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        Cbo['values'] = ('Aktif','Tidak Aktif')
        Cbo.current()
    
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=9, column=0, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=9, column=1, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=9, column=2, padx=5, pady=5)

        # define columns
        columns = ('idpeminjaman', 'nomorbukti', 'tgl_pinjam', 'kodeanggota', 'kodebuku1', 'kodebuku2', 'tglhrskembali', 'tgl_dikembalikan', 'status_pinjam')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idpeminjaman', text='ID')
        self.tree.column('idpeminjaman', width="30")
        self.tree.heading('nomorbukti', text='nomorbukti')
        self.tree.column('nomorbukti', width="80")
        self.tree.heading('tgl_pinjam', text='tgl_pinjam')
        self.tree.column('tgl_pinjam', width="80")
        self.tree.heading('kodeanggota', text='kodeanggota')
        self.tree.column('kodeanggota', width="200")
        self.tree.heading('kodebuku1', text='kodebuku1')
        self.tree.column('kodebuku1', width="100")
        self.tree.heading('kodebuku2', text='kodebuku2')
        self.tree.column('kodebuku2', width="60")
        self.tree.heading('tglhrskembali', text='tglhrskembali')
        self.tree.column('tglhrskembali', width="100")
        self.tree.heading('tgl_dikembalikan', text='tgl_dikembalikan')
        self.tree.column('tgl_dikembalikan', width="100")
        self.tree.heading('status_pinjam', text='status_pinjam')
        self.tree.column('status_pinjam', width="100")
        # set tree position
        self.tree.place(x=0, y=300)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,"")
        self.txtnb.delete(0,END)
        self.txtnb.insert(END,"")       
        self.txttgl_pinjam.delete(0,END)
        self.txttgl_pinjam.insert(END,"")
        self.txtka.delete(0,END)
        self.txtka.insert(END,"")
        self.txtkb1.delete(0,END)
        self.txtkb1.insert(END,"")
        self.txtkb2.delete(0,END)
        self.txtkb2.insert(END,"")
        self.txttgl1.delete(0,END)
        self.txttgl1.insert(END,"")
        self.txttgl2.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mhs = peminjaman()
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
        mhs = peminjaman()
        res = mhs.getByNIB(nim)
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txttgl_pinjam.focus()
        return res
        
    def TampilkanData(self, event=None):
        nim = self.txtNIM.get()
        mhs = peminjaman()
        res = mhs.getByNIB(nim)
        self.txtnb.delete(0,END)
        self.txtnb.insert(END,mhs.tgl_pinjam)       
        self.txttgl_pinjam.delete(0,END)
        self.txttgl_pinjam.insert(END,mhs.kodeanggota)
        self.txtka.delete(0,END)
        self.txtka.insert(END,mhs.kodebuku1)
        self.txtkb1.delete(0,END)
        self.txtkb1.insert(END,mhs.kodebuku2)
        self.txtkb2.delete(0,END)
        self.txtkb2.insert(END,mhs.tglhrskembali)
        self.txttgl1.delete(0,END)
        self.txttgl1.insert(END,mhs.tgl_dikembalikan)
        self.txttgl2.set(mhs.status_pinjam)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kb = self.txtNIM.get()
        ju = self.txtnb.get()
        kl = self.txttgl_pinjam.get()
        ki = self.txtka.get()
        kk = self.txtkb1.get()
        kt = self.txtkb2.get()
        kg = self.txttgl1.get()
        kh = self.txttgl2.get()
        
        
        mhs = peminjaman()
        mhs.nomorbukti = kb
        mhs.tgl_pinjam = ju
        mhs.kodeanggota = kl
        mhs.kodebuku1 = ki
        mhs.kodebuku2 = kk
        mhs.tglhrskembali = kt
        mhs.tgl_dikembalikan = kg
        mhs.status_pinjam = kh
        if(self.ditemukan==True):
            res = mhs.updateByno(kb)
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
        mhs = peminjaman()
        mhs.nomorbukti = nim
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
    aplikasi = Frmpeminjaman(root2, "Aplikasi Data Mahasiswa")
    root2.mainloop()