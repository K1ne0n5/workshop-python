#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)  # Mencari banana setelah memulai pencarian dari posisi 4
fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()


# In[2]:


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack

stack.pop()

stack

stack.pop()

stack.pop()

stack


# In[3]:


from collections import deque
queue = deque(["David Kim", "Mama Takata", "Travis Watanabe"])
queue.append("Daniel Choi")     # Memasukkan Daniel kedalam antrian
queue.append("Kyle Bang")       # Memasukkan Kyle kedalam antrian
queue.popleft()                 # Memindahkan data pertama

queue.popleft()                 # Memindahkan data kedua

queue                           # Menyusun kembali antrian berdasarkan data yang dimasukkan 


# In[4]:


squares = []
for x in range(4):
    squares.append(x**2)

squares

squares = list(map(lambda x: x**2, range(10)))

squares = [x**2 for x in range(10)]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs

vec = [-4, -2, 0, 2, 4]
# Membuat list baru dengan value berlipat
[x*2 for x in vec]

# Mem-filter daftar tidak termasuk bilangan negatif
[x for x in vec if x >= 0]

# Mengaplikasikan sebuah fungsi untuk semua elemen yang ada
[abs(x) for x in vec]

# Memanggil method dari elemen lain
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# Membuat sebuah list dari 2 tuple seperti nomer atau kotak
[(x, x**2) for x in range(6)]

# Sebuah tuple haruslah memiliki parenthesized atau tidak akan mengalami error
[x, x**2 for x in range(6)]




# Meratakan daftar menggunakan listcomp dengan dua seleksi for
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]


from math import pi
[str(round(pi, i)) for i in range(1, 6)]


# In[5]:


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed

list(zip(*matrix))


# In[6]:


t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v

empty = ()
singleton = 'Annyeonghaseo',    # <-- note trailing comma
len(empty)

len(singleton)

singleton

x, y, z = t


# In[7]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)          # Menampilkan duplikat setelah dipindahkan

'orange' in basket     # Menguji kecepatan membership

'crabgrass' in basket


# Mendemonstrasikan operasi set dengan unique letter dari dua kata

a = set('abracadabra')
b = set('alacazam')
a          # unique letters in a

a - b      # letters in a but not in b

a | b      # letters in a or b or both

a & b      # letters in both a and b

a ^ b      # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a


# In[8]:


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

{x: x**2 for x in (2, 4, 6)}

dict(sape=4139, guido=4127, jack=4098)


# In[9]:


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['Kevin Steward', 'patronous', 'black']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


for i in reversed(range(1, 10, 2)):
    print(i)


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data


# In[ ]:




