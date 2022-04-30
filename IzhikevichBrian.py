
from brian2 import *
from brian2tools import *
import time


start_scope()
start=time.time()  # just for timing and benchmarking different solvers
N = 10
a = 0.02/ms;
b = 0.2/ms;
c=-65*mV
d=6*volt/second

# I=280*volt/second
vRandInit=-40  #the range of random values that you want for your initial voltage
noiseAmp=3 #how large you want your noise to be


eqs = '''dvm/dt = (0.04/ms/mV)*vm**2+(5/ms)*vm+140*mV/ms-w + I +  (noiseAmp*xi*ms**-.5)*mV: volt
         dw/dt = a*(b*vm-w) : volt/second
         I=20*volt/second : volt/second'''
G = NeuronGroup(N, eqs,
                    threshold='vm > 30*mV',
                    reset='vm = c; w=w+d',method='milstein')
G.vm='rand()*vRandInit*mV'


spikemon = SpikeMonitor(G)
statemon=StateMonitor(G, 'vm',record=range(1) )

run(500*ms)

end=time.time()
print("The time of execution of above program is :", end-start)


plot(spikemon.t/ms, spikemon.i, '.k')
xlabel('Time (ms)')
ylabel('Neuron index');
figure()
brian_plot(statemon)
