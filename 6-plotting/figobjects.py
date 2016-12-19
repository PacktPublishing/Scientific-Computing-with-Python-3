from matplotlib.pyplot import  *
from scipy import *


fig=figure(1)
ax=subplot(111)
x=linspace(0,2*pi,1000)
ax.plot(x,sin(x),label='sin')
amod_sin=lambda x: (1.-0.1*sin(25*x))*sin(x)
ax.plot(x,amod_sin(x),label='modsin')

savefig('amp_mod_sin0.pdf',transparent=True,bbox_inches='tight')

for il,line in enumerate(ax.lines):
    if line.get_label() == 'sin':
       break
ax.lines[il].set_linestyle('-.')
ax.lines[il].set_linewidth(2)


ydata=ax.lines[il].get_ydata()
ydata[-1]=-0.5
ax.lines[il].set_ydata(ydata)


savefig('amp_mod_sin1.pdf',transparent=True,bbox_inches='tight')

annot1=ax.annotate('amplitude modulated\n curve', (2.1,1.0),(3.8,0.5),
arrowprops={'width':2,'color':'k', 'connectionstyle':'arc3,rad=+0.5', 'shrink':0.05},
verticalalignment='bottom', horizontalalignment='left',fontsize=15, 
bbox={'facecolor':'gray', 'alpha':0.1, 'pad':10})
annot2=ax.annotate('corrupted data', (6.3,-0.5),(6.1,-1.1),arrowprops={'width':0.5,'color':'k','shrink':0.1},
horizontalalignment='center', fontsize=12)


axf=ax.fill_between(x, sin(x), amod_sin(x),facecolor='gray')

savefig('amp_mod_sin2.pdf',transparent=True, bbox_inches='tight')

axf.remove()

axf=ax.fill_between(x, sin(x), amod_sin(x), where= amod_sin(x)-sin(x) > 0,facecolor='gray')

savefig('amp_mod_sin3.pdf',transparent=True, bbox_inches='tight')

ax.set_xticks(array([0,pi/2,pi,3/2*pi,2*pi]))
ax.set_xticklabels(('$0$','$\pi/2$','$\pi$','$3/2 \pi$','$2 \pi$'),fontsize=18)
ax.set_yticks(array([-1.,0.,1]))
ax.set_yticklabels(('$-1$','$0$','$1$'),fontsize=18)

savefig('amp_mod_sin4.pdf',transparent=True,bbox_inches='tight')
