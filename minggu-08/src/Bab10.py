#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os


# In[8]:


os.getcwd()      # Return the current working directory


# In[ ]:


os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system she


# In[3]:


import os


# In[4]:


dir(os)


# In[5]:


help(os)


# In[6]:


import shutil


# In[ ]:


shutil.copyfile('data.db', 'arichive.db')
shutil.move('/build/executables', 'installdir')


# In[8]:


import glob


# In[12]:


glob.glob('*.ipynb')


# In[3]:


import sys


# In[4]:


print(sys.argv)


# In[5]:


import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)


# In[6]:


sys.stderr.write('Warning, log file not found starting a new one\n')


# In[17]:


import re


# In[18]:


re.findall (r'\bf[a-z]*', 'which foot or hand fell fastest')


# In[19]:


re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')


# In[20]:


'tea for too'.replace('too', 'two')


# In[21]:


import math


# In[22]:


math.cos(math.pi / 4)


# In[23]:


math.log(1024, 2)


# In[24]:


import random


# In[25]:


random.choice(['apple', 'pear', 'banana'])


# In[26]:


random.sample(range(100), 10)   # sampling without replacement


# In[27]:


random.random()    # random float


# In[28]:


random.randrange(6)    # random integer chosen from range(6)


# In[29]:


import statistics


# In[30]:


data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)


# In[31]:


statistics.median(data)


# In[32]:


statistics.variance(data)


# In[33]:


from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline


# In[ ]:


import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                """To: jcaesar@example.org
                From: soothsayer@example.org
                Beware the Ides of March.
                """)
server.quit()


# In[35]:


# dates are easily constructed and formatted
from datetime import date
now = date.today()
now


# In[36]:


now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")


# In[37]:


# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days


# In[38]:


import zlib


# In[39]:


s = b'witch which has which witches wrist watch'
len(s)


# In[41]:


t = zlib.compress(s)
len(t)


# In[42]:


zlib.decompress(t)


# In[43]:


zlib.crc32(s)


# In[44]:


from timeit import Timer


# In[45]:


Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()


# In[46]:


Timer('a,b = b,a', 'a=1; b=2').timeit()


# In[47]:


def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests


# In[ ]:


import unittest

class TestStatisticalFunctions(unittest.TestCase):
    
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests

