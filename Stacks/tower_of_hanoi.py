from stack import Stack

#empty list to store stacks
stacks = []

#instantiate instances of Stack class for each stack
left_stack = Stack("left")
center_stack = Stack("center")
right_stack = Stack("right")

#append each stack object to the list of 'stacks'
stacks.append(left_stack)
stacks.append(center_stack)
stacks.append(right_stack)

num_disks = int(input("\nEnter number of disks greater than 3\n "))

while num_disks < 3:
    num_disks = int(input("\nToo low, please enter number of disks greater than 3\n"))

#calculate # of optimal moves given num_disks
num_optimal_moves = (2**num_disks) - 1

print("Given the number of disks you chose, the least amount of moves it will take to complete is {}".format(num_optimal_moves))

#Push all disks to left stack
for i in range(num_disks,0,-1):
    left_stack.push(i)

#Getting input from users 
def get_input():
    #getting first letter from each stack name
    choice = [stack.get_name()[0] for stack in stacks]
    while True:
        print("Here is a list of options:")
        for i in range(len(stacks)):
            #grab name and first letter of name
            name = stacks[i].get_name()
            letter = choice[i]
            print("Enter {} for {}".format(letter,name))
        user_input = input("")
        #checking if user input is in choices
        if user_input in choice:
            for i in range(len(stacks)):
                #checking which choice matches user_input
                if user_input == choice[i]:
                    #returning stack name
                    return stacks[i].get_name()
get_input()

#keep track of moves
num_of_moves = 0

#condition to exit game
while right_stack.get_size() != num_disks:
    print("\n\n...Current stack...")
    #print disks and corresponding stacks
    for i in range(len(stacks)):
        stacks[i].print_items()
    while True:
        #which stack to move from
        print("\nWhich stack would you like to move from?\n ")
        from_stack = get_input()
        if from_stack == "left":
            from_stack = left_stack
        elif from_stack == "center":
            from_stack = center_stack
        elif from_stack == "right":
            from_stack = right_stack
        if from_stack.is_empty():
            print("\nInvalid move, try again!")
            continue
        print("\nWhich stack would you like to move to?\n ")
        to_stack = get_input()
        #which stack to move to
        if to_stack == "left":
            to_stack = left_stack
        elif to_stack == "center":
            to_stack = center_stack
        elif to_stack == "right":
            to_stack = right_stack
        #game conditions to be met in order to move
        if to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            #remove disk from top of stack
            disk = from_stack.pop()
            #push disk on top of new stack
            to_stack.push(disk)
            #increment number of moves
            num_of_moves += 1
            print("Move {}".format(num_of_moves))
            break
        else:
            print("\n\nInvalid Move, Try again")
print("\n\nYou completed the game in {} moves and the optimal number of moves is {}".format(num_of_moves,num_optimal_moves))
