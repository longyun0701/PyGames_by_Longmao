#作者：龙家君----年龄：10岁半
#Author:Junlun Long----Age 10-&-a-half
#康威元胞自动机  Conway game of life
#size 23*11

import pygame
pygame.init()

time_len=4 #set speed
cell_w=28 #set virus size
cell_h=35
alC=(240,10,0) #set alive color
diC=(40,40,43) #set dead color
bgC=(0,0,0)
timer = pygame.time.Clock() #set timer
alive=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,1,0,0,1,1,0,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0],
       [0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0],
       [0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0],   #map setup
       [0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0],   #1 is alive,0 is dead
       [0,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,1,0,0],
       [0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,0],
       [0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0],
       [0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,0,0,0],
       [0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
       [0,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
       [0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

screen=pygame.display.set_mode((700,455))  #set screen

#cauculate:alive or dead?
def showAlive(x,y):
    num=0
    if(x==0 or y==0 or x==24 or y==12):
        alive[x][y]=0
    else:
        num=alive[x-1][y-1]+alive[x][y-1]+alive[x-1][y]+alive[x][y+1]+alive[x+1][y+1]+alive[x+1][y]+alive[x+1][y-1]+alive[x-1][y+1]
        if(num>3):
            alive[x][y]=0
        if(num<2):
            alive[x][y]=0
        if(num==3):
            alive[x][y]=1
    

#show:which one is alive?
def sts(alive):
    for x in range(1,24):
        for y in range(1,12):
            virusR=pygame.Rect(x*cell_w,y*cell_h,cell_w-1,cell_h-1)
            if(alive[y][x] == 0):
                pygame.draw.rect(screen,diC,virusR)
            else:
                pygame.draw.rect(screen,alC,virusR)

#other values
ans=3 #virus number
time=0 #era number
kg=True #quit or not

print("VIRUS SPREADING")

#game loop
while kg:
    if(ans<3): #too few cells to live
        kg=False
    for event in pygame.event.get(): #user quit
        if event.type == pygame.QUIT:
            kg=False
    time += 1 #era forward
    ans=0
    screen.fill(bgC)
    
    sts(alive) #show
    #cauculate
    for i in range(1,24):
        for j in range(1,12):
            showAlive(j,i)
    for i in range(1,24):
        for j in range(1,12):
            if(alive[j][i]):
                ans+=1
    pygame.display.update()
    print("still alive")
    timer.tick(time_len)

#end
if ans>2:
    print("same as every era,or is the virus too healthy?")
else:
    print("dead within",time,"era(s)")
pygame.quit()   
