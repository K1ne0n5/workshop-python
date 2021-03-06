#!/usr/bin/env python
# coding: utf-8

# In[ ]:


python3 -m venv tutorial-env


# In[ ]:


tutorial-env\Scripts\activate.bat


# In[ ]:


source tutorial-env/bin/activate


# In[ ]:


$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>


# In[ ]:


(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3


# In[ ]:


(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0


# In[ ]:


(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0


# In[ ]:


(tutorial-env) $ pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:


# In[ ]:


(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)


# In[ ]:


(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0


# In[ ]:


(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0


# In[ ]:


conda --version


# In[ ]:


conda update conda
Proceed ([y]/n)? y


# In[ ]:


conda create --name snowflakes biopython
Proceed ([y]/n)? y


# In[ ]:


conda info -e


# In[ ]:


conda create --name snakes python=3.9


# In[ ]:


conda activate snakes


# In[ ]:


conda activate snakes


# In[ ]:


conda info --envs


# In[ ]:


python --version


# In[ ]:


conda search beautifulsoup4


# In[ ]:


conda install beautifulsoup4


# In[ ]:


conda list


# In[ ]:




