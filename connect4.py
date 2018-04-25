class Cell(object):
    def __init__(self,is_empty=True,val='-',x=-1,y=-1):
        self.is_empty=is_empty
        self.val=val
        self.x,self.y=x,y

    def render(self):
        player=self.val
        if not(self.is_empty):
            return 'R' if player=='R' else 'Y'
        return ' '

class Player(object):
    def __init__(self,val):
        if val==1:
            self.val='R'
        else:
            self.val='Y'

class Game(object):
    def __init__(self,cols=7,rows=6):
        self.cols=cols
        self.rows=rows
        self.board=[[Cell() for col in range(self.cols)] for row in range(self.rows)]

    def validateCell(self,x,y,val):
        if  x<self.rows:
            if  y<self.cols:
                if self.board[x][y].val==val:
                    #print("True Value for: ",x,y)
                    return True
        return False

    def getCell(self,col):
        if col>6 or col<0:
            print("Wrong Column Entered")
            return -1
        i=-1
        while(not(self.validateCell(i,col,'-'))):
            i-=1
            if i==-(self.rows+1):
                print("Column Full, choose another value")
                return [9,9]
        print("Cell: ",self.rows+i,col)
        return [self.rows+i,col]


    def makeTurn(self,col,player):
        x,y=self.getCell(col)
        if x==9:
            return 9
        self.board[x][y].val=player.val
        #print("CHECKWIN")
        if self.checkWin(player.val,x,y):
            return 1
        return 0

    def checkWin(self,val,x,y):
        row=self.checkRows(player.val,x,y)
        #print("ROW CHECK: ",row)

        col=self.checkCols(player.val,x,y)
        #print("COL CHECK: ",col)

        posDiag=self.checkPosDiag(player.val,x,y)
        #print("POSDIAG CHECK: ",posDiag)

        negDiag=self.checkNegDiag(player.val,x,y)
        #print("NEGDIAG CHECK: ",negDiag)

        if row or col or posDiag or negDiag:
            print("Player :"+str(player.val)+" Wins")
            return True
        return False

    def checkRows(self,val,x,y):
        i,j=1,1
        count=0
        while(self.validateCell(x,y-i,val) or self.validateCell(x,y+j,val)):
            if self.validateCell(x,y-i,val):
                count+=1
                i+=1
            if self.validateCell(x,y+j,val):
                count+=1
                j+=1
        if count>=3:
            return True
        return False

    def checkCols(self,val,x,y):
        i,j=1,1
        count=0
        while(self.validateCell(x-i,y,val) or self.validateCell(x+j,y,val)):
            if self.validateCell(x-i,y,val):
                count+=1
                i+=1
            if self.validateCell(x+j,y,val):
                count+=1
                j+=1
        if count>=3:
            return True
        return False

    def checkPosDiag(self,val,x,y):
        i,j=1,1
        count=0
        while(self.validateCell(x+i,y+i,val) or self.validateCell(x-j,y-j,val)):
            if self.validateCell(x+i,y+i,val):
                count+=1
                i+=1
            if self.validateCell(x-j,y-j,val):
                count+=1
                j+=1
        if count>=3:
            return True
        return False

    def checkNegDiag(self,val,x,y):
        i,j=1,1
        count=0
        while(self.validateCell(x+i,y-i,val) or self.validateCell(x-j,y+j,val)):
            if self.validateCell(x+i,y-i,val):
                count+=1
                i+=1
            if self.validateCell(x-j,y+j,val):
                count+=1
                j+=1
        if count>=3:
            return True
        return False

    def printBoard(self):
        for r in range(self.rows):
            col=''
            for c in range(self.cols):
                col+=self.board[r][c].val + '   '
            print(col)


if __name__=='__main__':
    print("CONNECT4")
    game=Game()
    player1=Player(1)
    print("Player One Color: Red(R)")
    player2=Player(2)
    print("Player Two Color: Yellow(Y)")
    temp=input("Enter first Player Color (R/Y): ")
    if temp=='R':
        turn=1
        player=player1
    else:
        turn=2
        player=player2
    game.printBoard()
    while(True):
        chance=turn%2
        print("Player: "+str(player.val)+" chance")
        col=int(input("Enter column number to place turn(1-7)"))-1
        cont=game.makeTurn(col,player)
        if cont==1:
            break
        if cont==9:
            continue
        game.printBoard()
        if player==player1:
            player=player2
        else:
            player=player1

    if cont:
        game.printBoard()
