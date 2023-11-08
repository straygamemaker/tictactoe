def prettyPrintGrid(g):
 
    for row in g:
        for col in row:
            print(col, end = ' ')
        print()

def isFull(b):
    for row in b:
        if "*" in row:
            return(False)
    return(True)
    
def isWinner(b):

    winner = False
   
    for r in range(3):
        if( b[r][0] != '*') and (b[r][0] == b[r][1] == b[r][2]):
                winner = True
    
    for c in range(3):
        if( b[0][c] != '*')and (b[0][c] == b[1][c]  == b[2][c]):
                winner = True        
   
    if( b[1][1] != '*'):
        if (b[0][0] == b[1][1] == b[2][2]):
            winner = True
        elif (b[0][2] == b[1][1] == b[2][0]):
            winner = True
    return(winner) 