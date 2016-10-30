
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
from xmlrpclib import boolean
from operator import pos

#-----------------------------------
# 1.1. FUNCTION correct_golomb_size
#-----------------------------------
def correct_golomb_size(m):
    # 1. We assume that the input is not correct with a Boolean variable set initially to False
    is_correct = False
    # 2. We check whether the input message is actually an integer, and it is within 4 and 8. If so, we set the variable to True
    if m.isdigit() and int(m) >= 4 and int(m) <= 8:
        is_correct = True
    # 3. We return our variable as a way of reporting whether the message is correct or not.
    return is_correct
#-------------------------------
# 1.2. FUNCTION collect_message
#-------------------------------
def collect_message():      #kiem tra so nhap vao co dung yeu cau k
    # 1. We assume that, so far, we have not got the right message, using a Boolean variable set initially to False
    temp = False
    # 2. As long as we do not have a correct message
    while not temp:
        # 2.1. We ask the user to enter a new message by keyboard
        n = raw_input('Enter a integer in between 4 and 8: ')
        # 2.2. We use the function correct_golomb_size to see whether the message is correct or not, adapting our variable accordingly to it.
        temp = correct_golomb_size(n)
        
    # 3. Once we have a correct number, we just return it
    return n
    

#----------------------------------------
# 1.3. FUNCTION generate_list_of_numbers
#----------------------------------------
def generate_list_of_numbers(n):
    # 1. We initially create an empty list
    List_golomb = []
    # 2. As long as we have not generated as many numbers as required
    for elm in range(0,n):
        # 2.1. We generate a random number between 0 and 2 to the power of n
        elm = random.randint(0,math.pow(2,n))
        # 2.2. We append the number to the list we are creating
        List_golomb.append(elm)
    # 3. We return the generated list
    return List_golomb
#----------------------------
# 1. FUNCTION setup_the_game
#----------------------------
def setup_the_game():
    
    # 1. Get the size of the Golomb ruler from the user
    size = collect_message()
    # 2. Generate randomly the initial set of numbers of the sequence
    golomb_list = generate_list_of_numbers(int(size))
    # 3. Generate randomly the initial index of the sequence to be pointed
    position = random.randint(0, int(size)-1)
    # 4. Set the initial number of movements to 0
    movements = 0
    
    # 5. Return the logic of the game, consisting on the list of numbers, the initial position and the number of movements
    return golomb_list, position, movements
#--------------------------------
# 2. FUNCTION is_feasible_Golomb
#--------------------------------
def is_feasible_Golomb(sequence):
    # 1. We assume that, so far, the sequence is a feasible Golomb ruler.
    is_feasible = True
    # 2. We check the first property: Increasing order or the numbers            
    # As long as we have not checked it for each possible elements of the sequence
    elm = sequence[0]
    for i in range(1, len(sequence)):
        # 2.1. We pick each two consecutive elements of the sequence and compare them. If they do not follow an increasing order
        if elm > sequence[i]:
            # 2.1.1. We set our Golomb ruler straight away as an unfeasible one.
            is_feasible = False
            # 2.1.2. Otherwise, we keep trying with the next couple of consecutive elements
        else:
            elm = sequence[i]
    # 3. We check the second property: All differences are different
    # We create a list with all the differences. The list is so far empty.
    List_differences = []
    # As long as there are a couple of elements of the sequence to be compared, we do it
    for i in range(0, len(sequence)):
        for j in range(i+1, len(sequence)):
            # 3.1.1. We get the difference between each two elements
            diff = sequence[j] - sequence[i]
            # 3.1.2. If this difference is in the list, we set our Golomb ruler straight away as an unfeasible one.
            if diff in List_differences:
                is_feasible = False
                break
            # 3.1.3. Otherwise, we add the difference to our list, so as to take it into account for any upcoming difference taking the same value.
            else:
                List_differences.append(diff)
            # 3.1.4. We keep trying with any other two elements
        if not is_feasible:
            break
    # 4. Return whether the Golomb ruler is feasible or not
    return is_feasible
#-------------------------------
# 3. FUNCTION print_game_status
#-------------------------------

def print_game_status(golomb_list, position, movements):
    # 1. We clean the screen by printing a hundred empty lines
    print "\n"*3
    # 2. We print the Golomb list
    # 2.1. We wrap it with an upper line
    print '-----------------------------------------------------------------'
    # 2.2. We print the list of numbers
#     golomb_str = str(golomb_list)
    for elm in golomb_list:
        print elm,
        print '\t',
    # 2.3. We wrap it with an down line    
    print '\n-----------------------------------------------------------------'
    # 2.4. Print the index being selected
    for i in range(0,len(golomb_list)):
        if position == i:
            
            #dau_cach = (i * len(golomb_list) -i)
            print '\t' * position + '^'
            print 'Vi tri hien tai', i
    print 'Actual movements done so far: ', movements
    # 2.5. Print the number of movements
    
