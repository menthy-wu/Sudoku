#数独
#初始界面0
#游戏中1
#难度选择中2
#win 3
#game over 4
#需要加入计时系统，和错误上限
import pygame,sys,random,datetime
SCREEN_W,SCREEN_H = 600,600 #屏幕大小
myfont = 'AdobeArabic-BoldItalic.otf'
class CLS_board(object):
    def __init__(self):
        self.x,self.y = 50,50 #数独坐标
        self.w  = 50 #每个小格子的边长
        self.l1 = 5 #粗线宽度
        self.l2 = 2 #细线宽度
        self.boardList = [[[5,0],[8,0],[6,0],[2,0],[3,0],[1,0],[4,0],[7,0],[9,0]],\
                          [[4,0],[3,0],[7,0],[8,0],[9,0],[5,0],[1,0],[6,0],[2,0]],\
                          [[9,0],[1,0],[2,0],[4,0],[6,0],[7,0],[5,0],[3,0],[8,0]],\
                          [[6,0],[2,0],[9,0],[1,0],[7,0],[8,0],[3,0],[4,0],[5,0]],\
                          [[1,0],[5,0],[8,0],[9,0],[4,0],[3,0],[7,0],[2,0],[6,0]],\
                          [[3,0],[7,0],[4,0],[6,0],[5,0],[2,0],[8,0],[9,0],[1,0]],\
                          [[8,0],[6,0],[5,0],[7,0],[2,0],[4,0],[9,0],[1,0],[3,0]],\
                          [[2,0],[4,0],[3,0],[5,0],[1,0],[9,0],[6,0],[8,0],[7,0]],\
                          [[7,0],[9,0],[1,0],[3,0],[8,0],[6,0],[2,0],[5,0],[4,0]]]
        
        self.answerList =[[5,8,6,2,3,1,4,7,9],\
                          [4,3,7,8,9,5,1,6,2],\
                          [9,1,2,4,6,7,5,3,8],\
                          [6,2,9,1,7,8,3,4,5],\
                          [1,5,8,9,4,3,7,2,6],\
                          [3,7,4,6,5,2,8,9,1],\
                          [8,6,5,7,2,4,9,1,3],\
                          [2,4,3,5,1,9,6,8,7],\
                          [7,9,1,3,8,6,2,5,4]]
        self.n = 1
    def draw(self,screen):
        font = pygame.font.Font(myfont,55)
        img = font.render('End',True,(255,150,150))
        screen.blit( img ,(49,4))
        img = font.render('End',True,(200,100,100))
        screen.blit( img ,(51,6))
        img = font.render('End',True,(255,255,255))
        screen.blit( img ,(50,5))
        pygame.draw.rect(screen,(200,200,200),(450,9,150,50),0)
        if self.n == 1: 
            img = font.render('Easy',True,(200,80,100))
            img2 = font.render('Easy',True,(255,255,255))
            img3 = font.render('Easy',True,(160,40,60))
        if self.n == 2:
            img = font.render('Medium',True,(50,80,100))
            img2 = font.render('Medium',True,(255,255,255))
            img3 = font.render('Medium',True,(10,40,60))
        if self.n == 3:
            img = font.render('Hard',True,(50,150,150))
            img2 = font.render('Hard',True,(255,255,255))
            img3 = font.render('Hard',True,(10,110,110))
        screen.blit(img,(449,3))
        screen.blit(img3,(451,5)) 
        screen.blit(img2,(450,4)) 
        
        img = font.render('S u d o k u',True,(150,150,150))
        screen.blit( img ,(199,4))
        img = font.render('S u d o k u',True,(100,100,100))
        screen.blit( img ,(201,6))
        img = font.render('S u d o k u',True,(255,255,255))
        screen.blit( img ,(200,5))
        
        self.error()
        h = self.w*9+self.l1*4+self.l2*6
        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,h,h),0) #画格子
        for i in range(4):
            pygame.draw.rect(screen,(0,0,0),(self.x+i*3*self.w+i*self.l1+i*2*self.l2,self.y,5,h),0)#粗线
            pygame.draw.rect(screen,(0,0,0),(self.x,self.y+i*3*self.w+i*self.l1+i*2*self.l2,h,5),0)
        pygame.draw.rect(screen,(0,0,0),(self.x+self.l1+self.w              ,self.y,self.l2,h),0)#横细线
        pygame.draw.rect(screen,(0,0,0),(self.x+self.l1+self.w*2+self.l2    ,self.y,self.l2,h),0)
        pygame.draw.rect(screen,(0,0,0),(self.x+self.l1*2+self.w*4+self.l2*2,self.y,self.l2,h),0)
        pygame.draw.rect(screen,(0,0,0),(self.x+self.l1*2+self.w*5+self.l2*3,self.y,self.l2,h),0)
        pygame.draw.rect(screen,(0,0,0),(self.x+self.l1*3+self.w*7+self.l2*4,self.y,self.l2,h),0)
        pygame.draw.rect(screen,(0,0,0),(self.x+self.l1*3+self.w*8+self.l2*5,self.y,self.l2,h),0)
        
        pygame.draw.rect(screen,(0,0,0),(self.y,self.y+self.l1+self.w              ,h,self.l2),0)#竖细线
        pygame.draw.rect(screen,(0,0,0),(self.y,self.y+self.l1+self.w*2+self.l2    ,h,self.l2),0)
        pygame.draw.rect(screen,(0,0,0),(self.y,self.y+self.l1*2+self.w*4+self.l2*2,h,self.l2),0)
        pygame.draw.rect(screen,(0,0,0),(self.y,self.y+self.l1*2+self.w*5+self.l2*3,h,self.l2),0)
        pygame.draw.rect(screen,(0,0,0),(self.y,self.y+self.l1*3+self.w*7+self.l2*4,h,self.l2),0)
        pygame.draw.rect(screen,(0,0,0),(self.y,self.y+self.l1*3+self.w*8+self.l2*5,h,self.l2),0)
        if 0<=framwork.my < 9 and 0<=framwork.mx < 9 :
            for i in range(9):
                for p in range(9):#方格变绿
                    if self.boardList[framwork.my][framwork.mx][0] != ' ':
                        if self.boardList[i][p][0] == self.boardList[framwork.my][framwork.mx][0]:
                            x1 = (p//3)*5 + p*50 + (p-p//3)*2+55
                            y1 = (i//3)*5 + i*50 + (i-i//3)*2+55
                            pygame.draw.rect(screen,(150,200,200),(x1,y1,50,50),0)
            x1 = (framwork.mx//3)*5 + framwork.mx*50 + (framwork.mx-framwork.mx//3)*2+55#方格变灰
            y1 = (framwork.my//3)*5 + framwork.my*50 + (framwork.my-framwork.my//3)*2+55
            pygame.draw.rect(screen,(200,200,200),(x1,y1,50,50),0)
     
            
            
        font = pygame.font.Font('font.otf', 32) #画数字
        for y in range(9):
            for x in range(9):
                a = self.boardList[y][x][0]
                if self.boardList[y][x][1]==1:
                    c = (60,80,110)
                elif self.boardList[y][x][1]==2:
                    c = (255,0,0)
                else:
                    c = (0,0,0)
                x1 = (x//3)*self.l1 + x*self.w + (x-x//3)*self.l2+self.x+20
                y1 = (y//3)*self.l1 + y*self.w + (y-y//3)*self.l2+self.y+20
                img = font.render(str(a),True,c)
                screen.blit( img ,(x1,y1))
                
    def daluan(self):
        for i in range(3):  #按组打乱数独
            a = random.randint(0,2)
            b = random.randint(0,2)
            self.boardList[i*3+a],  self.boardList[i*3+b] = self.boardList[i*3+b]  ,self.boardList[i*3+a]#纵向打乱
            self.answerList[i*3+a],self.answerList[i*3+b] = self.answerList[i*3+b],self.answerList[i*3+a]#纵向打乱
            for p in range(9):#横向打乱
                self.boardList[p][3*i+a],self.boardList[p][3*i+b] = self.boardList[p][3*i+b],self.boardList[p][3*i+a]
                self.answerList[p][3*i+a],self.answerList[p][3*i+b] = self.answerList[p][3*i+b],self.answerList[p][3*i+a]
        a = random.randint(0,2)
        b = random.randint(0,2)
        for i in range(3):
            self.boardList[a*3+i],  self.boardList[b*3+i] = self.boardList[b*3+i]  ,self.boardList[a*3+i]#纵向打乱
            self.answerList[a*3+i],self.answerList[b*3+i] = self.answerList[b*3+i],self.answerList[a*3+i]#纵向打乱
            for p in range(9):#横向打乱
                self.boardList[p][3*a+i],self.boardList[p][3*b+i] = self.boardList[p][3*b+i],self.boardList[p][3*a+i]
                self.answerList[p][3*a+i],self.answerList[p][3*b+i] = self.answerList[p][3*b+i],self.answerList[p][3*a+i]
        for i in range(self.n*30): #随机取出数字
        #for i in range(1): 
            x = random.randint(0,8)
            y = random.randint(0,8)
            self.boardList[y][x][0] = ' '
            self.boardList[y][x][1] = 1
        return True
    def error(self):
        for y in range(9):
            for x in range(9):
                if self.boardList[y][x][0] != ' ' and self.boardList[y][x][0] != self.answerList[y][x]:
                    self.boardList[y][x][1] = 2
                if self.boardList[y][x][1] != 0 and self.boardList[y][x][0] == self.answerList[y][x]:
                    self.boardList[y][x][1] = 1
        return
class CLS_framwork(object):
    def __init__(self):
        self.board = CLS_board()
        self.mx,self.my = 10,10
        self.f = 0
        self.pos = 0
        self.e = 0
    def draw(self,scr):
        self.board.draw(scr)
        if self.e >= 3:
            pygame.draw.rect(screen,(255,255,255),(100,230,380,80),0)
            font = pygame.font.Font(myfont,100)
            img = font.render('Game Over',True,(50,80,100))
            screen.blit( img ,(110,215))
            font = pygame.font.Font(myfont,45)
            img = font.render('Press SPACE to continue',True,(215,80,100))
            screen.blit( img ,(120,315))
            self.f = 4
        if self.f == 0:
            pygame.draw.rect(screen,(250,140,190),(65,247,456,86),0)
            pygame.draw.rect(screen,(100,200,200),(68,250,453,83),0)
            pygame.draw.rect(screen,(255,255,255),(68,250,450,80),0)
            font = pygame.font.Font(myfont,45)
            img = font.render('Press SPACE to start the game',True,(200,80,100))
            screen.blit( img ,(80,245))
            img = font.render('Press Enter to choose level',True,(50,80,100))
            screen.blit( img ,(95,285))
        if self.win()==True and self.f == 3:
            pygame.draw.rect(screen,(255,255,255),(145,230,280,80),0)
            font = pygame.font.Font(myfont,100)
            img = font.render('you win',True,(50,80,100))
            screen.blit( img ,(160,215))
            img = font.render('you win',True,(215,80,100))
            screen.blit( img ,(162,217))
            img = font.render('you win',True,(255,255,255))
            screen.blit( img ,(161,216))
            font = pygame.font.Font(myfont,45)
            img = font.render('Press SPACE to continue',True,(215,80,100))
            screen.blit( img ,(110,320))
        if self.f == 2:
            font = pygame.font.Font(myfont,45)
            pygame.draw.rect(screen,(255,255,255),(200,165,190,50),0)
            img = font.render('Press 1:Easy',True,(200,80,100))
            screen.blit( img ,(207,165))
            pygame.draw.rect(screen,(255,255,255),(180,245,230,50),0)
            img = font.render('Press 2:Midium',True,(50,80,100))
            screen.blit( img ,(190,245))
            pygame.draw.rect(screen,(255,255,255),(200,325,190,50),0)
            img = font.render('Press 3:Hard',True,(50,150,150))
            screen.blit( img ,(207,325))
        pygame.draw.rect(screen,(200,200,200),(50,550,100,50),0)
        font = pygame.font.Font(myfont,45)
        img = font.render(str(self.e)+'/3',True,(200,80,100))
        screen.blit( img ,(50,540))
        pygame.draw.rect(screen,(200,200,200),(150,550,100,50),0)
        
    def start(self):
        self.board.daluan()
    def mousedown(self,pos,b):
        print(self.e)
        self.pos = pos
        mx,my = pos[0],pos[1]
        self.mx,self.my = (mx-65)//50,(my-65)//50
        if 50<= pos[0] <= 130 and 10<=pos[1]<=50:
            self.f = 0
            self.board.boardList =  [[[5,0],[8,0],[6,0],[2,0],[3,0],[1,0],[4,0],[7,0],[9,0]],\
                          [[4,0],[3,0],[7,0],[8,0],[9,0],[5,0],[1,0],[6,0],[2,0]],\
                          [[9,0],[1,0],[2,0],[4,0],[6,0],[7,0],[5,0],[3,0],[8,0]],\
                          [[6,0],[2,0],[9,0],[1,0],[7,0],[8,0],[3,0],[4,0],[5,0]],\
                          [[1,0],[5,0],[8,0],[9,0],[4,0],[3,0],[7,0],[2,0],[6,0]],\
                          [[3,0],[7,0],[4,0],[6,0],[5,0],[2,0],[8,0],[9,0],[1,0]],\
                          [[8,0],[6,0],[5,0],[7,0],[2,0],[4,0],[9,0],[1,0],[3,0]],\
                          [[2,0],[4,0],[3,0],[5,0],[1,0],[9,0],[6,0],[8,0],[7,0]],\
                          [[7,0],[9,0],[1,0],[3,0],[8,0],[6,0],[2,0],[5,0],[4,0]]]
            self.board.answerList = [[5,8,6,2,3,1,4,7,9],\
                          [4,3,7,8,9,5,1,6,2],\
                          [9,1,2,4,6,7,5,3,8],\
                          [6,2,9,1,7,8,3,4,5],\
                          [1,5,8,9,4,3,7,2,6],\
                          [3,7,4,6,5,2,8,9,1],\
                          [8,6,5,7,2,4,9,1,3],\
                          [2,4,3,5,1,9,6,8,7],\
                          [7,9,1,3,8,6,2,5,4]]
        return 
    def keydown(self,key):
        if key == 13 and self.f == 0:
            self.f = 2
        if key == pygame.K_SPACE and self.f == 0:
            self.start()
            self.f = 1
        if key == pygame.K_SPACE and self.f == 3:
            self.f = 0
        if pygame.K_1 <= key <= pygame.K_9:
            if self.mx !=10 and self.my != 10 :
                if self.board.boardList[self.my][self.mx][1]!= 0 and self.f==1:
                    if self.board.boardList[self.my][self.mx][0] == key-48:
                        self.board.boardList[self.my][self.mx][0] = ' '
                    else:
                        self.board.boardList[self.my][self.mx][0] = key-48
                    if self.board.boardList[self.my][self.mx][0] != self.board.answerList[self.my][self.mx] and self.board.boardList[self.my][self.mx][0] != ' ':
                        self.e += 1
        if pygame.K_1 <= key <= pygame.K_3 and self.f == 2:
            if key == pygame.K_1:
                self.board.n = 1
                self.f = 0
            if key == pygame.K_2:
                self.board.n = 2
                self.f = 0
            if key == pygame.K_3:
                self.board.n = 3
                self.f = 0
        if self.f == 4 and key == pygame.K_SPACE:
            print('hi')
            self.e = 0
            self.f = 0
            self.board.boardList =  [[[5,0],[8,0],[6,0],[2,0],[3,0],[1,0],[4,0],[7,0],[9,0]],\
                          [[4,0],[3,0],[7,0],[8,0],[9,0],[5,0],[1,0],[6,0],[2,0]],\
                          [[9,0],[1,0],[2,0],[4,0],[6,0],[7,0],[5,0],[3,0],[8,0]],\
                          [[6,0],[2,0],[9,0],[1,0],[7,0],[8,0],[3,0],[4,0],[5,0]],\
                          [[1,0],[5,0],[8,0],[9,0],[4,0],[3,0],[7,0],[2,0],[6,0]],\
                          [[3,0],[7,0],[4,0],[6,0],[5,0],[2,0],[8,0],[9,0],[1,0]],\
                          [[8,0],[6,0],[5,0],[7,0],[2,0],[4,0],[9,0],[1,0],[3,0]],\
                          [[2,0],[4,0],[3,0],[5,0],[1,0],[9,0],[6,0],[8,0],[7,0]],\
                          [[7,0],[9,0],[1,0],[3,0],[8,0],[6,0],[2,0],[5,0],[4,0]]]
            self.board.answerList = [[5,8,6,2,3,1,4,7,9],\
                          [4,3,7,8,9,5,1,6,2],\
                          [9,1,2,4,6,7,5,3,8],\
                          [6,2,9,1,7,8,3,4,5],\
                          [1,5,8,9,4,3,7,2,6],\
                          [3,7,4,6,5,2,8,9,1],\
                          [8,6,5,7,2,4,9,1,3],\
                          [2,4,3,5,1,9,6,8,7],\
                          [7,9,1,3,8,6,2,5,4]]
    def win(self):
        for y in range(9):
            for x in range(9):
                if self.board.boardList[y][x][0] == ' ':
                    return False
                elif self.board.boardList[y][x][0] != self.board.answerList[y][x]:
                    return False
        if self.f == 1 :
            self.f = 3
        return True
            
            
            
#————————main————————
framwork = CLS_framwork()
pygame.init()
screen = pygame.display.set_mode( (SCREEN_W,SCREEN_H) )
screen.fill((200,200,200))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            framwork.keydown(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            framwork.mousedown(event.pos,event.button)
    framwork.draw(screen)
    pygame.display.update()
