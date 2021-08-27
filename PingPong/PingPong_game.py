import pygame

pygame.init()
width=1000
hight=750
screen = pygame.display.set_mode([width,hight])
pygame.display.set_caption("8090GAME CENTER -- NOW PLAYING PINGPONG2")
keepGoing = True
pic = pygame.image.load('clust.png')                  
colorkey=pic.get_at((0,0))
pic.set_colorkey(colorkey)
pygame.mixer.init()
die=pygame.mixer.Sound('die.wav')
hit=pygame.mixer.Sound('hit.wav')
over=pygame.mixer.Sound('over.wav')

picx=0
picy=0
BLK=(0,0,0)
WHT=(240,240,255)
timer = pygame.time.Clock()
spdx=5
spdy=5
MAX_spd = 30
tim=0
timb=0
sppdx=1.12
sppdy=1.08
spppd=1
count=0
paw=200
pah=20
pax=(width-200)//2
pay=hight-50
picw=100
pich=100
points=0
lives=5
font=pygame.font.SysFont("Times",25)

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_F1:
                points=0
                lives=5
                spdx=5
                spdy=5
                picx=0
                picy=0
                count=0
            if event.key==pygame.K_F12:
                sppdx=sppdy=1
                spppd=0.95
                timb=1
    picx+=spdx
    picy+=spdy
    if timb==1:
        tim+=1
    if tim>1000:
        timb=0
        sppdx=1.12
        sppdy=1.08
        spppd=1
    if picx<=0 or picx>=(width-75):
        spdx = -spdx*sppdx
        spdx = min(spdx,MAX_spd)
        spdx = max(spdx,-MAX_spd)
    if picy<=0:
        spdy = -(spdy*sppdy)
        spdy = min(spdy,MAX_spd)
        spdy = max(spdy,-MAX_spd)
    if picy>=(hight-pich):
        lives-=1
        spdy=-5
        spdx=5
        picy=(hight-pich-1)
        if lives>0:
            die.play()
    screen.fill(BLK)
    screen.blit(pic,(picx,picy))
    pax=pygame.mouse.get_pos()[0]
    pax-=paw/2
    pygame.draw.rect(screen,WHT,(pax,pay,paw,pah))
    if picy+pich>=pay and picy+pich<=pay+pah and spdy>0:
        if picx+picw/2>=pax and picx+picw/2<=pax+paw:
            spdy=-spdy*spppd
            sppppp=int((spdy*1000)//5)
            points-=(sppppp/1000)
            points=int(points*1000)/1000
            hit.play()
    draw_string="Lives: "+str(lives)+"   Points:"+str(points)
    if (lives<1)&(count==0):
        spdx=spdy=0
        
        points1=int(points)
        over.play()
        draw_string="GAME OVER. Your score was "+str(points1)+"("+str(points)+"). Press F1 to play again."
        count+=1  
    
    text=font.render(draw_string,True,WHT)
    text_rect=text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y=10
    screen.blit(text,text_rect)
    pygame.display.update()
    timer.tick(60)

                
pygame.quit()
