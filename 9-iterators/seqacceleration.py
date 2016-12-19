from matplotlib.pyplot import *
import itertools

def Euler_accelerate(sequence):
        """
    Accelerate the iterator in the variable `sequence`.
        """
        s0 = next(sequence) # Si
        s1 = next(sequence) # Si+1
        s2 = next(sequence) # Si+2
        while True:
                yield s0 - ((s1 - s0)**2)/(s2 - 2*s1 + s0)
                s0, s1, s2 = s1, s2, next(sequence)
def pi_series():
        sum = 0.
        j = 1
        for i in itertools.cycle([1, -1]):
                yield sum
                sum += i/j
                j += 2
sna=array(list(itertools.islice(Euler_accelerate(pi_series()),30)))
snw=array(list(itertools.islice(pi_series(),30)))
plot(log10(abs(snw-pi/4)),label='not accelerated')
plot(log10(abs(sna-pi/4)),label='accelerated',linewidth=3)
legend()
grid()
ylabel('$\log_{10}(|S_N - \pi/4|)$',fontsize=18)
xlabel('N',fontsize=18)
