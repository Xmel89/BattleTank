import pygame

accel_but_d = False
accel_but_d_minus = False
caterpillar_r_f = False
caterpillar_l_f = False
caterpillar_r_u = False
caterpillar_l_u = False
turm_r_d = False
turm_l_d = False
turn_up = False
turn_down = False
shoot = None
def control(name):
    global support
    global accel_but_d
    global accel_but_d_minus
    global caterpillar_r_f
    global caterpillar_l_f
    global caterpillar_r_u
    global caterpillar_l_u
    global turm_r_d
    global turm_l_d
    global turn_up
    global turn_down
    global shoot
    for oneButton in pygame.event.get():

        if oneButton.type == pygame.KEYDOWN:
            if oneButton.key == pygame.K_ESCAPE:
                Start.done = False
            if oneButton.key == pygame.K_w:
                accel_but_d = True
                accel_but_u = False
            if oneButton.key == pygame.K_s:
                accel_but_d_minus = True
                accel_but_u_minus = False
            if oneButton.key == pygame.K_e:
                caterpillar_r_f = True
            if oneButton.key == pygame.K_q:
                caterpillar_l_f = True

            if oneButton.key == pygame.K_d:
                caterpillar_r_u = True

            if oneButton.key == pygame.K_a:
                caterpillar_l_u = True

            if oneButton.key == pygame.K_RIGHT:
                turm_r_d = True

            if oneButton.key == pygame.K_LEFT:
                turm_l_d = True

            if oneButton.key == pygame.K_DOWN:
                turn_down = True

            if oneButton.key == pygame.K_UP:
                turn_up = True

            if oneButton.key == pygame.K_SPACE:
                shoot = True


            '''if oneButton.key == pygame.K_r:
                print('caterpillar_r_f=', caterpillar_r_f, '\n'
                      'caterpillar_l_f=', caterpillar_l_f, '\n'
                      'caterpillar_r_u=', caterpillar_r_u, '\n'
                      'caterpillar_l_u=', caterpillar_l_u, '\n'
                      'x=', name.x, '\n'
                      'y=', name.y, '\n'
                      'angle=', name.angle, '\n'
                      'v=', name.v, '\n'''

                
        if oneButton.type == pygame.KEYUP:
            if oneButton.key == pygame.K_w:
                accel_but_d = False
                accel_but_u = True
            if oneButton.key == pygame.K_s:
                accel_but_d_minus = False
                accel_but_u_minus = True

            if oneButton.key == pygame.K_e:
                caterpillar_r_f = False

            if oneButton.key == pygame.K_q:
                caterpillar_l_f = False

            if oneButton.key == pygame.K_a:
                caterpillar_l_u = False
            if oneButton.key == pygame.K_d:
                caterpillar_r_u = False

            if oneButton.key == pygame.K_RIGHT:
                turm_r_d = False

            if oneButton.key == pygame.K_LEFT:
                turm_l_d = False

            if oneButton.key == pygame.K_DOWN:
                turn_down = False

            if oneButton.key == pygame.K_UP:
                turn_up = False

            if oneButton.key == pygame.K_SPACE:
                shoot = False

    return accel_but_d, accel_but_d_minus, caterpillar_r_f,\
           caterpillar_l_f, caterpillar_r_u, caterpillar_l_u,\
           turm_r_d, turm_l_d, turn_up, turn_down, shoot







