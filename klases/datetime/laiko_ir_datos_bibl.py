import datetime
import locale
#  Esamas laikas ir data
data_ir_laikas_dabar = datetime.datetime.today()
print(data_ir_laikas_dabar)


# Tik data: 
data_dabar = datetime.date.today()
# data_dabar = datetime.datetime.today().date() # kitas metodas gauti tik data
print(data_dabar)


# Tik laikas
laikas_dabar = datetime.datetime.today().time()
print(laikas_dabar)


#  Nustatome patys laika ir data_dabar
set_date_and_time = datetime.datetime(2022, 3, 14, 23, 55, 00)
print(set_date_and_time)


# Nusistatome kokiu formatu bus isvedama data ir laikas
print(set_date_and_time.strftime("%C"))


# LOCALE BIBLIOTEKA
# nustatyta lt data ir laikas
locale.setlocale(locale.LC_TIME,'lt_LT.utf8')
lt_data_ir_laikas = datetime.datetime(2022, 3, 14, 11, 55, 00)
print(lt_data_ir_laikas.strftime("%A %d %B %Y %I:%M %p"))

# Operacijos su datomis ir laiku

dabar = datetime.datetime.now()
print(dabar - datetime.timedelta(days = 5))
print(dabar + datetime.timedelta(hours = 5))
print(dabar + datetime.timedelta(days = 20, hours = 5, minutes = 3))

nepr_diena = datetime.datetime(1990, 3, 11)
skirtumas = dabar - nepr_diena
print(skirtumas)

# Datos ir laikos ivedimas

# ivesti_data = input("Iveskite data: ")
# data = datetime.datetime.strptime(ivesti_data, "%Y-%m-%d %H:%M:%S")
# skirtumas = (datetime.datetime.now() - data)
# print(skirtumas)

dabar1 = datetime.datetime.now()
print(dabar1.year)
print(dabar1.month)
print(dabar1.day)
print(dabar1.hour)
print(dabar1.minute)
print(dabar1.second)
print(dabar1.microsecond)
print(dabar1.weekday())

pradzia = datetime.datetime.today()
for n in range(10000000):
    n += n
print(n)
pabaiga = datetime.datetime.today()
print(f"Programa uztruko: {(pabaiga-pradzia).total_seconds()}")
