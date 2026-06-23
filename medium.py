#Question 1
numbers = [5, 12, 3, 20, 8]
largest = numbers[0]
for num in numbers:
     if num > largest:
          largest = num
print("Largest number:", largest)

#question 2 

numbers = [10, 20, 30, 40, 50]
total = 0
index = 0
while index < len(numbers):
    total += numbers[index]
    index += 1
average = total / len(numbers)
print("Average:", average)

#question 3

word = input("Enter a word: ")
is_palindrome = True
for i in range(len(word) // 2):
     is_palindrome = False
     break
if is_palindrome:
     print("Palindrome")
else:
     print("Not a palindrome")
     
#Question 4

n = int(input("How many terms? "))
term = 2
count = 0
while count < n:
     print(term)
     term = term * 2 
     count += 1

#Question 5 

numbers = [5, 12, 3, 20, 8]

largest = numbers[0]
second_largest = numbers[0]
for num in numbers:
     if num > largest:
        second_largest = largest
        largest = num
     elif num > second_largest and num != largest:
            second_largest = num
print("Second largest:", second_largest)

#question 6 

number = int(input("Enter a number: "))
factorial = 1
count = 1

while count <= number:
    factorial *= count
    count += 1
print("Factorial:", factorial)

#question 7
number = int(input("Enter a number: "))
perfect_square = False
for i in range(1, number + 1):
    if i * i == number:
          perfect_square = True
          break
if perfect_square:
     print("Perfect square")
else:
     print("Not a perfect square")

#question 8

num = 2
total = 0

while num <= 100:
   is_prime = True
   divisor = 2
   while divisor < num:
      if num % divisor == 0:
            is_prime = False
            break
      divisor += 1
if is_prime:
     total += num
num += 1
print("Sum of primes:", total)


#question 9 

sentence = input("Enter a sentence: ")
words = sentence.split()
count = 0
for word in words:
      count += 1
print("Number of words:", count)


#question 10 

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

index = 0

print("Common elements:")
while index < len(list1):
      if list1[index] in list2:
         print(list1[index])
      index += 1
   


     
    
      
              
  


          
     
     


         
          


          


          
     



