#write a program to create a list of 20 n0. given by user .Ask the user to input any number.Remove all the duplicate enteries of these numbers from the same  list .
numbers = []
print("Enter any 20 numbers:")
for x in range (20):
    num=int(input())
    #append into list 
    numbers.append(num)
print("-----------------------------------------------------------------")
element =int(input("Enter any number to remove its duplicacy:"))
#------------------------------------------------------------------------
#finding the frequency of given number 
frequency=numbers.count(element)
if frequency==0:
    print("Element not found")
elif frequency==1:
    print("No duplicate elements")
else:
    #reversing the list 
    numbers.reverse()
    for i in range (1,frequency):
        #removing element 
        numbers.remove(element)
    #reversing the list again 
    numbers.reverse()
    print("After removing duplicates")
    print(numbers)

                       