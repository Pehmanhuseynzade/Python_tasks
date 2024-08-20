# def number_function(number):
#     if number > 0 and number % 2 == 0:
#         return "Daxil etdiyiniz eded cut ve musbet ededdir"
#     elif number == 0 :
#         "sifir ne tek ne de cutdur"
#     elif number>0 :
#         return number**2
#     elif number<0:
#        return "menfi eded daxili etmeyin"

# print(number_function(int(input(":"))))    
#--------------------------------------------------------------------------
# def comprassion(a,b,c):
#     if a>b>c or a>c>b:
#         return a
#     elif b>a>c or b>c>a:
#         return b
#     elif c>a>b or c>b>a:
#         return c
#     else:
#         return "hamisi beraberdir!"
# print(comprassion(int(input("a:")),int(input("b:")),int(input("c:"))))

# --------------------------------------------------------------------------------

# def sentences(sentence):
#     if len(sentence)%2 == 0:
#         return "hello world!"
#     elif len(sentence)%2 == 1:
#         return str(len(sentence))*3
# print(sentences(input("Sentence:")))
        
#--------------------------------------------------------------------------------

# def sum():
#     sum = 0
#     for i in range(1,100):
#         if i%2 == 1:
#             sum+=i
#     return sum
# print(sum())
        
        
#----------------------------------------------------------------------

# set = {'bir':1,'iki':2,'on':10}
# # keys = set.keys()
# # values = set.values()
# for x,y in set.items():
#     print(x,y)
# print(type(set.items()))


#-----------------------------------------------------------------

# def my_enumerate(data,start = 0):
#     result = []
#     for i in data:
#         result.append((start,i))
#         start+=1
#     return result
# print(my_enumerate("salam",3))


#---------------------------------------------------------------------

# import random as rand
# data = [rand.randint(1,20) for x in range(1,10)]
# print(data)




#----------------------------------------------------
# import random as rand

# while True:
    
#     num1 = int(input("Enter the number(1-20):"))
    
#     num2 = int(input("Enter the number(1-20):"))
    
#     if 1<=num1<=20 and 1<=num2<=20:
#         break
#     else:
#         print("Please again enter the number between 1 and 20")
# data = rand.sample(range(1,20),9)
# print(f"Your numbers:{data}")

# if num1 in data and num2 in data:
#     print("Your numbers is succesful!Congrats!")
# else:
#     print("Failed!Good Luck!")
    
# Yuxaridaki kodu def ile yazmaq---------------------------------------------------------------


# import random as rand

# def random_numbers():
#     while True:
#         num1 = int(input("Enter the first number (1-20): "))
#         num2 = int(input("Enter the second number (1-20): "))

#         if num1 == num2:
#             print("Numbers must be different. Please enter different numbers.")
#             continue
        
#         if 1 <= num1 <= 20 and 1 <= num2 <= 20:
#             break  
#         else:
#             print("Please enter numbers between 1 and 20.")  
#     data = rand.sample(range(1, 21), 10) 
#     print(f"Your random numbers: {data}")

#     if num1 in data and num2 in data:
#         print("Your numbers are successful! Congrats!")
#     else:
#         print("Failed! Good Luck!")    

# random_numbers()

#-------------------------------------------------------------

# arr = []
# for i in range(10):
#     arr.append(i)
# print(arr)







# data = [x for x in range(10) if x%2==0]
# print(data)



# hello = lambda:"fcdcdcd"
# print(hello())



# add = lambda a,b:a+b
# print(add(3,4))


# import random as rand
# count_func = lambda count:[rand.randint(1,30) for x in range(count)]
# print(count_func(5))



# nums = [1,2,3,4,5]
# data = map(str,nums)
# print(list(data))




# nums = [1,2,3,4,5]
# data = map(lambda num : str(num**2),nums)
# print(list(data))


# nums = [1,2,3,4,5]
# data = map(lambda num:str(num),nums)
# print(data)


# Tapşırıq 2:Verilmiş bir string içərisində hər hərfin neçə dəfə təkrarlandığını hesablayan bir funksiy yaz. Nəticələri bir dictionary (sözlük) olaraq qaytar.

# def repeat_text(text):
#     filtered_text = [letter for letter in text]
    
#     count_letter = map(lambda letter:(letter,filtered_text.count(letter)),set(filtered_text))
    
#     return dict(count_letter)
# text = "Hello World!"
# print(repeat_text(text))

# Tapşırıq 1: Müsbət Rəqəmləri Tap və Onların Kvadratlarını Al

# def posetive_numbers(numbers):
#     filtered_numbers = [number for number in numbers if number>0]
    
#     square_numbers = map(lambda number:number**2,filtered_numbers)
    
#     return set(square_numbers)
# numbers = [1,-1,-2,-4,4,6,3]
# print(posetive_numbers(numbers))

# from faker import Faker
# fake = Faker()
# print(fake.name())

#->Callback<-
#1

# numbers: list[int] = [1,2,3,4]
# print(numbers)
# numbers: list[str] = list(map(str,numbers))
# print(numbers)

# Tapşırıq 2:Verilmiş bir string içərisində hər hərfin neçə dəfə təkrarlandığını hesablayan bir funksiy yaz. Nəticələri bir dictionary (sözlük) olaraq qaytar.


def sentence(text):
    filtered_text = [letter for letter in text]
    
    count_letters = map(lambda letter:(letter,filtered_text.count(letter)),set(filtered_text))
    
    return dict(count_letters)
text = "bvjhfjhsbjhb"
print(sentence(text))