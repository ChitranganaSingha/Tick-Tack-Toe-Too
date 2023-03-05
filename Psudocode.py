
# board= ["X","X","X","X","X","X","X","X","X"]
# board= ["O","O","O","O","O","O","O","O","O"]
board= ["-","-","-","-","-","-","-","-","-"]

def displayBoard():
    print( board[0],"|",board[1],"|",board[2]  )
    print( board[3],"|",board[4],"|",board[5]  )
    print( board[6],"|",board[7],"|",board[8]  )

def inputerOutputer():
    try:
        move= int(input("Enter Move:"))-1
        StorageCurrentState(move)
    except:
        print("Invalid Input Please Retry")
        inputerOutputer()
    
    
def StorageCurrentState(usersMove):
    # user move valid or not
    if ValidMove(usersMove):
        board[usersMove]= "X"
    else:
        print("Not valid move")
        
    pass

def ValidMove(newMove):
    if board[newMove]== "-":
        return True
    else:
        return False 


def EndGameOrNot():
    pass

def Gameretstarter():
    pass


# mainGameRunner 

def TesterFunctionInputting():
    # 1. Print current state of board
    # print(board)
    # 2. Take new position for board
    inputerOutputer()
    # 3. Print new board 
    displayBoard()
     
while True:
    TesterFunctionInputting()  




# Alt Shift up down
# clt d
# cls
