# l=[1,2,3,4,5,6,7,8]
# a = {0:[1,2,3],9:[2,3,45432]}
# a.get(9).append(123)
# a.update({9:[12,3,4]})
# print(a)
# it works!!!!!!!!!
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# initialize new board
def createBoard():
# board 1: easy one.
    board1 = [[1, 4, 2, 0, 9, 0, 0, 0, 5],
              [7, 0, 0, 4, 0, 0, 0, 8, 9],
              [8, 0, 5, 0, 0, 0, 0, 2, 4],
              [2, 0, 0, 0, 0, 4, 8, 0, 0],
              [0, 3, 0, 0, 0, 1, 2, 6, 0],
              [0, 8, 0, 0, 7, 2, 9, 4, 1],
              [0, 5, 0, 2, 0, 6, 0, 0, 0],
              [0, 2, 8, 0, 0, 9, 4, 1, 0],
              [0, 7, 9, 1, 0, 8, 5, 3, 0]]
# board 2: hard one.
    board2 = [[2, 0, 8, 0, 0, 7, 3, 0, 0],
              [0, 4, 0, 8, 0, 0, 0, 0, 0],
              [0, 7, 0, 0, 0, 0, 9, 6, 0],
              [0, 6, 5, 0, 0, 0, 0, 0, 0],
              [0, 3, 1, 0, 0, 0, 6, 0, 5],
              [0, 2, 9, 6, 0, 0, 0, 7, 0],
              [6, 9, 0, 0, 0, 0, 0, 2, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 5, 1, 0, 0, 6]]

# board 3: hard one.
    board3 = [[5, 0, 0, 0, 0, 0, 8, 0, 0],
              [8, 0, 0, 0, 1, 0, 4, 0, 6],
              [0, 0, 0, 0, 2, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 6, 0, 0],
              [0, 2, 0, 3, 8, 0, 0, 0, 9],
              [9, 6, 0, 0, 0, 0, 5, 7, 0],
              [0, 0, 0, 0, 0, 5, 0, 0, 0],
              [0, 0, 6, 8, 0, 7, 0, 1, 4],
              [0, 1, 0, 4, 0, 0, 0, 0, 8]]


# board 4: world's hardest one.
    board4 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 3, 6, 0, 0, 0, 0, 0],
              [0, 7, 0, 0, 9, 0, 2, 0, 0],
              [0, 5, 0, 0, 0, 7, 0, 0, 0],
              [0, 0, 0, 0, 4, 5, 7, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 3, 0],
              [0, 0, 1, 0, 0, 0, 0, 6, 8],
              [0, 0, 8, 5, 0, 0, 0, 1, 0],
              [0, 9, 0, 0, 0, 0, 4, 0, 0]]


    board5 = [[0, 0, 4, 0, 0, 8, 0, 0, 7],
              [0, 1, 0, 0, 4, 0, 0, 6, 0],
              [7, 0, 0, 6, 0, 0, 4, 0, 0],
              [3, 0, 0, 2, 0, 0, 6, 0, 0],
              [0, 7, 0, 0, 9, 0, 0, 8, 0],
              [0, 0, 9, 0, 0, 7, 0, 0, 1],
              [0, 0, 8, 0, 0, 1, 0, 0, 6],
              [0, 3, 0, 0, 5, 0, 0, 4, 0],
              [9, 0, 0, 3, 0, 0, 7, 0, 0]]
    return board5


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
            print("==================")

newBoard = createBoard()
printBoard()
# -------for non empty cells-----------------
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
def box(x, y):
    box=[]
    for i in range(x, x+3):
        for j in range(y, y+3):
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

# ------for empty cells----------
# find empty cells
def findEmptyCells():
    listEmptyCells = []
    for i in range(0,9):
        for j in range(0,9):
            if newBoard[i][j]==0:
                listEmptyCells.append(str(i)+","+str(j))
    return listEmptyCells

# --------update board-------------
def updateBoard(r, c, new_value):
    newBoard[r][c] = new_value

related = []
new_list = []
nl_2 = []
# list of possible value for each empty cell
# el is findEmptyCells()
# def allValuesForEmptyCell(r, c, l):
#     d = {}
#     d.update({(str(r)+str(c)): l})
#     return d
def irow(rx,cx,v,d):
    count_r=0
    for k in d.keys():
        ty = k.split(",")
        ry = int(ty[0])
        cy = int(ty[1])
        if ry == rx and cy != cx:
            if d[k].__contains__(v):
                count_r +=1
    return count_r
def icolumn(rx,cx,v,d):
    count_c=0
    for k in d.keys():
        ty = k.split(",")
        ry = int(ty[0])
        cy = int(ty[1])
        if ry != rx and cy == cx:
            if d[k].__contains__(v):
                count_c +=1
    return count_c

def ibox(x, y, v,d):
    count_b=0
    for k in d.keys():
        ty = k.split(",")
        ry = int(ty[0])
        cy = int(ty[1])
        if x<=ry and ry < x+3:
            if y <=cy and cy < y+3:
                if d[k].__contains__(v):
                    count_b+=1
    return count_b
def existsOnlyOnce(rx,cx,v,d):
    #check rows
    if irow(rx,cx,v,d) ==0:
        return True
    elif icolumn(rx,cx,v,d) ==0:
        return True
    else:
        r = 0
        while r < 9:
            c = 0
            while c < 9:
                if r <= rx and rx < r + 3:  # 0 <= 2 < 3
                    if c <= cx and cx < c + 3: # 6 <= 8 < 9
                        # box
                        if rx != r and cx != c:
                            if ibox(r,c,v,d) ==0:
                                return True
                c += 3
            r += 3
    return False

# while len(findEmptyCells()) != 0:
while range(len(findEmptyCells())) !=0:
    d = {}
    emptyCells = findEmptyCells()
    print(len(findEmptyCells()))
    for i in range(len(emptyCells)):
        index_emptyCells = emptyCells[i].split(",")
        rx = int(index_emptyCells[0])
        cx = int(index_emptyCells[1])
        r = 0
        related = []
        while r < 9:
            c = 0
            while c < 9:
                if r <= rx and rx < r+3:
                    if c <= cx and cx < c+3:
                        # box
                        related += box(r, c)
                        # column
                        related += column(cx)
                        # row
                        related += row(rx)
                c += 3
            r += 3
        for l in range(len(values)):
            if not related.__contains__(values[l]):
                new_list.append(values[l])
        d.update({(str(rx) +","+ str(cx)): new_list})  # allValuesForEmptyCell(rx, cx, new_list)
        new_list = []
    for keyx in d.keys():
        tt = keyx.split(",")
        rx = int(tt[0])
        cx = int(tt[1])
        if len(d[keyx]) == 1:
            updateBoard(rx, cx, d[keyx][0])
        elif len(d[keyx]) > 1:
            for i in range(len(d[keyx])):
                if existsOnlyOnce(rx,cx,d[keyx][i],d):
                    updateBoard(rx, cx, d[keyx][i])
    input()
    printBoard()
