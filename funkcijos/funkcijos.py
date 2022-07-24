
def pasisveikinimas(miestas, vardas, pavarde):
    return (f"Labas {vardas} {pavarde}, esate is {miestas}")    


def kelimas_kubu(skaicius):
    return pow(skaicius)


def skaicius_laipsniu(skaicius, laipsnis):
    return (f"{skaicius} pakeltas laipsniu {laipsnis} yra {pow(skaicius, laipsnis)}")


def ploto_skaiciavimas():
    """
    Sukurkite funkcija kuri apskaiciuotu staciakampio plota ir perimetra.
    vartotojas turi ivesti input staciakampio krastiniu ilgi.
    atsakyma isvesti i ekrana print
    """
    krastine_a = int(input("Iveskite krastines a ilgi:"))
    krastine_b = int(input("Iveskite krastinb_b ilgi:"))
    print(f"Plotas yra {krastine_a * krastine_b}")
    

def kvadrato_skaiciavimas(skaicius):
    kvadratu = skaicius**2
    return kvadratu
    

def triju_skaiciu_suma(skaicius_a, skaicius_b, skaicius_c):
    """
    Apsirasome funkcija kuri suskaiciuoja triju jai nurodytu argumentais skaiciu suma ir ta suma padaugina is paskutinio skaiciaus argumento.
    Atspausdina viena funkcija trys eilutes : suma, daugyba, grazina - return daugyba
    """
    suma = skaicius_a + skaicius_b + skaicius_c
    suma = suma * skaicius_c


def skaiciu_suma(sk1, sk2, sk3):
    rezultatas = sk1 + sk2 + sk3
    return rezultatas


def daug_argumentu_kvadratu(*args):
    for eiles_nr, skaicius in enumerate(args):
        print(eiles_nr+1, skaicius ** 2)


def teksto_skaidymas_ir_numeracija(*args):
    """
    Funkcijos su neribotais argumentais - isvedanti i ekrana nurodyta simboli ir jo eiles numeri.
    """
    skaidytas_tekstas = []
    for simbol in args:
        print(simbol)
        for i in simbol:
            skaidytas_tekstas.append(i)

    for eiles_nr, simbolis in enumerate(skaidytas_tekstas):
        print(eiles_nr + 1, simbolis)
  
        
def spausdinti_reiksmes(**kwargs):
    for raktazodis, reiksme in kwargs.items():
        print(raktazodis, reiksme)


def skaiciu_suma_su_neribotais_argumentais(*args):
    """
    Grazina is paduoto skaičių sąrašo, sumą ir skaiciu kieki 
    atliekama su neribotais argumentais
    Returns:
        integer : skaiciu suma ir saraso ilgi
    """
    return f"Saraso skaiciu suma yra - {sum(args)}, ilgis - {len(args)}"


def spausdinti_reiksmes(sk1, sk2, *args):
    print("Skaiciu suma:", sk1 + sk2)
    for vienas in args:
        print(vienas)
        

def daugyba_is_saves_su_lambda():
    "Neveikia !!!"
    daugyba_is_saves = [lambda i = skaicius: i*i for skaicius in range(1, 6)]
    print(daugyba_is_saves)


def didziausias_is_paduotu_skaiciu(*args):
    """
    Atspausdina didžiausią iš kelių paduotų skaičių (panaudojant *args).

    Returns:
        integer: max reiksme is saraso
    """
    maksikamali_reiksme = args[0]
    for i in args:
        if i > maksikamali_reiksme:
            maksikamali_reiksme = i
    return (f"Maksimali reiksme yra: {maksikamali_reiksme}")


def atspausdina_kiek_sakinyje_didziuju_raidziu():
    tekstas = """111Flat is better than nested.
                Sparse is better than dense.
                Readability counts.
                """

    didziosios_raides = []
    mazosios_raides =[]
    skaiciai = []
    for raide in tekstas:
        if raide.isupper():
            didziosios_raides.append(raide)
        elif raide.islower():
            mazosios_raides.append(raide)
        elif raide.isnumeric():
            skaiciai.append(raide)
            
            
          
    print(len(didziosios_raides))
    print(len(mazosios_raides))
    print(len(skaiciai))
    
    
