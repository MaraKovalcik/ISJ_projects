#!/usr/bin/env python3
# @Author: Marek Kovalčík (xkoval14)
import itertools


# vrátí první neopakující se znak ze vstupního řetězce
def first_nonrepeating(string):
    """vrátí první neopakující se znak ze vstupního řetězce"""
    # do chars se ukládají postupně znaky z řetězce str
    # do repetitiveChars se ukládají znaky, které už jsou  v chars (v řetězci se opakují)
    chars = list()
    repetitiveChars = list()
    result = None
    # Kontrola vstupního řetězce, jestli je str
    if not isinstance(string, str):
        return None
    # prázdný string
    if string == '' or string == ' ':
        return None
    # pouze escape sekvence ve stringu
    decoded_string = bytes(string, "utf-8").decode("unicode_escape")
    if decoded_string == '\t':
        return None
    # Postupné kontrolování znaků v řetězci
    for char in string:
        # Pokud je v char znak, který ještě neprocházel, vloží ho do listu znaků
        if char not in chars:
            chars.append(char)
        # Pokud je v char znak, který už je v listu chars, vloží char do listu repetitiveChars
        else:
            repetitiveChars.append(char)
    # Znovu prochází znaky v řetězci a pokud znak není v listu repetitiveChars, uloží ho do result a prohledávání se ukončí
    # breaknutím cyklu je ve výsledku první neopakující se znak
    for char in string:
        if not char in repetitiveChars:
            result = char
            break
    return result


# funkce dostane čtveřici 4 kladných celých čísel a očekávaný výsledek a vrátí setříděný seznam
# unikátních řešení matematických hádanek s výsledkem operací +, -, *, / nad 4 čísly
def combine4(lst, expectedResult):
    """funkce dostane čtveřici 4 kladných celých čísel a očekávaný výsledek a vrátí
    setříděný seznam  unikátních řešení matematických hádanek s výsledkem operací +, -, *, / nad 4 čísly"""
    result = list()
    symbols = ["+", "-", "*", "/"]
    # seznam pro uložení kombinací znamének, list bude vždy obsahovat 3 prvky
    operators = list()
    # seznam pro všechny kombinace hodnot vstupního seznamu
    operands = list()
    # vytvoří všechny možné kombinace symbolů, max 3 symboly (4 operandy)
    for combination in itertools.product(symbols, repeat=3):
        operators.append(combination)
    # vytvoří všechny možné kombinace 4 čísel ve vstupním seznamu
    for combination in itertools.permutations(lst, 4):
        operands.append(combination)
    # cyklus prochází všechny varianty zkombinovaných čísel
    for values_combination in operands:
        # zanořený cyklus for zpracováváa ke každé kombinaci čísel každou kombinaci operátorů
        for symbols_combination in operators:
            # try-except blok pro zachycení vyjímky při dělení nulou
            try:
                # vytvoří se výraz kde se střídá operand opetáror operand operátor operand operátor operand
                string = str(values_combination[0]) + symbols_combination[0] + str(values_combination[1]) + symbols_combination[1] + str(values_combination[2]) + symbols_combination[2] + str(values_combination[3])
                # tento výraz se vyhodnotí a shoduje-li se výsledek s očekávaným, přidá se do seznamu možných výsledků
                if eval(string) == expectedResult:
                    result.append(string)
                # stejný postup se provede pro jiné uzávorkování u stejného pořadí operandů a operátorů
                string = "(" + str(values_combination[0]) + symbols_combination[0] + str(values_combination[1]) + ")" + symbols_combination[1] + str(values_combination[2]) + symbols_combination[2] + str(values_combination[3])
                if eval(string) == expectedResult:
                    result.append(string)
                # opět stejný postup jako výše s jiným uzávorkováním
                string = str(values_combination[0]) + symbols_combination[0] + "(" + str(values_combination[1]) + symbols_combination[1] + str(values_combination[2]) + ")" + symbols_combination[2] + str(values_combination[3])
                if eval(string) == expectedResult:
                    result.append(string)
                # opět stejný postup jako výše s jiným uzávorkováním
                string = str(values_combination[0]) + symbols_combination[0] + str(values_combination[1]) + symbols_combination[1] + "(" + str(values_combination[2]) + symbols_combination[2] + str(values_combination[3]) + ")"
                if eval(string) == expectedResult:
                    result.append(string)
                # opět stejný postup jako výše s jiným uzávorkováním
                string = "(" + str(values_combination[0]) + symbols_combination[0] + str(values_combination[1]) + ")" + symbols_combination[1] + "(" + str(values_combination[2]) + symbols_combination[2] + str(values_combination[3]) + ")"
                if eval(string) == expectedResult:
                        result.append(string)
                # opět stejný postup jako výše s jiným uzávorkováním
                string = "(" + str(values_combination[0]) + symbols_combination[0] + str(values_combination[1]) + symbols_combination[1] + str(values_combination[2]) + ")" + symbols_combination[2] + str(values_combination[3])
                if eval(string) == expectedResult:
                        result.append(string)
                # opět stejný postup jako výše s jiným uzávorkováním
                string = str(values_combination[0]) + symbols_combination[0] + "(" + str(values_combination[1]) + symbols_combination[1] + str(values_combination[2]) + symbols_combination[2] + str(values_combination[3]) + ")"
                if eval(string) == expectedResult:
                        result.append(string)
                # opět stejný postup jako výše s jiným uzávorkováním
                string = "((" + str(values_combination[0]) + symbols_combination[0] + str(values_combination[1]) + ")" + symbols_combination[1] + str(values_combination[2]) + ")" + symbols_combination[2] + str(values_combination[3])
                if eval(string) == expectedResult:
                        result.append(string)
                # opět stejný postup jako výše s jiným uzávorkováním
                string = "(" + str(values_combination[0]) + symbols_combination[0] + "(" + str(values_combination[1]) + symbols_combination[1] + str(values_combination[2]) + "))" + symbols_combination[2] + str(values_combination[3])
                if eval(string) == expectedResult:
                        result.append(string)
                # opět stejný postup jako výše s jiným uzávorkováním
                string = str(values_combination[0]) + symbols_combination[0] + "((" + str(values_combination[1]) + symbols_combination[1] + str(values_combination[2]) + ")" + symbols_combination[2] + str(values_combination[3]) + ")"
                if eval(string) == expectedResult:
                        result.append(string)
                # opět stejný postup jako výše s jiným uzávorkováním
                string = str(values_combination[0]) + symbols_combination[0] + "(" + str(values_combination[1]) + symbols_combination[1] + "(" + str(values_combination[2]) + symbols_combination[2] + str(values_combination[3]) + "))"
                if eval(string) == expectedResult:
                        result.append(string)
            except ZeroDivisionError:
                pass
    # vrátí seznam možých kombinací bez duplicit
    return (list(set(result)))


# testovací funkce
def test():
    """testovací funkce"""
    assert first_nonrepeating('\t') is None
    assert first_nonrepeating(' ') is None
    assert first_nonrepeating('') is None
    print(combine4([6, 6, 5, 2], 36))


# vstupní funkce programu
if __name__ == '__main__':
    """vstupní bod programu, vyvolání testovací funkce"""
    test()