from visual import *
ball = sphere(pos=(-5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=(-8,0,0), size=(0.2,12,12), color=color.green)
wallL = box(pos=(25,0,0), size=(0.2,12,12), color=color.green)

#start motion
ball.velocity = vector(25,1,0)
deltat = 0.005
t=0
vscale = 0.1
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.yellow)
ball.trail = curve(color=ball.color)
while t < 6:
    rate(100)
    ball.trail.append(pos=ball.pos)
    if ball.pos.x < wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
    elif ball.pos.x > wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
    #position update
    ball.pos = ball.pos + ball.velocity*deltat
    t = t + deltat
    
