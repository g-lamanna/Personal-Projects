import random

already_guessed = []
body_parts_list = ["LEFT LEG","HEAD","LEFT ARM","RIGHT ARM","RIGHT LEG"]

#randomly generate word
def hang_word():
    words = ["i love you","Hello world","Barcelona"]
    return random.choice(words)

def hang_game():
    word = hang_word()
    new_board = hang_board(word)
    print("\t\t\t{}\t\t\t".format(new_board))
    current_board = guess(word,new_board)
    while win_or_lose(current_board) != True:
        print("\t\t\t{}\t\t\t".format(new_board))
        guess(word,current_board)
def win_or_lose(board):
    if "_" in board:
        return False
    else:
        print("Congrats! You won!")
        exit()

def body_parts(body_parts_list):
    part = random.choice(body_parts_list)
    body_parts_list.remove(part)
    print("You lost the {} with {} remaining".format(part,body_parts_list))
    if len(body_parts_list) == 0:
        return True
        
def guess(word,board):
    letter_index = 0
    c = Counter(word)
    user_guess = input("Guess a letter: ")
    user_guess = user_guess.lower()
    while user_guess in already_guessed:
        print("Try again")
        user_guess = input("Guess a letter: ")
    already_guessed.append(user_guess)
    if user_guess in word:
        for i in range(len(word)):
            if word[i] == user_guess:
                letter_index = i
            else:
                continue
            for word_index,letter in enumerate(word):
                if word_index == letter_index:
                    for board_index in range(len(board)):
                        if board_index == letter_index:
                            board[board_index] = letter
                            break
                    continue
        return board
    else:
        if body_parts(body_parts_list) == True:
            print("Sorry, you lost! Ran out of body parts :(")
            exit()
        else:
            return board
def hang_board(word,letter=None):
    if letter==None:
        board_str=[]
        for i in range(len(word)):
            if word[i] == " ":
                board_str.append(word[i])
            else:
                board_str.append("_")
        return board_str

def main():
    print("\n\n\t\t\t WELCOME TO.....\t\t\n\n")
    print("                                   ______")
    print("|      |       /\       |\    |    |         |\    /|      /\      |\    |")
    print("|      |      /  \      | \   |    |         | \  / |     /  \     | \   |")
    print("--------     /----\     |  \  |    |  ___    |  \/  |    /----\    |  \  |")
    print("|      |    /      \    |   \ |    |    |    |      |   /      \   |   \ |")    
    print("|      |   /        \   |    \|    |____|    |      |  /        \  |    \|\n\n\n\n")
    hang_game()
    
main()