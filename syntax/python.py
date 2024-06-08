# Python syntax
# https://github.com/sm3232/tutoring
# For educational purposes. Feel free to copy, share, edit, use, whatever, however you want

# +-----------------+
# | Part 1 - Basics |
# +-----------------+

# <- Hashtag/Pound/Tictactoe symbol makes comments
# Comments will not be run as code

example = 5 # Comments can be on the same line as code

variable = 1 # Assign values to variables with "="

# Variable names in python are usually all lowercase and have underscores (_) inbetween words
python_variable_with_more_than_one_word = 5 # This works, but you should avoid long names like this

string_variable = "string" # Strings are made with either double quotes ("") or single quotes ('')
string_variable = 'string' # ^

boolean_variable = True  # Booleans have a capital first letter (True/False)
boolean_variable = False # *

number_variable = 64 # Numbers are simple
number_variable = 64.2301 # Decimals are fine

array_variable = [1, 2, 3, 4, 5] # This is an array
tuple_varialbe = (1, 2, 3, 4, 5) # This is a tuple

first_value = array_variable[0] # Access elements
first_value = tuple_varialbe[0] # ^

if 1 == 2: # If statement
    one_equals_two = True # Notice the indent
else: # Else
    one_equals_two = False

for i in range(0, 10):
    print(i)