def pirminiai_skaiciai(skaicius):
    """
    Gražintų, ar paduotas skaičius yra pirminis.
    Pirminis skaičius– bet kuris natūralusis skaičius, didesnis nei 1, 
    kuris dalinasi tik iš savęs ir vieneto.
    
    """
    counter = 0 
    for daliklis in range(1,skaicius):
        if skaicius % daliklis == 0 :
            counter += 1
    
    if counter < 2:
        print(f"Skaicius {skaicius} yra pirminis")
    else:
        print(f"Skaicius {skaicius} yra nepirminis")


def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
 
 
def bool_to_word(bool):
    return "Yes" if bool else "No"    


def square_or_square_root(arr):
    
    num_list = []
    for number in arr:       
        if number **(1/2) %1 == 0:
            num_list.append(int(number **(1/2)))
        else:
            num_list.append(number **2)

    return num_list
            

def quarter_of(month):
    if 0 < month <= 3:
        return 1
    elif 3 < month <= 6:
        return 2
    elif 6 <= month <= 9:
        return 3
    else:
        return 4
    

def time_per_distance(speed, distance):
    speed = float(input("Iveskite greiti: "))
    distance = float(input("Iveskite atstuma: "))
    return 60*60*(distance / speed) 


def tip_calculator():
    #If the bill was $150.00, split between 5 people, with 12% tip. 
    #Each person should pay (150.00 / 5) * 1.12 = 33.6
    #Format the result to 2 decimal places = 33.60

    print(f"Welcome to the tip calculator!")
    bill = float(input("What was the total bill? $"))
    perc_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people_count = int(input("How many people to split the bill? "))
    bill_with_tips = (bill +(bill * (perc_tip / 100))) / people_count
    print(f"Each person should pay: ${bill_with_tips:.2f}")
 
    
def rock_paper_scissors():
    import random
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)__
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)__
            ______)
        __________)
        (____)
    ---.__(___)
    '''    
    
    
    hand_list = [rock, paper, scissors]
    computer_choice = hand_list[random.randint(0, 2)]
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    user_choice = hand_list[user_choice]
    if computer_choice == user_choice:
        print(user_choice)
        print(f"Computer choice:\n{computer_choice}")
        print("draw")
    elif computer_choice == rock and user_choice == paper:
        print(user_choice)
        print(f"Computer choice:\n{computer_choice}")
        print("You win!")
    elif computer_choice == rock and user_choice == scissors:
        print(user_choice)
        print(f"Computer choice:\n{computer_choice}")
        print("Computer win!")
    elif computer_choice == paper and user_choice == rock:
        print(user_choice)
        print(f"Computer choice:\n{computer_choice}")
        print("Computer win!")
    elif computer_choice == paper and user_choice == scissors:
        print(user_choice)
        print(f"Computer choice:\n{computer_choice}")
        print("You win!")
    elif computer_choice == scissors and user_choice == rock:
        print(user_choice)
        print(f"Computer choice:\n{computer_choice}")
        print("You win!")
    elif computer_choice == scissors and user_choice == paper:
        print(user_choice)
        print(f"Computer choice:\n{computer_choice}")
        print("Computer win!")         


def password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
    
    password = []
    hardened_password = []
    letters_list = []
    symbols_list = []
    numbers_list = []
    password_string = ""
    
    for letter in range(nr_letters):
        letters_list.append(letters[random.randint(0, len(letters)-1)])
    for symbol in range(nr_symbols):
        symbols_list.append(symbols[random.randint(0, len(symbols)-1)])
    for number in range(nr_numbers):
        numbers_list.append(numbers[random.randint(0, len(numbers)-1)])
    
    password = letters_list + symbols_list + numbers_list
    for i in password:
        hardened_password.append(password[random.randint(0, len(password)-1)])
    
    for char in hardened_password:
        password_string += char
    print(password)
    print(hardened_password)
    print(password_string)
    # arba galime joina
    # print(''.join([str(elem) for elem in hardened_password]))
    
    
        
password_generator()