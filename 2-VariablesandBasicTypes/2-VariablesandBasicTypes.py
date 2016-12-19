
# coding: utf-8

# # 2-Variables and Basic Types
# 
# 
# Always run this statement first, when working with this book:

# In[1]:

from scipy import *
from matplotlib.pyplot import *
get_ipython().magic('matplotlib inline')
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# ## Variables

# In[2]:

a = 1 
diameter = 3.
height = 5.
cylinder = [diameter, height] # reference to a list


# In[3]:

a = b = c = 1
a


# In[4]:

a = 1
a = a + 1 # a gets the value 2
a
a = 3 * a
a


# In[5]:

a = 1
a += 1 # same as a = a + 1
a
a *= 3 # same as a = 3 * a
a


# ## Numeric Types
# 
# ### Integers

# In[6]:

6 // 2  # 3

7 // 2  # 3

7 / 2   # 3.5 


# ### Floating Point Numbers

# In[7]:

0.4 - 0.3 # returns 0.10000000000000003

0.4 - 0.3 == 0.1  # returns False 


# ####  Infinite and Not a Number

# In[8]:

exp(1000.)  #  inf

a = inf

3 - a       # -inf

3 + a       #  inf


# In[9]:

a+a  # inf

a-a  # nan

a/a  # nan


# In[10]:

x = nan 

x < 0 # False

x > 0 # False

x == x # False


# In[11]:

0 < inf     # True 
inf <= inf  # True 
inf == inf  # True 
-inf < inf  # True 
inf - inf   # nan 
exp(-inf)   # 0 
exp(1 / inf)  # 1


# In[12]:

seterr(all = 'raise')


# #### Underflow: Machine Epsilon

# In[13]:

import sys
sys.float_info.epsilon # 2.220446049250313e-16 (depending on your system)


# In[14]:

a = '1.356'
float(a)


# #### Other float types in NumPy

# In[15]:

a  = pi # returns   3.141592653589793
a

a1 = float64(a)  # returns   3.1415926535897931
a1

a2=float32(a)  # returns   3.1415927
a2

a - a1  # returns   0.0 
a - a2  # returns   -8.7422780126189537e-08


# In[16]:

f32 = finfo(float32) 
f32.precision   # 6 (decimal digits) 
f64 = finfo(float64) 
f64.precision   # 15 (decimal digits) 
f = finfo(float) 
f.precision     # 15 (decimal digits) 
f64.max         # 1.7976931348623157e+308 (largest number) 
f32.max         # 3.4028235e+38 (largest number) 
help(finfo)     # Check for more options


# ### Complex Numbers

# In[17]:

b = 5.2 
z = bj   # returns a NameError 


# In[19]:

z = b*j  # returns a NameError


# In[20]:

z = b*1j # is correct
z


# In[21]:

z = 3.2 + 5.2j 
z.conjugate() # returns (3.2-5.2j)


# #### Real and Imaginary Parts

# In[22]:

z = 1j 
z.real       # 0.0 
z.imag       # 1.0 
z.imag = 2   # AttributeError: readonly attribute


# In[23]:

z = 1 + 0j 
z == 1     # True 
float(z)   # TypeError


# In[24]:

import matplotlib.pyplot as plt
N = 10
# the following vector contains the Nth roots of unity: 
unity_roots = array([exp(1j*2*pi*k/N) for k in range(N)])
# access all the real or imaginary parts with real or imag:
axes(aspect='equal')
plot(unity_roots.real, unity_roots.imag, 'o')
allclose(unity_roots**N, 1) # True


# In[25]:

z = 3.2+5.2j 
(z + z.conjugate()) / 2.   # returns (3.2+0j) 
((z + z.conjugate()) / 2.).real   # returns 3.2 
(z - z.conjugate()) / 2.   # returns 5.2j 
((z - z.conjugate()) / 2.).imag   # returns 5.2 
sqrt(z * z.conjugate())   # returns (6.1057350089894991+0j)


# ## Booleans

# In[26]:

a = True
a
b = 30>45  # b gets the value False
b


# In[27]:

x=3
if x>0:
   print("positive")
else:
   print("nonpositive")


