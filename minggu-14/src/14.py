#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
from sklearn import kernel_approximation

rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype='float32')
X.dtype


# In[13]:


import numpy as np
from sklearn import kernel_approximation

transformer = kernel_approximation.RBFSampler()
X_new = transformer.fit_transform(X)
X_new.dtype


# In[19]:


from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)


# In[15]:


from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)


list(clf.predict(iris.data[:3]))


# In[20]:


from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)


list(clf.predict(iris.data[:3]))


clf.fit(iris.data, iris.target_names[iris.target])


# In[21]:


from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)


list(clf.predict(iris.data[:3]))


clf.fit(iris.data, iris.target_names[iris.target])

list(clf.predict(iris.data[:3]))


# In[22]:


from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)

clf.fit(digits.data[:-1], digits.target[:-1])


# In[8]:


from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)

clf.fit(digits.data[:-1], digits.target[:-1])

clf.predict(digits.data[-1:])


# In[23]:


# python
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

print(digits.data)

digits.target
# array([0, 1, 2, ..., 8, 9, 8]) (Output)

# Shape of the data arrays

digits.images[0]


# In[27]:


# python
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

digits.target


# In[26]:


# python
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

digits.images[0]


# In[28]:


from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer

X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]

classif = OneVsRestClassifier(estimator=SVC(random_state=0))
classif.fit(X, y).predict(X)


# In[29]:


from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer

X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]

y = LabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)


# In[6]:


from sklearn.preprocessing import MultiLabelBinarizer
y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)


# In[30]:


import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)

clf = SVC()
clf.set_params(kernel='linear').fit(X, y)
SVC(kernel='linear')
clf.predict(X[:5])


# In[31]:


import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)

clf.set_params(kernel='rbf').fit(X, y)
SVC()
clf.predict(X[:5])


# In[ ]:




