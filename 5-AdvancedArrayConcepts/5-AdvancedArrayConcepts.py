
# coding: utf-8

# # 5-Advanced Array Concepts

# In[1]:

from scipy import *
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"    # toggle to: 'last_expr' or 'all'


# ## Array Views and Copies

# In[2]:

M = array([[1.,2.],[3.,4.]])
v = M[0,:] # first row of M
M
v


# In[3]:

v[-1] = 0.
v # array([[1.,0.]])
M # array([[1.,0.],[3.,4.]]) # M is modified as well


# In[4]:

v.base # array([[1.,0.],[3.,4.]])

v.base is M # True
M.base is None


# ### Slices as Views

# In[5]:

a = arange(4) # array([0.,1.,2.,3.])
b = a[[2,3]] # the index is a list [2,3]
b # array([2.,3.])


# In[6]:

print(b.base is None) # True, the data was copied
c = a[1:3]
c.base is None # False, this is just a view


# In[7]:

N = M[:] # this is a view of the whole array M
print(N.base is M)


# ### Transpose and Reshape as Views

# In[8]:

M = random.random_sample((3,3))
N = M.T
N.base is M # True


# In[9]:

v = arange(10)
C = v.reshape(-1,1) # column matrix
C.base is v # True


# ### Array Copy

# In[10]:

M = array([[1.,2.],[3.,4.]])
N = array(M.T) # copy of M.T
N.base is None


# ## Comparing Arrays

# In[11]:

A = array([0.,0.])
B = array([0.,0.])
if abs(B-A) < 1e-10: # an exception is raised here
    print("The two arrays are close enough")


# ### Boolean Arrays

# In[12]:

A = array([True,False]) # Boolean array
A.dtype # dtype('bool')


# In[13]:

M = array([[2, 3],
           [1, 4]])
M > 2 # array([[False, True],
      #        [False, True]])


# In[14]:

M == 0 # array([[False, False],
       #        [False, False]])


# In[15]:

N = array([[2, 3],
           [0, 0]])
M == N # array([[True, True],
       #        [False, False]])


# In[16]:

A = array([[1,2],[3,4]])
B = array([[1,2],[3,3]])
A == B # creates array([[True, True], [True, False]]) 
(A == B).all() # False
(A != B).any() # True
if (abs(B-A) < 1e-10).all():
    print("The two arrays are close enough")


# In[17]:

(A == B).all() # False


# In[18]:

(A != B).any() # True


# In[19]:

if (abs(B-A) < 1e-10).all(): 
    print("The two arrays are close enough")


# #### Checking for equality

# In[20]:

data = random.rand(2)*1e-3
small_error = random.rand(2)*1e-16
data == data + small_error # False
allclose(data, data + small_error, rtol=1.e-5, atol=1.e-8)   # True


# In[21]:

atol=1.e-6
rtol=1.e-4
(abs(A-B) < atol+rtol*abs(B)).all()


# In[22]:

data = 1e-3
error = 1e-16
data == data + error # False
allclose(data, data + error, rtol=1.e-5, atol=1.e-8)  #True


# ### Boolean Operations on arrays

# In[23]:

A = array([True, True, False, False])
B = array([True, False, True, False])
A and B # error!


# In[24]:

A & B # array([True, False, False, False])

A | B # array([True, True, True, False])

~A # array([False, False, True, True])


# In[25]:

data = linspace(1,100,100) # data
deviation = random.normal(size=100) # the deviations 
           #don't forget the parentheses in next statement!
exceptional = data[(deviation<-0.5)|(deviation>0.5)] 
exceptional = data[abs(deviation)>0.5] # same result 
small = data[(abs(deviation)<0.1)& (data <5.)] # small deviation and data #don't forget the parentheses!
exceptional
small


# ## Array Indexing
# ### Indexing with Boolean Arrays

# In[26]:

B = array([[True, False],
           [False, True]])
M = array([[2, 3],
           [1, 4]])
M[B] # array([2,4]), a vector


# In[27]:

M[B] = 0
M # [[0, 3], [1, 0]]


# In[28]:

M[B] = 10, 20
M # [[10, 3], [1, 20]]


