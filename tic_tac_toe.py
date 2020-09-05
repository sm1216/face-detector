# The game board layout
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Add three Global variables as suggested by the Clever Programmer
game_still_going = True

winner = None

current_player = "X"


# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():

  display_board()

  while game_still_going:

    change_turn(current_player)

    check_if_game_over()

    flip_player()
  
  # Show winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Display the board to the screen
# Borrowed Clever Programmer's idea to add '1,2,3...9' number display alongside with the board display. 
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# Change a turn for an arbitrary player
def change_turn(player):

  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")


  # Borrowed Clever Programmer's idea to flip Valid option from True to False so that the player could alternate easily. 
  valid = False              
  while not valid:


    # Borrowed Clever Programmer's idea to add another layer of code to prevent a break when the entry is a not a number. 
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  board[position] = player

  display_board()


def check_if_game_over():
  check_for_winner()
  check_for_tie()


def check_for_winner():

  global winner

  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


def check_rows():

  global game_still_going

  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going = False

  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 

  else:
    return None


def check_columns():

  global game_still_going

  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  if column_1 or column_2 or column_3:
    game_still_going = False

  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 

  else:
    return None



def check_diagonals():

  global game_still_going

  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"

  if diagonal_1 or diagonal_2:
    game_still_going = False

  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]

  else:
    return None


def check_for_tie():

  global game_still_going

  if "-" not in board:
    game_still_going = False
    return True

  else:
    return False


# Flip the current player from X to O, or O to X
def flip_player():

  global current_player

  if current_player == "X":
    current_player = "O"
    
  elif current_player == "O":
    current_player = "X"


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()
