from random import randint
import pygame
pygame.init()
run=True
font=pygame.font.SysFont("Comicsansms",10)
screen=pygame.display.set_mode((600,600))
Grid= [["-" for Column in range(26)] for Row in range(26)]
NewGrid= [["-" for Column in range(26)] for Row in range(26)]
NumberofMines=50


                            
def Start():
    
    screen.fill((255,255,255))
    pygame.display.set_caption("minesweeper")
    
    pygame.draw.rect(screen,(0,0,0),(0,0,600,600))
    pygame.draw.rect(screen,(150,150,150),(5,5,590,590))
    pygame.draw.rect(screen,(0,0,0),(100,100,400,400))
    pygame.draw.rect(screen,(255,255,255),(105,105,390,390))
    pygame.draw.rect(screen,(0,0,0),(0,0,90,30))
    pygame.draw.rect(screen,(255,255,255),(5,5,80,20))
    star=pygame.image.load('mine.png')
    star= pygame.transform.scale(star, (20, 20))
    screen.blit(star,(5,5,20,20))
    
    for i in range(0,390,15):
        for p in range(0,390,15):
            pygame.draw.rect(screen,(150,150,150),(105+i,105+p,14,14))
    for downline in range(0,390,15):
        pygame.draw.line(screen,(0,0,0),(105+downline,105),(105+downline,495))
    for sideline in range(0,390,15):
        pygame.draw.line(screen,(0,0,0),(105,105+sideline),(495,105+sideline))
    
   






        
def DisplayGrid():
    count=0

            #while NumberofMines>26*26 or NumberofMines<1:
            #    NumberofMines=int(input("How many bombs would you like?"))
    listofmines=[]
    while count<NumberofMines:
        RandomNumberColumn=randint(0,26-1) 
        RandomNumberRow=randint(0,26-1)
        addedco=str(RandomNumberRow)+'+'+str(RandomNumberColumn)
        if addedco not in listofmines:
            listofmines.append(addedco)
            Grid[RandomNumberRow][RandomNumberColumn]='*'
            #pygame.draw.rect(screen,(0,0,0),(120+(15*int(RandomNumberRow))-7,120+(15*int(RandomNumberColumn))-7,3,3))
            count+=1

         
def coordinatefornumber(Row,Column,Grid):
    count=0
    for Rowi in range(-1,2):
        for Columni in range(-1,2):
            try:
                if Grid[Row+Rowi][Column+Columni]=='*' and Row+Rowi>=0 and Column+Columni>=0:
                    count+=1
            except:
                pass
    return count
               
def NumbersAroundBombs(Grid):
    for Row in range(26):
        for Column in range(26):
            if Grid[Row][Column]!= '*':
                number=str(coordinatefornumber(Row,Column,Grid))
                Grid[Row][Column]=number
    
                    
    return Grid

def CountBombs(Grid):
    count=0
    for Row in range(26):
        for Column in range(26):
            if Grid[Row][Column]=='*':
                count+=1
    count=(26*26)-count
    return count

def EndGame(NewGrid,NumberofNotBombs):
    count=0
    for Row in range(26):
        for Column in range(26):
            if NewGrid[Row][Column]!='*' and NewGrid[Row][Column]!='-' and NewGrid[Row][Column]!='&':
                count+=1
    if count==NumberofNotBombs:
        return True
    else:
        return False
        
def split3(number):
    number=str(number)
    while len(number)!=3:
        number='0'+number
    return number

def UnlockSquare(Row,Column,Grid,NewGrid):
    pygame.draw.rect(screen,(255,255,255),(106.5+Row*15,106.5+Column*15,13,13))
    if Grid[Row][Column]!= '*':
        number=str(coordinatefornumber(Row,Column,Grid))



        if number!="0":
            if number=="1":
                text=font.render(number,True,(0,0,200))
            elif number=="2":
                text=font.render(number,True,(0,200,0))
            elif number=="3":
                text=font.render(number,True,(200,0,0))
            elif number=="4":
                text=font.render(number,True,(0,0,100))
            elif number=="5":
                text=font.render(number,True,(120,0,30))
            elif number=="6":
                text=font.render(number,True,(0,100,200))
            screen.blit(text,(107+Row*15,107+Column*15 ))
        pygame.display.update()
        NewGrid[Row][Column]=number
            
    else:
        star=pygame.image.load('mine.png')
        star= pygame.transform.scale(star, (13, 13))
        screen.blit(star,(106.5+Row*15,106.5+Column*15,13,13))
        text=font.render("You lose",True,(0,0,0))
        screen.blit(text,(300,50))
        
        pygame.display.update()
        pygame.time.delay(4000)
        Grid= [["-" for Column in range(26)] for Row in range(26)]
        NewGrid=[["-" for Column in range(26)] for Row in range(26)]
        Start() 
        DisplayGrid()
        pygame.draw.rect(screen,(255,255,255),(5,5,80,20))
        NumbersAroundBombs(Grid)
        numb=split3(NumberofMines)
        numb1=font.render(numb[0],True,(0,0,0))
        screen.blit(numb1,(30,7.5))
        numb2=font.render(numb[1],True,(0,0,0))
        screen.blit(numb2,(50,7.5))
        numb3=font.render(numb[2],True,(0,0,0))
        screen.blit(numb3,(70,7.5))
        star=pygame.image.load('mine.png')
        star= pygame.transform.scale(star, (20, 20))
        screen.blit(star,(5,5,20,20))
        pygame.display.update()
    return Grid,NewGrid,

