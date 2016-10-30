
#--------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
#--------------------------------------------------------

# Import random and math modules
import random
import math

#-----------------------------------
# 1.1. FUNCTION correct_golomb_size
#-----------------------------------
#def correct_golomb_size(m):
    # 1. We assume that the input is not correct with a Boolean variable set initially to False

    # 2. We check whether the input message is actually an integer, and it is within 4 and 8. If so, we set the variable to True

    # 3. We return our variable as a way of reporting whether the message is correct or not.

def correct_golomb_size(m):        # 1. We assume that the input is not correct with a Boolean variable set initially to False
    # 2. We check whether the input message is actually an integer, and it is within 4 and 8. If so, we set the variable to True
    if m.isdigit() and int(m) >= 4 and int(m) <= 8:
        return m    # 3. We return our variable as a way of reporting whether the message is correct or not.
    return False
#-------------------------------
# 1.2. FUNCTION collect_message
#-------------------------------
#def collect_message():
def collect_message():
    temp = False
    while not temp:
        n = raw_input('Please enter number: ')
        temp = correct_golomb_size(n)
    return correct_golomb_size(n)
    
    # 1. We assume that, so far, we have not got the right message, using a Boolean variable set initially to False

    # 2. As long as we do not have a correct message

        # 2.1. We ask the user to enter a new message by keyboard

        # 2.2. We use the function correct_golomb_size to see whether the message is correct or not, adapting our variable accordingly to it.

    # 3. Once we have a correct number, we just return it

    
#----------------------------------------
# 1.3. FUNCTION generate_list_of_numbers
#----------------------------------------
#def generate_list_of_numbers(n):
    # 1. We initially create an empty list

    # 2. As long as we have not generated as many numbers as required

        # 2.1. We generate a random number between 0 and 2 to the power of n

        # 2.2. We append the number to the list we are creating

    # 3. We return the generated list

def generate_list_of_numbers(n):
    List_golomb = []
    for elm in range(0,n): 
        elm = random.randint(0,math.pow(2,n))
        List_golomb.append(elm)
    return List_golomb
#----------------------------
# 1. FUNCTION setup_the_game
#----------------------------
#def setup_the_game():
    # 1. Get the size of the Golomb ruler from the user

    # 2. Generate randomly the initial set of numbers of the sequence

    # 3. Generate randomly the initial index of the sequence to be pointed

    # 4. Set the initial number of movements to 0

    # 5. Return the logic of the game, consisting on the list of numbers, the initial position and the number of movements

def setup_the_game():
    size = raw_input('Enter a integer between 4 and 8: ')
    flag = correct_golomb_size(size)
    while flag == False:
        size = raw_input('Enter a integer between 4 and 8: ')
        flag = correct_golomb_size(size)
    list = generate_list_of_numbers(int(size))
    index = random.randint(0, int(size)-1)
    movements = 0
    return list, index, movements
#--------------------------------
# 2. FUNCTION is_feasible_Golomb
#--------------------------------
#def is_feasible_Golomb(sequence):
    # 1. We assume that, so far, the sequence is a feasible Golomb ruler.

    # 2. We check the first property: Increasing order or the numbers

    # As long as we have not checked it for each possible elements of the sequence

        # 2.1. We pick each two consecutive elements of the sequence and compare them. If they do not follow an increasing order

            # 2.1.1. We set our Golomb ruler straight away as an unfeasible one.

            # 2.1.2. Otherwise, we keep trying with the next couple of consecutive elements

    # 3. We check the second property: All differences are different
    # We create a list with all the differences. The list is so far empty.

    # As long as there are a couple of elements of the sequence to be compared, we do it

            # 3.1.1. We get the difference between each two elements

            # 3.1.2. If this difference is in the list, we set our Golomb ruler straight away as an unfeasible one.

            # 3.1.3. Otherwise, we add the difference to our list, so as to take it into account for any upcoming difference taking the same value.

            # 3.1.4. We keep trying with any other two elements

    # 4. Return whether the Golomb ruler is feasible or not

def is_feasible_Golomb(sequence):
    is_feasible = True
    elm = sequence[0]
    for i in range(1, len(sequence)):
        if elm > sequence[i]:
            is_feasible = False
        else:
            elm = sequence[i]
    List_differences = []
    for i in range(0, len(sequence)):
        for j in range(i+1, len(sequence)):
            diff = sequence[j] - sequence[i]
            if diff in List_differences:
                is_feasible = False
                break
            else:
                List_differences.append(diff)
        if not is_feasible:
            break
    return is_feasible
#-------------------------------
# 3. FUNCTION print_game_status
#-------------------------------

