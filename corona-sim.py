import random
import time
import pygame
from pygame.locals import *
import matplotlib.pyplot as plt
pygame.init()
n = 0
FPS = 60
FramePerSec = pygame.time.Clock()
 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
DISPLAYSURF = pygame.display.set_mode((750,675))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Corona Simulation")
covdays = 240
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.seed = random.choice([0,1,1,1,1,1,1,1,1])
        self.image = pygame.image.load("/home/mylan/Dokumente/python/corona/blue_"+str(self.seed)+".png")
        self.surf = pygame.Surface((5, 5))
        self.rect = self.surf.get_rect()
        self.rect.top = random.randint(0,675)
        self.rect.left = random.randint(0,675)
        self.homex = int(self.rect.left/25)*25
        self.homey = int(self.rect.top/25)*25
        self.dayscorona = 0
        self.daysimmun = 0
        self.corona = False
        self.immun = False
        self.quaranteen = False

    def update(self):
        if self.quaranteen == True:
            pass
        elif self.seed == 0:
            self.rect.move_ip(random.choice([-25,0,25]),random.choice([-25,0,25]))
        else:
            self.rect.move_ip(random.randint(-25,25),random.randint(-25,25))
            if n%24 >= 20 and random.randint(0,int(corona14[21]/5)) == 1:
                self.rect.top = random.randint(0,500)
                self.rect.left = random.randint(0,500)
        if n % 24 >= 24-(corona14[21]+100)/20 and self.quaranteen == False:
            self.rect.top = self.homey
            self.rect.left = self.homex
        if self.quaranteen == False:
            if (self.rect.bottom > 675):
                self.rect.top = 675
            elif (self.rect.left > 675):
                self.rect.right = 675
            if (self.rect.bottom < 0):
                self.rect.top = 0
            elif (self.rect.left < 0):
                self.rect.right = 0
        if self.corona == True:
            self.dayscorona += 1
        if self.immun == True:
            self.daysimmun += 1
        if pygame.sprite.spritecollideany(self, infektziös) and self.immun == False and random.randint(0,int(corona14[1])) == 0:
            self.image = pygame.image.load("/home/mylan/Dokumente/python/corona/red_"+str(self.seed)+".png")
            corona.add(self)
            nüschts.remove(self)
            self.corona = True
        if self.dayscorona == 120:
            infektziös.add(self)
        if self.immun == True and self.daysimmun >= 2400 and random.randint(0,100) == 0:
            self.immun = False
            self.daysimmun = 0
            nüschts.add(self)
            immun.remove(self)
            self.image = pygame.image.load("/home/mylan/Dokumente/python/corona/blue_"+str(self.seed)+".png")
        if self.dayscorona >= 168 and random.randint(0, 5) == 0:
            self.rect.left = 725
            self.quaranteen = True
        if self.dayscorona >= covdays and random.randint(0,5) == 1:
            corona.remove(self)
            infektziös.remove(self)
            self.quaranteen = False
            if random.randint(0,2) != 1: 
                immun.add(self)
                self.immun = True
                self.image = pygame.image.load("/home/mylan/Dokumente/python/corona/green_"+str(self.seed)+".png")
            else:
                nüschts.add(self)
                self.image = pygame.image.load("/home/mylan/Dokumente/python/corona/blue_"+str(self.seed)+".png")
            self.corona = False
            self.dayscorona = 0
        if self.dayscorona >= covdays and random.randint(1,int(10*len(dots)/len(corona))) == 1:
            corona.remove(self)
            infektziös.remove(self)
            dots.remove(self)

        
    def draw(self, surface):
        surface.blit(self.image, self.rect)   

corona = pygame.sprite.Group()
dots = pygame.sprite.Group()
nüschts = pygame.sprite.Group()
immun = pygame.sprite.Group()
infektziös = pygame.sprite.Group()
for i in range(1):
    patient0 = Player()
    dots.add(patient0)
    corona.add(patient0)
    infektziös.add(patient0)
corona14 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
for i in range(0,5000):
    dots.add(Player())      
while True:
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
    for i in dots:        
        i.update()
    DISPLAYSURF.fill(WHITE)
    for i in dots:
        i.draw(DISPLAYSURF)
         
    pygame.display.update()
    if n % 24 == 0:
        corona14.insert(0,len(corona))
    if len(corona) == 0 or n % 480 == 0:        
        plt.plot(corona14)
        plt.show()
    print(str(corona14[0]/corona14[1])+"   "+str(len(corona))+"     "+str(5001-len(dots))+"    "+str(n))
    n += 1
    #time.sleep(0.15)
