def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

    n *= kwargs["add"]
    n +=  kwargs["multi"]
    print(n)

calculate(10,add= 10,multi=10)