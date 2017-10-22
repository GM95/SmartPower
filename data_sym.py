import time
import MySQLdb
import datetime
from threading import Thread


class generowanieDanychDoBazy(Thread):


    connection = None
    cursor = None
    thread1 = None
    thread2 = None

    def run(self):
        thread1 = Thread(target=self.polaczSieZBazaDanych())
        thread2 = Thread(target=self.zakonczDzialanieProgramu())
        return thread1, thread2

    def zakonczDzialanieProgramu(self):
        pass


    def polaczSieZBazaDanych(self):
        connection = MySQLdb.connect(user="root", passwd="lenovo", db="bolid") #laczenie z baza
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(id) FROM data")
        maxId = cursor.fetchone() #maxId to maksymalne id w bazie
        maxId = str(maxId)
        maxId = maxId[1:-2]
        print(maxId)
        return maxId, cursor


    def dodawajWpisyDoBazyDanych(self):
        while 1:
            try:
                maxId = int(maxId)
                maxId = maxId+1
                maxId = str(maxId)
                dodajWpisDoBazy = ("INSERT INTO data (id,czas,napiecie,prad,predkosc) VALUES (%s,%s,%s,%s,%s)")
                daneDoDodania = (maxId,datetime.datetime.now(),"23.2","24.2","25.2")
                cursor.execute(dodajWpisDoBazy,daneDoDodania)
                connection.commit()
                time.sleep(2)
                print(maxId)
            except:
                print("blad przy probie zapisu danych")
                break


    def wyczyscBazeDanych(self):
        cursor.execute("DELETE FROM data WHERE id>1")
