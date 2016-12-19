# See Hairer Wanner: Analysis by its history p. 65

def th52(x):
        fx=x
        k=1
        while True:
                yield fx
                fx=fx*(1-x**2/(k*pi)**2)
                k+=1
x=linspace(-1,3.5*pi,200)
it=th52(x)
for k in range(10):
    plot(x,next(it))
axis([-2,12,-5,5])
xlabel('x',fontsize=18)
ylabel('$P_k(x)$',fontsize=18)
xlabel('$x$',fontsize=18)
grid()
ax=gca()
ax.annotate('$k=5$',(8.6,3.4),(9.6,4.2),arrowprops=dict(facecolor='black', shrink=0.05, width=1),fontsize=18)
