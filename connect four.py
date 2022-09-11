board=[[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
#creates the gameboard
def draw_board():
    top=""
    for i in range(0,len(board)):
      top+="  "+str(i+1)+" "
    print(top)
    print("#---"*7+"#") 
    for i in range(len(board)-1):
      print("|   |","|   |","|   |","|   |",sep="   ")
      print("| "+str(board[0][i])+" | "+str(board[1][i])+" | "+str(board[2][i])+" | "+str(board[3][i])+" | "+str(board[4][i])+" | "+str(board[5][i])+" | "+str(board[6][i])+" |")
      print("|   |","|   |","|   |","|   |",sep="   ")
      print("#---"*7+"#")
#checks if piece is valid
def isValid_piece(player):
  if player not in ["X","O"]:
    return 0
  else:
    return 1
#checks if column given by user is valid
def isValid_column(column):    
   if column not in [1,2,3,4,5,6,7]:
      return 0
   else:
     return 1
#Places the piece in the given column at the avaiable place starting from the bottom
def drop(column,player):
  if isValid_column(column)==0:
    print("Choose a valid column from 1 to 7.")
  if isValid_piece(player)==0:
    print("Invalid piece. Choose either 'X' or 'O'.")
  elif isValid_column(column)==1 and isValid_piece(player)==1:
    for i in range(5,-1,-1):
       if board[column-1][i]==" ":
          board[column-1][i]=player
          print("Placed an",player,"in column",column)
          draw_board()
          break
    else:
          print("This column is full. Choose a column from 1 to 7 which is not full")

def check_vertical(player):
  for i in range(len(board)):
    for j in range(3):
      if board[i][j]==player and board[i][j+1]==player and board[i][j+2]==player and board[i][j+3]==player:
        return True
def check_horizontal(player):
  for j in range(6):
    for i in range(4):
      if board[i][j]==player and board[i+1][j]==player and board[i+2][j]==player and board[i+3][j]==player:
        return True
def check_diagonal(player):
  #up to down
  for i in range(len(board)-3):
    for j in range(3):
      if board[i][j]==player and board[i+1][j+1]==player and board[i+2][j+2]==player and board[i+3][j+3]==player:
        return True
  #down to up
  for i in range(len(board)-3):
    for j in range(3,6):
      if board[i][j]==player and board[i+1][j-1]==player and board[i+2][j-2]==player and board[i+3][j-3]==player:
        return True
def available_columns():
  lst=[1,2,3,4,5,6,7]
  count=0
  for i in range(len(board)):
    for j in range(len(board)-1):
      if board[i][j]!=" ":
        count+=1
    if count==6:
      lst.remove(i+1)
    count=0
  return lst


def tie():
  flag=1
  for i in range(len(board)):
    for j in range(len(board)-1):
      if board[i][j]==" ":
        flag=0
        break
  if flag==1:
    return True
def end_game(player):
  if check_horizontal(player)==True or check_vertical(player)==True or check_diagonal(player)==True:
    return 1
  elif tie()==True:
    return 0
def play_game():
  print("WELCOME TO CONNECT4!!!")
  print("*-------------------RULES-----------------------*")
  print("The First player to get 4 of their pieces in the") 
  print("same row either horizontally,vertically or")
  print("diagonally WINS the game.")
  print("X goes FIRST!!!")
  print("*-----------------------------------------------*")

  end=False
  player="X"
  draw_board()
  while end==False:
    options=available_columns()
    print("Available columns:",options)
    column=int(input("It's "+player+"'s turn "+"Select a column from the above list:"))
    drop(column,player)
    if isValid_column(column)==0 or column not in options:
      continue
    if end_game(player)==1:
      print(player,"has WON the game!")
      end=True
    elif end_game(player)==0:
      print("It's a TIE!")
      end=True
    if player=="X":
      player="O"
    else:
      player="X" 
play_game()


  






  






  






  





  







      

  
