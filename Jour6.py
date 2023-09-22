
'''
#Task00
def f ( x ) :
    return 2 * x + 1
def g () :
    return 7
y = f (2)
#fais le calcul de la fonction donc print(y) retourne 5
print ( y )
y = f (5) + g ()
#fais le calcul de la fonction donc print(y) retourne 11 + 7 donc 19
print ( y )
'''
'''
#Task01
def bread() :
    print(" <////////// > ")
def lettuce() :
    print(" ~~~~~~~~~~~~ ")
def tomato() :
    print("O O O O O O")
def ham() :
    print(" ============ ")
'''
'''
i = 0
while(i  < 42 ):
    print(bread(), lettuce(), tomato(), ham(), ham(), bread())
    i+=1
print(i)
'''
'''

def nbSandwiches (number, noham):
    if number < 0:
        print("I can't do this.")
    else:
        i = 0
        if(noham != None):
            while i < number:
                print(bread(), lettuce(), tomato(), bread())
                i+=1
        else:
            while i < number:
                print(bread(), lettuce(), tomato(), ham(), ham(), bread())
                i+=1

nbSandwiches(3,None)
'''
'''
def powercalc (number, power):
    i = 1
    newNum = number
    while i < power:
        newNum = newNum * number
        i += 1
    print(newNum)

powercalc(42, 84)
'''
'''
def palindromic (string):
    print(string)
    newString = ''.join(x for x in string if x.isalnum())
    print(newString)
    if(newString.upper() == newString[::-1].upper()):
        print("It is palindromic")
    else: 
        print("It is not palindromic")

palindromic("Was it a car or a cat I saw?")
'''
'''
import os

def List(path):
    # List all files and directories in the current path
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            print("File:", item_path)
        elif os.path.isdir(item_path):
            print("Directory:", item_path)
            # Liste récursivement les items
            List(item_path)

# Start listing from the current directory
current_directory = os.getcwd()
List(current_directory)
'''
'''
✓ funA checks if s contains at least n lowercase letters;
✓ funB checks if s contains at least n uppercase letters;
✓ funC checks if s contains at least n characters;
✓ funD checks if s contains at least n special characters;
✓ funE checks if s contains at least n numbers.'''

def funA(string, n):
    i = 0
    count = 0
    while i < len(string):
        if(string[i] == string[i].lower() and string [i] == string[i].isalpha()):
            count += 1
        i += 1
    if(count >= n):
        return True
    else:
        return False


def funB( string, n):
    i = 0
    count = 0
    while i < len(string):
        if(string[i] == string[i].upper()):
            count += 1
        i += 1
    if(count >= n):
        return True
    else:
        return False


def funC(string, n):
    i = 0
    count = 0
    s = ''.join(x for x in string if x.isalnum())
    count = len(s)
    if(count >= n):
        return True
    else:
        return False

def funD(string, n):
    i = 0
    count = 0
    while i < len(string):
        if(string[i].isalnum()):
            {}
        else: 
            count += 1
        i += 1
    if(count >= n):
        return True
    else:
        return False


def funE(string, n):
    numbers = "0123456789"
    i = 0
    count = 0
    while i < len(string):
        if(string[i].isdigit()):
            count += 1
        i += 1
    if(count >= n):
        return True
    else:
        return False

'''
funA("BOnjour",4 ) #True
funA("BONJOUR",4 ) #False
funB("BOnjour",4 ) #False
funB("BONJOUR",4 ) #True
funC("BOn334566667ur",4 ) #True
funC("B1???5",4 ) #False
funD("BOnjoutur?",4 ) #False
funD("B1???!!/::5",4 ) #True
funE("BOnjoutur2R?", 4) #False
funE("B1d1g5f6f4", 4) #True
'''
from random import *


def correctPassword(rule, nb, string):
    alphabetLower = "abcdefghijklmnopqrstuvwxyz"
    alphaberUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetSpecial = ",?;.:/!\()[+-*/]"
    alphabetNumber = "0123456789"
    a = alphaberUpper
    b = a + alphabetLower
    c = b + alphabetSpecial
    d = c + alphabetNumber
    alphabetMix = d
    newString = string
    if(rule == "lower"):
        i = randint(0,25)
        print('ICI')
        newString += alphabetLower[i]
    if(rule == "upper"):
        i = randint(0,25)
        newString += alphaberUpper[i]
    if(rule == "special"):
        i = randint(0,15)
        newString += alphabetSpecial[i]
    if(rule == "number"):
        i = randint(0,9)
        newString += alphabetNumber[i]
    if(rule == "length"):
        i = randint(0,77)
        newString += alphabetMix[i]
    print(newString)
    checkpassword(rule, nb, newString)

def checkpassword (rule, nb, string):
    rules = ['lower', 'upper', 'length', 'special', 'number']
    cond = 'false'
    if (rule == 'lower'):
        if(funA(string, nb)):
            cond = 'true'
    elif (rule == 'upper'):
        if(funB(string, nb) == True):
            cond = 'true'
    elif(rule == 'length'):
        if(funC(string, nb) == True):
            cond = 'true'
    elif (rule == 'special'):
        if(funD(string, nb) == True):
            cond = 'true'
    elif (rule == 'number'):
        if(funE(string, nb) == True):
            cond = 'true'
    if(cond == 'true'):
        print('Mot de passe valide.')
    else:
        print("Mot de passe invalide, correction proposée.")
        correctPassword(rule, nb, string)

checkpassword("lower", 4, "FUAJFJAFJ189415/§/.?§/")


'''        
        x = randint(0,4)
        if rules[x] == 'length':
            y = randint(10,30)
        else:
            y = randint(2,5)
        print('Nouvel essai : ')
        print(rules[x], " ", y, " ", string)
        checkpassword(rules[x], y, string)
'''
'''
a = input("Choisissez un type de correction : 'lower', 'upper', 'length', 'special' or 'number' : ")
b = int(input("Choisissez un nombre (entre 10 et 20 pour length et 2 à 5 pour les autres recommandés : )"))
c = input("Ecrivez votre chaîne de caractère : ")
'''
