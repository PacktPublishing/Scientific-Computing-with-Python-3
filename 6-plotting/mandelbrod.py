from matplotlib.pyplot import  *
from scipy import *

def mandelbrot(h,w, maxit=20):
    X,Y = meshgrid(linspace(-2, 0.8, w), linspace(-1.4, 1.4, h))
    c = X + Y*1j
    z = c
    exceeds = zeros(z.shape, dtype=bool)

    for iteration in range(maxit):
        z  = z**2 + c
        exceeded = abs(z) > 4
        exceeds_now = exceeded & (logical_not(exceeds))  
        exceeds[exceeds_now] = True        
        z[exceeded] = 2  # limit the values to avoid overflow
    return exceeds
fig1=figure(1)
ax=subplot(111)
ax.imshow(mandelbrot(400,400),cmap='gray')
ax.axis('off')
fig1.savefig('plotting_mandelbrot_gray.pdf',bbox_inches='tight',transparent=True)
fig2=figure(2)
ax1=subplot(121)
ax2=subplot(122)
ax1.imshow(mandelbrot(40,40),cmap='gray')
ax1.axis('off')
ax2.imshow(mandelbrot(40,40), interpolation='nearest', cmap='gray')
ax2.axis('off')
fig2.savefig('plotting_mandelbrot_small.pdf',bbox_inches='tight',transparent=True)
