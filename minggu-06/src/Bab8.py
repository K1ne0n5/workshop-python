#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True print('Hello world')


# In[2]:


print(10 * (1/0))
print(4 + spam*3)
print('2' + 2)


# In[3]:


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
         print("Oops!  That was no valid number.  Try again...")


# In[4]:


except (RuntimeError, TypeError, NameError):
    pass


# In[5]:


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


# In[6]:


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


# In[7]:


for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


# In[8]:


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)


# In[9]:


def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


# In[10]:


raise NameError('HiThere')


# In[11]:


raise ValueError  # shorthand for 'raise ValueError()'


# In[12]:


try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


# In[13]:


# exc must be exception instance or None.
raise RuntimeError from exc


# In[14]:


def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc


# In[15]:


try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None


# In[16]:


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


# In[17]:


def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())


# In[18]:


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")


# In[19]:


for line in open("myfile.txt"):
    print(line, end="")


# In[20]:


with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


# In[ ]:




