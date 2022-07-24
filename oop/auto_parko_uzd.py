# 3_PAVELDEJIMAS_POLIMORFIZMAS.Automobilių parkas. 
# Turite suvesti INPUT automobilių parkų (3 parkai) miestas, adresas, telefonas. 
# Įmonės automobilių parką sudaro lengvieji automobiliai, krovininiai automobiliai ir autobusai. 
# Sukurkite klasę „Transport“ (savybės – valstybinis numeris, gamintojas, modelis, 
# pagaminimo metai ir mėnuo, atliktos techninės apžiūros data, kuras, vidutinės kuro sąnaudos (100 km)),
# kurią paveldės klasės „Car“ (savybė – odometro rodmenys), 
# „Truck“ (savybė – priekabos talpa) ir „Bus“ (savybė – sėdimų vietų skaičius).

# *Raskite geriausią transporto priemonę kiekvienoje grupėje, atspausdinkite jos gamintoją, modelį, 
# valstybinius numerius ir amžių. 
# Lengvasis geriausias – nuvažiuota mažiausiai kilometrų, 
# krovininis geriausias – didžiausia priekabos talpa, 
# autobusas geriausias – daugiausia sėdimų vietų.
# *Sudarykite visų benzinu varomų lengvųjų automobilių sąrašą, ekrane atspausdinkite jų valstybinį numerį, 
# gamintoją, modelį, bei pagaminimo metus. 

class Automobiliai():
    def __init__(self, miestas, adresas, telefonas):
        self.miestas = miestas
        self.adresas = adresas
        self.telefonas = telefonas

    def __str__(self): 
        return f"miestas: {self.miestas}, adresas: {self.adresas}, telefonas {self.telefonas}"

    def __repr__(self):
        return f"miestas: {self.miestas}, adresas: {self.adresas}, telefonas {self.telefonas}"

parkas1 = Automobiliai("Klaipeda", "Juros g., 14", 865545555)
parkas2 = Automobiliai("Palanga", "Parko g., 17", 869396966)
parkas3  = Automobiliai("Kretinga", "Zalioji g. 17", 856655544)
print(parkas1, "\n", parkas2, "\n", parkas3)

class Transport():
    def __init__(self, valstybinis_numeris, gamintojas, modelis, pagaminimo_metai_ir_menuo, 
    atliktos_techninės_apziuros_data, kuras, vidutines_kuro_sanaudos_100_km):
        self.valstybinis_numeris = valstybinis_numeris
        self.gamintojas = gamintojas
        self.modelis = modelis
        self.pagaminimo_metai_ir_menuo = pagaminimo_metai_ir_menuo
        self.atliktos_techninės_apziuros_data = atliktos_techninės_apziuros_data
        self.kuras = kuras
        self.vidutines_kuro_sanaudos_100_km = vidutines_kuro_sanaudos_100_km

    def __str__(self): 
        return f"{self.valstybinis_numeris}, {self.gamintojas}, {self.modelis}, {self.pagaminimo_metai_ir_menuo} ,{self.atliktos_techninės_apziuros_data}, {self.kuras}, {self.vidutines_kuro_sanaudos_100_km}"

    def __repr__(self):
        return f"{self.valstybinis_numeris}, {self.gamintojas}, {self.modelis}, {self.pagaminimo_metai_ir_menuo} ,{self.atliktos_techninės_apziuros_data}, {self.kuras}, {self.vidutines_kuro_sanaudos_100_km}"


class Car(Transport):
    def __init__(self, valstybinis_numeris, gamintojas, modelis, pagaminimo_metai_ir_menuo, atliktos_techninės_apziuros_data, kuras, vidutines_kuro_sanaudos_100_km, odometro_rodmenys):
        super().__init__(valstybinis_numeris, gamintojas, modelis, pagaminimo_metai_ir_menuo, atliktos_techninės_apziuros_data, kuras, vidutines_kuro_sanaudos_100_km)
        self.odometro_rodmenys = odometro_rodmenys

    def __str__(self): 
        return f"{self.valstybinis_numeris}, {self.gamintojas}, {self.modelis}, {self.pagaminimo_metai_ir_menuo} ,{self.atliktos_techninės_apziuros_data}, {self.kuras}, {self.vidutines_kuro_sanaudos_100_km}, {self.odometro_rodmenys}"

class Truck(Transport):
    def __init__(self, valstybinis_numeris, gamintojas, modelis, pagaminimo_metai_ir_menuo, atliktos_techninės_apziuros_data, kuras, vidutines_kuro_sanaudos_100_km, priekabos_talpa):
        super().__init__(valstybinis_numeris, gamintojas, modelis, pagaminimo_metai_ir_menuo, atliktos_techninės_apziuros_data, kuras, vidutines_kuro_sanaudos_100_km)
        self.priekabos_talpa = priekabos_talpa

    def __str__(self):
        return f"{self.valstybinis_numeris}, {self.gamintojas}, {self.modelis}, {self.pagaminimo_metai_ir_menuo} ,{self.atliktos_techninės_apziuros_data}, {self.kuras}, {self.vidutines_kuro_sanaudos_100_km}, {self.priekabos_talpa}"