# In[29]:

M[M>2] = 0
M


# ### Using `where`

# In[30]:

def H(x):
    return where(x < 0, 0, 1)
x = linspace(-1,1,11)  # [-1. -0.8 -0.6 -0.4 -0.2 0. 0.2 0.4 0.6 0.8 1. ]
print(H(x))            # [0 0 0 0 0 1 1 1 1 1 1]


# In[31]:

x = linspace(-4,4,5)   # [-4. -2. 0. 2. 4.]
print(where(x > 0, sqrt(x), 0))  # [ 0.+0.j 0.+0.j 0.+0.j 1.41421356+0.j 2.+0.j ] 
print(where(x > 0, 1, -1)) # [-1 -1 -1 1 1]


# In[32]:

a = arange(9)
b = a.reshape((3,3))
b


# In[33]:

print(where(a > 5)) # (array([6, 7, 8]),)


# In[34]:

print(where(b > 5)) # (array([2, 2, 2]), array([0, 1, 2]))


# ## Performance and Vectorization
# 
# ### What is slow in Python?

# In[35]:

def my_prod(a,b):
    val = 0
    for aa,bb in zip(a,b):
        val += aa*bb
    return val


# In[36]:

a=arange(3)
my_prod(a,-a)


# In[37]:

v = arange(1000)
w = empty_like(v)
for i in range(len(v)):
    w[i] = v[i] + 5


# In[38]:

w = v + 5


# In[39]:

def my_avg(A):
    m,n = A.shape
    B = A.copy()
    for i in range(1,m-1):
        for j in range(1,n-1):
            B[i,j] = (A[i-1,j] + A[i+1,j] + A[i,j-1] + A[i,j+1])/4
    return B


# In[40]:

def slicing_avg(A):
    A[1:-1,1:-1] = (A[:-2,1:-1] + A[2:,1:-1] + A[1:-1,:-2] + A[1:-1,2:])/4
    return A


# In[41]:

A = arange(20).reshape(4,-1)
allclose(my_avg(A), slicing_avg(A))


# In[42]:

def my_func(x):
    y = x**3 - 2*x + 5
    if y>0.5:
        return y-0.5
    else:
        return 0


# In[43]:

v=arange(10,dtype=float64)
for i in range(len(v)): 
    v[i] = my_func(v[i])
v


# In[44]:

my_vecfunc = vectorize(my_func)


# In[45]:

v=arange(10,dtype=float64)
v = my_vecfunc(v)
v


# ## Broadcasting

# In[46]:

vector = arange(4) # array([0.,1.,2.,3.])
vector + 1. # array([1.,2.,3.,4.])


# In[47]:

C = arange(2).reshape(-1,1) # column
R = arange(2).reshape(1,-1) # row
C + R # valid addition: array([[0.,1.],[1.,2.]])


# In[48]:

M = array([[11, 12, 13, 14], 
           [21, 22, 23, 24], 
           [31, 32, 33, 34]])
v = array([100, 200, 300, 400])
M + v


# #### Shape missmatch

# In[49]:

M = array([[11, 12, 13, 14], 
           [21, 22, 23, 24], 
           [31, 32, 33, 34]])
v = array([100, 200, 300])
M + v  # returns an error


# In[50]:

M + v.reshape(-1,1)


# #### Rescale Rows

# In[51]:

coeff = array([1,10,100])
rescaled = M*coeff.reshape(-1,1)
rescaled


# #### Rescale columns

# In[52]:

coeff = array([1,10,100,10000])
rescaled = M*coeff
rescaled


# In[53]:

rescaled = M*coeff.reshape(1,-1)
rescaled


# #### Functions of two variables

# In[54]:

u=arange(2)
v=arange(3)
W=u.reshape(-1,1)+v
W


# In[55]:

x=linspace(0,2*pi,5)
y=linspace(0,pi,3)
w=cos(x).reshape(-1,1)+sin(2*y)
w


# In[56]:

x,y = ogrid[0:1:3j,0:1:3j] # x,y are vectors with the contents of linspace(0,1,3)
w = cos(x) + sin(2*y)
w


