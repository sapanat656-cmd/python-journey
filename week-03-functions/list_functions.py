##1.find the largest number in a list
#find_max()
def find_max(numbers):
    largest=numbers[0]
   
    for number in  numbers:
        if number>largest:
         largest = number
    return largest
result=find_max([12,5,28,17])
print (result)

#Find the smallest number in a list
def find_min(numbers):
 smallest=numbers[0]
 for number in numbers:

   if number<smallest:
      smallest=number
 return smallest
smallest=find_min([12,5,28,17])
print(smallest)

#Count the number of even numbers in the list
def count_even(numbers):
   count=0
   for number in numbers:
      if number%2==0:
         count+=1
   return count
count=count_even([3,8,10,5,7,12])
print (count)

#do the sum of all numbers in the list
def sum_list(numbers):
   total=0
   for number in numbers:
      total+=number
   return total
sum=sum_list([10,20,30,40])
print(sum)

##double_numbers(numbers)
def double_numbers(numbers):
   double=[]
   for number in numbers:  
      number=number*2
      double.append(number)
   return double
double=double_numbers([2,4,6,8])
print(double)

#sum of only the even numbers in a list
def sum_even(numbers):
   total=0
   for number in numbers:
      if number%2==0:
         total+=number
   return total
result=sum_even([13,8,25,16,31,22,6,19])
print(result)

#filter_positive(numbers)
def filter_positive(numbers):
   positive=[]
   for number in numbers:
      if number>0:
         positive.append(number)
   return positive
total=filter_positive([-5,10,-2,8,0,15])
print(total)

#Calculate_average(numbers)
def calculate_average(numbers):
   count=0
   total=0
   for number in numbers:
      total+=number
      count+=1
   average=total/count
   return average
result=calculate_average([10,20,30,40])
print(result)

#count positve numbers in the list
def count_positive(numbers):
   count=0
   for number in numbers:
      if number>0:
         count+=1
   return count
total=count_positive([-5,10,-2,8,0,15])
print (total)

#remove_duplicates(numbers)
def remove_duplicates(numbers):
   unique=[]
   for number in numbers:
      if number not in unique: #tells the number is repeated or not
         unique.append(number)
   return unique
result=remove_duplicates([4,2,4,7,2,9,7])
print(result)

#second_largest(number) without using max(), sort()
def second_largest(numbers):
   unique=[]

   for number in numbers:
      if number not in unique:
         unique.append(number)
   print (unique)

   largest=unique[0]
   second=None

   for number in unique:
     if number>largest:
        second=largest
        largest=number
     elif number<largest and (second is None or number>second):
        second=number
   return second 

result=second_largest([10,5,20,8,20,15])
print (result)

#second smallest number
def second_smallest(numbers):
   unique=[]
   for number in numbers:
      if number not in unique:
         unique.append(number)
   print (unique)

   smallest=unique[0]
   second=None
   for number in unique:
      if number<smallest:
         second=smallest
         smallest=number
      elif number>smallest and (second is None or number<second):
         second=number
   return second
result=second_smallest([12,5,8,3,5,10,3])
print ("the second smallest number in the list is:", result)

#count_frequency(numbers) that counts how many times each number appears in a list
def count_frequency(numbers):
   unique=[]
   for number in numbers:
      if number not in unique:
         unique.append(number)
   print (unique)

   for number in unique:
      count=0
      for item in numbers:
         if item==number:
            count+=1
      print(number, "appears", count, "times")
count_frequency([2,5,2,8,5,2])

#separate_even_odd(numbers)
def separate_even_odd(numbers):
   even=[]
   odd=[]
   for number in numbers:
      if number%2==0:
         even.append(number)
      else:
         odd.append(number)
   return odd ,even    
result=separate_even_odd([12,5,8,3,10,7,4])
odd,even=result
print("Even numbers:", even)       
print ("odd numbers:",odd)

#find common numbers in two lists
def common_numbers(list1,list2):
   common=[]
   for number in list1:
      if number in list2:
         if number not in common:
            common.append(number)
   return common
result=common_numbers([1,2,3,4,5], [3,4,5,6,7])
print(result)

#remove all negative numbers, put +ve and 0 
def remove_negative(numbers):
  positive=[]
  for number in numbers:
     if number>=0:
        positive.append(number)
  return positive
result=remove_negative([-5,10,-2,8,0,-7,15])
print("the list of positive numbers is:", result)    


#Count numbers greater than the average
def count_above_average(numbers):
      total=0
      count=len(numbers)

      for number in numbers:
         total+=number
      average=total/count

      count=0

      for number in numbers:
       if number>average:
        count+=1
      return count
result=count_above_average([10,20,30,40,50])
print (result)

#count_above_average(numbers)
def count_above_average(numbers):
   count=len(numbers)
   total=0

   for number in numbers:
      total+=number
   average=total/count

   count=0
   for number in numbers:
      if number>average:
          count+=1
   return count
result=count_above_average([10,10,10,10])
print(result)

#merge_unique(list1, list2), don't use set
def merge_unique(list1, list2):
   unique1=[]
   for number in list1:
         if number not in unique1:
          unique1.append(number)

   for number in list2:
     if number not in unique1:
      unique1.append(number)
   return unique1
result=merge_unique([2,4,6,8],[4,6,10,12])
print(result)

#find_missing_numbers()
def find_missing_numbers(numbers, start,end):
   missing=[]
   
   for number in range(start,end+1):
      if number not in numbers:
         missing.append(number)
   return missing
result=find_missing_numbers([1,3,5],1,5)
print(result)

   




         

               


         

      