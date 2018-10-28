from visual import *
from visual.graph import *
import math
# Motor 400 RPM = 400/60 Hz omega=400/60*2pi
frequency=400.0/60
omega=frequency*2*pi
scene1 = gdisplay(x=0, y=0, width=1000, height=400, xtitle='t', ytitle='v', background=(0.2, 0.6, 0.2))
scene2 = gdisplay(x=0, y=400, width=1000, height=400, xtitle='t', ytitle='Voltage', background=(0.2, 0.6, 0.2))
p1 = gcurve(color=color.yellow, gdisplay = scene2)
p2 = gcurve(color=color.cyan, gdisplay = scene2)
p3 = gcurve(color=color.red, gdisplay = scene2)
p4 = gcurve(color=color.blue, gdisplay = scene2)
p5 = gcurve(color=color.black, gdisplay = scene2)
t=0
dt=1E-4
phi1=2.0/3*pi
#phi2=4.0/3*pi
phi2=-2.0/3*pi
t=0
while t*frequency<2:
    rate(2000)
    t+=dt
    V1=cos(omega*t)
    V2=cos(omega*t+phi1)
    V3=cos(omega*t+phi2)
#    V_final=V1+V2+V3
    V_final=V1-V2
    vmax=0
    if abs(V_final)>abs(vmax):
        vmax=abs(V_final)
 #   print "V1= ",V1
 #   print "V2= ",V2
 #   print "V3= ",V3
    Power=0
    Power+=abs(V_final)**2
    p1.plot(pos=(t,V1))#yellow  power consumed to rotate the magnet
    p2.plot(pos=(t,V2))#cyan       output power
    p3.plot(pos=(t,V3))
    p4.plot(pos=(t,V_final))
print "Average power at 120 = ",Power
print "Vmax at 120 = ",abs(vmax)