#!/usr/bin/env python
# coding: utf-8

# In[2]:


import fibo

fibo.fib(1000)


# In[7]:


fibo.fib2(100)


# In[8]:


fibo.__name__


# In[4]:


fib = fibo.fib
fib(500)


# In[5]:


from fibo import fib, fib2
fib(500)


# In[6]:


from fibo import *
fib(500)


# In[7]:


import fibo as fib
fib.fib(500)


# In[1]:


from fibo import fib as fibonacci
fibonacci(500)


# In[ ]:


import fibo
if __name__ == "__main__":
    import sys
    fibo(int(sys.argv[1]))


# In[10]:


import sys

sys.ps1


# In[11]:


sys.ps2


# In[3]:


sys.ps1 = 'C> '


# In[4]:


import sys
sys.path.append('/ufs/guido/lib/python')


# In[17]:


import fibo, sys
dir(fibo)


# In[18]:


dir(sys)


# In[19]:


a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()


# In[20]:


import builtins
dir(builtins) 


# In[24]:


import sound.effects.echo

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)


# In[6]:


from sound.effects import echo

echo.echofilter(input, output, delay=0.7, atten=4)


# In[29]:


from sound.effects.echo import echofilter

echofilter(input, output, delay=0.7, atten=4)


# In[31]:


__all__ = ["echo", "surround", "reverse"]


# In[32]:


import sound.effects.echo
import sound.effects.surround
from sound.effects import *


# In[34]:


from . import echo
from .. import formats
from .. filters import equalizer


# In[ ]:




