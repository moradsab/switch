import random


def create_board():
  values=[i for i in range(1,19)]*2
  random.shuffle(values)
  board=[]
  for r in range(6):
    row=[]
    for c in range(6):
      row.append({"value": str(values.pop()), "open" : False })
    board.append(row)
  return board

def print_board(board):
  for i in range(6):
    row=""
    for j in range(6):
      if(board[i][j]["open"]==True):
        row += " " + board[i][j]["value"] + " "
      else:
        row+=" # "
    print(row)

def get_user_input():
  while True:
    try:
      user_input = input("enter row and column number between 1-6 without space ")
      row, col = int(user_input[0]) - 1, int(user_input[1]) - 1
      if 0 <= row < 6 and 0 <= col < 6 and len(user_input)==2:
        return row, col
      else:
        raise ValueError()
    except ValueError:
      print("Invalid input. Try again.")

def game():
  open=0
  board=create_board()
  
  print("Find all pairs")
  
  while open<17:

    print_board(board)

    #get first input
    r1,c1=get_user_input()
    if board[r1][c1]['open']:
        print("This cell is already open.")
        continue
    board[r1][c1]['open']=True
    
    print_board(board)

    #get second input
    r2,c2=get_user_input()
    if (r1, c1) == (r2, c2) or board[r2][c2]['open']:
      print("This cell is already open.")
      board[r1][c1]['open'] = False
      continue
    board[r2][c2]['open'] = True
        
    print_board(board)

    #if matched change to open cells
    if board[r1][c1]['value']==board[r2][c2]['value']:
      print("Matched")
      board[r2][c2]['open']=True
      open+=1
    else:
      print("Not matched")
      board[r1][c1]['open']=False
      board[r2][c2]['open']=False

  print("Found all pairs")
  print_board(board)

if __name__ == "__main__":
    game()
