# 1).
"""a=10
num=12
a=14
print(a+num+a)
"""""
# 2).
'''a='NavGurukul'
b=2016
c='main suru hua'

print(str(a))
print(b)
print(str(c))
'''
# 3).
'''a=75.0
print(complex(a))

'''
# 4).    
'''a=True
b=4
print(a+b)
print(type(a+b))'''

# 5).
'''a=10
b='sheetal'
c='vidhi'
d=20
c=24.7

print(a+d+'b')   # Type Error
print(float(b)+c) # Value Error
print('a'+b+c+'d'+str(c)) # type Error
print(a+d+c)
print(type(a+d+c))'''

# 6).
'''a='24.7'
b=float(a)
print(int(b))'''

# 7).
'''a='python'
b='is'
c='easy language'
print(a+'\t'+b+'\t'+c)'''

# 8).
'''
a=10
b='10'
print(a is b)'''

# 9)
'''1 or 0
1 and 0
0 or 1
0 and 1
'''
# 10).
'''
x=20
y=10
print(x+True+y-False)'''

#11).
"""x=20
y=30
z=20
print(not x==y) 
print(x>=y and y>=x)
print(not x is z)
print(x is not z)
print((x>=z) or (y<=z))
not ((x>=z)or(y<=z))"""

#12). 
"""a=['cherry','apple','banana','mango']
print('onion' in a)
print('apple' not in a)
"""

# 13).
'''a='sheetal'
b='vidhi'
a+=b
print(a)'''

# 14).1) if statement question
'''user=int(input('Enter number'))
if user%10==0 and user%3==0:
    print('yes')
else:
    print('No')    '''

# 14).2)
'''a=int(input('Enter number of a side'))
b=int(input('Enter number of b side'))
c=int(input('Enter numbner of c side'))
s=(a+b+c)/2
print('Area of triagle',s)      '''

#14).3)
"""a=int(input('Enter number of a'))
b=int(input('Enter number of b'))
c=int(input('Enter numbner of c'))

if a>b and a>c:
    print('A is greater',float(a))
elif b>a and b>c:
    print('B is greater',float(b))
elif c>a and c>b:
    print("c is greater",float(c))
            
"""


a=4
b=-7
a,b=b,a
print('a',a)
print('b',b)