# ### Boolean Operators

# In[28]:

True and False # False
False or True # True
(30 > 45) or (27 < 30) # True
not True # False
not (3 > 4) # True


# In[29]:

a=3; b=4; c=-1

a < b < c # same as: a < b and b < c

a == b == c # same as: a == b and b == c


# ### Boolean Casting

# In[30]:

bool([])   # False 
bool(0)   # False 
bool(' ')   # True 
bool('')   # False 
bool('hello')   # True 
bool(1.2)   # True 
bool(array([1]))   # True 
bool(array([1,2]))   # Exception raised!


# #### Automatic Boolean Casting

# In[31]:

if a:
   print('Im here')
if bool(a): # exactly the same as above
   print('Im there')


# In[32]:

L=[]
if L:
    print("list not empty")
else:
    print("list is empty")


# In[33]:

n=23
if n % 2:
    print("n is odd")
else:
    print("n is even")


# #### Return values of and and or

# In[34]:

def and_as_function(x,y):
    if not x:
        return x
    else:
        return y
    
and_as_function(True,False)


# In[35]:

def or_as_function(x,y):
    if x:
        return x
    else:
        return y
    
or_as_function(True,False)


# In[36]:

True or x_not_defined
False and x_not_defined


# In[37]:

[1] or 'a' # produces [1]
'a' or [1] # produces 'a'


# ### Booleans and Integers

# In[38]:

def print_ispositive(x):
    possibilities=['nonpositive', 'positive']
    return "x is {}".format(possibilities[x>0])

print_ispositive(-23)
print_ispositive(7)


# In[39]:

True+13
2*True+5


# ## Strings

# In[40]:

name = 'Johan Carlsson'
child = "Åsa is Johan Carlsson's daughter"
book = """Aunt Julia 
and the Scriptwriter""" 

print(name) 
print(child) 
print(book)


# In[41]:

book[-1] # returns 'r'

book[-12:] # returns 'Scriptwriter'


# In[42]:

book[1]='a'  # returns TypeError


# In[43]:

print('Temperature:\t20\tC\nPressure:\t5\tPa')


# In[44]:

a="""
A multiline
example"""
a # returns '\nA multiline\nexample'


# In[45]:

latexfontsize="\\tiny"
print(latexfontsize)


# In[46]:

latexfs=r"\tiny"  
latexfs             # returns "\\tiny"
latexfontsize == latexfs  # returns True


# In[47]:

r"\""   # returns  '\\"'
r"\\"   # returns  '\\\\'


# In[48]:

r"\"    # returns an error


# ### Operations on strings and string methods

# In[49]:

last_name='Carlsson'
first_name='Johanna'
Full_name=first_name+' '+last_name  # returns 'Johanna Carlsson'

Full_name


# In[50]:

game=2*'Yo' # returns 'YoYo'
game


# In[51]:

'Anna' > 'Arvid' # returns false

'ANNA' < 'anna'  # returns true

'10B' < '11A' # returns true


# In[52]:

text = 'quod erat    demonstrandum'
text.split() # returns ['quod', 'erat', 'demonstrandum']
table = 'Johan;Carlsson;19890327'
table.split(';') # returns ['Johan','Carlsson','19890327']
king = 'CarlXVIGustaf'
king.split('XVI')  # returns ['Carl','Gustaf']


# In[53]:

sep=';'
sep.join(['Johan','Carlsson','19890327']) # returns 'Johan;Carlsson;19890327'


# In[54]:

birthday='20101210'
birthday.find('10') # returns 2 


# ### String Formatting

# In[55]:

course_code = "NUMA21"
print("This course's name is {}".format(course_code)) # This course's name is NUMA21


# In[56]:

quantity = 33.45
print("qty{:f}".format(quantity)) # qty33.450000
print("qty{:8.1f}".format(quantity)) # qty    33.5
print("qty{:10.2e}".format(quantity)) # qty  3.35e+01


# In[57]:

print("{name} {value:.1f}".format(name="quantity",value=quantity)) # "quantity 33.5"


# In[58]:

r"we {} in LaTeX \begin{{equation}}".format('like')

