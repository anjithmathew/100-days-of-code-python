def check(number):
    if number % 2 ==0:
        return True
    
if check(int(input("Enter a number:"))):
    print("Even")
else:
    print("odd ")