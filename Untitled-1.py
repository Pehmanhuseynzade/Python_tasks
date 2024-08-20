# text = "Hello World! I am Pehman Huseynzade!"

# convert_to_lower = text.lower()

# letters = {}

# for characters in convert_to_lower:
#     if characters.isalpha():
#         if characters in letters:
#             letters[characters]+=1
#         else:
#             letters[characters] = 1
# the_most_popular_characters = max(letters,key = letters.get)
# count_of_letters = letters[the_most_popular_characters]

# print(f"The most popular letter:{the_most_popular_characters}")
# print(f"count of letter: {count_of_letters}")




# def popular_letter(text):
#     convert_to_lower = text.lower()
#     letters = {}
#     for characters in convert_to_lower:
#         if characters.isalpha():
#             if characters in letters:
#                 letters[characters]+=1
#             else:
#                 letters[characters] = 1
#     the_most_popular_letter = max(letters,key = letters.get)
#     count_of_letters = letters[the_most_popular_letter]
#     print(f"The most popular letter: {the_most_popular_letter}")
#     print(f"Count of letter:{count_of_letters}")
# text = " Salam Baki. Biz qayitdiq!"
# print(popular_letter(text))







# new_list = []

# while True:
#     elements = input(" Add new elemnents to list:")
    
#     if elements.lower() == "stop":
#         break    
#     new_list.append(elements)
    
# print("Show list:",new_list)





# # Boş bir liste oluştur
# liste = []

# # Kullanıcıdan eleman eklemesini sağla
# while True:
#     eleman = input("Listeye eklemek istediğiniz bir eleman girin (durdurmak için 'stop' yazın): ")
    
#     if eleman.lower() == "stop":
#         break  # "stop" yazıldığında döngüyü kır
    
#     liste.append(eleman)  # Elemanı listeye ekle

# # Listenin içeriğini yazdır
# print("Liste içeriği:", liste)






#OOP OBJECT ORIENTED PROGGRAMMING:

#Sinif (Class) təyin edirik
# class Car:
#     # Sinifin xüsusiyyətləri (Attributes)
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0

#     # Sinifin metodu (Method)
#     def accelerate(self, increase):
#         self.speed += increase

#     def brake(self, decrease):
#         self.speed -= decrease

#     def display_info(self):
#         print(f"Car: {self.year} {self.make} {self.model}, Speed: {self.speed} km/h")

# # Obyekt yaradılır (Object)
# my_car = Car("Toyota", "Corolla", 2022)

# # Obyektin metodu çağırılır (Method)
# my_car.accelerate(50)
# my_car.display_info()

# my_car.brake(20)
# my_car.display_info()




#Constroctur or INITALIZER method

# class Person:
#     # Konstruktor metodu (__init__)
#     def __init__(self, name, age):
#         self.name = name  # Ad xüsusiyyəti (Attribute)
#         self.age = age    # Yaş xüsusiyyəti (Attribute)

#     # Metod
#     def greet(self):
#         print(f"Salam, mənim adım {self.name}dir, mən {self.age} yaşındayam.")

# # Yeni obyekt yaradılır (Person sinifindən)
# person1 = Person("Ali", 25)

# # Greet metodu çağırılır
# person1.greet()

#---------------CALCULATOR---------------------------------------------------------

# class Calc(object):
#     """init method"""
    
#     def __init__(self, num1, num2):
#         self.value1 = num1
#         self.value2 = num2
#         """methods"""
    
#     def add(self):
#         result = self.value1 + self.value2
#         return result
    
#     def sub(self):
#         result = self.value1 - self.value2
#         return result
    
#     def mult(self):
#         result = self.value1 * self.value2
#         return result
    
#     def division(self):
#         result = self.value1 // self.value2
#         return result
    
#     def percentage(self, percentage):
#         """Yeni funksiya: Birinci dəyərin müəyyən faizi"""
#         result = (self.value1 * percentage) / 100
#         return result

# # Obyekt yaradılır
# final_calc = Calc(20, 5)

# # Yeni funksiya istifadəsi
# print(final_calc.percentage(25))  # 20-nin 25%-i


#=========TASK=========================

# class Books(object):
#     def __init__(self,name,auther,price,page_count):
#         self.name = name
#         self.auther = auther
#         self.__price = price
#         self.page_count = page_count
        
#     def show_price(self):
#         return self.__price
    
#     def enter_price(self):
#         pass
        
#     def get_information(self):
#         print(f"Book name is {self.name}. The book was written by {self.auther}.The book's : {self.__price}$ and book is {self.page_count} ")
        
# book = Books( "Sefiller","Viktor Huqo",22,261)
# book.get_information() 






