import math
'''
n = 9
sum = 0
temp = 1
i = 0

while i < n:
    sum += temp
    i += 1
    temp = temp * 10 + 1
print(sum)

pui = int(input("Donnez une puissance"))
print(sum**pui)
'''
'''
max = 9
i = 1
s = 0
while i < max + 1 :
    s = s * 10
    s = s + i
    i += 1

print(s)
pui = int(input("Donnez une puissance : "))
result = s ** pui
print(result)
'''
'''
max = 10
i = 1
j = 1
s = 0
while i < max + 1 :
    s = s * 10
    if(max >= 10) and (i == 8):
        s = s + 9
        s = s * 10
        s += 0
        j = 1
        i += 2
        continue
    s = s + j
    j += 1
    i += 1

print(s)
pui = int(input("Donnez une puissance : "))
result = s ** pui
print(result)
'''

n = 16
sum = 0
temp = 1
i = 0


while i < n:
    sum += temp
    if (temp == 111111111):
        temp = 111111110
        pass
    temp = temp * 10 + 1
    i += 1
    print(temp)
    print(sum)



print(sum)

pui = int(input("Donnez une puissance"))
print(sum**pui)

'''
print(42/4)
print(42//4)
print((42//4)//4)
'''
'''
a = int(input("Saisir un nombre : "))
if (a % 2 == 0):
    print("Even")
else:    
    print("Odd")
'''    
'''
Suite = 44490320097
i = 0

while Suite > 0:
    i += Suite % 10
    Suite //= 10

print(i)
'''
'''
a = 12.24
print(int(a))
print(a - int(a))
'''
'''
a = int(input(""))
i = 1
j = 1
result = 0
while i <= a:
    if i % 2 == 0:
        result -= 4 / j
    else:
        result += 4 / j
    j += 2
    i += 1

print(result)
'''
'''
a = int(input("Combien de décimales de π voulez-vous voir : "))
i = 1
j = 1
result = 1

while i <= a:
    if i % 2 == 0:
        result += 1 / (2 * j + 1)
    else:
        result -= 1 / (2 * j + 1)
    j += 1
    i += 1
result *= 4

print(result)
'''
'''
a = int(input("Dividende : "))*
a1 = a
b = int(input("Diviseur : "))
b1 = b
pgcd = math.gcd(a, b)

if pgcd == 1:
    print("La fraction", a, "/", b, "n'est pas réductible.")
else:
    a = a // pgcd
    b = b // pgcd
    print("La fraction", a1, "/", b1, "peut être réduite en", a, "/", b)
'''