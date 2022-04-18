#!/usr/bin/env python
# coding: utf-8

# In[1]:


import reprlib


# In[2]:


reprlib.repr(set('supercalifragilisticexpialidocious'))


# In[3]:


import pprint


# In[4]:


t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
                                                        'yellow'], 'blue']]]


# In[5]:


pprint.pprint(t, width=30)


# In[6]:


import textwrap


# In[7]:


doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""


# In[8]:


print(textwrap.fill(doc, width=40))


# In[1]:


import locale


# In[2]:


locale.setlocale(locale.LC_ALL, 'English_United States.1252')


# In[3]:


conv = locale.localeconv()          # get a mapping of conventions


# In[4]:


x = 1234567.8
locale.format("%d", x, grouping=True)


# In[13]:


locale.format_string("%s%.*f", (conv['currency_symbol'],
                                conv['frac_digits'], x), grouping=True)


# In[14]:


from string import Template


# In[15]:


t = Template('${village}folk send $$10 to $cause.')


# In[16]:


t.substitute(village='Nottingham', cause='the ditch fund')


# In[18]:


t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t.substitute(d)


# In[19]:


t.safe_substitute(d)


# In[20]:


import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')


# In[21]:


t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))


# In[ ]:


import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()
    
start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header


# In[ ]:


import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')


# In[22]:


import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


# In[23]:


import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)


# In[24]:


a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']                # fetch the object if it is still alive


# In[25]:


del a                       # remove the one reference
gc.collect()                # run garbage collection right away


# In[26]:


d['primary']                # entry was automatically removed


# In[27]:


from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)


# In[28]:


a[1:3]


# In[29]:


from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())


# In[ ]:


unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)


# In[31]:


import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores


# In[32]:


from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
[heappop(data) for i in range(3)]  # fetch the three smallest entries


# In[33]:


from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)


# In[34]:


round(.70 * 1.05, 2)


# In[35]:


Decimal('1.00') % Decimal('.10')


# In[36]:


1.00 % 0.10


# In[37]:


sum([Decimal('0.1')]*10) == Decimal('1.0')


# In[38]:


sum([0.1]*10) == 1.0


# In[39]:


getcontext().prec = 36
Decimal(1) / Decimal(7)


# In[ ]:




