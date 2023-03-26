from db import DBConnection as mydb

class kategori:

    def __init__(self):
        self.__idkategori=None
        self.__kodekategori=None
        self.__nama_kategori=None
        self.__info=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "idkategori:" + self.__idkategori + "\n" + "kodekategori:" + self.__kodekategori + "\n" +  "nama_kategori:" + self.__nama_kategori + "\n"
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__idkategori

    @property
    def kodekategori(self):
        return self.__kodekategori

    @kodekategori.setter
    def kodekategori(self, value):
        self.__kodekategori = value

    @property
    def nama_kategori(self):
        return self.__nama_kategori

    @nama_kategori.setter
    def nama_kategori(self, value):
        self.__nama_kategori = value

    

    def simpan(self):
        self.conn = mydb()
        val = (self.__kodekategori, self.__nama_kategori)
        sql="INSERT INTO kategori (kodekategori, nama_kategori) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, idkategori):
        self.conn = mydb()
        val = (self.__kodekategori, self.__nama_kategori, idkategori)
        sql="UPDATE kategori SET kodekategori = %s, nama_kategori = %s WHERE idkategori=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykodee(self, kodekategori):
        self.conn = mydb()
        val = (self.__kodekategori, self.__nama_kategori, kodekategori)
        sql="UPDATE kategori SET kodekategori = %s, nama_kategori = %s WHERE kodekategori=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, idkategori):
        self.conn = mydb()
        sql="DELETE FROM kategori WHERE idkategori='" + str(idkategori) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNID(self, kodekategori):
        self.conn = mydb()
        sql="DELETE FROM kategori WHERE kodekategori='" + str(kodekategori) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, idkategori):
        self.conn = mydb()
        sql="SELECT * FROM kategori WHERE idkategori='" + str(idkategori) + "'"
        self.result = self.conn.findOne(sql)
        self.conn.disconnect
        return self.result

    def getByNIK(self, kodekategori):
        a=str(kodekategori)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM kategori WHERE kodekategori='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kodekategori = self.result[1]
            self.__nama_kategori = self.result[2]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodekategori = ''
            self.__nama_kategori = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM kategori"
        self.result = self.conn.findAll(sql)
        return self.result
    
a = kategori()
b = a.getAllData()
print(b)