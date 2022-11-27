# bmi program


height = float(input("Enter Your height  :"))

weight = float(input("Enter Your weight in Kg :"))

bmi = weight/height**2
if bmi <18.5:
    print("you are under weight")
elif bmi <25:
    print("you are normal weight")
elif bmi <30:
    print("you are over weight")
elif bmi <35:
    print("you are obses")
else:
    print("you are  clinically obses")
    
