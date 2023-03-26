from db import DBConnection as mydb

class anggota:

    def __init__(self):
        self.__idanggota=None
        self.__kodeanggota=None
        self.__nama=None
        self.__jk=None
        self.__alamat= None
        self.__info=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "idanggota:" + self.__idanggota + "\n" + "kodeanggota:" + self.__kodeanggota + "\n" +  "nama:" + self.__nama + "\n" + "jk:" + self.__jk + "\n" + "alamat:" + self.__alamat  + "\n"
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__idanggota

    @property
    def kodeanggota(self):
        return self.__kodeanggota

    @kodeanggota.setter
    def kodeanggota(self, value):
        self.__kodeanggota = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, value):
        self.__alamat = value


    def simpan(self):
        self.conn = mydb()
        val = (self.__kodeanggota, self.__nama, self.__jk, self.__alamat)
        sql="INSERT INTO anggota (kodeanggota, nama, jk, alamat) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, idanggota):
        self.conn = mydb()
        val = (self.__kodeanggota, self.__nama, self.__jk, self.__alamat, idanggota)
        sql="UPDATE anggota SET kodeanggota = %s, nama = %s, jk = %s, alamat = %s WHERE idanggota=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykodee(self, kodeanggota):
        self.conn = mydb()
        val = (self.__kodeanggota, self.__nama, self.__jk, self.__alamat, kodeanggota)
        sql="UPDATE anggota SET kodeanggota = %s, nama = %s, jk = %s, alamat = %s WHERE kodeanggota=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, idanggota):
        self.conn = mydb()
        sql="DELETE FROM anggota WHERE idbuku='" + str(idanggota) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNID(self, kodeanggota):
        self.conn = mydb()
        sql="DELETE FROM anggota WHERE kodeanggota='" + str(kodeanggota) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, idanggota):
        self.conn = mydb()
        sql="SELECT * FROM anggota WHERE idanggota='" + str(idanggota) + "'"
        self.result = self.conn.findOne(sql)
        self.conn.disconnect
        return self.result

    def getByNIDD(self, kodeanggota):
        a=str(kodeanggota)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM anggota WHERE kodeanggota='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kodeanggota = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__alamat = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodeanggota = ''
            self.__nama = ''
            self.__jk = ''
            self.__alamat = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM anggota"
        self.result = self.conn.findAll(sql)
        return self.result
    
a = anggota()
b = a.getAllData()
print(b)