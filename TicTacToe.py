Import tkinter as tk
From tkinter import ttk 

super_board =[]
for _ in range(3):
	row =[]
	for _ in range(3):
		row.append()

	super_board.append(row)
mini_boards =[]
for _ in range(3):
	board =[]
	for _ in range3:
		min_board =[]
		for _ in range3:
			row =[]
			for i in range3:
				row.appemd(“”)
			mini_board.append(row)
		board.append)mini_board
	mini_boards.append(board)

Def check_Winner(board):
	for i in range(3):
		if board[i][0] == board [i][1] ==board[i][2] != “”
			return board[i][0]
		if board[0][i]
			return board[0][i]

	if all(board[i][j] != “” for i in range(3) for j in range(3)):
		return “Tie”

	return “”
#Check_super_winner():

Def check_super_winner()
	winner = checkwinner superboard
	return winner

#Command function

def make_move(bi, bj, i, j, buttons, turn_label):
    global x_turn, next_board, over
	  
	button = buttons[bi][bj][i][j]
	button[“text”] = “X” if x_turn else “0”
	button[“state”] = “disabled”
	miniboard[i][j]. = “X”  if x_turn else =“0”
	button[“state”]
	





 
Window = tk.Tk()
Window.title(“Ultimate tic tac toe”)
Window.geometry(“1000 x1000”)

Title_label = ttk.Label(window, test = “Knight Hacks Tkinter”, dont = (“Calibri”, 18, “bold”)

Title_label.pack(paddy = 20, pads =20)
Desc_label = ttk.Label(window, text = “A 3x3 game of Tic Tac Toe”, font= “Calibri”, 18))
Desc_label.pack()
Turn_label = ttk.Label(window, text =“X’s turn”, font = (“Calibri”, 18))
Turn_label.pack(padx=10, paddy =10)

Buttons =[[[[] for _in range(3)] for _in range(3) for _in range(3)]
 
For bi in range(3):
	for bj in range(3):
		
		mini_frame = ttk.Frame() 
		mini_frame.grid(row =bi, column =bj, padx =10, pady=10) #padding doesnt work in grid
		for i in range(3):
			for j in range(3):
				#Create the button
				button = ttk.Button(mini_frame, text =‘’)
				button.grid(row=i, column =j)
				buttons[bi][bj][i].append(button)

