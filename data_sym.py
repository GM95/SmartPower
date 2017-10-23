import time
import MySQLdb
import datetime
from threading import Thread, Event


class GeneratingRandomData(Thread, Event):

    """
    DZIAŁA Konstruktor łączy się z bazą danych, ustawia max_id w bazie na aktualne wywołując funkcję self.set_acctual_id()
    """
    def __init__(self):
        self.connection = MySQLdb.connect(user="root", passwd="lenovo", db="bolid") #laczenie z baza
        self.cursor = self.connection.cursor()
        print(self.cursor)
        self.max_id = self.set_acctual_id()
        self.clear_database()
    """
    DZIAŁA zwraca najwyższe id z bazy danych 
    """
    def set_acctual_id(self):
        self.cursor.execute("SELECT MAX(id) FROM data")
        print(self.cursor)
        max_id = self.cursor.fetchone() #maxId to maksymalne id w bazie
        max_id = str(max_id)
        max_id = max_id[1:-2]
        print("lICZBA WPISÓW W BAZIE " + max_id)
        return max_id

    """
    DZIAŁA ALE trzeba to odpalić jako osobny wątek/proces, bo blokuje cały program. Co dwie sekundy dodaje nowy wpis do bazy, z wyższym id i aktualnym czasem.
    Trzeba też zrobić obsługę błędów. 
    """
    def data_generator(self): #trzeba to przerobić na wątek, żeby szło to zatrzymać wywołujac inną funkcję
        while 1:
            try:
                max_id = int(self.max_id)
                max_id = max_id +1
                max_id = str(max_id )
                add_line_to_base = ("INSERT INTO data (id,czas,napiecie,prad,predkosc) VALUES (%s,%s,%s,%s,%s)")
                data_to_add = (max_id, datetime.datetime.now(), "23.2", "24.2", "25.2") #dorobić generator liczb losowych :)
                self.cursor.execute(add_line_to_base, data_to_add)
                self.connection.commit()
                time.sleep(2)
                print("Dodano wpis numer " + max_id)
            except:
                print("blad przy probie zapisu danych")
                break
    """
    DZIAŁA, czyści bazę danych, zostaje tylko rząd z id=1
    """
    def clear_database(self):
        self.cursor.execute("DELETE FROM data WHERE id>1")
        self.connection.commit()
        print(self.cursor)


random_data_generator = GeneratingRandomData()
random_data_generator.data_generator()

