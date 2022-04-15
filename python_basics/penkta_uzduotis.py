def operacijos_su_modulus():
    """Isveda i ekrana pasirinktos operacijos rezultata,
    reiksmes gaunamos is vartotojo

    Args:
        a (float): a operandas
        c (int): operacija
    """
    a = float(input("Ivesti skaiciu: "))
    b = str(input("Koki veiksma norite atlikti:\n a - patikrinti ar skaičius lyginis\n b - patikrinti ar skaicius dalinas iš trijų \n Jūsų pasirinkimas: "))
    if b == "a" :
        if a % 2  == 0:
            print(f"Skaičius {a} yra lyginis")
        else:
            print(f"Skaičius {a} yra nelyginis")
    if b == "b" :
        if a % 3 == 0:
            print(f"Skaičius {a} dalinasi iš trijų")
        else:
            print(f"Skaičius {a} nesidalina iš trijų") 
        
