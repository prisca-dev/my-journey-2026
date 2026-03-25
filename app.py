# email = input("Enter Email: ")
# print(email is not None and email !="")

score = int(input("Enter score: "))
submitted_project = False
# if score >=90:
#     question = input("Have yousubmitted your project?? [Yes or No]: ").strip().lower()
#     if question == 'yes':
#         submitted_project = True
#         print('A+') 
#     else:
#         print("A")
# elif score >=80:
#     print("B")
# elif score >=70:
#     print("C")
# elif score <60:
#     question = input("Have yousubmitted your project?? [Yes or No]: ").strip().lower()
#     if question == 'yes':
#         submitted_project = True
#         print('F') 
#     else:
#         print('F9')

# score = int(input("Enter Score: "))
# submitted= False
# question = input("Have you submitted your project [yes or no: ").strip().lower()
# if score >=50:
#     print("Passed")
# else:
#     print("Fail")

# if question == 'yes':
#     print("project submitted")
# else:
#     print("Project not submitted")

# print("Passed" if score>=50 else "Fail")

grade = "Passed" if score >=50 else "Fail"
print(grade)


    