def AIAroundNumber(Grid,NewGrid,one,two,three):
    for Row in range(one,two,three):
        for Column in range(one,two,three):
            if NewGrid[Row][Column]!='-':
                if NewGrid[Row][Column]=='0':
                   for row in range(-1,2):
                       for column in range(-1,2):
                           
                           try:
                               if 0<=Row+row<26 and 0<=Column+column<26:
                                   UnlockSquare(Row+row,Column+column,Grid,NewGrid)
                           except:
                               pass
                elif NewGrid[Row][Column]=='1':
                    count=0
                    for row in range(-1,2):
                       for column in range(-1,2):                           
                           try:
                               if 0<=Row+row<26 and 0<=Column+column<26:
                                   if NewGrid[Row+row][Column+column]=='-' or NewGrid[Row+row][Column+column]=='&' :
                                       count+=1
                                       crow=Row+row
                                       ccolumn=Column+column
                                   if NewGrid[Row+row][Column+column]=='&':
                                       for i in range(-1,2):
                                           for p in range(-1,2):
                                               if NewGrid[Row+i][Column+p]=='-' and 0<=Row+i<26 and 0<=Column+p<26:
                                                   UnlockSquare(Row+i,Column+p,Grid,NewGrid)
                           except:
                               pass
                    if count==1:
                        flagging(crow,ccolumn,Grid)
                        
                elif NewGrid[Row][Column]=='2':
                    count=0
                    lolcount=0
                    othercount=0
                    for row in range(-1,2):
                       for column in range(-1,2):                           
                           try:
                               if 0<=Row+row<26 and 0<=Column+column<26:
                                   if NewGrid[Row+row][Column+column]=='-' or NewGrid[Row+row][Column+column]=='&' :
                                       count+=1
                                       if NewGrid[Row+row][Column+column]=='-':
                                           crow=Row+row
                                           ccolumn=Column+column
                                           othercount+=1
                                   if NewGrid[Row+row][Column+column]=='&':
                                       lolcount+=1
                                       if lolcount==2:
                                           for i in range(-1,2):
                                               for p in range(-1,2):
                                                   if 0<=Row+i<26 and 0<=Column+p<26:
                                                       if NewGrid[Row+i][Column+p]=='-':
                                                           UnlockSquare(Row+i,Column+p,Grid,NewGrid)
                                                       
                                          

                           except:
                               pass
                    if count==2 and othercount==1:
                        flagging(crow,ccolumn,Grid)
                    
                elif NewGrid[Row][Column]=='3':  
                    count=0
                    lolcount=0
                    othercount=0
                    for row in range(-1,2):
                       for column in range(-1,2):                           
                           try:
                               if 0<=Row+row<26 and 0<=Column+column<26:
                                   if NewGrid[Row+row][Column+column]=='-' or NewGrid[Row+row][Column+column]=='&' :
                                       count+=1
                                       if NewGrid[Row+row][Column+column]=='-':
                                           crow=Row+row
                                           ccolumn=Column+column
                                           othercount+=1
                                   if NewGrid[Row+row][Column+column]=='&':
                                       lolcount+=1
                                       if lolcount==3:
                                           for i in range(-1,2):
                                               for p in range(-1,2):
                                                   if 0<=Row+i<26 and 0<=Column+p<26:
                                                       if NewGrid[Row+i][Column+p]=='-':
                                                           UnlockSquare(Row+i,Column+p,Grid,NewGrid)
                                                       
                                          

                           except:
                               pass
                    if count==3 and othercount==1:
                        flagging(crow,ccolumn,Grid)
                        
                        
                                   
                                   
                               
                           
