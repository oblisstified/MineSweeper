from random import randint
import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.set_caption("minesweeper")
Grid= [["-" for Column in range(26)] for Row in range(26)]
pygame.draw.rect(screen,(0,0,0),(0,0,600,600))
pygame.draw.rect(screen,(150,150,150),(5,5,590,590))
pygame.draw.rect(screen,(0,0,0),(100,100,400,400))
pygame.draw.rect(screen,(255,255,255),(105,105,390,390))

for i in range(0,390,15):
    for p in range(0,390,15):
        pygame.draw.rect(screen,(150,150,150),(105+i,105+p,14,14))
for downline in range(0,390,15):
    pygame.draw.line(screen,(0,0,0),(105+downline,105),(105+downline,495))
for sideline in range(0,390,15):
    pygame.draw.line(screen,(0,0,0),(105,105+sideline),(495,105+sideline))

run=True
font=pygame.font.SysFont("Comicsansms",10)






        
def DisplayGrid():
    count=0
    NumberofMines=False
    NumberofMines=150
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
DisplayGrid()
pygame.display.update()
         
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
                
                
                '''if number!="0":
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
                    screen.blit(text,(107+Row*15,107+Column*15 ))'''
                        
                    
    return Grid
NumbersAroundBombs(Grid)   

pygame.display.update()


while True:
    for event in pygame.event.get():
        mouse=pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for Row in range(0,26):
                for Column in range(0,26):
                
                    if 105+14+(15*Row)>mouse[0]>105+(15*Row) and 105+14+(15*Column)>mouse[1]>105+15*Column:
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
                                
                        else:
                            pygame.draw.rect(screen,(0,0,0),(120+(15*int(Row))-7,120+(15*int(Column))-7,3,3))
                            pygame.display.update()
                            run=False
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
            
    def CountBombs(Grid):
        count=0
        for Row in range(Dimensions):
            for Column in range(Dimensions):
                if Grid[Row][Column]=='*':
                    count+=1
        count=(Dimensions*Dimensions)-count
        return count
    
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
    
    
    