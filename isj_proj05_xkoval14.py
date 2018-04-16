#!/usr/bin/env python3

# @Author: Marek Kovalčík (xkoval14)

# Třída reprezentující polynom
class Polynomial:
    '''Třída reprezentující polynom'''

    # Redefinice funkce __init__ se zavolá při vytvoření polynomu a převede jej na seznam
    def __init__(self, *args, **kwargs):
        '''Polynom se převede na list'''

        self.args = args
        self.kwargs = kwargs
        self.values = list()

        if not len(args) == 0 and isinstance(args[0], list):
            self.values = args[0]

        elif not self.kwargs:
            for arg in self.args:
                self.values.append(arg)

        else:
            values = {index.replace('x', ''): kwargs[index] for index in kwargs.keys()}
            values = {int(key): int(value) for key, value in values.items()}

            maxkey = max(values.keys())

            for i in range(0, maxkey + 1):
                if not i in values.keys():
                    values[i] = 0

            for i in range(0, maxkey + 1):
                self.values.append(values[i])

            while self.values[-1] == 0 and not len(self.values) == 1:
                self.values.pop()


    # Přepsání metody __str__ obejektu
    def __str__(self):
        '''Převedení seznamu do tvaru např. 2x^3 - 3x + 1'''
        result = ""
        zero = True
        for i in self.values:
            if i != 0:
                zero = False
        if zero == True:
            return "0"

        revList = reversed(list(enumerate(self.values)))

        for index, value in revList:
            if index == 1:

                if result:
                    if value == 1:
                        result = result + " + x"
                    elif value == -1:
                        result = result + " - x"
                    elif value > 0:
                        result = result + " + " + str(value) + "x"
                    elif value < 0:
                        result = result + " - " + str(-value) + "x"
                    elif value == 0:
                        pass
                else:
                    if value == 1:
                        result = "x"
                    elif value == -1:
                        result = "- x"
                    elif value > 0:
                        result = str(value) + "x"
                    elif value < 0:
                        result = "- " + str(-value) + "x"
                    elif value == 0:
                        pass

            elif index == 0:

                if result:
                    if value > 0:
                        result = result + " + " + str(value)
                    elif value < 0:
                        result = result + " - " + str(-value)
                    elif value == 0:
                        pass
                else:
                    if value > 0:
                        result = str(value)
                    elif value < 0:
                        result = "- " + str(-value)
                    elif value == 0:
                        pass

            elif result:
                if value == 1:
                    result = result + " + x^" + str(index)
                elif value == -1:
                    result = result + " - x^" + str(index)
                elif value > 0:
                    result = result + " + " + str(value) + "x^" + str(index)
                elif value < 0:
                    result = result + " - " + str(-value) + "x^" + str(index)
                elif value == 0:
                    pass
            else:
                if value == 1:
                    result = "x^" + str(index)
                elif value == -1:
                    result = "- x^" + str(index)
                elif value > 0:
                    result = str(value) + "x^" + str(index)
                elif value < 0:
                    result = "- " + str(-value) + "x^" + str(index)
                elif value == 0:
                    pass

        return result

    # Redefinice funkce porovnávání vektorů
    def __eq__(self, druhy_vektor):
        '''Funkce vrátí True, jsou-li vektory shodné, jinak False'''
        return self.values == druhy_vektor.values

    # Redefinice funkce pro scítání polynomů
    def __add__(self, druhy_vektor):
        '''Funkce vrátí součet hodnot dvou polynomů'''
        vektor1Len = len(self.values)
        vektor2Len = len(druhy_vektor.values)
        values = list()

        # Funkce provede sečtení dvou vektorů
        def secti(prvni_vektor, druhy_vektor):
            '''sečtení vektorů'''
            result = list(x + y for x, y in zip(prvni_vektor, druhy_vektor))
            return result

        if vektor1Len == vektor2Len:
            values = secti(self.values, druhy_vektor.values)
        else:
            if vektor1Len > len(druhy_vektor.values):
                for i in range(len(druhy_vektor.values), vektor1Len):
                    druhy_vektor.values.append(int(0))
            else:
                for i in range(vektor1Len, vektor2Len):
                    self.values.append(int(0))
            values = secti(self.values, druhy_vektor.values)
        return Polynomial(values)


    # Redefinice metody __pow__ objektu
    # mocnina polynomu opakovaně volá násobení polynomu
    def __pow__(self, n):
        '''Funkce vrátí umocněný polynom na n'''

        # Funkce pro násobení polynomů
        def nasobPolynom(nasobenec, nasobitel):
            '''Funkce provede násobení polynomů'''
            resultNasobeni = [0] * (len(nasobenec) + len(nasobitel) - 1)

            for i in range(len(nasobenec)):
                tmp = nasobenec[i]
                for j in range(len(nasobitel)):
                    resultNasobeni[i + j] += tmp * nasobitel[j]
            return resultNasobeni

        value = [1]
        for k in range(n):
            value = nasobPolynom(value, self.values)

        return Polynomial(value)

    # Funkce pro derivaci polynomu
    def derivative(self):
        '''Derivace polynomu'''

        newValues = list()
        valuesLen = len(self.values);

        for i in range(1, valuesLen):
            newValues.append(i * self.values[i])

        return Polynomial(newValues)

    # Funkce vrátí hodnotu polynomu pro zadané x
    # je-li zadáné více parametrů, je výsledkem rozdíl mezi hodnotu 2. a 1. parametru
    # může sloužit pro výpočet určitého integrálu
    def at_value(self, *args):
        '''Funkce vrátí hodnotu polynomu por zadané x'''
        argsLen = len(args)
        valuesLen = len(self.values)
        result = 0.0
        # dva mezivýsledky pro připad zadání dvou argumentů
        vysledek1 = 0.0
        vysledek2 = 0.0

        # Je zadán pouze jeden argument pro zpracování
        if argsLen == 1:
            x = args[0]
            for i in range(0, valuesLen):
                result += self.values[i] * (x ** i)
            return result
        # jsou zadány dva argumenty
        elif argsLen == 2:
            x1 = args[0]
            x2 = args[1]

            for i in range(0, valuesLen):
                vysledek1 += self.values[i] * (x1 ** i)
            for i in range(0, valuesLen):
                vysledek2 += self.values[i] * (x2 ** i)
            result = vysledek2 - vysledek1
            return result


# Testovací funkce
def test():
    '''Funkce obsahuje asserty ze zadání'''
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

# Hlavní funkce programu
if __name__ == '__main__':
    '''Vyvolání testovací funkce na třídu Polynomial'''
    test()