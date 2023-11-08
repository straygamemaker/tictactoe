def main(): 
    griddd = [['*','*','*'], 
              ['*','*','*'], 
              ['*','*',*'*']]
    
    total = 0

    while isFull(griddd) == False and isWinner(griddd) == False:
        prettyPrintGrid(griddd)
        

        if total %2 == 0:
            player = "x"
            print("Player x, your turn. Remember, you're counting from 0. Top row = 0, second row = 1, bottom row = 2.")
        else:
            player = 'o'
            print("Player o, your turn. Remember, you're counting from 0. Top row = 0, second row = 1, bottom row = 2.")

            #isFull()
            #isWinner()

        rowInput = int(input("Which row would you like to enter? 0-2 ? "))
        columnInput = int(input("Which column would you like? 0-2 ? "))
        #checkifspacetaken(griddd)

        total += 1
        

        griddd[rowInput][columnInput] = player


#def checkifspacetaken():
    #if griddd 

def prettyPrintGrid(g):

    for row in g:
        for col in row:
            print(col, end = ' ')
        print()

def isFull(b):
    for row in b:
        if "*" in row:
            return(False)
            print("That's already full!")
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
            print("We have a winner! ")
    return(winner)

main()
