# integrado a python
import datetime

# hora
mi_hora = datetime.time(11,37)
print(mi_hora)
print(mi_hora.minute)
print(mi_hora.hour)


# fecha
mi_fecha = datetime.date(2024,2,7)
print(mi_fecha)
print(mi_fecha.day)
print(mi_fecha.year)
# fecha actual
print(mi_fecha.today())

# dia y fecha importo datetime de datetime
from datetime import datetime
mi_fecha = datetime(2024,2,7,11,40)
print(mi_fecha)

# reemplaza
mi_fecha = mi_fecha.replace(hour=12)
print(mi_fecha)

# calculo de tiempos
# años que vivio alguien
from datetime import date
nacimiento = date(1945,5,31)
muerte = date(2022,5,19)
vida = muerte - nacimiento
print(vida)

# cuanto dormi hoy

despertar = datetime(2024,2,7,6,40)
dormir = datetime(2024,2,7,20,40)
vigilia = dormir-despertar
print(vigilia )




