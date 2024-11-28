
# lists are a way to store many values in the same variable
# lists are denoted like below
# below is a list of numbers of int type
my_list = [10, 20, 30, 40, 50]

# lists are some kind of python objects
# they got methods that we can use to operate on them

# add the number 60 to the end of the list
my_list.append(60)

# find and remove the number 30 from the list
my_list.remove(30)

# lists have length that indicates how many elements are in the array
my_list_length = len(my_list)
print(my_list_length)

# lists are indexed starting from 0 up to the length of the list - 1
# this means that the first element in the list in number 0 and the last
# element is number len(my_list) - 1

# so to select the first element
first_element = my_list[0]
print(first_element)

# to select the last element
index_of_last_element = my_list[len(my_list)-1]
last_element = my_list[index_of_last_element]
print(last_element)

# there is also another way which is to count from the end of the list
# using negative numbers
# for example to get the first element in the array
last_element = my_list[-1]
second_to_last_element = my_list[-2] # and so on

# range indexing
# we can choose a subset of our list
# this will give us a smaller list
smaller_list = my_list[1:4]
print(smaller_list)

# we can change the values inside our list using indexing
my_list[0] = 5
print(my_list)

# we can combine (concatenate) lists using + operator
combined_list = my_list + smaller_list
print(combined_list)