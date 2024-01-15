import datetime
import math
import time

rok = int(input("podaj rok"))
miesiac = int(input("podaj miesiac"))
dzien = int(input("podaj dzien"))
koniec_poprzedniego_roku = datetime.datetime(rok-1,12,31)
data = datetime.datetime(rok,miesiac,dzien)

print("ktory dzien roku",(data-koniec_poprzedniego_roku).days)
print("ktory tydzien roku",math.ceil((data-koniec_poprzedniego_roku).days/7))
print("data 2 tyg przed",data-datetime.timedelta(days=14))
print("data 2 tyg po",data+datetime.timedelta(days=14))
ile_do_nastepnej_niedzieli = 7-data.isoweekday()
if ile_do_nastepnej_niedzieli ==0:
    ile_do_nastepnej_niedzieli = 7
print("data kolejnej niedzieli",datetime.datetime(rok,miesiac,dzien+ile_do_nastepnej_niedzieli))

czas_biezacej_godziny_w_podanym_dniu = data+datetime.timedelta(hours=datetime.datetime.now().hour)
print("czas unixowy",time.mktime(czas_biezacej_godziny_w_podanym_dniu.timetuple()))