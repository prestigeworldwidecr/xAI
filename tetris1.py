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

def detonate(board, ol) :
# {
    for i, j in ol :
    # {
        # all surrounding boxes explode
        if (type(board[i][j]) is tuple) :
        # {            
            board[i][j] = '*'

            # left
            if (j - 1 >= 0 and board[i][j - 1] == '#') :
            # {
                board[i][j - 1] = '-'
            # }

            else :
            # {
                None
            # }
                
            # up-left
            if (i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == '#') :
            # {
                board[i - 1][j - 1] = '-'
            # }

            else :
            # {
                None
            # }

            # up
            if (i - 1 >= 0 and board[i - 1][j] == '#') :
            # {
                board[i - 1][j] = '-'
            # }

            else :
            # {
                None
            # }
            
            # up-right
            if (i - 1 >= 0 and j + 1 < len(board[0]) and board[i - 1][j + 1] == '#') :
            # {
                board[i - 1][j + 1] = '-'
            # }

            else :
            # {
                None
            # }

            # right
            if (j + 1 < len(board[0]) and board[i][j + 1] == '#') :
            # {
                board[i][j + 1] = '-'
            # }

            else :
            # {
                None
            # }
            
            # down-right
            if (i + 1 > len(board) and j + 1 < len(board[0]) and board[i + 1][j + 1] == '#') :
            # {
                board[i + 1][j + 1] = '-'
            # }

            else :
            # {
                None
            # }

            # down
            if (i + 1 > len(board) and board[i + 1][j] == '#') :
            # {
                board[i + 1][j] = '-'
            # }

            else :
            # {
                None
            # }
            
            # down-left
            if (i + 1 < len(board) and j - 1 >= 0 and board[i + 1][j - 1] == '#') :
            # {
                #print('!')
                board[i + 1][j - 1] = '-'
            # }

            else :
            # {
                None
            # }

        # }

        else :
        # {
            None
        # }

    # }

    return board

# }

def obstacle_locations(board) :
# {
    ol = []

    for row in range(len(board)) :
    # {
        try :
        # {
            column = board[row].index('*')
            ol.append((row, column))
        # }
        
        except :
        # {
            None
        # }

    # }

    return ol

# }

def row_step_down(board, row) :
# {
    for j in range(len(board[0])) :
    # {
        if (board[row][j] == '#') :
        # {            
            if (board[row + 1][j] == '-') :
            # {
                board[row + 1][j] = board[row][j]
                board[row][j] = '-'
            # }

            elif (board[row + 1][j] == '*') :
            # {
                board[row + 1][j] = (board[row][j], board[row + 1][j])
                board[row][j] = '-'
            # }

            # thud
            elif (board[row + 1][j] == '#') :
            # {
                None
            # }

            else :
            # {
                None 
            # }

        # }
        
        else :
        # {
            None            
        # }

    # }

    return board

# }

def print_board(board) :
# {
    for r in range(len(board)) :
    # {
        print(board[r])
    # }

# }

def run_gravity_simulation(board) :
# {
    max_x = len(board) - 2
    min_x = -1
    ol = obstacle_locations(board)
    
    while (max_x > min_x) :
    # {
        for i in range(max_x, min_x, -1) :
        # {
            board = row_step_down(board, i)
        # }

        board = detonate(board, ol)
        min_x = min_x + 1

    # }

    return board

# }

def solution(board) :
# {
    run_gravity_simulation(board)

    return board

# }

board = [['#', '-', '#', '#', '*'],
        ['#', '-', '-', '#', '#'],
        ['-', '#', '-', '#', '-'],
        ['-', '-', '#', '-', '#'],
        ['#', '*', '-', '-', '-'],
        ['-', '-', '*', '#', '-']]  

print_board(board)
print()
print_board(solution(board))

# 

