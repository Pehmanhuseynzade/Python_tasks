#TASK 1
# name = "Pehman"
# age = 21
# sentence = f"My name is {name}. I am {age} years old"
# print(sentence)

#TASK 2

# name = "Pehman"
# age = 21
# height = 178
# student = True

# print(type(name),type(age),type(student))

#TASK 3

# my_string = "Hello, World!"
# slice_string2 = my_string[-6:]
# print(slice_string2)

#TASK 4

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[::2])

# #TASK 5
# my_string = "Python"
# print(my_string[::1])

#TASK 6

# sentence = "    I love programming in Java"
# new_sentence = sentence[:22]+ "Python"
# print(len(sentence.strip()))


#ekrana 10 dene salam yaz

# word = "salam"
# stars = ""
# for letter in word:
#     if letter == "a":
#         letter = "*"
#     stars+=letter
# print(stars)




# players = ["Ronaldo","Messi","Bale","Benzema","Reus"]
# r_players = []
# for i in players:
#     if i.startswith("R"):
#         r_players.append(i)
# print(r_players)



# word = "salam"
# stars = ""
# for letter in word:
#     if letter == "a":
#         letter = "*"
#     stars+=letter
# print(stars)


#--------------------------list version-------------------------------------------
# players = ["Ronaldo", "Messi", "Bale", "Benzema"]
# new_arr = []
# for player in players:
#     new_arr.append(list(player))
# print(new_arr)

#------------------for version-----------------------------------

# players = ["Ronaldo", "Messi", "Bale", "Benzema"]
# new_arr = []
# for player in players:
#     player_arr = []
#     for new_player in player:
#         player_arr.append(new_player)
#     new_arr.append(player_arr)

# print(new_arr)





# players = ["Ronaldo", "Messi", "Bale", "Benzema"]
# new_arr = []
# for player in players:
#     new_arr.append(list(player))
# print(new_arr)





# players = ["Ronaldo", "Messi", "Bale", "Benzema"]
# new_arr = []
# for player in players:
#     player_arr = []
#     for new_player in player:
#         player_arr.append(new_player)
#     new_arr.append(player_arr)
# print(new_arr)


# number = (5,)
# print(type(number))


# import pandas as pd

# file_path = r'C:\Users\pehman.huseynzade\OneDrive - Agro Dairy LLC\Documents\Job\Job1\updated version hr\Book1.xlsx'
# print(pd.read_excel(file_path,index_col=0))



#---------------------------
# arr = []
# while 5>len(arr):
#     numbers = int(input("Ededi daxil edin: "))
#     if numbers % 2 == 0:
#         arr.append(numbers)
#     print(arr)

# print("SON")
#----------------------------

# Görev 1: Pozitif Sayılar Toplamı
# Görev: Kullanıcıdan sürekli olarak pozitif sayılar girmesini isteyin ve girilen sayıların toplamını hesaplayın. Kullanıcı negatif bir sayı girdiğinde program dursun ve toplamı ekrana yazdırın.
# İpucu: while döngüsünü kullanarak, negatif bir sayı girilene kadar döngü devam etmelidir.

# toplam = 0

# while True:
#     number = int(input("Enter a positive number (negative to quit): "))
#     if number < 0:
#         break  
#     toplam += number  

# print("Toplam:", toplam)
# print("SON!")

# Görev 2: Kullanıcıdan Şifre İsteme
# Görev: Kullanıcıdan doğru bir şifre girene kadar şifre istemeye devam edin. Şifre doğru girildiğinde, "Giriş Başarılı" mesajı verin ve programı sonlandırın.
# İpucu: Şifreyi sabit bir değer olarak kodlayın (örneğin, "12345").


# password = "AgroDairy123!"
# while True:
#     true_pass = input("Enter the password:")
#     if password == true_pass:
#         break
# print("Password is succesfull!")
    


# Görev 3: Faktöriyel Hesaplama
# Görev: Kullanıcıdan bir sayı alın ve bu sayının faktöriyelini hesaplayın. Faktöriyel, 1'den başlayarak verilen sayıya kadar olan tüm pozitif sayıların çarpımıdır.
# İpucu: Örneğin, 5! = 5 * 4 * 3 * 2 * 1 = 120. Bir while döngüsü kullanarak faktöriyel hesaplayın.

# factorial_num = int(input("Enter the number:"))
# factorial = 1
# while factorial_num>1:
#     factorial*=factorial_num
#     factorial_num -= 1
# print(factorial)



# Görev 1: Pozitif Sayılar Toplamı
# Görev: Kullanıcıdan sürekli olarak pozitif sayılar girmesini isteyin ve girilen sayıların toplamını hesaplayın. Kullanıcı negatif bir sayı girdiğinde program dursun ve toplamı ekrana yazdırın.
# İpucu: while döngüsünü kullanarak, negatif bir sayı girilene kadar döngü devam etmelidir.

# number = int(input("Enter the number:"))
# toplam = 0
# while True:
#     if number<0:
#         break
#     toplam+=number
# print(toplam)




#Fibanocci


# n = int(input("Fibonacci serisinde kaç eleman görmek istersiniz?: "))

# a, b = 0, 1  # İlk iki Fibonacci sayısı

# # İlk iki sayıyı yazdırıyoruz, çünkü Fibonacci serisi 0 ve 1 ile başlar
# print("Fibonacci Serisi:")
# print(a, end=' ')
# if n > 1:
#     print(b, end=' ')

# # Fibonacci serisini hesaplamak ve yazdırmak için döngü
# for _ in range(2, n):
#     a, b = b, a + b
#     print(b, end=' ')
# print()  # Sonunda yeni bir satıra geçmek için






# Görev 3: Liste Elemanlarını Ters Çevirme
# Görev: Bir listenin elemanlarını ters sırada ekrana yazdırın. Örneğin, [1, 2, 3, 4, 5] listesi için çıktı [5, 4, 3, 2, 1] olmalıdır.
# İpucu: for döngüsü kullanarak listeyi tersten yazdırın.

# list_1 = [1,2,3,4,5]
# list_2 = []

# for i in list_1:
#     list_2.append(i)
# list_2.reverse()
# print(list_2)


#1--------------------------------------------------------

# def adding_elemets():
#     arr = []
#     while True:
#         elements = input("Adding elemets to list:")
#         if elements.lower() == "stop":
#             break
#         arr.append(elements)
#     return arr
# print("Final List:",adding_elemets())


#2-------------------------------------------------------

# def sorting():
#     arr = []
#     while True:
#         numbers = input("Enter the numbers:")
#         if numbers.lower() == "stop":
#             break
#         arr.append(int(numbers))
#     arr.sort()
#     return arr
# print("Final List:",sorting())

#3-------------------------------------------------------
# import random
# nums = [x for x in range(100)]
# print(random.choice(nums))








 












