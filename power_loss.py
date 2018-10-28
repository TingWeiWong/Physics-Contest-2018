from visual import *
from visual.graph import *
import math
# Motor 400 RPM = 400/60 Hz omega=400/60*2pi
frequency=400.0/60
R,Vm=1.08,200**0.5
omega=frequency*2*pi
scene1 = gdisplay(x=0, y=400, width=1000, height=400, xtitle='t', ytitle='Voltage', background=(0, 0, 0))
p1 = gcurve(color=color.yellow, gdisplay = scene1)
t=0
dt=0.01
phi1=2.0/3*pi
for i in range(5):
    phi2=-1.0/6*(i+2)*pi
    t=0
    while t*frequency<4:
        rate(20)
        t+=dt
        V1=Vm*cos(omega*t)
        V2=Vm*cos(omega*t+phi1)
        V3=Vm*cos(omega*t+phi2)
        V_final=V1+V2+V3
        V_loss=-V_final
        Power=0
        Power+=(V_loss)**2/R
        p1.plot(pos=(t,Power))
    print "Neutral loss at ",240-(i+2)*30,"degree = ",Power