#--------------------------------
    
    
# def print_game_status(golomb_list, position, movements):
def print_game_status(golomb_list, position, movements):
    # 1. We clean the screen by printing a hundred empty lines
    print "\n"*100
    # 2. We print the Golomb list
    
    # 2.1. We wrap it with an upper line
    print '----------------------------'
    # 2.2. We print the list of numbers
    for i in golomb_list:
        print i,
        print '\t',
    print
    # 2.3. We wrap it with an down line  
    print '----------------------------'  
    # 2.4. Print the index being selected
    for elm in range(0, len(golomb_list)):
        if position == elm:
            print '\t' * position + '^'     
    # 2.5. Print the number of movements
    print 'Actual movements done so far: ',movements
    
    print 'Enter your command ->'
    print '\t\t "A" or "a": To move the index to the left'
    print '\t\t "D" or "d": To move the index to the right'
    print '\t\t "Q" or "q": To swap the number with the one placed at its left'
    print '\t\t "E" or "e": To swap the number with the one placed at its right'
    print '\t\t "Z" or "z": To add one to the number'
    print '\t\t "C" or "c": To subtract one to the number'
    

#---------------------------

# 4.1. FUNCTION get_command
#---------------------------

# ham kiem tra command nhapj vaoa
def check_command(command_input):
    valid_character_upper = ['A','D','Z','C','Q','E']
    valid_character_lower = ['a','d','z','c','q','e']
    #check
    for i in valid_character_upper:
        if i == command_input:
            return command_input
    for i in valid_character_lower:
            if i == command_input:
                return command_input
    else:  
        return False

#def get_command():

    # 1. We assume that, so far, the command is not a valid one.
    # 2. As long as we have not get a valid command from the user

        # 2.1. We inform of the possible commands to be entered

        # 2.2. We ask the user to enter one command by keyboard

        # 2.3. If the command is a valid one, we set our variable to true

 # 3. Once we have a valid command from the user, we return it

def get_command():
    print '--------------------------------'
    a = raw_input('Entered your true command: ')
    flag = check_command(a)
    while flag == False:
        print '--------------------------------'
        print 'You entered the wrong command'
        print 'You have to enter the true command'  
        a = raw_input('Entered your true command: ') 
        flag = check_command(a)
    else:
        return flag


#-----------------------------
# 4.2. FUNCTION modify_status
#-----------------------------
def modify_status(golomb_list, position, movements, key):
    # 1. We process the command 'A' or 'a'
    if key == 'A' or key == 'a':
        if position == 0:
            print 'Khong the di chuyen con tro sang trai'
        else: 
            position = position -1
    # 2. We process the command 'D' or 'd'
    if key == 'D' or key == 'd':
        if position == len(golomb_list)-1:
            print 'Khong the di chuyen con tro sang phai'
        else:
            position = position + 1
    # 3. We process the command 'Q' or 'q'
    if key == 'q' or key == 'Q':
        if position == 0:
            print 'Khong hoan vi duoc'
        else:
            current_string = golomb_list[position-1]
            golomb_list[position-1] = golomb_list[position]
            golomb_list[position] = current_string
    # 4. We process the command 'E' or 'e'
    if key == 'e' or key == 'E':
        if position == len(golomb_list)-1:
            print 'Khong hoan vi duoc'
        else:
            current_string = golomb_list[position+1]
            golomb_list[position+1] = golomb_list[position]
            golomb_list[position] = current_string
    # 5. We process the command 'Z' or 'z'
    if key == 'Z' or key == 'z':
        golomb_list[position] = golomb_list[position] + 1
    # 6. We process the command 'C' or 'c'
    if key == 'C' or key == 'c':
        golomb_list[position] = golomb_list[position] - 1
    # 7. We return the new current status of the golomb_list, index of the sequence we are working with and movements
    return golomb_list, position, movements
#---------------------------------
# 4. FUNCTION make_a_new_movement
#---------------------------------
#def make_a_new_movement(golomb_list, position, movements):
def make_a_new_movement(golomb_list, position, movements):
    # 1. We ask for a new movement
    # 2. We perform the movement
    movements = movements + 1
    # 3. Return the new current status of the golomb_list, index of the sequence we are working with and movements
    return golomb_list, position, movements



#-----------------------
# FUNCTION my_main
#-----------------------
#def my_main():
def my_main():
    # 1. Setup the game
    
    se, pos, move = setup_the_game()
    # 2. As long as the Golomb ruler is not feasible
    print_game_status(se, pos, move)
    if is_feasible_Golomb(se):
        print 'congrats! THIS IS FEASIBLE GOLOMB'
    while is_feasible_Golomb(se) == False:
        print '------------------------------------'
        print 'This is not feasible Golomb'
        # 2.1. Print the game status
        print_game_status(se, pos, move)
        # 2.2. Make a new movement
        key = get_command()
        se, pos, move = modify_status(se, pos, move,key)
        se, pos, move = make_a_new_movement(se, pos, move)
    # 3. Print the game status and a solved message
    


#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
   
