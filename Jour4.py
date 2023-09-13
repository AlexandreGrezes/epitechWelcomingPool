#Task00
#Retourne True quand vrai False quand faux

#Task01
'''
if ( input("Ecrivez quelque chose : ") == 42):
    print("Correct Answer")
'''
#Task02
'''
if(int(input("Ecrivez un nombre : ")) % 2 == 0):
    print("This integer is even")
else:
    print("This integer is odd")
'''
#Task03
'''
a = input("Tapez une phrase pour ouvrir la porte : ")
if (a == "open sesame"):
    print("access granted")
if (a == "will you open, you goddamn !¤*@¡‘, display"):
    print("access fucking granted")
else:
    print("permission denied")
'''
#Task04
'''
a = int(input("Ecrivez un nombre : "))
if(a == 42 or a <= 21 or a % 2 == 2 or a / 2 < 21 or (a >= 45 and a % 2 == 1)):
    print("OK")
else:
    print("You got wrong my poor friend!")
'''
#Task05
'''
a = 42
b = 41
if a == b:
    print ("A and B are the same ")
if b <= a:
    print ("B is equal or lower than A")
if b != a:
    print ("B is different from A")
'''
#Task00
'''
for i in range (1, 1001):
    print(i)
'''

#Task01
'''
string = input("Ecrivez un mot : ")
a = len(string)
newString = ""

for i in range (0, a):
    newString += 2 * string[i]
    i+=1
print(newString)
'''
#Task02
'''
i = 10000
while i > 1: 
    if i % 7 == 0:
        print(i)
        i -= 7
    else:
        i-=1    
'''

#Task 03
'''
i = -30 
while i <= 30:
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
        i+=1
        pass
    if (i % 3 == 0):
        print("Fizz")
    if (i % 5 == 0):
        print("Buzz")
    else: 
        print(i)
    i+=1
'''
#Task 04
'''
i = 99
while i > 1:
    print(i, " bottles of age-appropriate beverage on the wall ", i, " bottles of age-appropriate beverage on the wall. Take one down, pass it around.")
    i -= 1
if (i == 1):
    print(i, " bottle of age-appropriate beverage on the wall ", i, " bottle of age-appropriate beverage on the wall. Take one down, pass it around.")
    i -= 1
'''
#Task05
'''
n = int(input("Ecrivez un nombre entier : "))

for i in range(2, (n//2)+1):
    multiples = ""
    temp = i
    while temp < n:
        multiples = str(temp) + " " + multiples
        temp += i
    print(multiples)    
'''
#Challenge
'''
integer = int(input("Ecrivez un nombre : "))
string = (input("Ecrivez un mot : "))

if (integer != 0):
    if (string.find("a" or"e" or "i" or "o" or "u")):
        print(integer)
    else:
        if (string.find("y")):
            print("y is not always a vowel in english, but here's your integer : ", integer)
        else:
            if (integer >= 42):
                print(integer)
else:
    print(string)
'''
#Task01


'''
def encrypt(string, int):
    i = 0
    newString = ""
    while i < len(string):
        if(string[i] == " "):
            i += 1
        temp = ord(string[i]) + int
        if (temp > 90):
            calc = temp - 90
            if (ord(string[i]) > 64 and ord(string[i]) < 91):
                temp = chr(65 + calc)
        if(temp > 122):
            calc = temp - 122       
            if (ord(string[i]) > 96 and ord(string[i]) < 123):
                temp = chr(97 + calc)
        if(temp.__class__ == i.__class__):
            temp = chr(temp)
        newString += temp
        i+=1
    string = newString
    print(string)


sentence = input("Write a sentence you like : ")
key = int(input("Choisissez un nombre qui n'est pas un multiple de 26 : "))

if (key > 25):
    print("Choisissez un nombre entre 0 et 25 s'il vous plait")
'''    

'''
def decrypt(string, int):
    i = 0
    newString = ""
    print(ord("u"))
    while i < len(string):
        if(string[i] == " "):
            i += 1
        temp = ord(string[i]) - int
        if (temp < 65):
            calc = 65 - temp
            if (ord(string[i]) > 65 and ord(string[i]) < 91):
                temp = chr(91 - calc)
        if(temp < 97):
            calc = 97 - temp        
            if (ord(string[i]) > 96 and ord(string[i]) < 123):
                temp = chr(122 - calc)
        if(temp.__class__ == i.__class__):
            temp = chr(temp)
        newString += temp
        i+=1
    string = newString
    print(string)

sentence = 'Ivuqvcy'
key = 7
decrypt(sentence, key)

'''

#Task02

from curses import keyname


def EncryptVigenere(text, key):
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = "abcdefighjklmnopqrstuvwxyz"
    i = 0
    j = 0
    keyNum = ord(key)
    keyNumFinal = keyNum - 65 # 12 
    encryptedText = " "  
    while i < len(text):
        textNum = ord(text[i])
        print(textNum)
        textNumFinal = textNum - 65 #C = 2
        almostNum = keyNumFinal + textNumFinal
        finalNum = almostNum % 26
        for j in range(0, len(ALPHABET)):
            print(ALPHABET[j])
            print(finalNum)
            if(text[i] == ALPHABET[j]):
                encryptedText += ALPHABET[finalNum]
                print(almostNum)
            elif(text[i] == alphabet[j]):
                encryptedText += alphabet[finalNum]
        i += 1
    text = encryptedText
    return''.join(text)

# C -> O  C = 2   O -> A  O = 14  U -> G U = 20  M = 12

def DecryptVigenere(text, key):
    
    print("Hello")



def main():
    while True:
        choice = input("Enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit: ").upper()

        if choice == 'Q':
            break

        if choice == 'E':
            originalText = input("Enter the text to encrypt: ")
            key = input("Enter the key letter : ")
            encryptedText = EncryptVigenere(originalText, key)
            print(f"Encrypted Text: {encryptedText}")
        elif choice == 'D':
            encryptedText = input("Enter the text to decrypt: ")
            key = input("Enter the key letter : ")
            decryptedText = decryptedText(encryptedText, key)
            print(f"Decrypted Text: {decryptedText}")
        else:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")

if __name__ == "__main__":
        main()
        


