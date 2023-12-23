import pygame, sys, math
PI = math.pi

pygame.init()

COLOR_BLACK =    pygame.Color(0, 0, 0)

sonya = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Zigzag art cinetic')

def zigzag (ecart):
    COLOR_CERCLE = (255, 255, 255)
    pygame.draw.arc(sonya, COLOR_CERCLE, (x + ecart, y + ecart, AXE, AXE), PI/4, 5*PI/4, 6)
    pygame.draw.arc(sonya, COLOR_CERCLE, (x + 150 - 41.535 - 6 + ecart, y - 150 + 41.535 + 6 + ecart, AXE, AXE), 5*PI/4, PI/4, 6)
    pygame.draw.arc(sonya, COLOR_CERCLE, (x - 150 + 41.535 + 6 + ecart, y + 150 - 41.535 - 6 + ecart, AXE, AXE), 5*PI/4, PI/4, 6)
    pygame.draw.arc(sonya, COLOR_CERCLE, (x + 300 - 83.07 - 12 + ecart, y - 300 + 83.07 + 12 + ecart, AXE, AXE), PI/4, 5*PI/4, 6)
    pygame.draw.arc(sonya, COLOR_CERCLE, (x - 300 + 83.07 + 12 + ecart, y + 300 - 83.07 - 12 + ecart, AXE, AXE), PI/4, 5*PI/4, 6)
    pygame.draw.arc(sonya, COLOR_CERCLE, (x + 450 - 124.605 - 18 + ecart, y - 450 + 124.605 + 18 + ecart, AXE, AXE), 5*PI/4, PI/4, 6)
    pygame.draw.arc(sonya, COLOR_CERCLE, (x - 450 + 124.604 + 18 + ecart, y + 450 - 124.605 - 18 + ecart, AXE, AXE), 5*PI/4, PI/4, 6)
    


clock = pygame.time.Clock()
x=0
y=0

while True:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
    sonya.fill(COLOR_BLACK)
    COLOR_CERCLE = (255, 255, 255)
    AXE = 150

    zigzag(-30)
    zigzag(0)
    zigzag(30)
    zigzag(60)
    zigzag(90)
    zigzag(120)
    zigzag(150)
    zigzag(180)
    zigzag(210)
    zigzag(240)
    zigzag(270)
    zigzag(300)
    zigzag(330)
    zigzag(360)
    zigzag(390)
    zigzag(420)
    zigzag(450)
    zigzag(480)
    zigzag(510)
    zigzag(540)
    zigzag(570)
    zigzag(600)
    x+=5
    y+=5
    if x == 30:
        x = 0
        y = 0

    pygame.display.update()
    
