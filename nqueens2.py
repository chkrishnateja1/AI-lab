N=int(input("enter no.of queens"))
def printsolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                print("Q",end=" ")
            else:
                print("-",end=" ")
        print()
def issafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
         if board[i][j]==1:
             return False
    return True
def solveNQuntil(board,col):
    if col>=N:
        return True
    for i in range(N):
        if issafe(board,i,col):
            board[i][col]=1
            if solveNQuntil(board,col+1)==True:
                return True
            board[i][col]=0
    return False
board=[]
for i in range(N):
    b=[]
    for j in range(N):
        b.append(0)
    board.append(b)
if solveNQuntil(board,0)==False:
    print("solution doesnot exist")
else:
    printsolution(board)
        
            
