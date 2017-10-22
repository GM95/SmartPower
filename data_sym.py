import time
import MySQLdb
import datetime
from threading import Thread

class GeneratingRandomData(Thread):

    cursor = None
    connection = None

    def run(self):                                              #funkcja wykonywana automatycznie po stworzeniu obiektu
        thread1 = Thread(target=self.connect_to_database())
        thread2 = Thread(target=self.close_program())
        return thread1, thread2

    def close_program(self):
        pass

    def connect_to_database(self):
        self.connection = MySQLdb.connect(user="root", passwd="lenovo", db="bolid") #laczenie z baza
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT MAX(id) FROM data")
        max_id = self.cursor.fetchone() #maxId to maksymalne id w bazie
        max_id = str(max_id)
        max_id = max_id[1:-2]
        print(max_id)
        return max_id, self.cursor

    def add_data_to_base(self):
        while 1:
            try:
                max_id = int(max_id)
                max_id = max_id+1
                max_id = str(max_id)
                add_line_to_base = ("INSERT INTO data (id,czas,napiecie,prad,predkosc) VALUES (%s,%s,%s,%s,%s)")
                data_to_add = (max_id,datetime.datetime.now(),"23.2","24.2","25.2") #dorobić generator liczb losowych :)
                self.cursor.execute(add_line_to_base, data_to_add)
                self.connection.commit()
                time.sleep(2)
                print(max_id)
            except:
                print("blad przy probie zapisu danych")
                break

    def clear_database(self):
        self.cursor.execute("DELETE FROM data WHERE id>1")
