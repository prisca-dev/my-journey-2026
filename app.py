# email = input("Enter Email: ")
# print(email is not None and email !="")

score = int(input("Enter score: "))
submitted_project = False
if score >=90:
    question = input("Have yousubmitted your project?? [Yes or No]: ").strip().lower()
    if question == 'yes':
        submitted_project = True
        print('A+') 
    else:
        print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score <60:
    question = input("Have yousubmitted your project?? [Yes or No]: ").strip().lower()
    if question == 'yes':
        submitted_project = True
        print('F') 
    else:
        print('F9')

