import datetime
import MySQLdb


class GetDataFromDataBase():

    def __init__(self):
        self.connection = MySQLdb.connect(user="root", passwd="lenovo", db="bolid")

    def get_last_row(self):
        pass

    def get_current(self):
        pass

    def get_voltage(self):
        pass

    def get_speed(self):
        pass


czas = None


def get_time():
    global czas
    czas = datetime.datetime.now()
    return czas


cnx = MySQLdb.connect(user="root", passwd="lenovo", db="bolid")
print(str(cnx))
cur = cnx.cursor()
dane = cur.execute("SELECT prad FROM data")
i = cur.fetchall()
print(str(i))
get_time()
print(str(czas))
