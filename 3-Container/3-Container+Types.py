
# coding: utf-8

# # 3-Container Types

# In[1]:

from scipy import *
from matplotlib.pyplot import *
get_ipython().magic('matplotlib inline')
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# ## Lists

# In[2]:

L = ['a', 20.0, 5]
M = [3,['a', -3.0, 5]]
L
M

L[1] # returns 20.0

L[0] # returns 'a'

M[1] # returns ['a',-3.0,5]

M[1][2] # returns 5


# In[3]:

L=list(range(4)) # generates a list with four elements: [0, 1, 2 ,3]
L


# In[4]:

L=list(range(17,29,4)) # generates [17, 21, 25]
L

len(L) # returns 3


# ### Slicing

# In[5]:

L = ['C', 'l', 'o', 'u', 'd','s']
L[1:5] # remove one element and take three from there

L = ['C', 'l', 'o', 'u','d', 's']
L[1:] # ['l', 'o', 'u', 'd','s']

L[:5] # ['C', 'l', 'o','u','d']


L[-2:] # ['d', 's']


# In[6]:

L = list(range(4)) # [0, 1, 2, 3]
L[4] # IndexError: list index out of range


# In[7]:

L[1:100] # same as L[1:]


# In[8]:

L[-100:-1] # same as L[:-1]


# In[9]:

L[-100:100] # same as L[:]


# In[10]:

L[5:0] # empty list []


# In[11]:

L[-2:2] # empty list []


# In[12]:

L[1:100]


# In[13]:

a = [1,2,3]
for iteration in range(4):
    print(sum(a[0:iteration-1]))


# ### Strides

# In[14]:

L = list(range(100))
L[:10:2] # [0, 2, 4, 6, 8]


# In[15]:

L[::20] # [0, 20, 40, 60, 80]


# In[16]:

L[10:20:3] # [10, 13, 16, 19]


# In[17]:

L = [1, 2, 3]
R = L[::-1] # L is not modified
print(R)


# ### Altering Lists

# In[18]:

L = ['a', 1, 2, 3, 4]
L[2:3] = [] # ['a', 1, 3, 4]
L


# In[19]:

L[3:] = [] # ['a', 1, 3]
L


# In[20]:

L[1:1] = [1000, 2000] # ['a', 1000, 2000, 1, 3]
L


# In[21]:

L = [1, -17]
M = [-23.5, 18.3, 5.0]
L+M # gives [1, -17, 23.5, 18.3, 5.0]


# In[22]:

n = 3
n*[1.,17,3] # gives [1., 17, 3, 1., 17, 3, 1., 17, 3]


# In[23]:

[0]*5 # gives [0,0,0,0,0]


# ### Belonging to a list

# In[24]:

L = ['a', 1, 'b', 2]
'a' in L # True


# In[25]:

3 in L # False


# In[26]:

4 not in L # True


# ### List Methods

# In[27]:

L = [1, 2, 3]
L.reverse() # the list L is now reversed
L # [3, 2, 1]


# In[28]:

L=[3, 4, 4, 5]
newL = L.sort()
print(newL)


# In[29]:

L =  [0,1,2,3,4]
L.append(5)
L


# In[30]:

L.reverse()	
L


# In[31]:

L.sort()
L


# In[32]:

L.remove(0) # [1, 2, 3, 4, 5]
L


# In[33]:

L.pop() # [1, 2, 3, 4]
L


# In[34]:

L.pop() # [1, 2, 3, 4]
L


# In[35]:

L.extend(['a','b','c']) # [1, 2, 3, 'a', 'b', 'c']
L


# In[36]:

L.count(2)


# ### Merging Lists - `zip`

# In[37]:

ind = [0,1,2,3,4]
color = ["red", "green", "blue", "alpha"]
list(zip(color,ind))


# ### List Comprehension

# In[38]:

L = [2, 3, 10, 1, 5]

L2 = [x*2 for x in L] # [4, 6, 20, 2, 10]
L2


# In[39]:

L3 = [x*2 for x in L if 4 < x <= 10] # [20, 10]
L3


# In[40]:

M=[[1,2,3],[4,5,6]]
flat = [M[i][j] for i in range(2) for j in range(3)] # [1, 2, 3, 4, 5, 6]
flat


# ## Arrays

# In[41]:

v = array([1.,2.,3.])
v


# In[42]:

A = array([[1.,2.,3.],[4.,5.,6.]])
A


# In[43]:

v[2]   # returns 3.0


# In[44]:

A[1,2] # returns 6.0


# In[45]:

M = array([[1.,2.],[3.,4.]])
v = array([1., 2., 3.])
v[0] # 1.


# In[46]:

v[:2] # array([1.,2.])


# In[47]:

M[0,1] # 2.


# In[48]:

v[:2] = [10, 20] # v is now array([10., 20., 3.])


# ## Tuples

# In[49]:

my_tuple = 1, 2, 3 # our first tuple


# In[50]:

my_tuple = (1, 2, 3) # the same


# In[51]:

my_tuple = 1, 2, 3,  # again the same


# In[52]:

len(my_tuple) # 3, same as for lists


# In[53]:

my_tuple[0] = 'a' # error! tuples are immutable


# In[54]:

singleton = 1, # note the comma
len(singleton) # 1


# In[55]:

a, b = 0, 1 # a gets 0 and b gets 1
print(a)
print(b)


# In[56]:

a, b = [0, 1] # exactly the same effect


# In[57]:

(a, b) = 0, 1 # same


# In[58]:

[a,b] = [0,1] # same thing


# In[59]:

a, b = b, a
print(a)
print(b)


# In[60]:

1, 2 == 3, 4


# In[61]:

(1, 2) == (3, 4)


# ## Dictionaries
# 
# ### Creating and Altering Dictionaries

# In[62]:

truck_wheel = {'name':'wheel','mass':5.7,
               'Ix':20.0,'Iy':1.,'Iz':17.,
               'center of mass':[0.,0.,0.]}


# In[63]:

truck_wheel['name']


# In[64]:

truck_wheel['mass'] 


# In[65]:

truck_wheel['Ixy'] = 0.0


# In[66]:

truck_wheel = dict([('name','wheel'),('mass',5.7),
                     ('Ix',20.0),('Iy',1.),('Iz',17.),('center of mass',[0.,0.,0.])]) 
truck_wheel


# ### Looping over Dictionaries

# In[67]:

for key in truck_wheel.keys():
    print(key)


# In[68]:

for key in truck_wheel:
    print(key)


# In[69]:

for value in truck_wheel.values():
    print(value)


# In[70]:

for item in truck_wheel.items():
    print(item)


# ## Sets

# In[71]:

A = {1,2,3,4}
B = {5}


# In[72]:

C = A.union(B) # returns set([1,2,3,4,5])
C


# In[73]:

D = A.intersection(C) # returns set([1,2,3,4])
D


# In[74]:

E = C.difference(A)  # returns set([5])
E


# In[75]:

5 in C # returns True


# In[76]:

A = {1,2,3,3,3}
B = {1,2,3}
A == B # returns True


# In[77]:

A = {1,2,3}
B = {1,3,2}
A == B # returns True


# In[78]:

A={1,2,3,4}
A.union({5})


# In[79]:

A.intersection({2,4,6}) # returns set([2, 4])


# In[80]:

{2,4}.issubset({1,2,3,4,5})   # returns True


# In[81]:

{1,2,3,4,5}.issuperset({2,4}) # returns True


# In[82]:

empty_set=set([]) 


# ## Type checking

# In[83]:

label = 'local error'
type(label) # returns str


# In[84]:

x = [1, 2] # list
type(x) # returns list


# In[85]:

isinstance(x, list) # True


# In[86]:

test = True
isinstance(test, bool) # True


# In[87]:

isinstance(test, int) # True


# In[88]:

type(test) == int # False


# In[89]:

type(test) == bool # True


# In[90]:

if isinstance(test, int):
    print("The variable is an integer")

