import math, Control, time

def phisics(name, nameTurm, Xmark, Shell):
    rotation = 0
    a = 0.05
    p = 0.05*name.v
    control = Control.control(name)
    accel_but_d = control[0]
    accel_but_d_minus = control[1]
    caterpillar_r_f = control[2]
    caterpillar_l_f = control[3]
    caterpillar_r_u = control[4]
    caterpillar_l_u = control[5]
    turm_r_d = control[6]
    turm_l_d = control[7]
    turn_up = control [8]
    turn_down = control [9]
    shoot = control [10]
    if name.angle >= 360:
        name.angle -= 360
    if name.angle < 0:
        name.angle += 360
    rad = name.angle * (math.pi / 180)
    rad_turm = nameTurm.angle * (math.pi / 180)
    cos_turm = math.cos(rad_turm)
    sin_turm = math.sin(rad_turm)
    rad_shell = Shell.angle * (math.pi / 180)
    cos_shell = math.cos(rad_shell)
    sin_shell = math.sin(rad_shell)
    cos = math.cos(rad)
    sin = math.sin(rad)
    tt = time.time()
    lenshoot = math.sqrt((Shell.x - nameTurm.x)**2 + (Shell.y - nameTurm.y)**2)

    if accel_but_d == True:         #gas +
        if rotation < 100:
            rotation += 0.1
        #print(rotation)
    if accel_but_d_minus == True:           #gas -
        if rotation > 0:
            rotation -= 0.1
        #print(rotation)

    if name.v > 0:
        name.x += (name.v * cos)
        name.y -= (name.v * sin)
        name.v -= p
    if name.v < 0:
        name.x += (name.v * cos)
        name.y -= (name.v * sin)
        name.v -= p

    if caterpillar_r_f == True and caterpillar_l_f == True:
        name.v += 1.5*a

    elif caterpillar_r_f == True:           #forward right caterpillar
        name.v += a
        name.angle += 0.4
        nameTurm.angle += 0.4

    elif caterpillar_l_f == True:           #forward left caterpillar
        name.v += a
        name.angle -= 0.4
        nameTurm.angle -= 0.4

    if caterpillar_r_u == True and caterpillar_l_u == True:
        name.v -= a

    elif caterpillar_r_u == True:           #forward right caterpillar
        name.v -= a*0.75
        name.angle -= 0.4
        nameTurm.angle -= 0.4

    elif caterpillar_l_u == True:           #forward left caterpillar
        name.v -= a*0.75
        name.angle += 0.4
        nameTurm.angle += 0.4

    if turm_r_d == True:           #right turm
        nameTurm.angle -= 0.4

    if turm_l_d == True:           #left turm
        nameTurm.angle += 0.4

    if turn_up == True:
        if Xmark.r < 800:
            Xmark.r += 5


    if turn_down == True:
        if Xmark.r > 70:
            Xmark.r -= 5

    Xmark.x = Xmark.r * cos_turm + nameTurm.x
    Xmark.y = -Xmark.r * sin_turm + nameTurm.y



    if shoot == None or tt - Shell.begtime > 3:
        Shell.v = 0
        Shell.angle = nameTurm.angle
        Shell.x = 55 * cos_turm + nameTurm.x
        Shell.y = -55 * sin_turm + nameTurm.y

    if shoot == True and ((tt - Shell.begtime) > 3):
        Shell.lenXmark = math.sqrt((Xmark.x - nameTurm.x)**2 + (Xmark.y - nameTurm.y)**2)
        Shell.begtime = tt
        Shell.v = 6

    #print(Shell.lenXmark, lenshoot)

    if Shell.v != 0:
        Shell.v -= 0.01
        Shell.x += (Shell.v * cos_shell)
        Shell.y -= (Shell.v * sin_shell)
        if lenshoot > Shell.lenXmark:
            Shell.v = 0