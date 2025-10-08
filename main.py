#EVEN AND ODD NUMBER PROGRAM
#num_list contains the list of numbers
num_list = [10,501,22,37,100,999,87,351]
#odd_num list will store the odd number values
odd_num = []
#even_num list will store the even number values
even_num = []
#iterating the values in num_list
for num in num_list:
    #if the number divided by 2 gives remainder as 0 then if condition will be true
    if num%2 == 0:
        even_num.append(num)
    #if the remainder is not 0 this part will get executed
    else:
        odd_num.append(num)
print("The ODD numbers from the list:",odd_num)
print("The EVEN numbers from the list:", even_num)

#PRIME NUMBER PROGRAM
#import math for using sqrt function
import math
#number_list variable holds given list of values
number_list = [10,501,22,37,100,999,87,351]
#primenumber_list variable is used to store prime numbers
primenumber_list = []
#iterating the list values
for num in number_list:
    #is_prime flag is used to check whether the number is prime if it is true value will get added to primenumber_list
    is_prime = True
    #math.sqrt(num) is used to calculate the square root value of num
    for i in range(2,int(math.sqrt(num)) + 1):
        if num%i == 0:
            is_prime = False
            break
    #if is_prime flag is true this condition will get satisfied and prime number will get added to primenumber_list
    if is_prime:
        primenumber_list.append(num)
print("List of prime numbers are:",primenumber_list)

#HAPPY NUMBER PROGRAM
#num_list hold the given number of values
num_list = [10,501,22,37,100,999,87,351]
#happynumber_list will hold the happy numbers
happynumber_list = []
#num_list value will get iterated
for i in range (len(num_list)):
    #number variable will hold the ith index value from num_list
    number = num_list[i]
    #number_x variable will hold the same number value
    number_x=number
    #this loop will get executed until the happy number sum is 1
    while number_x >= 10:
        #initializing sum variable as 0
        sum = 0
        while number_x >0:
            #modulous % operator which calculated the remainder of a division
            remainder = number_x%10
            #calculates the square of the remainder value
            sum = sum+(remainder**2)
            #// performs integer division
            number_x=number_x//10
        number_x = sum
        #if sum value is equal to 1 then it is a happy number if part will be executed
        if number_x ==1:
         happynumber_list.append(number)
print("Happy numbers are:",happynumber_list)

#FIRST AND LAST DIGIT OF AN INTEGER
flag = True
while flag:
     #Getting input from the number
     number = input("Enter the Number:")
     #checks whether user have entered the integer number
     if number.isnumeric():
      #converted numeric value into string representation
      num_str = str(number)
      #fetching first index value
      first_digit = int(num_str[0])
      #fetching last index value
      last_digit = int(num_str[-1])
      #adding first and last index values
      addition = first_digit + last_digit
      print("Addition of first and last digit of the Number is", addition)
      flag = False
     else:
      print("Kindly enter a valid number")

#COINS PROGRAM
#coins declaration
coins = [1, 2, 5, 10]
#coin_count variable holds count
coin_count=len(coins)
n=10
#table is used to store number of solutions for value i
table = [0 for k in range(n+1)]
#if given value is zero
table[0] = 1
#pick the coins and update in table[] one by one
for i in range(0,coin_count):
    for j in range(coins[i], n + 1):
        table[j] += table[j - coins[i]]
        result = table[n]
print("output:",result)

#FIND DUPLICATE NUMBERS
#importing collection for using counter
from collections import Counter
list_1 = [40,60,20,77,11,32,56,87,100]
list_2 = [50,32,12,40,66,93,20,60,99]
list_3 = [75,45,50,99,77,35,24,60,98]
#all_lists contains values of three list
all_lists = [list_1,list_2,list_3]
#empty list to store the combines list values
all_items = []
for item_list in all_lists:
    #combine all items into a single list [40,60,20,77,11,32,56,87,100,50,32,12,40,66,93,20,60,99,75,45,50,99,77,35,24,60,98]
    all_items.extend(item_list)
    #use of counter is to count the number of occurrence
    item_counts = Counter(all_items)
    #filtering the duplicate values
    duplicates = [item for item, count in item_counts.items() if count > 1]
print("Here are the duplicate values:",duplicates)

#FIND NON_REPEATING ELEMENT
#list of numbers
list4 = [1, 2, 3, 1, 2, 4, 5, 6, 7, 8]
#initializes an empty dictionary and assigns it to variable mp
mp = dict()
#empty list
result = []
#calculating the list size
size = len(list4)
#iterating the list values and count the frequencies
for i in range(size):
    if list4[i] in mp.keys():
        mp[list4[i]] += 1
    else:
        mp[list4[i]] = 1
        #Traverse through map and print the frequencies
for x in mp:
    if mp[x] == 1:
        result.append(x)
print("Non Repeating Elements in the given list are:", result)
#if there is no repeating elements in the list this part will get executed
if not result:
    print("List does not contain any Non Repeating Elements")
else:
    print("First Non Repeating Element is:", result[0])


#MINIMUM ELEMENT IN A ROTATED AND SORTED LIST
#list of values
list5 = [30,58,15,97]
#smallest variable will hold the index[0] value after the sorting
smallest = list5[0]
#Traverse over list5[] to find minimum element
for i in range(1,len(list5)):
    smallest = min(smallest, list5[i])
print("Minimum element in the given list:",smallest)

#TRIPLET PROGRAM
#given list
list6 = [10,20,30,9]
target = 59
#length of the list
size = len(list6)
#traversing through the values
for i in range(size-2):
    for j in range(i+1,size-1):
        for k in range(j+1,size):
            #summing the values to check for the target value 59
            if (list6[i] + list6[j] + list6[k]) == target:
                print("Triplet values:",list6[i],list6[j],list6[k])


#SUB LIST PROGRAM
#list of values
list7 = [4,2,-3,1,6]
#length of the list
size = len(list7)
flag = False
#traverse through the given values
for i in range(size -1):
    sum = list7[i]
    for j in range(i+1,size):
        sum += list7[j]
        #if prefix sum is 0
        if sum == 0:
            print("yes sub list exits!")
            flag = True
if not flag:
    print ("no sub list")

