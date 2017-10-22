import datetime
import MySQLdb


global zapytanie
global id
global napiecie
global prad
global predkosc


def pobiezczas():
    global czas
    czas = datetime.datetime.now()
    return czas


cnx = MySQLdb.connect(user="root",passwd="lenovo",db="bolid")
print(str(cnx))
cur = cnx.cursor()
dane = cur.execute("SELECT prad FROM data")
i = cur.fetchall()
print(str(i))
pobiezczas()
print(str(czas))
