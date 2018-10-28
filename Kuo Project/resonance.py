from visual import *
from visual.graph import *
N = 2
g = 9.8
b = 1.5
k = 1E6
theta = pi/9
rod_l, rod_r = 7.5*N, 0.5
string_l, string_r = 7.0, 0.1
ms = {'rod':3500.0,'bob':100.0}
pen_list = []
index = 0
t = 0.0
mu = 0.1
#en=False
tot_momentum=0.0
sum_momentum = 0.0
an_list=[]
def keyInput(evt):
    global index, en,tot_momentum
    if index < N:        
        pen_list[index].bob.pos = pen_list[index].string.pos + vector(-string_l*sin(theta),-string_l*cos(theta),0)
        pen_list[index].string.axis = pen_list[index].bob.pos - pen_list[index].string.pos
        index += 1
def spring_F(axis):
    return -k*(abs(axis) - string_l)*axis.norm()
def damp_F(x,v):
    return ms['bob']*(mu*(1-x**2)*v.x-x)*vector(1,0,0)
scene = display(width=800,height=800,background=(0.5,0.5,0),center=(0,0,0)) ##
scene1=gdisplay(x=800,width=800,height=300,xtitle="t",ytitle="angle",background=(0.5,0.5,0))
aa=gcurve(color=color.red,display=scene1)
bb=gcurve(color=color.cyan,display=scene1)
scene.bind('keydown', keyInput)###
rod = cylinder(radius=rod_r,pos=vector(-6.0,0,0),axis=vector(rod_l,0,0),material=materials.wood)
rod.v = vector(0,0,0)
scene.center=(2,-5,0)
class pendulum():
    def __init__(self):
        self.bob = sphere(radius=5*string_r,v=vector(0,0,0),material=materials.earth)
        self.string =cylinder(radius=0.5*string_r,pos=vector(0,0,0),axis=vector(0,-string_l,0))
    def set_pos(self,index):
        self.string.pos = rod.pos + vector(5.0*(index+1),0,0) 
        self.bob.pos = self.string.pos + self.string.axis
for i in range(N):
    pen_list.append(pendulum())
    pen_list[i].set_pos(i)
##red=sphere(radius=1,color=color.red,pos=vector(0,0,0))##
dt = 0.001
###
for i in range(2):
    an_list.append(asin((pen_list[i].bob.pos-pen_list[i].string.pos).x/abs(pen_list[i].bob.pos-pen_list[i].string.pos)))
while True:
    rate(10000)
    for i in range(N):
        if t != 0.0:
            pen_list[i].string.pos = rod.pos + vector((i+1)*5.0,0,0)
        a = (vector(0,-ms['bob']*g,0)+spring_F(pen_list[i].string.axis)+damp_F(pen_list[i].bob.pos.x-pen_list[i].string.pos.x,pen_list[i].bob.v))/ms['bob']
        pen_list[i].bob.v += a*dt 
        pen_list[i].bob.pos += pen_list[i].bob.v*dt
        pen_list[i].string.axis = pen_list[i].bob.pos - pen_list[i].string.pos
        sum_momentum += ms['bob']*pen_list[i].bob.v.x
#    if en:
    rod.v = vector(-sum_momentum/ms['rod'],0,0)###
    rod.pos += rod.v*dt
    sum_momentum = 0.0
    t += dt
#    scene.center+=vector(1E-4,0,0)
    for i in range(2):
        an_list[i]=asin((pen_list[i].bob.pos-pen_list[i].string.pos).x/abs(pen_list[i].bob.pos-pen_list[i].string.pos))
    aa.plot(pos=(t,an_list[0]))
    bb.plot(pos=(t,an_list[1]))