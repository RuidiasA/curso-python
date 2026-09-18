from datetime import datetime
# fecha y hora actual
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("Hora:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# formato mm/dd/YY H:M:S
print("Formato uno:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# formato dd/mm/YY H:M:S
print("Formato dos:", time_two)

# Commit de prueba para verificacion de inicializacion correcta de git