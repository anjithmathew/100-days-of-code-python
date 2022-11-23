def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    removed = '$'
    str_float = float(d.split(removed, 1).pop(1))
    return str_float


def percent_to_float(p):
    removed = '%'
    str_float = float(p.split(removed, 1).pop(0))
    percentage = str_float/100
    return percentage



main()
