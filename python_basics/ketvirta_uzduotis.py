a = int(input("Ivesti skaiciu a: "))
b = float(input("Iveskite skaiciu b: "))
c = str(input("Koki veiksma norite atlikti: "))

        
def paprastas_kalkuliatorius(a, b, c):
    """Paklaustų, kokį matematinį veiksmą reiktų atliktų
        Atspausdintų rezultatą: pasirinktų skaičių suma, daugybą ar pan.

    Args:
        a (int): a skaicius
        b (int): b skaicius_
        c (str): norima atlykti operacija
    """
    if c == "<":
        if a < b:
            print(f"a({a}) yra maziau uz b({b})")
    elif c == ">":
        if a > b:
            print(f"a({a}) yra daugiau uz b({b})")
        
    elif c == "=":
        if a == b:
            print(f"a({a}) yra lygus b({b})")
        
    elif c == "!=":
        if a != b:
            print(f"a({a}) yra nelygus b({b})")
            
    elif c == "+":
        print(f"a({a}) sudetys su b({b}) yra lygu {a + b}")
        
    elif c == "-":
        print(f"a({a}) atimtis su b({b}) yra lygu {a - b}")
        
    elif c == "/":
        print(f"a({a}) dalyba su b({b}) yra lygu {a / b}")
        
    elif c == "*":
        print(f"a({a}) daugyba su b({b}) yra lygu {a * b}")

    else:
        print("blogai ivesta operacija")