##function
def add_ten(number):
    return number+10
print(add_ten(7))

#multiply two numbers
def multiply(a,b):
 return a*b
print(multiply(4,5))

def check_voting_age(age):
    if age>=18:
        return "You are eligible to vote"
    else:
        return "You are not eligible to vote"
print(check_voting_age(20))

#none result function
def show_number(number):
   print(number*2)
result=show_number(5)
print(result) #this will print None because the function does not return anything

#use return instead of print
def show_number(number):
   return number*2
result=show_number(5)
print(result) #this will print 10 because the function returns a value

def calculate_price(price):
  print(price+5)
  return price*2
result=calculate_price(10)
print(result)

#check if a number is positive, negative or zero
def check_number(number):
 if number>0:
  return"Positive"
 elif number==0:
  return "Zero"
 elif number<0:
  return"negative"
answer=check_number(-3)
print(answer)

#check_age
def check_age(age):
  if age>=18:
    print("Adult")
  else:
    print("Minor")
result=check_age(16)
print(result) #this will print None because the function does not return anything

#function+loop+if
def print_even(n):
  for i in range(1, n+1):
    if i%2==0:
      print(i)
print_even(10)
print("------------------------------------------------------")

def sum_numbers(n):
  total=0

  for i in range(1,n+1):
    total+=i
    print(total)
    
  return total
result=sum_numbers(4)
print(sum_numbers(4))

