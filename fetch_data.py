import MySQLdb


class GetDataFromDataBase():

    def __init__(self):
        """
        Działa, kostruktor, łączy się z baza danych bolid na localhoscie, tworzy dwie zmienne dla każdego obiektu
        """
        self.connection = MySQLdb.connect(user="root", passwd="lenovo", db="bolid")
        self.cursor = self.connection.cursor()

    def get_last_id(self):
        """
        DZIAŁA zwraca najwyższe id w bazie jako typ int
        """
        self.cursor.execute("SELECT MAX(id) FROM data")
        max_id = self.cursor.fetchone() #maxId to maksymalne id w bazie
        max_id = str(max_id)
        max_id = max_id[1:-2]
        print(max_id)
        max_id = int(max_id)
        return max_id

    def get_current(self, id):
        """
        DZIAŁA, zwraca prąd jako typ String dla podanego liczbowo id
        """
        self.cursor.execute("SELECT prad FROM data WHERE id="+str(id))
        current = self.cursor.fetchone()
        current = str(current)
        current = current[10:-4]
        print(current)
        return current

    def get_voltage(self, id):
        """
        DZIAŁA, zwraca napięcie jako typ String dla podanego liczbowo id
        """
        self.cursor.execute("SELECT napiecie FROM data WHERE id="+str(id))
        voltage = self.cursor.fetchone()
        voltage = str(voltage)
        voltage = voltage[10:-4]
        print(voltage)
        return voltage

    def get_speed(self, id):
        """
        DZIAŁA, zwraca prędkość jako typ String dla podanego liczbowo id
        """
        self.cursor.execute("SELECT predkosc FROM data WHERE id="+str(id))
        speed = self.cursor.fetchone()
        speed = str(speed)
        speed = speed[10:-4]
        print(speed)
        return speed

    def get_time_by_id(self, id):
        """
        DZIAŁA, ALE zwraca "nieobrobione" dane ze śmieciami jako typ string, dla podanego liczbowo id
        """
        self.cursor.execute("SELECT czas FROM data WHERE id="+str(id))
        time = self.cursor.fetchone()
        time = (time)
        #time = time[10:-4]
        print(time)
        return time


app = GetDataFromDataBase()
last_id = app.get_last_id()
current_flow = app.get_current(last_id)
current_voltage = app.get_voltage(last_id)
current_speed = app.get_speed(last_id)
current_time = app.get_time_by_id(last_id)
