
# coding: utf-8

# # 1-Getting Started
# 
# Always run this statement first, when working with this book:

# In[1]:

from scipy import *

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# ## Numbers

# In[2]:

2 ** (2 + 2)
1j ** 2 # A complex number
1. + 3.0j  # Another complex number


# ## Strings

# In[3]:

'valid string'

"string with double quotes"

"you shouldn't forget comments"

'these are double quotes: ".." '


# In[4]:

"""This is
 a long,
 long string"""


# ## Variables

# In[5]:

x = [3, 4] # a list object is created
y = x # this object now has two labels: x and y
del x # we delete one of the labels
del y # both labels are removed: the object is deleted


# In[6]:


x = [3, 4] # a list object is created
print(x)


# ## Lists

# In[7]:

L1 = [5, 6]

L1[0] # 5

L1[1] # 6

L1[2] # raises IndexError


# In[8]:

L2 = ['a', 1, [3, 4]]

L2[0] # 'a'

L2[2][0] # 3

L2[-1] # last element: [3,4]

L2[-2] # second to last: 1


# In[9]:

print(list(range(5)))


# In[10]:

len(['a', 1, 2, 34])


# In[11]:

L = ['a', 'b', 'c']
L[-1] # 'c'

L.append('d')
L # L is now ['a', 'b', 'c', 'd']

L[-1] # 'd'


# ### Operations on Lists

# In[12]:

L1 = [1, 2]
L2 = [3, 4]
L = L1 + L2 # [1, 2, 3, 4]
L


# In[13]:

L = [1, 2]
3 * L # [1, 2, 1, 2, 1, 2]


# ## Boolean Expressions

# In[14]:

2 >= 4  # False
2 < 3 < 4 # True
2 < 3 and 3 < 2 # False
2 != 3 < 4 or False # True
2 <= 2 and 2 >= 2 # True
not 2 == 3 # True
not False or True and False # True!


# ## Repeating statements by loops

# In[15]:

L = [1, 2, 10]
for s in L:
    print(s * 2) # output: 2 4 20


# ### Repeating a task

# In[16]:

n = 30
k=0
for iteration in range(n):
    k+= iteration #do_something(this gets executed n times)
k


# ### Break and else

# In[17]:

threshold=30
x_values=range(20)

for x in x_values:
    if x > threshold:
       break
print(x)


# In[18]:

for x in x_values:
    if x > threshold:
       break
else:
    print("all the x are below the threshold")


# ## Conditional Statements

# In[19]:

# The absolute value
x=-25

if x >= 0:
  print(x)
else:
  print(-x)


# ## Encapsulating code by functions
#  
# Example:
# $$x \mapsto f(x) := 2x + 1$$

# In[20]:

def f(x):
    return 2*x + 1


# Calling this function:

# In[21]:

f(2) # 5

f(1) # 3


# ## Scripts and modules

# In[22]:

def f(x):
  return 2*x + 1

z = []
for x in range(10):
  if f(x) > pi:
    z.append(x)
  else:
    z.append(-1)
print(z)


# In[23]:

exec(open('smartscript.py').read())
get_ipython().magic('run smartscript')


# ## Simple modules - collecting Functions
# 
# For the next example to work, you need a file `smartfunctions.py`in the same folder as this notebook: 

# In[24]:

def f(x):
    return 2*x + 1
def g(x):
    return x**2 + 4*x - 5
def h(x):
    return 1/f(x)


# ### Using modules and namespaces

# In[25]:

import smartfunctions
print(smartfunctions.f(2))

from smartfunctions import g  #import just this one function
print(g(1))

from smartfunctions import * #import all
print(h(2)*f(2))


# ## Interpreter

# In[26]:

def f(x):
  return y**2
a = 3 # here both a and f are defined


# In[27]:

f(2) # error, y is not defined

