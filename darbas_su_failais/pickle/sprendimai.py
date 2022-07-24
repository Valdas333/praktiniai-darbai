from datetime import datetime
zen =             """The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!")
    """
def safe_text_to_file():

    with open("Tekstas.txt", "w") as failas:
        failas.write(zen)
    failas.close()
    
def read_text_from_file():  
    
    with open("Tekstas.txt", "r", encoding="utf-8") as failas:
        print(failas.read())   
    
def datos_pridejimas():
    
    with open("tekstas.txt", "w") as failas:
        failas.write(zen)
    with open('tekstas.txt', 'a') as failas:
        failas.write(str(datetime.today()))
    
    failas.close()
        
def eiluciu_numeracija():
    count = 0
    with open("tekstas.txt", 'r') as failas:
        for eilute in failas:
            count += 1
            print(f"{count}. {eilute.strip()}")
                       
def eilutes_keitimas():
    
    kuo_keisime = "Gražu yra geriau nei bjauru."
    
    with open("Tekstas.txt", 'r+', encoding= "UTF-8") as failas:
        data = failas.read()
        pakeistas_tekstas = data.replace("Beautiful is better than ugly.", kuo_keisime)
        failas.write(pakeistas_tekstas)

def tekstas_atbulai():
    with open("Tekstas.txt", 'r+', encoding= "UTF-8") as failas:
        data = failas.read()
        failas.write(data[-1])
        
safe_text_to_file()            
eiluciu_numeracija()
eilutes_keitimas()
read_text_from_file()
tekstas_atbulai()


            

    
