# Tic-Tac-Toe Game
# Welcome Screen that displays the intro of the game
def welcome_screen():

    print("\t---------------------------------------------------\n\t----------WELCOME TO THE TIC-TAC-TOE "
          "GAME----------\n\t---------------------------------------------------\n\n")
# EOF - end of function!!


# Display Tic-Tac-Toe graph
def display_tictactoe(board_list):
    print("{} {} {}".format(board_list[0], board_list[1], board_list[2]))
    print("{} {} {}".format(board_list[3], board_list[4], board_list[5]))
    print("{} {} {}".format(board_list[6], board_list[7], board_list[8]))


# This function takes the input of the player details, i.e., who will be 'X' and who will be 'O'
def player_details():

    player1 = input("\nPlayer 1: What do you want to be? [ 'X' OR 'O' ]: ")
    while player1 not in ['X', 'O']:
        print("Sorry Buddy! You have entered a wrong input!")
        player1 = input("Player 1: What do you want to be? [ 'X' OR 'O' ]:\n")

    # Check for 'X' or 'O'
    if player1 == 'X' or player1 == 'O':
        player_inputs(player1)
# EOF - end of function!!


# Player inputs to be taken for the game
def player_inputs(player1):

    player1_bool_default = False
    player_1_input = input("Player 1: Enter your '{}' value position from 0 - 8: ".format(player1))

    while not player1_bool_default:
        if player_1_input.isdigit():
            if int(player_1_input) in range(0, 9):
                player1_bool_default = True
            else:
                print("Sorry Buddy! You have entered a wrong input!")
                player_1_input = input("Player 1: Enter your '{}' value position from 0 - 8: ".format(player1))
        else:
            print("Sorry Buddy! You have entered a wrong input!")
            player_1_input = input("Player 1: Enter your '{}' value position from 0 - 8: ".format(player1))

    player2_bool_default = False
    if player1 == 'X':
        player2 = 'O'
        player_2_input: str = input("Player 2: Enter your '{}' value position from 0 - 8: ".format(player2))
        while not player2_bool_default:
            if player_2_input.isdigit():
                if int(player_2_input) in range(0, 9):
                    player2_bool_default = True
                else:
                    print("Sorry Buddy! You have entered a wrong input!")
                    player_2_input = input("Player 2: Enter your '{}' value position from 0 - 8: ".format(player_2_input
                                                                                                          ))
            else:
                print("Sorry Buddy! You have entered a wrong input!")
                player_2_input = input("Player 2: Enter your '{}' value position from 0 - 8: ".format(player_2_input))
    else:
        player2 = 'X'
        player_2_input = input("Player 2: Enter your '{}' value position from 0 - 8: ".format(player2))
        while not player2_bool_default:
            if player_2_input.isdigit():
                if int(player_2_input) in range(0, 9):
                    player2_bool_default = True
                else:
                    print("Sorry Buddy! You have entered a wrong input!")
                    player_2_input = input("Player 2: Enter your '{}' value position from 0 - 8: ".format(player_2_input
                                                                                                          ))
            else:
                print("Sorry Buddy! You have entered a wrong input!")
                player_2_input = input("Player 2: Enter your '{}' value position from 0 - 8: ".format(player_2_input))

    # Call the graph update method
    display_output_value = update_tictactoe_graph(int(player_1_input), player1, int(player_2_input), player2)

    if display_output_value == "Player 1 Wins!!":
        print("Player 1 Wins!!")
        exit()
    elif display_output_value == "Player 2 Wins!!":
        print("Player 2 Wins!!")
        exit()
    else:
        print("Its a Tie!!")
        exit()


