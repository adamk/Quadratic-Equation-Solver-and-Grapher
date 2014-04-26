# This is my Quadratic Formula program and more

import math, pygame
from pygame import *
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial",18)
def mymain():
    # global variables being used in other functions
    global a, b, c, Vx, Vy, d, x1, x2

    # input the a, b, and c vaules by the user
    print'What is the coefficient of x^2, a?'
    a = raw_input('>>> ')
    print'What is the coefficient of x, b?'
    b = raw_input('>>> ')
    print'What is the constant?'
    c = raw_input('>>> ')

    # change the input to real values
    a = float(a)
    b = float(b)
    c = float(c)

    # discriminant
    d = b**2-4*a*c

    # vertex of the parabola
    Vx = -b/(2*a)
    Vy = a*Vx**2+b*Vx+c

    print 'The symmetry line is at x = ', Vx
    print 'The vertex is at (',Vx,',',Vy,')'
    

    # testing the discriminant
    if d < 0:
        print 'The solution is imaginary.'
        print 'The discriminant is ',d
    else:
        # evaluate the quadratic formula 
        x1 = Vx + math.sqrt(d)/(2*a)
        x2 = Vx - math.sqrt(d)/(2*a)
        x1 = round(x1,2)
        x2 = round(x2,2)

        # print solution
        print "The 'x' intercepts are", x1,"and", x2
    GraphEq()
        
def GraphEq():
    # setup a window using the pygame library
    width,height = 500, 500
    screen = pygame.display.set_mode([width+400,height])
    pygame.display.set_caption('Quadratic Graph')
    screen.fill([255,255,255])
    
    # graph paper scale in k pixels per grid
    k = 10

    # draw graph paper
    for i in range(width/k):
        gridx = k*i
        gridy = k*i
        pygame.draw.line(screen, (100,50,240), (gridx, 0), (gridx, height), 1)
        pygame.draw.line(screen, (100,50,240), (0, gridy), (width, gridy), 1)

    # draw the x and y axis on the screen
    midx = (width/k)/2
    midy = (height/k)/2
    pygame.draw.line(screen, (0,0,0), (midx*k,0), (midx*k,height), 3)
    pygame.draw.line(screen, (0,0,0), (0,midy*k), (width, midy*k), 3)

    # graph the parabola across the width
    for i in range (width):
        x = (width/2 - i)/float(k)
        y = a*x**2+b*x+c
        pos1 =[width/2+x*k, height/2-y*k]
#        pygame.draw.circle(screen, (255,0,0), pos1, 3)
        nx = (width/2 - (i+1))/float(k)
        ny = a*nx**2+b*nx+c
        pos2 =[width/2+nx*k, height/2-ny*k]
        pygame.draw.line(screen, (255,0,0), pos1, pos2, 3)

# displaying the results symmetry line, vertex, and zeros
    symline = font.render("The line of symmetry is at x = "+str(Vx),1,(255,0,0))
    screen.blit(symline, (width+10, 20))
    instruct = font.render("Select 's' to graph the symmetry line.", 1, (200,0,0))
    screen.blit(instruct, (width+20, 45))
    
    vertex = font.render("The vertex is at ("+str(Vx)+","+str(Vy)+")",1,(0,255,0))
    screen.blit(vertex, (width+10, 75))
    instruct = font.render("Select 'v' to plot the vertex point.", 1, (0,200,0))
    screen.blit(instruct, (width+20, 100))
    if d<0:
        xint = font.render("The are no x-intercepts.",1,(0,0,255))
        screen.blit(xint, (width+10, 130))
        instruct = font.render("The discriminant is "+str(d), 1, (0,0,200))
        screen.blit(instruct, (width+20, 155))
    else:
        xint = font.render("The x-intercepts are at ("+str(x1)+",0) ("+str(x2)+", 0)",1,(0,0,255))
        screen.blit(xint, (width+10, 130))
        instruct = font.render("Select 'x' to plot the x-intercepts.", 1, (0,0,200))
        screen.blit(instruct, (width+20, 155))
    instruct = font.render("Select 'n' to show graph another parabola.", 1, (0,0,0))
    screen.blit(instruct, (width+10, height-30))
    
    # run an infinite loop to control the window
    active = True
    while active:
        # update the screen
        pygame.display.update()

        # keyboard and mouse actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == KEYDOWN:
                if event.key == K_s:
                    pygame.draw.line(screen, (200,0,0), (width/2+Vx*k,10),(width/2+Vx*k,height-10),3)
                if event.key == K_v:
                    pygame.draw.circle(screen, (0,200,0), (int(width/2+Vx*k),int(height/2-Vy*k)),4)
                if event.key == K_x:
                    if d<0:
                        instruct = font.render("The discriminant is "+str(d), 1, (250,0,0))
                        screen.blit(instruct, (width+20, 155))
                    else:
                        pygame.draw.circle(screen, (0,0,200), (int(width/2+x1*k),int(height/2)),4)
                        pygame.draw.circle(screen, (0,0,200), (int(width/2+x2*k),int(height/2)),4)
  
                if event.key == K_n:
                    mymain()
                
    # if exited from loop, then just quit
    pygame.quit()


    
        
    
if __name__=='__main__':
    mymain()
