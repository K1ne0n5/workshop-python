
# In[1]:


x = int(input("Please enter an integer "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else: 
    print('More')


# In[2]:


# Measure some strings:
    
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# In[3]:


# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


# In[4]:


for i in range(5):
    print(i)


# In[5]:


list(range(5, 10))


# In[6]:


list(range(0, 10, 3))


# In[7]:


list(range(-10, -100, -30))


# In[8]:


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


# In[9]:


range(10)


# In[10]:


sum(range(4))


# In[11]:


for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')


# In[12]:


for num in range(2, 10):
     if num % 2 == 0:
         print("Found an even number", num)
         continue
     print("Found an odd number", num)


# In[ ]:


while True:
    pass


# In[ ]:


class MyEmptyClass:
    pass


# In[ ]:


def initlog(*args):
    pass 


# In[ ]:


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


# In[ ]:


case 401 | 403 | 404:
    return "Not allowed"


# In[ ]:


# point is an (x, y) tuple
match Point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


# In[ ]:


class Point:
    x: int
    y: int

def where_is(Point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


# In[ ]:


match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")


# In[ ]:


match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")


# In[ ]:


from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")


# In[ ]:


def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()


# In[ ]:


fib

f = fib
f(100)


# In[ ]:


fib(0)
print(fib(0))


# In[ ]:


def fib2(n): 
     """Return a list containing the Fibonacci series up to n."""
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    # see below
         a, b = b, a+b
     return result

f100 = fib2(100)   
f100


# In[ ]:


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[ ]:


i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# In[ ]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[ ]:


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# In[ ]:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# In[ ]:


def function(a):
    pass
function(0, a = 0)


# In[ ]:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# In[ ]:


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# In[ ]:


def standard_arg(arg):
    print(arg)


# In[ ]:


def pos_only_arg(arg, /):
    print(arg)


# In[ ]:


def kwd_only_arg(*, arg):
    print(arg)


# In[ ]:


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# In[ ]:


standard_arg(2)


# In[ ]:


tandard_arg(arg=2)


# In[ ]:


pos_only_arg(1)


# In[ ]:


pos_only_arg(arg=1)


# In[ ]:


kwd_only_arg(3)


# In[ ]:


kwd_only_arg(arg=3)


# In[ ]:


combined_example(1, 2, 3)


# In[ ]:


combined_example(1, 2, kwd_only=3)


# In[ ]:


combined_example(1, standard=2, kwd_only=3)


# In[ ]:


combined_example(pos_only=1, standard=2, kwd_only=3)


# In[ ]:


def foo(name, **kwds):
    return 'name' in kwds


# In[ ]:


foo(1, **{'name': 2})


# In[ ]:


def foo(name, /, **kwds):
    return 'name' in kwds
    foo(1, **{'name': 2})
True


# In[ ]:


def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):


# In[ ]:


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# In[ ]:


def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")


# In[ ]:


list(range(3, 6))    


# In[ ]:


args = [3, 6]


# In[ ]:


list(range(*args)) 


# In[ ]:


def parrot(voltage, state='a stiff', action='voom'):
     print("-- This parrot wouldn't", action, end=' ')
     print("if you put", voltage, "volts through it.", end=' ')
     print("E's", state, "!")


# In[ ]:


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# In[ ]:


def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

f(1)


# In[ ]:


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs


# In[ ]:


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)


# In[ ]:


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
