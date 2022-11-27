def leap(year):
    if year%4 ==0:
        if year % 100 ==0:
            if year % 4 ==0:
                print(leap)
            else:
                print("not leap")

leap(2100)