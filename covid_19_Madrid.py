from requests import *

url = get(
    "https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json",
    verify=False)
data = url.json()
data = data["data"]
new_data = data[0:199]

def get_total_confirmed():
    total = 0
    for confirmed in new_data:
        if type(confirmed.get("casos_confirmados_totales")) == int:
            total += confirmed.get("casos_confirmados_totales")
    return total


print(get_total_confirmed())