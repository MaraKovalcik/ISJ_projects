#!/usr/bin/env python3
# @Author: Marek Kovalčík (xkoval14)

import sys


# 1. dekorátor @limit_calls s parametry max_calls a error_message_tail (defaultní hodnoty 2 a 'called too often') pro obecné funkce
def limit_calls(max_calls=2, error_message_tails="called too often"):
    '''1. dekorátor @limit_calls s parametry max_calls a error_message_tail (defaultní hodnoty 2 a 'called too often') pro obecné funkce'''
    # dekorační funkce
    def decorate(func):
        '''Funkce dekorátoru limit_calls'''
        # ověřování počtu volání dle zadaných argumentů
        def checking(*args, **kargs):
            '''Funce kontroluje počet volání funkce'''
            # v calls je uložen počet volání
            checking.calls += 1
            # pokud je v calls více než je maximální možný počet volání, vyvolá se vyjímka
            if checking.calls > max_calls:
                # Vytvoří se vyjímka dle zadání:
                #   __main__.TooManyCallsError: function "pyth" - that is too much
                msg = "function \"" + str(func.__name__) + "\" - " + error_message_tails
                raise MyException(msg)
            # vrátí se dekorovaná funkce
            return func(*args, **kargs)
        checking.calls = 0
        return checking
    return decorate


# Pomocná třáda pro vyvolání vyjímkys
class MyException(Exception):
    '''Pomocná třáda pro vyvolání vyjímkys'''
    pass


# 2. generátorovou funkci ordered_merge, která bude moci být volána s libovolným počtem iterovatelných objektů a parametrem selector, udávajícím, z kterého iterovatelného objektu má prvek na dané pozici být, a bude vybírat prvky v zadaném pořadí (první iterovatelný objekt má v selector index 0).
# Například tedy:
# print(list(ordered_merge('abcde', [1, 2, 3], (3.0, 3.14, 3.141), range(11, 44, 11), selector = [2,3,0,1,3,1])))
# vypíše [3.0, 11, 'a', 1, 22, 2]
def ordered_merge(*args, **kwargs):
    '''generátorová funkce ordered_merge'''
    # seznam obsahující hodnoty k vrácení
    result = list()
    # funkce ordered_merge má proměnný počet argumentů, v args je seznam těchto argument
    arguments = list()
    # pokud jeden z argumentů není 'selector', vrací se prázdný seznam
    if not kwargs.__contains__("selector"):
        return []
    # uložení hodnoty paramaetru selector
    selector = kwargs["selector"]
    # uloží postupně všech argumentů do seznamu s argumenty
    for i in args:
        arguments.append(list(i))
    # pro každý index i předán do selectoru, se do výsledku přidá první prvek z z argumentu na tomto indexu
    for i in selector:
        # [0] načítá první prvek
        result.append(arguments[i][0])
        arguments[i].pop(0)
    # vrací se seznam vybraných prvků
    return result


# Třída Log
class Log():
    '''Třída Log'''
    # Funkce volaná při inicializaci
    def __init__(self, filename):
        '''Funkce volaná při inicializaci'''
        try:
            self.result = open(filename, "w+")
        except:
            sys.stderr.write("Failed to open file")
    # Vytvoření začátku logovacího výstupu dle zadání
    def __enter__(self):
        '''Vytvoření začátku logovacího výstupu dle zadání'''
        self.result.write("Begin\n")
        return self
    # Uzavření logovacího souboru
    def __exit__(self, exc_type, exc_val, exc_tb):
        '''# Uzavření logovacího souboru'''
        try:
            self.result.write("End\n")
            self.result.close()
        except:
            sys.stderr.write("Failed to close file")
    # Funkce pro zápis informací do logovacího souboru
    def logging(self, msg):
        # Funkce pro zápis informací do logovacího souboru
        self.result.write(msg + "\n")


# testovací funkce
def test():
    '''Funkce pro testování dekorátoru, generátorové funkce a třídy Log'''
    # 1. Testovací část pro dekorátor limit_calls
    import math
    @limit_calls(1, 'that is too much')
    def pyth(a, b):
        c = math.sqrt(a ** 2 + b ** 2)
        return c

    print(pyth(3, 4))
    #print(pyth(6, 8)) # pokud je tento print odpoznámkovaný, vyvolá se vyjímka

    # 2. Testovací část pro funkci ordered_merge
    print(list(ordered_merge('abcde', [1, 2, 3], (3.0, 3.14, 3.141), range(11, 44, 11), selector=[2, 3, 0, 1, 3, 1])))
    # vypíše[3.0, 11, 'a', 1, 22, 2]

    # 3. Vytvořit třídu Log tak, aby po vrácení chyby z kódu:

    with Log('mylog.txt') as logfile:
        logfile.logging('Test1')
        logfile.logging('Test2')
        #a = 1 / 0
        logfile.logging('Test3')

    # bylo v souboru mylog.txt
    #   Begin
    #   Test1
    #   Test2
    #   End


# Vstupní bod programu
if __name__ == "__main__":
    '''Hlavní funkce programu'''
    # Vyvolání testovací funkce
    test()