'''

***** BONEYARD *****

solution(board) = [['-', '-', '-', '-', '*'],
                   ['-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-'],
                   ['-', '*', '-', '-', '#'],
                   ['#', '-', '*', '-', '#']]

# or board[i][j] == '*') :
                   
# print(ol)

# print(max_x)

# print(row, j, len(board), len(board[5]), board[row + 1][j])

# if(row == 2) :
# {
# print("!!!")
# }

# else :
# {
    # None
# }
                    

board = row_step_down(board, 4)
print_board(board)
print()
board = row_step_down(board, 3)
print_board(board)
print()
board = row_step_down(board, 2)
print_board(board)
print()
board = row_step_down(board, 1)
print_board(board)
print()
board = row_step_down(board, 0)
print_board(board)
print()
board = detonate(board, ol)
print_board(board)
print()
board = row_step_down(board, 4)
print_board(board)
board = row_step_down(board, 3)
print_board(board)
# print(len(board[3]))
print()
board = row_step_down(board, 2)
print_board(board)
print()
board = row_step_down(board, 1)
print_board(board)
print()
board = detonate(board, ol)
print_board(board)
print()
                   
# for i in range(len(board) - 2, min_x, -1) :
# {
# }

if (i == 4 and j == 1) :
# {
    print("!!", i + 1, j - 1, i + 1 < len(board), j - 1 >= 0)
# }

else :
# {
    None
# }

        
# ol = obstacle_locations(board)

# print(ol)

# print("*****BOOM*****")


# print("!!", i, j, board[i][j], len(ol), type(board[i][j]))

                           

detonate = False


# detonate = True

if (detonate) :
# {
    detonate(board)
# }

else :
# {
    None
# }


# print(row)

# print (row, j)


# print("hi1", row + 1, j)
# print("hi2", row + 1, j)

# print("h3", row + 1, j)

# print("hi5", row + 1, j)

print()
board = row_step_down(board, 3)
board = evaluate_board(board, ol)
print_board(board)
print()
board = row_step_down(board, 2)
board = evaluate_board(board, ol)
print_board(board)
print()
board = row_step_down(board, 1)
board = evaluate_board(board, ol)
print_board(board)
print()
board = row_step_down(board, 0)
board = evaluate_board(board, ol)
print_board(board)
print()


# run_gravity_simulation()

# print(obstacle_locations(board))


# print_board(board)

    

print()
# row_step_down(board, 3)
print()
# row_step_down(board, 2)
print()
# row_step_down(board, 1)
print()
# row_step_down(board, 0)
print()

# evaluate_board(board)

# row_step_down(board, 4)
print()
# row_step_down(board, 3)
print()
# row_step_down(board, 2)
print()
# evaluate_board(board)

def evaluate_board(board) :
# {
    for i in range(len(board)) :
    # {
        for j in range(len(board[0])) :
        # {
            # all surrounding boxes explode
            
            if (type(board[i][j]) is tuple or board[i][j] == '*') :
            # {
                # print(i, j)

                board[i][j] = '*'

                # left
                if (j - 1 >= 0 and board[i][j - 1] == '#') :
                # {
                    board[i][j - 1] = '-'
                # }

                else :
                # {
                    None
                # }
                    
                # up-left
                if (i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == '#') :
                # {
                    board[i - 1][j - 1] = '-'
                # }

                else :
                # {
                    None
                # }

                # up
                if (i - 1 >= 0 and board[i - 1][j] == '#') :
                # {
                    board[i - 1][j] = '-'
                # }

                else :
                # {
                    None
                # }
                
                # up-right
                if (i - 1 >= 0 and j + 1 < len(board[0]) and board[i - 1][j + 1] == '#') :
                # {
                    board[i - 1][j + 1] = '-'
                # }

                else :
                # {
                    None
                # }

                # right
                if (j + 1 < len(board[0]) and board[i][j + 1] == '#') :
                # {
                    board[i][j + 1] = '-'
                # }

                else :
                # {
                    None
                # }
                
                # down-right
                if (i + 1 > len(board) and j + 1 < len(board[0]) and board[i + 1][j + 1] == '#') :
                # {
                    board[i + 1][j + 1] = '-'
                # }

                else :
                # {
                    None
                # }

                # down
                if (i + 1 > len(board) and board[i + 1][j] == '#') :
                # {
                    board[i + 1][j] = '-'
                # }

                else :
                # {
                    None
                # }
                
                # down-left
                if (i + 1 > len(board) and j - 1 >= 0 and board[i + 1][j - 1] == '#') :
                # {
                    print('!')
                    board[i + 1][j - 1] = '-'
                # }

                else :
                # {
                    None
                # }

            # }

            else :
            # {
                None
            # }
        # }

    # }

    print()
    print_board(board)

# }

if (1) :
# {
    None
    # board[i].index('*')
# }


def run_gravity_simulation() :
# {
    max_x = 6
    max_y = 5

    for i in range(max_x) :
    # {
        for j in range(max_y - 1, -1, -1) :
        # {
            print(j)
        # }

        max_y = max_y - 1

    # }

# }


print("hi")
# up
if (0 < i < len(board) - 1 and 0 < j < len(board[0]) - 1) :
# {

# }

# down
# left
# right

if (board[row][j] == '#') :
# {

    if (board[row + 1][j] == '#') :
    # {
        board[row + 1][j] = '-'
    # }

    elif (board[row + 1][j] == '*') :
    # {
        board[row + 1][j] = (board[row][j], board[row + 1][j])
    # }
    
    else :
    # {
        # board[row + 1][j] = (board[row][j], board[row + 1][j])
        board[row + 1][j] = board[row][j]
    # }
    
    board[row][j] = '-'
# }

else :
# {
    None
# }

elif (board[row][j] == '#' and board[row][j + 1] == '#') :
            # {
                board[row][j] = '-'
                board[row + 1][j] = '-'
            # }

    # print(board[row][j])
            
            
    # print_board(board)

# print(row)
    
    # start from bottom, board height - 1
    



def place_bombs(board) :
# {
    
# }

active_board = [['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-']]  

active_board = [['-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-']]  
    
    


'''