def flagging(Row,Column,Grid) :
    global NumberofMines
    NumberofMines=50
    NewGrid[Row][Column]='&'
    flag=pygame.image.load('flag.png')
    flag= pygame.transform.scale(flag, (13, 13))
    pygame.draw.rect(screen,(255,255,255),(5,5,80,20))
    star=pygame.image.load('mine.png')
    star= pygame.transform.scale(star, (20, 20))
    screen.blit(star,(5,5,20,20))
    screen.blit(flag,(106.5+Row*15,106.5+Column*15,13,13))
    for row in range(0,26):
        for column in range(0,26):
            if NewGrid[row][column]=='&':
                NumberofMines-=1
    numb=split3(NumberofMines)
    numb1=font.render(numb[0],True,(0,0,0))
    screen.blit(numb1,(30,7.5))
    numb2=font.render(numb[1],True,(0,0,0))
    screen.blit(numb2,(50,7.5))
    numb3=font.render(numb[2],True,(0,0,0))
    screen.blit(numb3,(70,7.5))
    pygame.display.update()
    
    
def MinesweeperAI(Grid,NewGrid):
    randomx=randint(0,25)
    randomy=randint(0,25)
    UnlockSquare(randomx,randomy,Grid,NewGrid)

    for i in range(7):
        AIAroundNumber(Grid,NewGrid,0,26,1)
        AIAroundNumber(Grid,NewGrid,25,-1,-1)
    
    
    
    
    

Start()
DisplayGrid()
NumbersAroundBombs(Grid) 
NumberofNotBombs=CountBombs(Grid)
numb=split3(NumberofMines)
numb1=font.render(numb[0],True,(0,0,0))
screen.blit(numb1,(30,7.5))
numb2=font.render(numb[1],True,(0,0,0))
screen.blit(numb2,(50,7.5))
numb3=font.render(numb[2],True,(0,0,0))
screen.blit(numb3,(70,7.5))
  

pygame.display.update()
MinesweeperAI(Grid,NewGrid,)
while True:
    for event in pygame.event.get():
        mouse=pygame.mouse.get_pos()
        
                
        '''if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for Row in range(0,26):
                for Column in range(0,26):
                
                    if 105+14+(15*Row)>mouse[0]>105+(15*Row) and 105+14+(15*Column)>mouse[1]>105+15*Column and NewGrid[Row][Column]!='&':
                        pygame.draw.rect(screen,(255,255,255),(106.5+Row*15,106.5+Column*15,13,13))
                        
                        if Grid[Row][Column]!= '*':
                            number=str(coordinatefornumber(Row,Column,Grid))

                
                
                            if number!="0":
                                if number=="1":
                                    text=font.render(number,True,(0,0,200))
                                elif number=="2":
                                    text=font.render(number,True,(0,200,0))
                                elif number=="3":
                                    text=font.render(number,True,(200,0,0))
                                elif number=="4":
                                    text=font.render(number,True,(0,0,100))
                                elif number=="5":
                                    text=font.render(number,True,(120,0,30))
                                elif number=="6":
                                    text=font.render(number,True,(0,100,200))
                                screen.blit(text,(107+Row*15,107+Column*15 ))
                            pygame.display.update()
                            NewGrid[Row][Column]=number
                                
                        else:
                            star=pygame.image.load('mine.png')
                            star= pygame.transform.scale(star, (13, 13))
                            screen.blit(star,(106.5+Row*15,106.5+Column*15,13,13))
                            text=font.render("You lose",True,(0,0,0))
                            screen.blit(text,(300,50))
                            
                            pygame.display.update()
                            pygame.time.delay(4000)
                            Grid= [["-" for Column in range(26)] for Row in range(26)]
                            NewGrid=[["-" for Column in range(26)] for Row in range(26)]
                            Start() 
                            DisplayGrid()
                            pygame.draw.rect(screen,(255,255,255),(5,5,80,20))
                            NumbersAroundBombs(Grid)
                            numb=split3(NumberofMines)
                            numb1=font.render(numb[0],True,(0,0,0))
                            screen.blit(numb1,(30,7.5))
                            numb2=font.render(numb[1],True,(0,0,0))
                            screen.blit(numb2,(50,7.5))
                            numb3=font.render(numb[2],True,(0,0,0))
                            screen.blit(numb3,(70,7.5))
                            star=pygame.image.load('mine.png')
                            star= pygame.transform.scale(star, (20, 20))
                            screen.blit(star,(5,5,20,20))
                            pygame.display.update()'''

                        
                        
        '''if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for Row in range(0,26):
                for Column in range(0,26):
                    if 105+14+(15*Row)>mouse[0]>105+(15*Row) and 105+14+(15*Column)>mouse[1]>105+15*Column and NewGrid[Row][Column]=='-':

                        NewGrid[Row][Column]='&'
                        flag=pygame.image.load('flag.png')
                        flag= pygame.transform.scale(flag, (13, 13))
                        pygame.draw.rect(screen,(255,255,255),(5,5,80,20))
                        star=pygame.image.load('mine.png')
                        star= pygame.transform.scale(star, (20, 20))
                        screen.blit(star,(5,5,20,20))
                        screen.blit(flag,(106.5+Row*15,106.5+Column*15,13,13))
                        NumberofMines-=1
                        numb=split3(NumberofMines)
                        numb1=font.render(numb[0],True,(0,0,0))
                        screen.blit(numb1,(30,7.5))
                        numb2=font.render(numb[1],True,(0,0,0))
                        screen.blit(numb2,(50,7.5))
                        numb3=font.render(numb[2],True,(0,0,0))
                        screen.blit(numb3,(70,7.5))
                        pygame.display.update()
                        
                    elif 105+14+(15*Row)>mouse[0]>105+(15*Row) and 105+14+(15*Column)>mouse[1]>105+15*Column and        NewGrid[Row][Column]=='&':
                        NewGrid[Row][Column]='-'
                        pygame.draw.rect(screen,(150,150,150),(106+15*Row,106+15*Column,13,13))
                        pygame.draw.rect(screen,(255,255,255),(5,5,80,20))
                        star= pygame.transform.scale(star, (20, 20))
                        screen.blit(star,(5,5,20,20))
                        NumberofMines+=1
                        numb=split3(NumberofMines)
                        numb1=font.render(numb[0],True,(0,0,0))
                        screen.blit(numb1,(30,7.5))
                        numb2=font.render(numb[1],True,(0,0,0))
                        screen.blit(numb2,(50,7.5))
                        numb3=font.render(numb[2],True,(0,0,0))
                        screen.blit(numb3,(70,7.5))
                        pygame.display.update()'''
            
        if EndGame(NewGrid,NumberofNotBombs)==True:  
            text=font.render("You win",True,(0,0,0))
            screen.blit(text,(300,50))
        if event.type == pygame.QUIT: 
             pygame.quit()