# In[57]:

x,y = ogrid[0:1:3j, 0:1:3j]
print(x)
print(y)


# In[58]:

x,y = ogrid.__getitem__((slice(0, 1, 3j),slice(0, 1, 3j)))
print(x)
print(y)


# In[59]:

x,y = ogrid[0:1.5:.5, 0:1.5:.5]
print(x)
print(y)


# ## Sparse Matrices
# ### Compressed Sparse Row (CSR)

# In[60]:

import scipy.sparse as sp
A=array([[1,0,2,0],[0,0,0,0],[3.,0.,0.,0.],[1.,0.,0.,4.]])
AS=sp.csr_matrix(A)
AS.data # returns array([ 1.,  2.,  3.,  1.,  4.])


# In[61]:

AS.indptr # returns array([0, 2, 2, 3, 5])


# In[62]:

AS.indices # returns array([0, 2, 0, 0, 3])


# In[63]:

AS.nnz  # returns 5


# ### Compressed Sparse Column (CSC)

# In[64]:

import scipy.sparse as sp
A=array([[1,0,2,0],[0,0,0,0],[3.,0.,0.,0.],[1.,0.,0.,4.]])
AS=sp.csc_matrix(A)
AS.data # returns array([ 1.,  3.,  1.,  2.,  4.])


# In[65]:

AS.indptr # returns array([0, 3, 3, 4, 5])


# In[66]:

AS.indices # returns array([0, 2, 3, 0, 3])


# In[67]:

AS.nnz # returns 5


# ### Row--Based Linked List Format (LIL)

# In[68]:

import scipy.sparse as sp
A=array([[1,0,2,0],[0,0,0,0],[3.,0.,0.,0.],[1.,0.,0.,4.]])
AS=sp.lil_matrix(A)
AS.data # returns array([[1.0, 2.0], [], [3.0], [1.0, 4.0]], dtype=object)


# In[69]:

AS.rows # returns array([[0, 2], [], [0], [0, 3]], dtype=object)


# In[70]:

AS.nnz # returns 5


# #### Altering and Slicing matrices in LIL format

# In[71]:

BS=AS[1:3,0:2] 
BS.data # returns array([[], [3.0]], dtype=object)


# In[72]:

BS.rows # returns array([[], [0]], dtype=object)


# In[73]:

AS[0,1]=17
AS.data # returns array([[1.0, 17.0, 2.0], [], [3.0], [1.0, 4.0]], dtype=object)


# In[74]:

AS.rows # returns array([[0, 1, 2], [], [0], [0, 3]], dtype=object)


# In[75]:

AS.nnz # returns 6


# ### Generating Sparse Matrices

# In[76]:

import scipy.sparse as sp
sp.eye(20,20,format='lil')


# In[77]:

sp.spdiags(ones((20,)),0,20,20,format='csr')


# In[78]:

sp.identity(20,format='csc')


# In[79]:

AS=sp.rand(20,200,density=0.1,format='csr') 
AS.nnz # returns 400 


# In[80]:

import scipy.sparse as sp
Z=sp.csr_matrix((20,200))
Z.nnz


# ### Sparse Matrix Methods

# In[81]:

AS.toarray() # converts sparse formats to a numpy array


# In[82]:

AS.tocsr()


# In[83]:

AS.tocsc()


# In[84]:

AS.tolil()


# In[85]:

import scipy.sparse as sp
def sparse_sin(A):
   if not (sp.isspmatrix_csr(A) or sp.isspmatrix_csc(A)):
      A=A.tocsr()
   A.data=sin(A.data)
   return A
sparse_sin(AS)


# In[86]:

import scipy.sparse as sp
A=array([[1,0,2,0],[0,0,0,0],[3.,0.,0.,0.],[1.,0.,0.,4.]])
AS=sp.csr_matrix(A)
b=array([1,2,3,4])
c=AS.dot(b) # returns array([  7.,   0.,   3.,  17.])
c


# In[87]:

C=AS.dot(AS) # returns $4 \times 4$ csr_matrix
C


# In[88]:

d=dot(AS,b) # does not return the expected result!

