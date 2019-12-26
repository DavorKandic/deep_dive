from fractions import Fraction as Fr 
from sys import exit as ex

print('Welcome to simple fractions calculator!')
first = input('Enter first fraction: ')
op = input('Enter operation (+,-,/,*,**): ')
second = input ('Enter second fraction: ') 
one = Fr(first)
two = Fr(second)
if op == '+':
    res = one + two
elif op == '-':
    res = one - two
elif op == '/':
    res = one / two
elif op == '*':
    res = one * two
elif op == '**':
    res = Fr(str(round(one ** two, 3)))
    
else:
    print('Wrong input!')
    ex()
print(f'{one} {op} {two} = {res}')
