from datetime import datetime
# fecha y hora actual
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("Hora:", t)
# formato mm/dd/YY H:M:S
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formato uno:", time_one)
# formato dd/mm/YY H:M:S
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("Formato dos:", time_two)

date_string = "5 December, 2019"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


from datetime import date
d = date(202,1,1)
print(d)
# fecha actual
print("Fecha actual: ", d.today())
# objeto date de hoy
today = date.today()
print("Año actual:", today.year)
print("Mes actual:", today.month)
print("Dia actual:", today.day)


from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute y second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute y second)
c = time(hour=10, minute=30, second=50)
print("b =", b)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)


today = date(year=2026, month=10, day=11)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
print("Tiempo hasta año nuevo:", time_left_for_newyear)

t1 = datetime(year=2026, month=10, day=11, hour=1, minute=40 ,second=9)
t2 = datetime(year= 2027, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
print("Tiempo hasta año nuevo:", diff)


from datetime import timedelta
t1 = timedelta(weeks=41,days=11,hours=10,minutes= 43,seconds=0)
t2 = timedelta(days=20, hours= 10, minutes= 6, seconds=58)
t3 = t1 - t2 
print("t3 =", t3)


# Ejercicios: Día 16
# 1. Obtén el día, mes, año, hora, minuto y timestamp actuales desde el módulo datetime.
now = datetime.now()
print(now)
print(now.timestamp())

# 2. Formatea la fecha actual con el formato: "%m/%d/%Y, %H:%M:%S"
f = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f)

# 3. Hoy es 5 de diciembre de 2019. Convierte esa cadena de fecha a un objeto datetime.
today = "5 de December de 2019"
date_object = datetime.strptime(today, "%d de %B de %Y")
print(date_object)

# 4. Calcula la diferencia entre ahora y el próximo año nuevo.
today = datetime(year=2026, month=10, day=11)
new_year = datetime(year=2027, month=1, day=1)
diff = new_year - today
print(diff) 

# 5. Calcula la diferencia entre el 1 de enero de 1970 y ahora.
day = datetime(year=1970, month=1, day=1)
today = datetime(year=2026, month=10, day=11)
diff = today - day
print(diff)

# 6. Piensa: ¿para qué puedes usar el módulo datetime? Por ejemplo:
#    Análisis de series temporales
#    Obtener timestamps para eventos en una aplicación
#    Añadir la fecha de publicación en un blog