
#question 1

def problem1():
    number = int(input("Enter a number: "))
    for factor in range(2, number + 1):
         if number % factor == 0:
               is_prime = True

               for divisor in range(2, factor):
                     if factor % divisor == 0:
                          is_prime = False
                if is_prime:
                     print(factor)


# question 2

def problem2():
    n = int(input("Enter n: "))
    first = 0
    second = 1
    count = 1
    while count < n:
        next_number = first + second
        first = second
        second = next_number
        count += 1
    print(first)


#question 3

def problem3():
     word1 = input("Enter first word: ")
     word2 = input("Enter second word: ")
     if len(word1) != len(word2):
          print("Not anagram")
     else:
          is_anagram = True
          for letter in word1:
               if word1.count(letter) != word2.count(letter):
                    is_anagram = False
          if is_anagram:
               print("Anagram")
          else: 
                print("Not anagram")


#question 4 

def problem4():
     n = int(input("How many terms? "))
     term = 2
     count = 0
     while count < n:
          print(term)
          term += 2
          count += 1


#question 5

def problem5():
     numbers = [5, 2, 9, 1, 7, 4]
     for i in range(len(numbers)):
           for j in range(i + 1, len(numbers)):
                 if numbers[i] > numbers[j]:
                      temp = numbers[i]
                      numbers[i] = numbers[j]
                      numbers[j] = temp
     middle = len(numbers) // 2
     if len(numbers) % 2 == 1:
          print(numbers[middle])
     else:
          median = (numbers[middle - 1] + numbers[middle]) / 2
          print(median)

#question 6 
def problem6():
     number = int(input("Enter a number: "))
     total = 0
     divisor = 1
     while divisor < number:
          if number % divisor == 0:
               total += divisor
          divisor += 1
     if total == number:
          print("Perfect number")
     else:
          print("Not perfect number")

#question 7 
def problem7():
     number = input("Enter a number: ")
     total = 0
     for digit in number:
          total += int(digit)
     print(total)


#question 8 

def problem8():
     sentence = input("Enter a sentence: ")
     words = sentence.split()
     longest = ""
     index = 0
     while index < len(words):
          if len(words[index]) > len(longest):
               longest = words[index]
          index += 1 
     print(longest)


#question 9 

def problem9():
     sentence = input("Enter a sentence: ")
     alphabet = "abcdefghijklmnopqrstuvwxyz"
     sentence = sentence.lower()

     is_pangram = True
     for letter in alphabet:
          if letter not in sentence:
               is_pangram = False
     if is_pangram:
          print("Pangram")
     else:
          print("Not pangram")


# question 10 

def problem10():
     number = 2
     while number <= 1000:
          divisor = 2
          is_prime = True
          while divisor < number:
               if number % divisor == 0:
                    is_prime = False
               divisor += 1
          if is_prime:
               print(number)
               number += 1 
                  
               


          

     
          
          
               
          







     


     
          


     



          
          

               
          



     



                
          

                

     
          

     



     
               
               
                    
               

       
          
      
          
     

     
        
         











