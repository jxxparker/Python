# 1)Countdown - Create a function that accepts a number 
# as an input. Return a new list that counts down 
# by one, from the number (as the 0th element) 
# down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    numlist = []
    for val in range(num, -1, -1):
        numlist.append(val) #append puts object at the end
    return numlist
print(countdown(14))

# 2) Print and Return - 
# Create a function that will receive a list 
# with two numbers. 
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 
# and return 2

def print_and_return(numlists):
    print(numlists[0])
    return numlists[1]
print(print_and_return([10,12]))

# 3) First Plus Length - 
# Create a function that accepts a 
# list and returns the sum of the first value in 
# the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) 
# should return 6 (first value: 1 + length: 5)

def first_plus_length(num_list):
    return num_list[0] + len(num_list)
print(first_plus_length([13,2,5]))

# 4) Values Greater than Second - 
# Write a function that accepts a list and creates 
# a new list containing only the values from the 
# original list that are greater than its 2nd value. 
# Print how many values this is and then return 
# the new list. If the list has less than 2 elements, 
# have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) 
# should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) 
# should return False

def values_greater_than_second(orig_list):
    new_list = []
    # get the second value in the original list
    second_val = orig_list[1]
    # scan through the original list, find values greater than second value and add them to the new list
    for idx in range(len(orig_list)):
        if orig_list[idx] > second_val:
            new_list.append(orig_list[idx])
    
    print(len(new_list))
    return new_list