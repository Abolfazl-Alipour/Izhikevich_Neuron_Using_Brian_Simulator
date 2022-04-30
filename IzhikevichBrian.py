
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


# you can change these parameters to get different behaviors:


# COMMENT
#         a        b       c      d       Iin
# ================================================================================
#       0.02      0.2     -65     6      14       % tonic spiking
#       0.02      0.25    -65     6       0.5     % phasic spiking
#       0.02      0.2     -50     2      15       % tonic bursting
#       0.02      0.25    -55     0.05    0.6     % phasic bursting
#       0.02      0.2     -55     4      10       % mixed mode
#       0.01      0.2     -65     8      30       % spike frequency adaptation
#       0.02     -0.1     -55     6       0       % Class 1
#       0.2       0.26    -65     0       0       % Class 2
#       0.02      0.2     -65     6       7       % spike latency
#       0.05      0.26    -60     0       0       % subthreshold oscillations
#       0.1       0.26    -60    -1       0       % resonator
#       0.02     -0.1     -55     6       0       % integrator
#       0.03      0.25    -60     4       0       % rebound spike
#       0.03      0.25    -52     0       0       % rebound burst
#       0.03      0.25    -60     4       0       % threshold variability
#       1         1.5     -60     0     -65       % bistability
#       1         0.2     -60   -21       0       % DAP
#       0.02      1       -55     4       0       % accomodation
#      -0.02     -1       -60     8      80       % inhibition-induced spiking
#      -0.026    -1       -45     0      80       % inhibition-induced bursting    
# ENDCOMMENT
