from math import *
from visual import *

RodWidth = 0.1
R= 1.0
SphereRadius= 0.2
theta_o=0.0
omega =1.0
dt=0.01
time=0.0

#intial setup of system
VerticalRod = cylinder(
    pos=(R*sin(theta_o), -R, 0),
    color=color.red,
    radius=RodWidth,
    axis=(0,2,0),
    opacity=0.6)
HorizontalRod= cylinder(
    pos=(-R, R*cos(theta_o), 0),
    color=color.red,
    radius=RodWidth,
    axis=(2,0,0),
    opacity=0.6)
Dot=sphere(
    pos=(R*sin(theta_o), R*cos(theta_o), 0),
    color=color.yellow,
    radius=SphereRadius,
    opacity=0.5)
Trace=curve(color=color.yellow)

scene.autoscale=False

while True:
    rate(100)
    time = time + dt
    #calculate x and y with respect to time
    x = R*sin(omega*time)
    y = R*cos(omega*time)
    VerticalRod.x=x
    HorizontalRod.y=y
    Dot.pos=(x,y,0)
    Trace.append(Dot.pos)
