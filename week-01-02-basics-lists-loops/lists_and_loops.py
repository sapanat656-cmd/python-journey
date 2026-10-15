print("Hello, World!")
#len()
students= ["Bibek", "John", "Maria", "David", "Alex"]
print(len(students))
print("1------------------------------------------------------")

numbers=[10, 20, 30, 40, 50, 60]
print(len(numbers))
print("2------------------------------------------------------")

#slicing 
numbers=[10,20,30,40,50, 60]
print(numbers[2:5])
print("3------------------------------------------------------")

numbers=[10,20,30,40,50, 60]
print(numbers[:3])#from the beginning upto index 3.
print("4------------------------------------------------------")

numbers=[10,20,30,40,50, 60]
print(numbers[3:])#from index 3 to end.
print("5------------------------------------------------------")

numbers=[10,20,30,40,50, 60]
print(numbers[0:6:2]) #start:stop:step, start from 0 go upto before 6 by jumping 2 steps.
print("6------------------------------------------------------")

numbers=[10,20,30,40,50,60]
print(numbers[::2]) #start from 0 index and stop before end by jumping 2 steps.
print("7------------------------------------------------------")

numbers=[10,20,30,40,50,60]
print(numbers[::-1])#start from the end and go to the beginning by jumping 1 step backward.
print("8------------------------------------------------------")

numbers=[10,20,30,40,50,60]
print(numbers[5:1:-2])#start from index 5 and go to index 1 by jumping 2 steps backward.
print("9------------------------------------------------------")

numbers=[10,20,30,40,50,60]
print(numbers[-3:-1])#start from index -3 and go to index -1 by jumping 1 step backward.
print("10------------------------------------------------------")

#exercise-------
numbers=[10,20,30,40]
total=0
for num in numbers:
    total += num
    print(total)

    prices=[15,25,10,50,20]
    total=0
    for price in prices:
        total += price
        print(total)

prices=[15,25,10,50,20]
total=0
for price in prices:
    total += price
 
print(total) 
print("11------------------------------------------------------")

#find largest number in a list
numbers=[15, 8, 32, 12, 25]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number

print("the largest number is:", max)
print("12------------------------------------------------------")

#Find smallest number in the list
numbers=[15, 8, 32, 12, 25]
min=numbers[0]
for number in numbers:
    if number<min:
        min=number
print("the smallest number is:", min)
print("13------------------------------------------------------")

#find how many numbers are greater than 20
numbers=[10,25,15,40,30,5]
count=0
for number in numbers:
    if number>20:
        count+=1
print("14------------------------------------------------------")

#Calculate the sum of only the numbers greater then 20
nmbers=[10, 25, 15, 40, 30, 5]
total=0
for number in numbers:
    if number>20:
        total+=number
print ("the sum of numbers greater than 20  is:", total)
print("15------------------------------------------------------")

#show both clculation greater than 20 and count total numbers greater than 20
numbers=[5, 12, 25, 30, 8, 40]
total=0
count=0
for number in numbers:
    if number>20:
        total+=number
        count+=1
print('sum greater than 20:', total)
print('count of numbers greater than 20:', count)
print("16------------------------------------------------------")

#find the smallest number without using min()
numbers=[18, 7, 32, 4, 25,11]
smallest=numbers[0]
for number in numbers:
    if number<smallest:
        smallest=number

print("the smallest number is:", smallest)
print("17------------------------------------------------------")

#find the largest number without using max()
numbers=[12,45,6,29,3,50,18]
largest=numbers[0]
for number in numbers:
    if number>largest:
        largest=number

print("the largest number is:", largest)
print("18------------------------------------------------------")

#sum of even numbers in a list
numbers = [4, 7, 10, 13, 16, 19]
total = 0
count=0
even_numbers=[]
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        total += number
        count+=1
        average=total/count
print("The even numbers in the list are:", even_numbers) #list inside the bracket in single line
print("the sum of even numbers is:", total)
print("the average of even numbers is:", average)
print("the  even numbers are:", ",".join(str(number) for number in even_numbers))#list without bracket in single line
print("19------------------------------------------------------")

#another way to print even numbers in a list without using join() method
even_numbers = [4, 10, 16]

print("The even numbers in the list are:", end=" ")

for number in even_numbers:
    print(number, end=", ")
print("20------------------------------------------------------")

#searching in lists
fruits = ["apple", "banana", "orange", "mango"]
print("banana" in fruits)
print("grapes" in fruits)

numbers = [12, 7, 25, 40, 18, 30]
target=25
found=False
for number in numbers:
    if number==target:
        found=True
        print("Target found:", found)
print("21------------------------------------------------------")

#break
numbers=[1,2,3,4,5,6]
even_number=[]
for number in numbers:
    if number%2==0:
        even_number.append(number)
print("the even numbers are:",",".join(str(number) for number in even_number))

numbers = [3, 8, 11, 14]
even_numbers = []

for number in numbers:
    if number % 2 != 0:
        continue
    even_numbers.append(number)

print(even_numbers)
print("22------------------------------------------------------")

#calculate average , skip odd numbers ,sum of even numbers ,count total even numbers, print sum,count and average
numbers=[5, 10, 15, 20, 25, 30, 35]
even_numbers=[]
count=0
total=0
for number in numbers:
    if number%2!=0:
        continue
    even_numbers.append(number)
    total+=number
    count+=1
average=total/count
print("the sum is:",total)
print("the count is:", count)
print("the average is:",average)
print("the list is:",even_numbers)
print("------------------------------------------------------")

#skip odd  numbers, find largest even number.
numbers=[13,8,25,16,31,22,6,19]
for number in numbers:
    if number%2!=0:
        continue
    if number>largest:
        largest=number
print("the largest even number is:",largest)
print("24------------------------------------------------------")

#skip odd numbers, find smallest even number.
numbers=[13,8,25,16,31,22,6,19]
small_num=float("inf") #initialize small_num to positive infinity
for number in numbers:
    if number%2!=0:
        continue
    if number<small_num:
        small_num=number
print("the smallest even number is:",small_num)
print("25------------------------------------------------------")

