import datetime

class Laikas_ir_data:
    
    def __init__(self, data):
        self.data = data
        
    def dabartine_data(self):
        data_dabar = datetime.datetime.now() 
        return data_dabar
        
    def laiko_atemimas(self, dienos): 
        self.dienos = int(dienos)
        return Laikas_ir_data.dabartine_data(self) - datetime.timedelta(days=(self.dienos))
    
    def laiko_pridejimas(self, valandos):
        self.valandos = int(valandos)
        return Laikas_ir_data.dabartine_data(self) + datetime.timedelta(hours=(self.valandos))
        
    def laiko_spausdinimas(self):
        print((Laikas_ir_data.dabartine_data(self)).strftime("%Y %m %d %H:%M:%S"))
        
    def laiko_skaiciuokle(self):
            self.datos_ivestis = input("Iveskite savo gimimo data: ")
            year = datetime.datetime.today().year - datetime.datetime.strptime(self.datos_ivestis, "%Y-%m-%d").year
            month = datetime.datetime.today().month - datetime.datetime.strptime(self.datos_ivestis, "%Y-%m-%d").month
            days = datetime.datetime.today().day - datetime.datetime.strptime(self.datos_ivestis, "%Y-%m-%d").day
            minutes = datetime.datetime.today().minute - datetime.datetime.strptime(self.datos_ivestis, "%Y-%m-%d").minute
            sekundes = datetime.datetime.today().second - datetime.datetime.strptime(self.datos_ivestis, "%Y-%m-%d").second
            total_days = (datetime.datetime.today()-datetime.datetime.strptime(self.datos_ivestis, "%Y-%m-%d")).days
            total_sec = (datetime.datetime.today()-datetime.datetime.strptime(self.datos_ivestis, "%Y-%m-%d")).total_seconds()
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

    def konvertavimas(self, data):
        self.data = data
        return datetime.datetime.strptime(self.data, "%Y-%m-%d")
        
    def sekmadieniai(self):
        data_nuo = datetime.datetime.strptime(("2021-01-01"), "%Y-%m-%d")
        data_iki = datetime.datetime.strptime(("2022-01-01"), "%Y-%m-%d")
        sekmadieniu_sarasas = []
        sekmadienis = datetime.datetime(2022, 4, 24).strftime("%a")
        
        while data_nuo != data_iki:
            if data_nuo.strftime("%a") == sekmadienis:
                sekmadieniu_sarasas.append(data_nuo.strftime("%Y-%m-%d"))
            data_nuo = data_nuo + datetime.timedelta(days = 1)
            
        print(sekmadieniu_sarasas)

    def mikros_sekundziu_ismetimas(self):
        return datetime.datetime.strftime(datetime.datetime.today(), "%Y-%m-%d %H:%M:%S")

    def paskutinio_antradienio_data(self):
            siandiena = datetime.datetime.today()
            data = datetime.datetime.strftime(siandiena,"%Y-%m-%d")
            data = datetime.datetime.strptime(data, "%Y-%m-%d")
            antradienis = datetime.datetime(2022, 4, 26)
            antradienis = datetime.datetime.strftime(antradienis, "%A")
            while data.strftime("%A") != antradienis:
                data = data - datetime.timedelta(days = 1)
                print(data.strftime("%A"))
            print(data)
        
class Turto_Agentura:
    
    def __init__(self, pavadinimas, adresas, telefonas):
        self.pavadinimas = pavadinimas
        self.adresas = adresas
        self.telefonas = telefonas
        
    def greet(self):
        print(self.pavadinimas)
               
class Real_Estate(Turto_Agentura):
    
    def __init__(self, miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kambariu_skaicius):
        self.miestas = miestas
        self.mikrorajonas = mikrorajonas
        self.gatve = gatve
        self.namo_numeris = namo_numeris
        self.tipas = tipas
        self.pastatymo_metai = pastatymo_metai
        self.plotas = plotas
        self.kambariu_skaicius = kambariu_skaicius
               
class Flat(Real_Estate):
    def __init__(self, sildymo_budas):
        super().__init__(sildymo_budas)
    
    
    