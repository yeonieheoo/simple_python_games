
import random
import os
board = []
alphabet_column ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chr_str = ["X", "O", "V", "H", "M"]

def is_invalid(choice):
	return (choice == "") or (choice not in alphabet_column) or (choice.islower() == True) or (alphabet_column.find(choice) >= number_col) or (board[0][alphabet_column.find(choice)] != "   ")

num_players = int(input("Enter a number of players (2~5): "))

# setting the grid
number_row = input("Enter a number of rows: ")
checkrow = True
while (checkrow == True):
	checkrow = False
	if not number_row.isdigit(): 
		print("You entered an invalid number of row!")
		number_row = input("Please enter a valid digit: ")
		checkrow = True 

number_col = input("Enter a number of columns: ")
checkcol = True
while (checkcol == True):
	checkcol = False
	if not number_col.isdigit():
		print("You entered an invalid number of row!")
		number_col = input("Please enter a valid digit: ")
		checkcol = True 

number_col = int(number_col)
number_row = int(number_row)

# make board
for row in range(number_row):
	row_list = []
	for col in range(number_col):
		row_list.append("   ")
	board.append(row_list)

for col in range(number_col):
	print("   " + alphabet_column[col], end="")

# print first line of board
print("\n +" + "---+" * number_col)

# display board
for row in range(number_row):
	print(" |", end="")
	for col in range(number_col):
		print(board[row][col] + "|", end="")
	print("\n +" + "---+" * number_col)

# setting
turn = random.randint(0, (int(num_players) - 1))
current_chr = chr_str[turn]
print("Player " + current_chr + "'s turn!")

col_empty = True

# play game
game_over = False

while not game_over:
	choice = input("Enter a column to place a check: ")
	column_index = alphabet_column.find(choice)
	
	while is_invalid(choice):
		print("You entered an invalid coordinate!")
		choice = input("Enter a valid coordinate column (ex: A, B, C): ")

	choice_index = alphabet_column.find(choice)

	# change the check
	current_chr = chr_str[turn]


	for row in range(number_row-1):
		if board[row+1][choice_index] != "   ":
			board[row][choice_index] = " " + current_chr + " "
			col_empty = False
			break

	print(col_empty)

	if col_empty: 
		board[number_row-1][choice_index] = " " + current_chr + " "
	
	col_empty = True

	# print the board 
	for col in range(number_col):
		print("   " + alphabet_column[col], end="")
	print("\n +" + "---+" * number_col)

	for row in range(number_row):
			print(" |", end="")
			for col in range(number_col):
				print(board[row][col] + "|", end="")
			print("\n +" + "---+" * number_col)


	# check 4 in a row 
	for row in range(number_row):              # check horizontally
		for col in range(number_col - 3):
			if board[row][col] == " " + current_chr + " ":
				if board[row][col+1]==" " + current_chr + " " and board[row][col+2]==" " + current_chr + " " and board[row][col+3]==" " + current_chr + " " and " " + current_chr + " ":
					game_over = True

	for col in range(number_col):
		for row in range(number_row - 3):      # check vertically
			if board[row][col] == " " + current_chr + " ":
				if board[row+1][col] == board[row+2][col] == board[row+3][col] == " " + current_chr + " ":
					game_over = True

	for row in range(number_row - 3):          # check diagonally 
		for col in range(3, number_col):
			if board[row][col] == " " + current_chr + " ":
				if board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] == " " + current_chr + " ":
					game_over = True

	for row in range(number_row - 3):		   # check diagonally
		for col in range(number_col - 3):
			if board[row][col] == " " + current_chr + " ":
				if board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == " " + current_chr + " ":
					game_over = True

	# game over
	cnt = 0
	tie = False
	for col in range(number_col):
		if board[0][col] != "   ":
			cnt = cnt + 1
			if cnt == number_col:
				tie = True

	if tie == True:
		print("Tie!")
		break 

	if game_over == True:
		print("Player " + current_chr + " wins!")
		break

	# change player	
	turn = (turn + 1) % (num_players)
	print("Player " + chr_str[turn] + " goes next!")



















