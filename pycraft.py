import pygame
from pygame import mixer
from time import sleep
mixer.init()
pygame.init()
print('''
loading...''')
def load(s):
    return pygame.transform.scale(pygame.image.load(s+'.png'), (l.teps, l.teps))
def sload(s):
    return pygame.transform.scale(pygame.image.load(s+'.png'), (20*l.teps, 20*l.teps))
class l:
    evel=[
          '111111111111111111000000000000010000111111111110000000011111111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '011111111111111110000000000000120000011111111100000000000012000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '000212121212121200000000022222220000000111110000000000000000000000000000000000011111100000000000000000000000000000011111111111000000111111111111000000022200000222222222222000000000000000000000000000000011000000000000000000000000000000000000',
          '000002222222220000000000000222000000000001000000000000000000000000011111111000002222000001122220000222221100000000022222222222000000000000200000000000000000000000000000000000111100222222222200000110000011000000000000000000000000000000011111',
          '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110000011000011000111111100000011111111111111',
          '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',]
    teps=30
    ock_x=[]
    ock_y=[]
    leng=120
class i:
    back=[sload('cool'), sload('books_b')]
    images=[[load('air'), load('grass'), load('stone')], [load('air'), load('books'), load('books')]]
    seec=[load('dirt'), load('books')]
class song:
    def play(music, vol=0.7):
        mixer.music.set_volume(vol)
        mixer.music.play()
    def stop():
        mixer.music.stop()
screen=pygame.display.set_mode((l.teps*20, l.teps*20))

class pac():

    def __init__(self):
        self.x=0
        self.y= -340
        self.image=[load('player')]
        self.i=0
        self.speed=l.teps
        self.y_s=0
        self.i_x=9
        self.jump=True
    def move(self, x, y):
        self.x+=x
        self.y+=y
        if bool(x):
            if x > -1:
                self.i_x += 1
            else:
                self.i_x += -1
    def get(self):
        return [self.x, self.y, self.x+l.teps, self.y]

    
    def find_pos(self, some):
        g=[]
        for i in l.evel:
            g.append(i[some])
        k = find_h(g)
        return k


        
    def cols(self):
        '''0=left
1=right
2=up
3=down'''
        i=0
        h=[False]*4
        lx=l.ock_x
        ly=l.ock_y
        for zx in lx:
            if not h[3]:
                h[3]=self.get()[3] >= (l.teps*self.find_pos(self.i_x))
            if not h[1]:
                h[1]=self.find_pos(self.i_x+1)<self.find_pos(self.i_x) and not self.jump
            if not h[0]:
                h[0]=self.find_pos(self.i_x-1)<self.find_pos(self.i_x) and not self.jump
            i+=1
        return h
    def next(self):
        self.i+=1
        if self.i>len(self.image)-1:
            self.i=0
    def update(self):
        keys=pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] and not self.cols()[0]) and not self.y> -160:
            self.move(-self.speed, 0)
        if (keys[pygame.K_RIGHT] and not self.cols()[1]) and not self.y> -160:
            self.move(self.speed, 0)
        if keys[pygame.K_UP] and not self.jump:
            self.jump=True
            self.y_s= -10
        self.move(0, self.y_s)
        while self.cols()[3]:
            self.y_s=0
            self.move(0, -1)
            self.jump=False
        if not self.cols()[3]:
            self.y_s+=2
        self.image[self.i] = pygame.transform.scale(self.image[self.i], (l.teps, l.teps))
        screen.blit(self.image[self.i], (300, 300))
        if self.y> -160:
            self.x=0
            self.i_x=9
            self.y= -340
def make_level():
    l.ock_x=[]
    l.ock_y=[]
    x= -p.x
    y= -p.y
    o1= -1
    o2= -1
    for i in l.evel:
        x= -p.x
        o1= -1
        y+=l.teps
        o2+=1
        for j in str(i):
            x+=l.teps
            o1+=1
            run_scan_code(j, o1, o2, x, y)
def make(image, x, y):
    screen.blit(image, (x, y))
def run_scan_code(j, o1, o2, x, y):
    j=int(j)
    if int(j)==1 and o2>0:
        if bool(int(str(l.evel[o2-1])[o1])):
            make(i.seec[abs(int(p.i_x/l.leng))], x, y)
            l.ock_x.append(x)
            l.ock_y.append(y)
        else:
            make(i.images[abs(int(p.i_x/l.leng))][int(j)], x, y)
            l.ock_x.append(x)
            l.ock_y.append(y)
    else:
        make(i.images[abs(int(p.i_x/l.leng))][int(j)], x, y)
        l.ock_x.append(x)
        l.ock_y.append(y)
def check_all(k):
    g = k[0]
    mode = True
    for i in k:
        if not g == i:
            mode=False
            break
    return mode
def find_h(h):
    if check_all(h):
        return 100
    else:
        c= -11
        t=False
        for typ in h:
            c+=1
            if not typ == '0':
                break
        return c*(l.teps/30)
def backe():
    screen.blit(i.back[abs(int(p.i_x/l.leng))], (0,0))
p=pac()
            

while True:
    backe()
    make_level()
    p.update()
    pygame.event.get()
    pygame.display.update()
pygame.quit()
