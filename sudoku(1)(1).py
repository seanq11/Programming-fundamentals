# import libraries here. Use the following ones only.
from ast import Break
import time, sys, random
import timeit

#def sudoku_game():
# add your implementation of the required functions here
def print_board(sudoku):
    for i in range(9):
        print(sudoku[i][0:3],'|',sudoku[i][3:6],'|',sudoku[i][6:9])
        if i==5 or i==2:
            print('-'*51)
            
if __name__ == '__main__':

    # Don't change the layout of the following sudoku examples
    sudoku1 = [
        [' ', '1', '5', '4', '7', ' ', '2', '6', '9'],
        [' ', '4', '2', '3', '5', '6', '7', ' ', '8'],
        [' ', '8', '6', ' ', ' ', ' ', ' ', '3', ' '],
        ['2', ' ', '3', '7', '8', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', ' ', ' ', ' ', ' ', '9', ' '],
        ['4', ' ', ' ', ' ', '6', '1', ' ', ' ', '2'],
        ['6', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '4', ' ', ' ', ' ', '1', ' ', '7'],
        [' ', ' ', ' ', ' ', '3', '7', '9', '4', ' '],
    ]
    sudoku2 = [
        [' ', ' ', ' ', '3', ' ', ' ', ' ', '7', ' '],
        ['7', '3', '4', ' ', '8', ' ', '1', '6', '2'],
        ['2', ' ', ' ', ' ', ' ', ' ', ' ', '3', '8'],
        ['5', '6', '8', ' ', ' ', '4', ' ', '1', ' '],
        [' ', ' ', '2', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', '8', ' ', ' ', '2', '5', '4'],
        [' ', '7', ' ', ' ', ' ', '2', '8', '9', ' '],
        [' ', '5', '1', '4', ' ', ' ', '7', '2', '6'],
        ['9', ' ', '6', ' ', ' ', ' ', ' ', '4', '5'],
    ]
    sudoku3 = [
        ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
        [' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
        [' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
        [' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
        [' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
        [' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
        [' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' '],
    ]
    sudoku4 = [
        [' ', '4', '1', ' ', ' ', '8', ' ', ' ', ' '],
        ['3', ' ', '6', '2', '4', '9', ' ', '8', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '7', ' '],
        [' ', ' ', ' ', '4', '7', ' ', '2', '1', ' '],
        ['7', ' ', ' ', '3', ' ', ' ', '4', ' ', '6'],
        [' ', '2', ' ', ' ', ' ', ' ', ' ', '5', '3'],
        [' ', ' ', '7', ' ', '9', ' ', '5', ' ', ' '],
        [' ', ' ', '3', ' ', '2', ' ', ' ', ' ', ' '],
        [' ', '5', '4', ' ', '6', '3', ' ', ' ', ' '],
    ]

    # make sure 'option=2' is used in your submission
    option = 2

    if option == 1:
        sudoku = sudoku1
    elif option == 2:
        sudoku = sudoku2
    elif option == 3:
        sudoku = sudoku3
    elif option == 4:
        sudoku = sudoku4
    else:
        raise ValueError('Invalid choice!')


#upadates the game board with the user's input
def update_board():
    #add user input into the x,y coordinate they chose
    sudoku[board_y][board_x] = input_num
    print_board(sudoku)


#check if full board is correct
def check_win():
    #if grid is correct stop and display time, moves and ask to play again
    def correct_grid():
        stop = timeit.default_timer()
        print("correct")
        print('Moves taken:', moves)
        print('CPU runtime:', stop - start) 
        play_again = input("Would you like to play again?: ")
        if play_again != "yes":
            choice_of_play()
        else:
            quit()
    #if grid is incorrect display time, moves and ask to play again
    def fail_grid():
        stop = timeit.default_timer()
        print("fail")
        print('Moves taken:', moves)
        print('CPU runtime:', stop - start) 
        play_again = input("Would you like to play again?: ")
        if play_again != "yes":
            quit()
        else:
            choice_of_play()

    #create new lists for the 3x3 squares
    columns = len(sudoku[0])
    rows = len(sudoku)
    #count = 0
    col = []
    square1 = []
    square2 = []
    square3 = []
    square4 = []
    square5 = []
    square6 = []
    square7 = []
    square8 = []
    square9 = []
    #append to the new lists
    for f in range(3):
        square1.append(sudoku[f][0])
        square1.append(sudoku[f][1])
        square1.append(sudoku[f][2])
        square2.append(sudoku[f][3])
        square2.append(sudoku[f][4])
        square2.append(sudoku[f][5])
        square3.append(sudoku[f][6])
        square3.append(sudoku[f][7])
        square3.append(sudoku[f][8])

    row1 = 3
    for g in range(3):
        square4.append(sudoku[row1][0])
        square4.append(sudoku[row1][1])
        square4.append(sudoku[row1][2])
        square5.append(sudoku[row1][3])
        square5.append(sudoku[row1][4])
        square5.append(sudoku[row1][5])
        square6.append(sudoku[row1][6])
        square6.append(sudoku[row1][7])
        square6.append(sudoku[row1][8])
        row1 = row1+1
    row2 = 6
    for h in range(3):
        square7.append(sudoku[row2][0])
        square7.append(sudoku[row2][1])
        square7.append(sudoku[row2][2])
        square8.append(sudoku[row2][3])
        square8.append(sudoku[row2][4])
        square8.append(sudoku[row2][5])
        square9.append(sudoku[row2][6])
        square9.append(sudoku[row2][7])
        square9.append(sudoku[row2][8])
        row2 = row2+1

    pass_count = 0
    #check if 3x3 grids comply with rules
    if len(list(set(square1))) == 9:
        if len(list(set(square2))) == 9:
            if len(list(set(square3))) == 9:
                if len(list(set(square4))) == 9:
                    if len(list(set(square5))) == 9:
                        if len(list(set(square6))) == 9:
                            if len(list(set(square7))) == 9:
                                if len(list(set(square8))) == 9:
                                    if len(list(set(square9))) == 9:
                                        pass_count += 1
    #check if columns and rows comply with rules
    for i in range(columns):
        col = []
        if len(list(sorted(set(sudoku[i])))) == 9:
            pass_count += 1
        for j in range(rows):
            col.append(sudoku[j][i])
            if len(col) == 9:
                if len(list(sorted(set(col)))) == 9:
                    pass_count += 1

                    
    #if whole grid complies with rules the user is correct
    if pass_count == 19:
        correct_grid()  
    else:
        fail_grid()    

#help the user with a square
def user_help():
    def is_possible(y,x,n):
        global grid
        n = str(n)
        #check rows
        for i in range(0,9):
            #print(grid[y][i])
            if sudoku[y][i] == n:
                #print('false')
                return False
        #check columns
        for i in range(0,9):
            if sudoku[i][x] == n:
                #print('false')
                return False
        #check 3x3 grids
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if sudoku[y0+i][x0+i] == n:
                    #print('false')
                    return False
        #print('true')
        return True
    global grid
    #look for empty space and try numbers from 1 to 9
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == ' ':
                for n in range(1,10):
                    n = str(n)
                    if is_possible(y,x,n):
                        print("try input number",n,"in position","x =",x+1,"y =",y+1)
                        #print(sudoku[y][x])
                        return
                #print('here')
                return

#code for human play
def human_play():
    global moves
    moves = 0
    global start
    start = timeit.default_timer()
    global hints_taken
    global hints_left
    hints_taken = 0
    hints_left = 4
    def ask_user():
        global board_x
        global board_y
        global input_num
        global hints_taken
        global hints_left
        #ask the user for an x and y coordinate and the number they would like to place
        print(hints_left,"hints left")
        ask_help = input("Enter 'h' for a hint: ")
        if ask_help == 'h':
            hints_taken+=1
            hints_left-=1
            if hints_taken >= 5:
                print("too many hints")
            else:
                user_help()
        board_x = int(input("Enter the x coordinate for your move: "))
        board_y = int(input("Enter the y coordinate for your move: "))
        input_num = int(input("Enter the number you want to input: "))
        input_num = str(input_num)
        board_y = board_y -1
        board_x = board_x -1
        global moves
        moves = moves + 1
        update_board()

    print_board(sudoku)
    board_complete = False
    global columns
    global rows
    columns = len(sudoku[0])
    rows = len(sudoku)

    #check if there is an empty space in the grid
    while board_complete == False:
        found = False
        for i in range(columns):
            for j in range(rows):
                if sudoku[j][i] == ' ':
                    found = True

                    break
            if found:
                break
        if found:
            ask_user()
        else:
            check_win()
            break

#code for computer play
def computer_play():
    print("Unsolved:")
    print_board(sudoku)
    start = timeit.default_timer()
    #check if a number is allowed in a certain spot
    def is_possible(y,x,n):
        global grid
        n = str(n)
        #check rows
        for i in range(0,9):
            #print(grid[y][i])
            if sudoku[y][i] == n:
                #print('false')
                return False
        #check columns
        for i in range(0,9):
            if sudoku[i][x] == n:
                #print('false')
                return False
        #check 3x3 grids
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if sudoku[y0+i][x0+i] == n:
                    #print('false')
                    return False
        #print('true')
        return True

    #place possible number in place + backtracking 
    def solve():
        global grid
        #look for empty space and try numbers from 1 to 9
        for y in range(9):
            for x in range(9):
                if sudoku[y][x] == ' ':
                    for n in range(1,10):
                        n = str(n)
                        if is_possible(y,x,n):
                            sudoku[y][x] = n
                            #print(sudoku[y][x])
                            solve()
                            sudoku[y][x] = ' '
                    #print('here')
                    return
        print(" ")
        print(" ")
        print("Solved:")
        print_board(sudoku)
        print(" ")
        stop = timeit.default_timer()
        print('CPU runtime:', stop - start) 
        print(" ")
        play_again = input("Would you like to play again?: ")
        if play_again != "yes":
            quit()
        else:
            choice_of_play()

    solve()

#check if user wants computer play or human play
def answer():
    if choice == "human play":
        moves = 0
        human_play()
    else:
        computer_play()

#user chooses human or computer play
def choice_of_play():
    while True:
        try:
            global choice
            choice = input("Human play or Computer play?: ")
        except ValueError:
            print("Try again")
            continue
        if choice == "Human play" or "human play" or "Computer play" or "computer play":
            break
        else:
            print("Try again")
            continue
    answer()
    

choice_of_play()


#sudoku_game()        
