'''

You are running a gravity simulation involving falling boxes and exploding obstacles. The scenario is represented by a rectangular matrix of characters board.

Each cell of the matrix board contains one of three characters:

'-', which means that the cell is empty;
'*', which means that the cell contains an obstacle;
'#', which means that the cell contains a box.
The boxes all fall down simultaneously as far as possible, until they hit an obstacle, another grounded box, or the bottom of the board. If a box hits an obstacle, the box explodes, destroying itself and any other boxes within eight cells surrounding the obstacle. All the explosions happen simultaneously as well.

Given board, your task is to return the state of the board after all boxes have fallen.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(board[0].length · board.length^2) will fit within the execution time limit.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.char board

A matrix that shows where the boxes and obstacles are located. The matrix consists only of characters '-', '*', and '#'.

Guaranteed constraints:
3 ≤ board.length ≤ 100,
3 ≤ board[i].length ≤ 100.

[output] array.array.char

Return a matrix representing the state of the board after all of the boxes have fallen.

'''

def print_board(b) :
# {
    for row in b :
    # {
        print(' '.join(row))
    # }

    print()

# }

def process_board(b) :
# {
    bumper = len(b[0]) # most recent stop line
    print_board(b)  # os.system('cls')
    
    for y in range(len(b) - 1) : # start from first column
    # {
        for x in range(len(b[0]) - 1, -1, -1) : # start from last row
        # {
            cur = b[x][y]

            if (cur == '-') :
            # {
                None
            # }

            elif (cur == '*') :
            # {
                bumper = x
            # }

            elif (cur == '#') :
            # {
                for i in range(x, bumper) :
                # {                   
                    nxt = b[i + 1] [y]
                    print("i: ", i, "cur: ", cur, " nxt: ", nxt, " bumper: ", bumper)

                    if (nxt == '#') :
                    # {
                        bumper = i + 1
                        i = bumper # exit loop
                    # }

                    elif (nxt == '*') :
                    # {
                        b[i] [y] = '-'
                        bumper = i + 1
                        i = bumper # exit loop
                    # }

                    elif (nxt == '-') :
                    # {
                        # b[i] [y] = '-'

                        if (i == bumper - 1) : # last row
                        # {
                            b[i] [y] = '-'
                            b[i + 1] [y] = '#'
                            # bumper = i + 1
                            # i = bumper # exit loop
                        # }

                        else :
                        # {
                            b[i] [y] = '-'
                            b[i + 1] [y] = '#'
                        # }
                        
                    # }

                    else :
                    # {
                        None
                    # }

                # }
            
            # }

            else :
            # {
                None
            # }

        # }

    # }

    print_board(b)
    
# }

def solution(board) :
# {           
    process_board(board)
# }

board = [['#', '-', '#', '#', '*'],
            ['#', '-', '-', '#', '#'],
            ['-', '#', '-', '#', '-'],
            ['-', '-', '#', '-', '#'],
            ['#', '*', '-', '-', '-'],
            ['-', '-', '*', '#', '-']]  

solution(board)

'''

***** BONEYARD *****

solution(board) = [['-', '-', '-', '-', '*'],
                   ['-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-'],
                   ['-', '*', '-', '-', '#'],
                   ['#', '-', '*', '-', '#']]
                   
board dimensions doesnt matter
column based
change each column, make row
    send column, return clean one
each row, move right
store row
change back to column  


    # print('!')
    # print(len(b[1]))
    
    # tmp_row = list()
    
    # for i in range(b) :
    # {
        # tmp_row = list()
        
        # for j in range(b[0]) :
        # {
            # print(b[i][j])
            # tmp_row.append(j)
        # }
        
        # print(tmp_row)
        
    # }
                     
    # print(b[2][2])      
    
# print(j, i)
            # print(b[j])   
            
# tmp_row = list()
        print(tmp_row)   
        
up to down      

tmp_row = list()         

# print(tmp_row)          

tmp_row.append(b[i][j])  

# print(x, y)
        # tmp_row = list()
        
for i in range(len(b) - 1) :
    # {
        for j in range(len(b[0])) :
        # {
            
            next_cell_down = b[x + 1][y]
            # print(x, y, b[x][y])
            
            if (b[x][y] == '*') :
            # {
                x = x - 1    # move up one row, we have a block
            # }
            
            elif (b[x][y] == '#') :
            # {
                print('#', x, y)
            # }
            
            elif (b[x][y] == '-' and next_cell_down == '#') :
            # {
                None  # move up one row, we have a blank
            # }
            
            else :
            # {
                None
            # }
            
            x = x - 1
            
        # }
    
        y = y + 1
        
    # }          

    # tmp_row = list()
    # y_max = len(b[0]) - 1
    x_max = len(b) - 1

# x = len(b) - 1
    # y = 0

    
def simulate_column(c) :
# {
    None
# }


                    # tmp = cur
                    # tmp = b[i][y]

# bumper = x

# print(x, y)                    

'''