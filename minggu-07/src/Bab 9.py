#!/usr/bin/env python
# coding: utf-8

# In[1]:


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


# In[2]:


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


# In[3]:


x = MyClass()


# In[4]:


def __init__(self):
    self.data = []


# In[5]:


x = MyClass()


# In[6]:


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i


# In[7]:


x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


# In[ ]:


x.f()


# In[ ]:


xf = x.f
while True:
    print(xf())


# In[43]:


class Dog:

    kind = 'canine'         
    def __init__(self, name):
        self.name = name    

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  
>>> e.kind                  
'canine'
>>> d.name                 
'Fido'
>>> e.name                 
'Buddy'


# In[44]:


class Dog:

    tricks = []            

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over', 'play dead']


# In[45]:


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']


# In[18]:


class Warehouse:
        purpose = 'storage'
        region = 'west'


# In[19]:


w1 = Warehouse()
print(w1.purpose, w1.region)


# In[20]:


w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)


# In[21]:


def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


# In[24]:


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


# In[26]:


class Employee:
    pass

john = Employee()  


john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000


# In[27]:


for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')


# In[28]:


s = 'abc'
it = iter(s)
it


# In[29]:


next(it)


# In[30]:


next(it)


# In[31]:


next(it)


# In[32]:


next(it)


# In[33]:


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# In[34]:


rev = Reverse('spam')
iter(rev)


# In[35]:


for char in rev:
    print(char)


# In[36]:


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


# In[37]:


for char in reverse('golf'):
    print(char)


# In[38]:


sum(i*i for i in range(10))


# In[39]:


xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))


# In[40]:


unique_words = set(word for line in page  for word in line.split())


# In[41]:


valedictorian = max((student.gpa, student.name) for student in graduates)


# In[42]:


data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))


# In[ ]:




