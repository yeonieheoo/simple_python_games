
import random
import os
board = []
number_row = 6
number_col = 6
alphabet_column = "ABCDEF"
num_players = 2
chr_str = "XO"


# make board
for row in range(number_row):
	row_list = []
	for col in range(number_row):
		row_list.append("   ")
	board.append(row_list)

for col in range(number_row):
	print("   " + alphabet_column[col], end="")

# print first line of board
print("\n +" + "---+" * number_row)

# display board
for row in range(number_row):
	print(str(row) + "|", end="")
	for col in range(number_col):
		print(board[row][col] + "|", end="")
	print("\n +" + "---+" * number_row)


# generate the order of players
next_player = random.randint(0, num_players - 1)
print("Player " + str(next_player + 1) + "'s turn!")

# play game
game_over = False
choice = input("Enter a coordinate to place a check (ex: A1): ")

while not game_over:

	checkInput = True
	while (checkInput == True):
		checkInput = False
		if (choice == "") or (choice[0] not in alphabet_column) or (choice.isalpha() == True) or (choice.isdigit() == True) or (len(choice)!= 2)  or (choice[0].islower() == True) or (int(choice[1])>=number_row): 
			print("You entered an invalid coordinate!")
			choice = input("Try another! Enter a valid coordinate (ex: A1, B4, F0): ")
			checkInput = True

	letter = choice[0]
	number = choice[1]
	letter_index = alphabet_column.find(letter)
	number_index = int(number)

	# change the check
	current_chr = chr_str[next_player]

	changed = False
	if board[number_index][letter_index] == "   ":
		board[number_index][letter_index] = " "+current_chr+" "
		changed = True


	# check if the block is empty & place checkers
	alphabet_column.find(letter) 
	row = number_index
	col = letter_index

	if changed and (0<=row+1<6) and changed == True and (board[row+1][col] == "   "):
		board[row+1][col] = " # "
		
	if changed and (0<=col-1<6) and changed == True and (board[row][col-1]== "   "):
		board[row][col-1] = " # "
		
	if changed and (0<=col+1<6) and changed == True and (board[row][col+1]== "   "):
		board[row][col+1] = " # "
		
	if changed and (0<=row-1<6) and changed == True and (board[row-1][col]== "   "):
		board[row-1][col] = " # "
		
	if changed and (0<=row-1<6) and changed == True and (0<=col+1<6) and (board[row-1][col+1]== "   "):
		board[row-1][col+1] = " # "
		
	if changed and (0<=row+1<6) and changed == True and (0<=col+1<6) and (board[row+1][col+1]== "   "):
		board[row+1][col+1] = " # "
		
	if changed and (0<=row-1<6) and changed == True and(0<=col-1<6) and (board[row-1][col-1]== "   "):
		board[row-1][col-1] = " # "
		
	if changed and (0<=row+1<6) and changed == True and (0<=col-1<6) and (board[row+1][col-1] == "   "):
		board[row+1][col-1] = " # "


	# display game
	os.system("clear")
	for row in range(number_row):
		row_list = []
		for col in range(number_row):
			row_list.append("   ")
		board.append(row_list)

	for col in range(number_row):
		print("   " + alphabet_column[col], end="")

	print("\n +" + "---+" * number_row)

	for row in range(number_row):
		print(str(row) + "|", end="")
		for col in range(number_col):
			print(board[row][col] + "|", end="")
		print("\n +" + "---+" * number_row)


	cnt = 0
	for row in range(number_row):
		for col in range(number_col):
			if board[row][col] == "   ":
				cnt = cnt + 1
	if cnt == 0:
		game_over = True
		print("No place to put a check, game over!")
		break

	if changed == False: 
		print("This place is filled already.") 

	# setting the next player
	next_player = (next_player+1)%2 
	print("Player " + str(next_player+1) + " goes next!")

	
	choice = input("Enter a coordinate to place a check (ex: A1): ")

# game result
print("Player", ((next_player-1)%2), "wins!")


