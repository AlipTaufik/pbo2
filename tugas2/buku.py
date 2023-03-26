from db import DBConnection as mydb

class buku:

    def __init__(self):
        self.__idbuku=None
        self.__kodebuku=None
        self.__judul=None
        self.__pengarang=None
        self.__penerbit= None
        self.__tahun=None
        self.__kodekategori=None
        self.__info=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "idbuku:" + self.__idbuku + "\n" + "kodebuku:" + self.__kodebuku + "\n" +  "judul:" + self.__judul + "\n" + "pengarang::" + self.__pengarang + "\n" + "penerbit:" + self.__penerbit + "\n" + "tahun:" + self.__tahun + "\n" + "kodekategori:" + self.__kodekategori + "\n"
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__idbuku

    @property
    def kodebuku(self):
        return self.__kodebuku

    @kodebuku.setter
    def kodebuku(self, value):
        self.__kodebuku = value

    @property
    def judul(self):
        return self.__judul

    @judul.setter
    def judul(self, value):
        self.__judul = value

    @property
    def pengarang(self):
        return self.__pengarang

    @pengarang.setter
    def pengarang(self, value):
        self.__pengarang = value

    @property
    def penerbit(self):
        return self.__penerbit

    @penerbit.setter
    def penerbit(self, value):
        self.__penerbit = value

    @property
    def tahun(self):
        return self.__tahun 

    @tahun.setter
    def tahun(self, value):
        self.__tahun = value

    @property
    def kodekategori(self):
        return self.__kodekategori

    @kodekategori.setter
    def kodekategori(self, value):
        self.__kodekategori = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kodebuku, self.__judul, self.__pengarang, self.__penerbit, self.__tahun, self.__kodekategori)
        sql="INSERT INTO buku (kodebuku, judul, pengarang, penerbit, tahun, kodekategori) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, idbuku):
        self.conn = mydb()
        val = (self.__kodebuku, self.__judul, self.__pengarang, self.__penerbit, self.__tahun, self.__kodekategori, idbuku)
        sql="UPDATE buku SET kodebuku = %s, judul = %s, pengarang = %s, penerbit = %s, tahun = %s, kodekategori = %s WHERE idbuku=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykode(self, kodebuku):
        self.conn = mydb()
        val = (self.__kodebuku ,self.__judul, self.__pengarang, self.__penerbit, self.__tahun, self.__kodekategori, kodebuku)
        sql="UPDATE buku SET kodebuku = %s, judul = %s, pengarang = %s, penerbit = %s, tahun = %s, kodekategori = %s WHERE kodebuku=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, idbuku):
        self.conn = mydb()
        sql="DELETE FROM buku WHERE idbuku='" + str(idbuku) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNID(self, kodebuku):
        self.conn = mydb()
        sql="DELETE FROM buku WHERE kodebuku='" + str(kodebuku) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, idbuku):
        self.conn = mydb()
        sql="SELECT * FROM buku WHERE idbuku='" + str(idbuku) + "'"
        self.result = self.conn.findOne(sql)
        self.conn.disconnect
        return self.result

    def getByNID(self, kodebuku):
        a=str(kodebuku)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM buku WHERE kodebuku='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kodebuku = self.result[1]
            self.__judul = self.result[2]
            self.__pengarang = self.result[3]
            self.__penerbit = self.result[4]
            self.__tahun = self.result[5]
            self.__kodekategori = self.result[6]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodebuku = ''
            self.__judul = ''
            self.__pengarang = ''
            self.__penerbit = ''
            self.__tahun = ''
            self.__kodekategori = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM buku"
        self.result = self.conn.findAll(sql)
        return self.result
    
a = buku()
b = a.getAllData()
print(b)