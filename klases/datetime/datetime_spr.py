import datetime

def pirma_uzduotis():
    dabartine_data = datetime.datetime.now()
    print(dabartine_data)
    print(dabartine_data - datetime.timedelta(days=5))
    print(dabartine_data + datetime.timedelta(hours=8))
    print(dabartine_data.strftime("%Y %m %d %H:%M:%S"))
    
def antra_uzduotis():
    datos_ivestis = input("Iveskite savo gimimo data: ")
    year = datetime.datetime.today().year - datetime.datetime.strptime(datos_ivestis, "%Y-%m-%d").year
    month = datetime.datetime.today().month - datetime.datetime.strptime(datos_ivestis, "%Y-%m-%d").month
    days = datetime.datetime.today().day - datetime.datetime.strptime(datos_ivestis, "%Y-%m-%d").day
    minutes = datetime.datetime.today().minute - datetime.datetime.strptime(datos_ivestis, "%Y-%m-%d").minute
    sekundes = datetime.datetime.today().second - datetime.datetime.strptime(datos_ivestis, "%Y-%m-%d").second
    total_days = (datetime.datetime.today()-datetime.datetime.strptime(datos_ivestis, "%Y-%m-%d")).days
    total_sec = (datetime.datetime.today()-datetime.datetime.strptime(datos_ivestis, "%Y-%m-%d")).total_seconds()
    if month < 0:
        year = year - 1
        month = 12 + month

    print(f"Metai {year}")
    print(f"Menesiai {month}")
    print(f"Dienos {days}")
    print(f"Minutes {minutes}")
    print(f"Sekundes {sekundes}")
    print(total_days)
    print(total_sec)

def trecia_uzduotis():
    datos_ivestis = str(input("Iveskite data: "))
    data = datetime.datetime.strptime(datos_ivestis, "%Y-%m-%d")
    print(data)
        
def ketvirta_uzduotis():
    data_nuo = datetime.datetime.strptime(("2021-01-01"), "%Y-%m-%d")
    data_iki = datetime.datetime.strptime(("2022-01-01"), "%Y-%m-%d")
    sekmadieniu_sarasas = []
    sekmadienis = datetime.datetime(2022, 4, 24).strftime("%a")
    
    while data_nuo != data_iki:
        if data_nuo.strftime("%a") == sekmadienis:
            sekmadieniu_sarasas.append(data_nuo.strftime("%Y-%m-%d"))
        data_nuo = data_nuo + datetime.timedelta(days = 1)
        
    print(sekmadieniu_sarasas)
            
def penkta_uzduotis():
    return datetime.datetime.strftime(datetime.datetime.today(), "%Y-%m-%d %H:%M:%S")
    
def sesta_uzduotis():
    siandiena = datetime.datetime.today()
    data = datetime.datetime.strftime(siandiena,"%Y-%m-%d")
    data = datetime.datetime.strptime(data, "%Y-%m-%d")
    antradienis = datetime.datetime(2022, 4, 26)
    antradienis = datetime.datetime.strftime(antradienis, "%A")
    while data.strftime("%A") != antradienis:
        data = data - datetime.timedelta(days = 1)
        print(data.strftime("%A"))
    print(data)
    
