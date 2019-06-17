values = [1,2,3,4,5,6,7,8,9]
# initialize new board
def createBoard():
#board1: easy one. it works!
    board1 = [[1, 4, 2, 0, 9, 0, 0, 0, 5],
             [7, 0, 0, 4, 0, 0, 0, 8, 9],
             [8, 0, 5, 0, 0, 0, 0, 2, 4],
             [2, 0, 0, 0, 0, 4, 8, 0, 0],
             [0, 3, 0, 0, 0, 1, 2, 6, 0],
             [0, 8, 0, 0, 7, 2, 9, 4, 1],
             [0, 5, 0, 2, 0, 6, 0, 0, 0],
             [0, 2, 8, 0, 0, 9, 4, 1, 0],
             [0, 7, 9, 1, 0, 8, 5, 3, 0]]
#board2: hard one.
    board2 = [[2, 0, 8, 0, 0, 7, 3, 0, 0],
             [0, 4, 0, 8, 0, 0, 0, 0, 0],
             [0, 7, 0, 0, 0, 0, 9, 6, 0],
             [0, 6, 5, 0, 0, 0, 0, 0, 0],
             [0, 3, 1, 0, 0, 0, 6, 0, 5],
             [0, 2, 9, 6, 0, 0, 0, 7, 0],
             [6, 9, 0, 0, 0, 0, 0, 2, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 5, 1, 0, 0, 6]]
    return board2


# print board
def printBoard():
    print("__________________")
    for i in range(len(newBoard)):
        for j in range(len(newBoard[i])):
            if j == 2 or j == 5 or j == 8:
                print(newBoard[i][j],end='|')
            else:
                print(newBoard[i][j],end='|')
        print('')
        if i == 2 or i == 5 or i == 8:
            #print("__________________")
            print("==================")


newBoard = createBoard()
printBoard()
#-------for non empty cells-----------------
# boxes:
# from 00,01,02,10,11,12,20,21,22
# from 03,04,05,13,14,15,23,24,25
# from 06,07,08,16,17,18,26,27,28
# from 30,31,32,40,41,42,50,51,52
# from 33,34,35,43,44,45,53,54,55
# from 36,37,38,46,47,48,56,57,58
# from 60,61,62,70,71,72,80,81,82
# from 63,64,65,73,74,75,83,84,85
# from 66,67,68,76,77,78,86,87,88
def box(x,y):
    box=[]
    for i in range(x,x+3):
        for j in range(y,y+3):
            box.append(newBoard[i][j])
    return box

# columns:
# from 00,08
# from 10,18
# from 20,28
# from 30,38
# from 40,48
# from 50,58
# from 60,68
# from 70,78
# from 80,88
def column(c):
    column=[]
    for r in range(0,9):
        column.append(newBoard[r][c])
    return column
#
# rows:
# from 00,80
# from 01,81
# from 02,82
# from 03,83
# from 04,84
# from 05,85
# from 06,86
# from 07,87
# from 08,88
def row(r):
    row=[]
    for c in range(0,9):
        row.append(newBoard[r][c])
    return row

#------for empty cells----------
# find empty cells
def findEmptyCells():
    listEmptyCells = []
    #listNonEmptyCells = []
    for i in range(0,9):
        for j in range(0,9):
            if newBoard[i][j]==0:
                listEmptyCells.append(str(i)+","+str(j))
    return listEmptyCells
#--------update board-------------
def updateBoard(r,c,new_value):
    newBoard[r][c]=new_value

related=[]#this needs to be a dictionary, or not nevermind???
new_list=[]
counter =0
nl_2=[]
# list of possible value for each empty cell
# el is findEmptyCells()
def allValuesForEmptyCell(r,c,l):
    d = {}
    d.update({(str(r)+str(c)):l})
    return d

while len(findEmptyCells()) !=0:
    emptyCells = findEmptyCells()
    for i in range(len(emptyCells)):
        index_emptyCells = emptyCells[i].split(",")
        rx = int(index_emptyCells[0])
        cx = int(index_emptyCells[1])
        if newBoard[rx][cx] == 0:
            r = 0
            related = []
            while r < 9:
                c = 0
                while c < 9:
                    if r <= rx and rx < r+3:
                        if c <= cx and cx < c+3:
                            #box
                            related+=box(r,c)
                            #column
                            related+=column(cx)
                            #row
                            related+=row(rx)
                    c+=3
                r+=3
            for l in range(len(values)):
                if not related.__contains__(values[l]):
                    new_list.append(values[l])
                    counter+=1
            vv = allValuesForEmptyCell(rx, cx, new_list)
            nl_2.append(vv)
            if counter ==1:
        # we update board to include new value
                updateBoard(rx,cx,new_list[0])
                print(str(rx)+str(cx)+"-> "+str(new_list[0]))
                print(len(findEmptyCells()))
        #        emptyCells.remove(index_emptyCells)
        #        printBoard()
            new_list=[]
            counter=0
    input()
    printBoard()

# it works only for simple ones!
# need to do more...
