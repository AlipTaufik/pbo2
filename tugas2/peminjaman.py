from db import DBConnection as mydb

class peminjaman:

    def __init__(self):
        self.__idpeminjaman=None
        self.__nomorbukti=None
        self.__tgl_pinjam=None
        self.__kodeanggota=None
        self.__kodebuku1= None
        self.__kodebuku2=None
        self.__tglhrskembali=None
        self.__tgl_dikembalikan=None
        self.__status_pinjam=None
        self.__info=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "idpeminjaman:" + self.__idpeminjaman + "\n" + "nomerbukti:" + self.__nomorbukti + "\n" +  "tgl_pinjam:" + self.__tgl_pinjam + "\n" + "kodeanggota:" + self.__kodeanggota + "\n" + "kodebuku1:" + self.__kodebuku1 + "\n" + "kodebukku2:" + self.__kodebuku2 + "\n" + "tglhrskembali:" + self.__tglhrskembali + "\n" + "tgl_dikembalikan:" + self.__tgl_dikembalikan + "\n" + "status_pinjam:" + self.__status_pinjam + "\n"
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__idpeminjaman

    @property
    def nomorbukti(self):
        return self.__nomorbukti

    @nomorbukti.setter
    def nomorbukti(self, value):
        self.__nomorbukti = value

    @property
    def tgl_pinjam(self):
        return self.__tgl_pinjam

    @tgl_pinjam.setter
    def tgl_pinjam(self, value):
        self.__tgl_pinjam = value

    @property
    def kodeanggota(self):
        return self.__kodeanggota

    @kodeanggota.setter
    def kodeanggota(self, value):
        self.__kodeanggota = value

    @property
    def kodebuku1(self):
        return self.__kodebuku1

    @kodebuku1.setter
    def kodebuku1(self, value):
        self.__kodebuku1 = value

    @property
    def kodebuku2(self):
        return self.__kodebuku2 

    @kodebuku2.setter
    def kodebuku2(self, value):
        self.__kodebuku2 = value

    @property
    def tglhrskembali(self):
        return self.__tglhrskembali

    @tglhrskembali.setter
    def tglhrskembali(self, value):
        self.__tglhrskembali = value
    
    @property
    def tgl_dikembalikan(self):
        return self.__tgl_dikembalikan

    @tgl_dikembalikan.setter
    def tgl_dikembalikan(self, value):
        self.__tgl_dikembalikan = value

    @property
    def status_pinjam(self):
        return self.__status_pinjam

    @status_pinjam.setter
    def status_pinjam(self, value):
        self.__status_pinjam = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nomorbukti, self.__tgl_pinjam, self.__kodeanggota, self.__kodebuku1, self.__kodebuku2, self.__tglhrskembali, self.__tgl_dikembalikan, self.__status_pinjam)
        sql="INSERT INTO peminjaman (nomorbukti, tgl_pinjam, kodeanggota, kodebuku1, kodebuku2, tglhrskembali, tgl_dikembalikan, status_pinjam) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, idpeminjaman):
        self.conn = mydb()
        val = (self.__nomorbukti, self.__tgl_pinjam, self.__kodeanggota, self.__kodebuku1, self.__kodebuku2, self.__tglhrskembali, self.__tgl_dikembalikan, self.__status_pinjam, idpeminjaman)
        sql="UPDATE peminjaman SET nomorbukti = %s, tgl_pinjam = %s, kodeanggota = %s, kodebuku1 = %s, kodebuku2 = %s, tglhrskembali = %s, tgl_dikembalikan = %s, status_pinjam = %s  WHERE idpeminjaman=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByno(self, nomorbukti):
        self.conn = mydb()
        val = (self.__nomorbukti, self.__tgl_pinjam, self.__kodeanggota, self.__kodebuku1, self.__kodebuku2, self.__tglhrskembali, self.__tgl_dikembalikan, self.__status_pinjam, nomorbukti)
        sql="UPDATE peminjaman SET nomorbukti = %s, tgl_pinjam = %s, kodeanggota = %s, kodebuku1 = %s, kodebuku2 = %s, tglhrskembali = %s, tgl_dikembalikan = %s, status_pinjam = %s  WHERE nomorbukti=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, idpeminjaman):
        self.conn = mydb()
        sql="DELETE FROM peminjaman WHERE idpeminjaman='" + str(idpeminjaman) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNID(self, nomorbukti):
        self.conn = mydb()
        sql="DELETE FROM peminjaman WHERE nomorbukti='" + str(nomorbukti) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, idpeminjaman):
        self.conn = mydb()
        sql="SELECT * FROM peminjaman WHERE idpeminjaman='" + str(idpeminjaman) + "'"
        self.result = self.conn.findOne(sql)
        self.conn.disconnect
        return self.result

    def getByNIB(self, nomorbukti):
        a=str(nomorbukti)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM peminjaman WHERE nomorbukti='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nomorbukti = self.result[1]
            self.__tgl_pinjam = self.result[2]
            self.__kodeanggota = self.result[3]
            self.__kodebuku1 = self.result[4]
            self.__kodebuku2 = self.result[5]
            self.__tglhrskembali = self.result[6]
            self.__tgl_dikembalikan = self.result[7]
            self.__status_pinjam = self.result[8]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nomorbukti = ''
            self.__tgl_pinjam = ''
            self.__kodeanggota = ''
            self.__kodebuku1 = ''
            self.__kodebuku2 = ''
            self.__tglhrskembali = ''
            self.__tgl_dikembalikan = ''
            self.__status_pinjam = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM peminjaman"
        self.result = self.conn.findAll(sql)
        return self.result
    
a = peminjaman()
b = a.getAllData()
print(b)