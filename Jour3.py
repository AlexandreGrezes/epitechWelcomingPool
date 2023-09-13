'''
print('')
print('exercice')
print('')
a = 'ABCdefGHIjkl'
print(a)

print('')
print('exercice')
print('')

for i in range(0 , 5):
    if(i == 0 or i == 4):
        print(a[i])

print('')
print('exercice')
print('')

print(a[len(a)-1])

print('')
print('exercice')
print('')
   
print(a[4:9])

print('')
print('exercice')
print('')

print(a.lower())

print('')
print('exercice')
print('')

a = 'tutu on the tuki-kata'

new_a =''

for i in range(0, len(a)):
    if(a[i] == 'u' and a[i-1] == 't'):
        new_a += 'a'
    else:
        new_a += a[i]
        
print(new_a)

print('')
print('exercice')
print('')

string = " hello world "
position = string . find ("a")
print ( position )
#Trouve la position du premier 'a' et retourne la position de celui-ci


print('')
print('exercice')
print('')
p = " abcdefghij "

print ( p [::-2]) #Prends tous les caractères en partant de la fin avec un pas de deux donc 'igeca'
print ( p [::-2][:5]) #Prends les 4 premiers caractères de p[::-2]
print ( p [::-2][:5][::-1]) #Inverse la chaîne p[::-2][:5]
print ( p [::-2][:5][::-1][3:]) #Prends les caractères à partir de la 4eme position de la chaine p p [::-2][:5][::-1]


print('')
print('exercice')
print('')
print(p[9:][:1]) #prends les 9 premiers caractères puis seulement le premier.


print('')
print('exercice')
print('')
print('hello'*10)


print('')
print('exercice')
print('')
s1 = "Hello "
s2 = '42' #Ajout des '' 
concat = s1 + s2
print ( concat )

print('')
print('exercice')
print('')

string1 = "42"
string2 = " is"
string3 = " the answer"
concat = string1 + string2 + string3
print (concat)
print(len(concat))


print('')
print('exercice')
print('')
sub = 'thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN'
string = sub.lower()
count = 0
cat = 'cat'
mice = 'mice'
garden = 'garden'

print(string)
for i in range(0, len(sub)):
    if(string[i] == 'c'):
        if((string[i] + string[i+1] + string[i+2] == cat) or (string[i] + string[i-1] + string[i-2] == cat)):
            count +=1
    if(string[i] == 'm'):
        if((string[i] + string[i+1] + string[i+2] + string[i+3] == mice) or (string[i] + string[i-1] + string[i-2] + string[i-3] == cat)):
            count +=1
    if(string[i] == 'g'):
        if((string[i] + string[i+1] + string[i+2] + string[i+3] + string[i+4] + string[i+5] == garden) or (string[i] + string[i-1] + string[i-2] + string[i-3] + string[i-4] + string[i-5] == garden)):
            count +=1
print(count)


print('')
print('exercice')
print('')
username = input('Hello, insert your username : ')
print('Hello', username.capitalize())


print('')
print('exercice')
print('')
num1 = int(input('Type one number : '))
num2 = int(input('Type a second one : '))
print('The sum of the two provided numbers is ', num1 + num2)


print('')
print('exercice')
print('')
wholeNum = input('Type one whole number : ')
print("L'entrée est de la classe ", wholeNum.__class__ )


print('')
print('exercice')
print('')
sentence = 'This is a test. Is it possible to fly? Good things come to those who never give up. '
newSentence = ''

for i in range(0, len(sentence)):
    if(i == 0):
        while sentence[i] != ' ':
            newSentence += sentence[i]
            i += 1
    if((sentence[i] == '.') or (sentence[i] == '?') and (i < len(sentence) - 2)):
        print(sentence[i])
        i += 2
        newSentence += ' '
        while sentence[i] != ' ':
            newSentence += sentence[i]
            i += 1

print(newSentence)


sentence = 'Bonjour1a1tous21je1suis1Albert1Nestor21le1castor31En1janvier1de1l4année1dernière21plus1de1dix5mille1personnes1m4ont1voués1un1culte31C4était1marrant21mais1un1peu1bizarre31En1tout1cas1plus1que1de1s4appeler1Albert1Nestor1en1étant1un1castor.'
length = len(sentence)
i = 0
count = 0

s1 = sentence.replace("1", " ")
s2 = s1.replace("2", ", ")
s3 = s2.replace("3", ". ")
s4 = s3.replace("4", "'")
s5 = s4.replace("5", "-")


while i < length:
    if((sentence[i] == 'c') and (sentence[i+1] == 'a') and (sentence[i+2] == 's') and (sentence[i+3] == 't') and (sentence[i+4] == 'o') and (sentence[i+5] == 'r')): 
        count += 1
        sentence[i].capitalize
    i += 1


print(count)
print(s5)

'''


from itertools import count


sentence = 'racecarbananaappleleveldeifiedcivicnoonradarrotorreferkayakmadamtenetwowbobpoppeepredderrepaperrotatorlevelerreviverredividerdetartratedmalayalam'
test = 'racecarbananaapplelevel'
length = len(sentence) + 1
testL = len(test)
print(length)


def findPalindromicSubstring(str):
    i = 0
    j = i + 1
    count = 0
    for i in range(0, length):
        for j in range(i + 1, length):
            if(j - i >= 2):              
                if(isPalindromic(str[i:j]) == True):
                    print(str[i:j])
                    count += 1
    print(count)

def isPalindromic(word):
    newWord = word
    newWord = newWord[::-1]
    if(word == newWord):
        return True

findPalindromicSubstring(sentence)

