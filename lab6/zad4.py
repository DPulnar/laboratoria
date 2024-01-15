import datetime


ostatnie_zajecia = datetime.datetime(2023,12,13)
kolokwium = datetime.datetime(2024,2,12)
dzisiaj = datetime.datetime.now()
print(dzisiaj-ostatnie_zajecia)
print(kolokwium-dzisiaj)