# Player 1 Input retake
# def player_1_retake(player1):
#
#     player1_bool_default = False
#     player1_retake = input("Player 1: Enter your '{}' value position from 0 - 8: ".format(player1))
#
#     while not player1_bool_default:
#         if player1_retake.isdigit():
#             if int(player1_retake) in range(0, 9):
#                 player1_bool_default = True
#             else:
#                 print("Sorry Buddy! You have entered a wrong input!")
#                 player1_retake = input("Player 1: Enter your '{}' value position from 0 - 8: ".format(player1))
#         else:
#             print("Sorry Buddy! You have entered a wrong input!")
#             player1_retake = input("Player 1: Enter your '{}' value position from 0 - 8: ".format(player1))
#
#     return player1_retake


# Player 2 input retake
# def player_2_retake(player2):
#
#     player2_bool_default = False
#     player2_retake = input("Player 1: Enter your '{}' value position from 0 - 8: ".format(player2))
#
#     while not player2_bool_default:
#         if player2_retake.isdigit():
#             if int(player2_retake) in range(0, 9):
#                 player1_bool_default = True
#             else:
#                 print("Sorry Buddy! You have entered a wrong input!")
#                 player2_retake = input("Player 1: Enter your '{}' value position from 0 - 8: ".format(player2))
#         else:
#             print("Sorry Buddy! You have entered a wrong input!")
#             player2_retake = input("Player 1: Enter your '{}' value position from 0 - 8: ".format(player2))
#
#     return player2_retake


# Updating the tic-tac-toe graph: player_1_input = position
def update_tictactoe_graph(player_1_input, player1, player_2_input, player2):

    player1_str = '|' + player1 + '|'
    player2_str = '|' + player2 + '|'

    # Clause to check if the position is available to store the value.
    if default_board[player_1_input] == "| |":
        default_board[player_1_input] = "|" + player1 + "|"
    # else:
    #     print("Sorry Buddy! You have entered a wrong input!")
    #     player_1_input = player_1_retake(player1)

    # Clause to check if the position is available to store the value.
    if default_board[player_2_input] == "| |":
        default_board[player_2_input] = "|" + player2 + "|"
    # else:
    #     print("Sorry Buddy! You have entered a wrong input!")
    #     player_2_input = player_2_retake(player2)

    while "| |" in default_board:
        display_tictactoe(default_board)

        if (player1_str == default_board[0] and player1_str == default_board[1] and player1_str == default_board[2]) or (
                player1_str == default_board[3] and player1_str == default_board[4] and (player1_str == default_board[5]) or player1_str ==
                default_board[6] and player1_str == default_board[7] and player1_str == default_board[8]) or (
                player1_str == default_board[0] and player1_str == default_board[3] and player1_str == default_board[6]) or (
                player1_str == default_board[1] and player1_str == default_board[4] and player1_str == default_board[7]) or (
                player1_str == default_board[2] and player1_str == default_board[5] and player1_str == default_board[8]) or (
                player1_str == default_board[0] and player1_str == default_board[4] and player1_str == default_board[8]) or (
                player1_str == default_board[2] and player1_str == default_board[4] and player1_str == default_board[6]):
            return "Player 1 Wins!!"
        elif (player2_str == default_board[0] and player2_str == default_board[1] and player2_str == default_board[2]) or (
                player2_str == default_board[3] and player2_str == default_board[4] and (player2_str == default_board[5]) or player2_str ==
                default_board[6] and player2_str == default_board[7] and player2_str == default_board[8]) or (
                player2_str == default_board[0] and player2_str == default_board[3] and player2_str == default_board[6]) or (
                player2_str == default_board[1] and player2_str == default_board[4] and player2_str == default_board[7]) or (
                player2_str == default_board[2] and player2_str == default_board[5] and player2_str == default_board[8]) or (
                player2_str == default_board[0] and player2_str == default_board[4] and player2_str == default_board[8]) or (
                player2_str == default_board[2] and player2_str == default_board[4] and player2_str == default_board[6]):
            return "Player 2 Wins!!"
        player_inputs(player1)


# Function Calling

# welcome_function call
welcome_screen()

# defining default global board
default_board = ['| |', '| |', '| |', '| |', '| |', '| |', '| |', '| |', '| |']
display_tictactoe(default_board)

player_details()
