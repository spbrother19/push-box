#可以另外画地图，只需导入即可改装成一系列关卡
import pygame
def getpic(lspic,index):  #给一个索引，返回图像列表的对应元素名称
    return lspic[index]


def update(x,y,x1,y1,x2,y2,ls,goalpos,step):#传入键盘事件，尝试更改列表,和主角坐标
##    print(ls[x][y],ls[x1][y1],ls[x2][y2])
    if 0<=x2<=lsw and 0<=y2<=lsh:
        if ls[y1][x1]==0 and (ls[y2][x2]==1 or ls[y2][x2]==2):
            ls[y][x],ls[y1][x1],ls[y2][x2]=1,3,0
            x,y=x1,y1
            step+=1
        elif ls[y1][x1]==1 or ls[y1][x1]==2:
            ls[y][x],ls[y1][x1]=1,3
            x,y=x1,y1
            step+=1
    elif 0<=x1<=lsw and 0<=y1<=lsh:
        if ls[y1][x1]==1 or ls[y1][x1]==2:
            ls[y][x],ls[y1][x1]=1,3
            x,y=x1,y1
            step+=1
            
    for myx,myy in goalpos:
        if ls[myy][myx]==1:
            ls[myy][myx]=2
    return x,y,step

def mydraw(ls):#更新图像
    for i in range(lsh):
        for j in range(lsw):
            pic=getpic(lspic,ls[i][j])
            picx=x0+(j+1)*size
            picy=y0+(i+1)*size
            screen.blit(pic,(picx,picy))
            
def myfont(step,goalpos):#更新文字
    remain=3
    for myx,myy in goalpos:
        if ls[myy][myx]==0:
            remain-=1
    gastr="Step:"+str(step)+"   Remain pont:"+str(remain)
    if remain==0:
        gastr+="  You Win!"
    text=font.render(gastr,True,WHITE)
    text_rect=text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y=10
    screen.blit(text,text_rect)

pygame.init()
winw=900      
winh=700
screen=pygame.display.set_mode([winw,winh])
timer=pygame.time.Clock()
WHITE=(255,255,255)
BLACK=(0,0,0)
font=pygame.font.SysFont('Time',50)
x0=20
y0=20
stone=pygame.image.load("stone.bmp")       
box=pygame.image.load("box.bmp")       
dirt=pygame.image.load("dirt.bmp")       
goal=pygame.image.load("goal.bmp")       
man=pygame.image.load("man.bmp")       
tree=pygame.image.load("tree.bmp")
file = open("lev1.txt","r")
perls = file.readlines()
ls = []
for fields in perls: 
    fields=fields.strip()
    fields=fields.strip("[]")
    fields=fields.split(",")
    ls.append(fields)
file.close()
lsh=len(ls)
lsw=len(ls[0])
##print(lsh,lsw)
for i in range(lsh):
    for j in range(lsw):
        ls[i][j]=int(ls[i][j])
##        print(ls[i][j],end=" ")
##    print()
lspic=[box,dirt,goal,man,stone,tree]
x=0
y=0
goalpos=[]
size=dirt.get_width()
for i in range(lsh):
    for j in range(lsw):
        if ls[i][j]==3:
            x=j
            y=i
##            print(x,y)
        if ls[i][j]==2:
            goalpos.append([j,i])
##goalpos=[[5,2],[6,2],[7,2]]
##print(goalpos)
step=0
keep_going=True
while keep_going:   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                x,y,step=update(x,y,x,y-1,x,y-2,ls,goalpos,step)
##                print(x,y)
            if event.key==pygame.K_DOWN:
                x,y,step=update(x,y,x,y+1,x,y+2,ls,goalpos,step)
##                print(x,y)
            if event.key==pygame.K_LEFT:
                x,y,step=update(x,y,x-1,y,x-2,y,ls,goalpos,step)
##                print(x,y)
            if event.key==pygame.K_RIGHT:
                x,y,step=update(x,y,x+1,y,x+2,y,ls,goalpos,step)
##                print(x,y)
    screen.fill(BLACK)       #填充背景颜色去掉后将显示轨迹 
    mydraw(ls)
    myfont(step,goalpos) 
    pygame.display.update()       #更新窗口
    timer.tick(30)       #游戏帧数
pygame.quit()       

