
# Way number one to gather inpit to create a 2d list,
# This way requires the same thing you are doing, which
# is asking several times for the same thing, but it does
# control the amount of numbers collected. This is longer,
# but you can control the number entering with a loop to ensure
# there are nine numbers.

temp = []
square = []

print('This method will collect the nine magic numbers one by one \n')

for first in range(3):
     temp = []
     for second in range(3):
         temp.append(input('Enter a Magic number from the sequence'))
     square.append(temp)



print(square)
print()


# This way will work for collecting the whole list as a single input.
# I'm using List Comprehensions. A list is created by have the integer
# temporarily converted to a string, so each element is itreable, and then
# those string peices are converted back into a integer, so we can use them
# in your program.
# The second part is essentially doing the same thing, but I declare what the
# sublist will look like, and then insert three numbers into that list, until
# I run out of my initial list of numbers. A Range is providing the count of each
# sublist.
#
# This method defiitely requires more manipulation to get into the 2D list, but the
# end result is what you are looking for, and requires less work from the viewer.


print('This method will collect the nine magic numbers all at once \n')

#collecting the nine magic numbers
nums = int(input('Give me all nine magic numbers in a list'));


#Checking to see if there are nine

if len(str(nums)) == 9:


    # This will take eack number an put into a list
    # It temporailty converts the number to a string,
    # so it can be iterated through, then back to a integer.

    nums = [int(nums) for nums in str(nums)]

    # This is essentially doing the same as above, but it
    # taking each item in the list, and creating sublists
    # of threes, using a range function to keep track of the
    # the count that's why I added the WHILE above.
    
    square = [nums [x:x + 3] for x in range(0, len(nums), 3)]


else:
    
    print('Not nine')


print()
print(square)