class Bus(Transport):
    def __init__(self, valstybinis_numeris, gamintojas, modelis, pagaminimo_metai_ir_menuo, atliktos_techninės_apziuros_data, kuras, vidutines_kuro_sanaudos_100_km, sedimu_vietu_skaicius):
        super().__init__(valstybinis_numeris, gamintojas, modelis, pagaminimo_metai_ir_menuo, atliktos_techninės_apziuros_data, kuras, vidutines_kuro_sanaudos_100_km)
        self.sedimu_vietu_skaicius = sedimu_vietu_skaicius

    def __str__(self):
        return f"{self.valstybinis_numeris}, {self.gamintojas}, {self.modelis}, {self.pagaminimo_metai_ir_menuo} ,{self.atliktos_techninės_apziuros_data}, {self.kuras}, {self.vidutines_kuro_sanaudos_100_km}, {self.sedimu_vietu_skaicius}"


auto1 = Car("HJK 858", "Honda", "Civic", "2020-12", "2020-02-12", "benzinas", 7, 200200)
auto2 = Car("GJK 467", "Opel", "Corsa", "2011-05", "2022-04-12", "benzinas", 5, 100200)
auto3 = Car("KOL 789", "Subaru", "Legacy", "1999-10", "2000-02-03", "dyzelis", 8, 360520)

auto = [auto1, auto2, auto3]

sunkvezimis1 = Truck("PLK 020", "Kamaz", "modeliukas", "1997-11", "2001-12-11", "dyzelis", 6, 13)
sunkvezimis2 = Truck("ASD 036", "Kamaz", "kamaziukas", "1987-01", "2010-03-17", "dyzelis", 5, 15)

sunkvezimiai = [sunkvezimis1, sunkvezimis2]

busas1 = Bus("NUJ 123", "Busas", "autobusas", "1996-03", "2022-03-03", "dyzelis", 8, 50)
busas2 = Bus("YRA 236", "KLO", "busikas", "2010-05", "2022-05-12", "elektra", 4, 56)

busai = [busas1, busas2]


def geriausias_lengvasis(auto):
    min_rida = auto[0].odometro_rodmenys
    kita_info = auto[0].gamintojas, auto[0].modelis, auto[0].valstybinis_numeris, auto[0].pagaminimo_metai_ir_menuo
    for masina in auto:
        if masina.odometro_rodmenys > min_rida:
            masina.odometro_rodmenys = min_rida
        else: 
            min_rida
    print(f"Maziausia nuvaziuota kilometru: " , min_rida, "\n", "sios transporto priemones: ", kita_info,)

geriausias_lengvasis(auto)

def geriausias_krovininis(sunkvezimiai):
    max_priekab_talpa = sunkvezimiai[0].priekabos_talpa
    kita_info = sunkvezimiai[0].gamintojas, sunkvezimiai[0].modelis, sunkvezimiai[0].valstybinis_numeris, sunkvezimiai[0].pagaminimo_metai_ir_menuo
    for fura in sunkvezimiai:
        if fura.priekabos_talpa < max_priekab_talpa:
            fura.priekabos_talpa = max_priekab_talpa
        else:
            max_priekab_talpa
    print("Geriausias sunkvezimis: ", max_priekab_talpa, kita_info)

geriausias_krovininis(sunkvezimiai)


def geriausias_autobusas(busai):
    sedimos_vietos = busai[0].sedimu_vietu_skaicius
    kita_info = busai[0].gamintojas, busai[0].modelis, busai[0].valstybinis_numeris, busai[0].pagaminimo_metai_ir_menuo
    for busikas in busai:
        if busikas.sedimu_vietu_skaicius < sedimos_vietos:
            busikas.sedimu_vietu_skaicius = sedimos_vietos
        else:
            sedimos_vietos
    print("Geriausias busas: ", sedimos_vietos, kita_info)

geriausias_autobusas(busai)


def benzininiai_automobiliai(auto):
    benziniai = auto[0].kuras
    kita_info = auto[0].gamintojas, auto[0].modelis, auto[0].pagaminimo_metai_ir_menuo
    for masinukas in auto:
        if masinukas.kuras < benziniai:
            masinukas.kuras = benziniai
        else:
            benziniai
    print("Benziniai automobiliai: ", benziniai, kita_info)

benzininiai_automobiliai(auto)






# *Sudarykite visų benzinu varomų lengvųjų automobilių sąrašą, ekrane atspausdinkite jų valstybinį numerį, 
# gamintoją, modelį, bei pagaminimo metus. 







