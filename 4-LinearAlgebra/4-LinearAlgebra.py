
# coding: utf-8

# # 4-Linear Algebra

# In[1]:

from scipy import *
from scipy.linalg import *
from matplotlib.pyplot import *
get_ipython().magic('matplotlib inline')


# ## Overview
# 
# ### Vectors and Matrices

# In[2]:

v = array([1.,2.,3.])


# In[3]:

# two vectors with three components
v1 = array([1., 2., 3.]) 
v2 = array([2, 0, 1.]) 


# In[4]:

2*v1 # array([2., 4., 6.])


# In[5]:

v1/2 # array([0.5, 1., 1.5])


# In[6]:

# linear combinations
3*v1 #  array([ 3.,  6.,  9.])


# In[7]:

3*v1 + 2*v2  # array([  7.,   6.,  11.])


# In[8]:

# norm
norm(v1) #  3.7416573867739413


# In[9]:

# scalar product
dot(v1, v2) # 5.


# In[10]:

v1 @ v2  #  5 ; alternative formulation 


# In[11]:

# elementwise operations:
v1 * v2 # array([2., 0., 3.])


# In[12]:

v2 / v1 # array([2.,0.,.333333])


# In[13]:

v1 - v2 # array([-1.,  2.,  2.])


# In[14]:

v1 + v2 # array([ 3.,  2.,  4.])


# In[15]:

cos(v1) # cosine, elementwise: array([ 0.5403, -0.4161, -0.9899])


# In[16]:

M = array([[1.,2],[0.,1]])


# ### Indexing and Slices

# In[17]:

v = array([1.,2.,3])
M = array([[1.,2],[3.,4]])

v[0] # works as for lists


# In[18]:

v[1:] # array([2.,3.])


# In[19]:

M[0,0] # 1.


# In[20]:

M[1:] # returns the matrix array([[3.,4]])


# In[21]:

M[1] # returns the vector array([3.,4.])


# In[22]:

# access
v[0] # 1.


# In[23]:

v[0] = 10


# In[24]:

# slices
v[:2] # array([10., 2.])


# In[25]:

v[:2] = [0, 1] # now v == array([0.,1.,3.])
v


# In[26]:

v[:2] = [1,2,3] # error!


# ### Linear Algebra Operations

# In[27]:

v = array([1.,2.])
M = array([[1.,2],[3.,4]])
dot(M,v) # matrix vector multiplication; returns a vector


# In[28]:

M @ v # alternative formulation


# In[29]:

w = array([7.,0.])
dot(v,w) # scalar product; the result is a scalar


# In[30]:

v @ w # alternative formulation


# In[31]:

N = array([[3., 8.],[0., 1.]])
dot(M,N) # results in a matrix


# In[32]:

M @ N # alternative formulation


# #### Solving a Linear System

# In[33]:

import scipy.linalg as sl
A = array([[1., 2.], 
           [3., 4.]])
b = array([1., 4.])
x = sl.solve(A,b)


# In[34]:

allclose(dot(A, x), b) # True


# In[35]:

allclose(A @ x, b)  # alternative formulation


# ## Mathematical Preliminaries
# ### The dot operations

# In[36]:

angle = pi/3
M = array([[cos(angle), -sin(angle)], 
           [sin(angle), cos(angle)]])
v = array([1., 0.])
y = dot(M, v) 
y


# ## The Array Type
# ### Array Properties

# In[37]:

A=array([[1,2,3],[3,4,6]])
A.shape  # (2, 3)


# In[38]:

A.dtype  #  dtype('int64')


# In[39]:

A.strides    # (24, 8)


# ### Creating Arrays from Lists

# In[40]:

V = array([1., 2., 1.], dtype=float)
V


# In[41]:

V = array([1., 2., 1.], dtype=complex)
V


# In[42]:

V = array([1, 2]) # [1, 2] is a list of integers
V.dtype # int


# In[43]:

V = array([1., 2]) # [1., 2] mix float/integer
V.dtype # float


# In[44]:

V = array([1. + 0j, 2.]) # mix float/complex
V.dtype # complex


# In[45]:

a = array([1, 2, 3])
a[0] = 0.5 
a   # now: array([0, 2, 3])


# In[46]:

# the identity matrix in 2D
Id = array([[1., 0.], [0., 1.]])
# Python allows this:
Id = array([[1., 0.],
            [0., 1.]])
# which is more readable


# ### Vectors and Matrices

# In[47]:

v = array([1., 2., 1.])
shape(v)


# In[48]:

R = array([[1.,2.,1.]]) # notice the double brackets: this is a matrix
shape(R) # (1,3): this is a row matrix


# In[49]:

C = array([1.,2.,1.]).reshape(3,1)
shape(C) # (3,1): this is a column matrix


# ## Array Indexing
# ### Accessing Array Entries

# In[50]:

M = array([[1., 2.],[3.,4.]])
M[0,0] # first row, first column: 1.


# In[51]:

M[-1,0] # last row, first column: 3.


# In[52]:

v = array([1., 2., 3.])
v1 = v[:2] # v1 is array([1.,2.])
v1


# In[53]:

v1[0] = 0. # if v1 is changed ...
v1


# In[54]:

v #   ... v is changed too: array([0., 2., 3.])


# ### Altering an array using slices

# In[55]:

M = array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
shape(M)


# In[56]:

M[1,2] = 2.0 # scalar
M


# In[57]:

M[2,:] = [1.,2.,3.] # vector
M


# In[58]:

M[1:3,:] = array([[1.,2.,3.],[-1.,-2.,-3.]]) # matrix
M


# In[59]:

M[1:4,2:3] = array([[1.],[0.],[-1.0]]) # column matrix
M


# ## Functions to Construct Arrays

# In[60]:

identity(3)


# ## Accessing and Changing the Shape

# In[61]:

M = identity(3)
shape(M) # (3, 3)


# In[62]:

v = array([1., 2., 1., 4.])
shape(v) # (4,) <- singleton (1-tuple)


# In[63]:

M = array([[1.,2.]])
shape(M) # (1,2)


# In[64]:

M.shape # (1,2)


# In[65]:

shape(1.) # ()


# In[66]:

shape([1,2]) # (2,)


# In[67]:

shape([[1,2]]) # (1,2)


# ### Number of Dimensions

# In[68]:

A=rand(2,3)
ndim(A) # 2


# In[69]:

A.ndim


# In[70]:

T = zeros((2,2,3)) # tensor of shape (2,2,3); three dimensions
ndim(T) # 3


# In[71]:

len(shape(T)) # 3


# ### Reshape

# In[72]:

v = array([0,1,2,3,4,5])
M = v.reshape(2,3)
M


# In[73]:

shape(M)  # returns (2,3)


# In[74]:

M[0,0] = 10 # now v[0] is 10
v


# In[75]:

v = array([1,2,3,4,5,6,7,8])
M = v.reshape(2,-1)
shape(M)   # returns (2,4)


# In[76]:

M = v.reshape(-1,2)
shape(M)   # returns (4,2)


# In[77]:

M = v.reshape(3,-1) # returns error 


# ### Transpose

# In[78]:

A = rand(3,4)
shape(A) # 3,4


# In[79]:

B = A.T # A transpose
shape(B) # 4,3


# In[80]:

v = array([1.,2.,3.])
v.T # exactly the same vector!


# In[81]:

v.reshape(-1,1) # column matrix containing v


# In[82]:

v.reshape(1,-1) # row matrix containing v


# # Stacking
# 
# ### Stacking vectors

# In[83]:

# v is supposed to have an even length.
def symp(v):
  n = len(v) // 2 # use the integer division //
  return hstack([v[-n:], -v[:n]])
v = arange(1,5)
symp(v)


# # Functions Acting on Arrays
# 
# ## Universal Functions
# 
# ### Built-in Universal Functions

# In[84]:

cos(pi) # -1


# In[85]:

cos(array([[0, pi/2, pi]])) # array([[1, 0, -1]])


# In[86]:

2 * array([2, 4]) # array([4, 8])
array([1, 2]) * array([1, 8]) # array([1, 16])


# In[87]:

array([1, 2])**2 # array([1, 4])


# In[88]:

2**array([1, 2]) # array([1, 4])


# In[89]:

array([1, 2])**array([1, 2]) # array([1, 4])


# #### Create Universal Functions: `vectorize`

# In[90]:

def const(x):
    return 1
const(array([0, 2])) # returns 1 instead of array([1, 1])


# In[91]:

def heaviside(x):
    if x >= 0:
        return 1.
    else:
        return 0.
heaviside(array([-1, 2])) # error


# In[92]:

vheaviside = vectorize(heaviside)
vheaviside(array([-1,2])) # array([0,1]) as expected


# In[93]:

xvals=linspace(-1,1,100)
plot(xvals,vectorize(heaviside)(xvals))
axis([-1.5,1.5,-0.5,1.5])


# ### Array Functions: `axis` Argument

# In[94]:

A = arange(1,9).reshape((2,-1))
A


# In[95]:

sum(A) # 36


# In[96]:

sum(A, axis=0) # array([ 6,  8, 10, 12])


# In[97]:

A.sum(axis=1) # array([10, 26])


# ## Linear Algebra Methods in SciPy

# In[98]:

import scipy.linalg as sl
A = array([[1,2], [-6,4]])
[LU,piv] = sl.lu_factor(A)


# In[99]:

bi = array([1,1])
xi=sl.lu_solve((LU,piv),bi)
xi


# ### Solving a least squares problem with SVD

# In[100]:

import scipy.linalg as sl
A = array([[1, 2], [-6, 4], [0, 8]])
b = array([1,1,1])
[U1, Sigma_1, VT] = sl.svd(A, full_matrices = False, compute_uv = True)
xast = dot(VT.T, dot(U1.T, b)/ Sigma_1)
r = dot(A, xast) - b  # computes the residual
nr = sl.norm(r, 2)     # computes the Euclidean norm of the residual
nr

