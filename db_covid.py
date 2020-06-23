import csv
from covid_19_Madrid import get_total_confirmed
import datetime
import matplotlib.pyplot as plt
import pandas as pd

total = get_total_confirmed()


def write_data():
    with open("db_covid.csv", "w") as file:
        lista = ["hola", "kuga"]
        csv_writer = csv.writer(file, delimiter=",")
        csv_writer.writerow(["fecha", "casos confirmados"])
        csv_writer.writerow([datetime.date(2020, 5, 25), total])


def append_data():
    with open("db_covid.csv", "a") as file:
        csv_append = csv.writer(file, delimiter=",")
        csv_append.writerow([datetime.date.today(), int(total)])


# append_data()


def enter_dicta():
    dicta = {"fecha": [], "casos_confirmados": []}
    with open("db_covid.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if len(row) > 1:
                dicta["fecha"].append(row[0])
                dicta["casos_confirmados"].append(int(row[1]))
    return dicta


dicta = enter_dicta()
print(dicta)

df = pd.DataFrame(dicta)
df = pd.DataFrame(df, columns=['fecha', 'casos_confirmados'])
df.plot(x='fecha', y='casos_confirmados', kind='line', color="red")
plt.show()