#---------------------------
# 4.1. FUNCTION get_command
#---------------------------

# ham kiem tra command nhap vao
def check_command(key):
    if key == 'a' or key == 'A':
        return ': To move the index to the left'
    elif key == 'd' or key == 'D':
        return ': To move the index to the right'
    elif key == 'z' or key =='Z':
        return ': To swap the number with the one place at its left'
    elif key == 'c' or key == 'C':
        return ': To swap the number with the one place at its right'
    elif key == 'q' or key == 'Q':
        return ': To add one to the number'
    elif key == 'e' or key == 'E':
        return ': To subtract one to the number'
    return

def get_command():
    valid_character_upper = ['A', 'D', 'Z', 'C', 'Q', 'E']
    valid_character_lower = ['a', 'd', 'z', 'c', 'q', 'e'] 
    # 1. We assume that, so far, the command is not a valid one.
    is_command = False
    # 2. As long as we have not get a valid command from the user
    while not is_command:
        # 2.1. We inform of the possible commands to be entered
        print 'Enter a command ->'
        for i in range(6):
            print " " * 20 + valid_character_upper[i] + ' or ' + valid_character_lower[i] + check_command(valid_character_lower[i])
        # 2.2. We ask the user to enter one command by keyboard
        enter_by_user = raw_input("")
        # 2.3. If the command is a valid one, we set our variable to true
        for i in range(6):
            if enter_by_user == valid_character_lower[i] or enter_by_user == valid_character_upper[i]:
                is_command = True
                break
 # 3. Once we have a valid command from the user, we return it
    return enter_by_user
      
    
#-----------------------------
# 4.2. FUNCTION modify_status
#-----------------------------
def modify_status(golomb_list, position, movements, key):

    
    # 1. We process the command 'A' or 'a'
    if key == 'A' or key == 'a':
        position = position - 1
        if position < 0:
            print '\nKhong chuyen qa ben trai duoc nua!!!!'
            print 'Please Enter Again :)'
    # 2. We process the command 'D' or 'd'
    if key == 'D' or key == 'd':
        if position > len(golomb_list)-2:
            print '\nKhong chuyen qua ben phai duoc nua!!!!' 
            print 'Please Enter Again :)'     
        else:
            position = position + 1
    # 3. We process the command 'Q' or 'q'
    if key == 'q' or key == 'Q':
        if position == 0:
            print '\nGia tri o vi tri 0 nay khong hoan vi duoc nua!!!!'
            print 'Please Enter Again :)'
        else:
            current_string = golomb_list[position-1]
            golomb_list[position-1] = golomb_list[position]
            golomb_list[position] = current_string
    # 4. We process the command 'E' or 'e'
    if key == 'e' or key == 'E':
        if position == len(golomb_list) -1 :
            print '\nGia tri o vi tri nay khong hoan vi duoc nua!!!' 
            print 'Please Enter Again :)'
        else:
            current_string = golomb_list[position+1]
            golomb_list[position+1] = golomb_list[position]
            golomb_list[position] = current_string
    # 5.We process the command 'Z' or 'z'
    if key == 'Z' or key == 'z':
        golomb_list[position] = golomb_list[position] + 1
    # 6. We process the command 'C' or 'c'
    if key == 'C' or key == 'c':
        if golomb_list[position] == 0:
            print '\nGia nay da toi thieu. Khong giam duoc nua!!!'
            print 'Please Enter Again :)'
        else:
            golomb_list[position] = golomb_list[position] - 1
    # 7. We return the new current status of the golomb_list, index of the sequence we are working with and movements
    return golomb_list, position, movements
#---------------------------------
# 4. FUNCTION make_a_new_movement
#---------------------------------
def make_a_new_movement(golomb_list, position, movements):

    # 1. We ask for a new movement
    # 2. We perform the movement
    movements = movements + 1
    # 3. Return the new current status of the golomb_list, index of the sequence we are working with and movements
    return golomb_list, position, movements
#-----------------------
# FUNCTION my_main
#-----------------------
def my_main():

    # 1. Setup the game\
    #size = collect_message()
    golomb_list, position, movements = setup_the_game()
    print_game_status(golomb_list, position, movements)
    # 2. As long as the Golomb ruler is not feasible
    while not is_feasible_Golomb(golomb_list):
        # 2.1. Print the game status
        print_game_status(golomb_list, position, movements)
        key = get_command()
        golomb_list, position, movements = modify_status(golomb_list, position, movements, key)
        # 2.2. Make a new movement
        golomb_list, position, movements = make_a_new_movement(golomb_list, position, movements)
    # 3. Print the game status and a solved message
    golomb_str = str(golomb_list)
    print '-----------------------------------------------------------------'
    print ' ' * 28 + 'Solved!!'
    print '-----------------------------------------------------------------'
    print 'Golomb Ruler: ' + golomb_str + ' is a feasible :D :D :D :D :D '
    

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
    
