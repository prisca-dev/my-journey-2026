# country = input("Enter Country: ").title()

# match country:
#     case "United States":
#         print("US")
#     case"Nigeria" :
#         print("NGN")
#     case "Ghana":
#         print("GH")
#     case"England" |"Scotland" | "Wales":
#         print("UK")
#     case _:
#         print("country not found")

     
# for i in (1,2,3):
#     for x in(1,4,5):
#         print(i,x)
#         # print(x,i)

# colour  = ('red','black','white')
# size = ('L', 'M','S')
# for i in colour:
#    for x in size:
#       print(i,x)
# import time
# years = [2025,2026]
# months =['Jan','Feb']
# days = range(1,29)
# for month in months:
#    for year in years:
#       for day in days:
#          print(f"{year}_{month}_{day}")
#          time.sleep(1)
# week = ['Monday','Tuesday','Wednesday','Thursdays','Friday','Saturday','Sunday']
# weekends = ('Saturday','Sunday')
# for day in week:
#    if day in weekends:
#       print(day," is a weekend")
#    continue
#            print(day)      

# i = 1
# while i<4:
#     print (i)
#     i+=1

# i = 1
# while i<=5:
#     print(i)
#     i+=1 

# answer  = ''

# while answer != 'yes':
#     answer = input("Do you agree? ")
# print("Thank you")

# import random as r
# System choose a random color from the list 
# attempts = 0
# color_list = ['red','green','blue','yellow','white','black']
# while attempts<=3:
#     colour_choice = r.choice(color_list)

# #System prompt the use to guess the color
# user_guess = input("Guess what colour i picked: ").strip().Lower()
# attempts + =1 #System records each attempts
# if user_guess == colour_choice:
#     print(f"You guessed right. i picked{colour_choice}")
#     break
# else:
#     print("Wrong choice , Try Again")

# attempts = 0
# answer = ""
# while attempts < 3:
#      answer = input("Do you agree?: ").strip().lower()
#      attempts +=1
#      if answer == 'yes':
#          print("Glad we're on same page")
#          break
#      else:
#          print("Wrong answer.")
#          continue
# else:
#    print("3 strike!, you are out")

# empty = ['a',True,3,4.8]
# lst = list("Python")
# print(empty)
# print(lst)
# print(type(empty))
import statistics as s
raph = list(range(1,40,5))
print(max(raph))
print(min(raph))
print(sum(raph))
print(s.mean(raph))
print(s.median(raph))

animals =['gorilla','lizard']
animals.append('goat')
animals.append('tiger')
animals.insert(0,'lion')
print(animals)
animals[2]= 'python'
print(animals)
animals.pop(3)
print(animals)