'''                    
    def UpdatedGrid(Grid,NewGrid):
        Choice=input("Flag,Unflag or Choose(F,U,C)")
        if Choice.lower()=='c':
            RowNumber=int(input("Row number:"))
            ColumnNumber=int(input("Column Number"))
            if Grid[RowNumber][ColumnNumber]!='*':
                NewGrid[RowNumber][ColumnNumber]=Grid[RowNumber][ColumnNumber]
                DisplayGrid(NewGrid)
                return NewGrid
            else:
                NewGrid[RowNumber][ColumnNumber]=Grid[RowNumber][ColumnNumber]
                DisplayGrid(NewGrid)
                print("You have lost sucker")
                input()
                return False
        elif Choice.lower()=='f':
            RowNumber=int(input("Row number:"))
            ColumnNumber=int(input("Column Number"))
            if NewGrid[RowNumber][ColumnNumber]=='-':
                NewGrid[RowNumber][ColumnNumber]='&'
            DisplayGrid(NewGrid)
            return NewGrid
        elif Choice.lower()=='u':
            RowNumber=int(input("Row number:"))
            ColumnNumber=int(input("Column Number"))
            if NewGrid[RowNumber][ColumnNumber]=='&':
                NewGrid[RowNumber][ColumnNumber]='-'
            DisplayGrid(NewGrid)
            return NewGrid
            

    
    def EndGame(NewGrid,NumberofNotBombs):
        count=0
        for Row in range(Dimensions):
            for Column in range(Dimensions):
                if NewGrid[Row][Column]!='*' and NewGrid[Row][Column]!='-':
                    count+=1
        if count==NumberofNotBombs:
            return True
        else:
            return False
          
              
    
    
    
    def Game():
        global Dimensions
        Dimensions=int(input("What Length would you like?"))
        Grid= [["-" for Column in range(Dimensions)] for Row in range(Dimensions)]
        MinePlace(Grid)
        NumbersAroundBombs(Grid)
        NumberofNotBombs=CountBombs(Grid)
        NewGrid=[["-" for Column in range(Dimensions)] for Row in range(Dimensions)]
        while UpdatedGrid(Grid,NewGrid)!=False:
            if EndGame(NewGrid,NumberofNotBombs)==True:
                print("You have won the game somehow?")
                print('The secret code is 29/05/2020')
                input()'''


            
    
    
    
    
 #Things that are wrong: top row and left-most column. the numbers are wrong (done)
 #Asks for row number after mine has been clicked(Done)
 
 
 
 
#to do list: make squares for each number/bomb
    #make a menu
    #choose amount of bombs(DONE)
    #hide everything from the user and ask them for a coordinate, and make the piece visable and lose if hitting a bomb(done)
#ability to add a flag to the game()
# do not put flag on numbers, ability to unflag,
    
    
    