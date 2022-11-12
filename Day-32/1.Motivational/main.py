import datetime as dt
import smtplib
import random

EMAIL ="anjithmathew777@gmail.com"
PASSWORD = "djxmnugewhgsgaxi"
RECEIVER ="anjithmathew777@gmail.com"



# def lines():
#     with open("/home/anjithmathew/Documents/5.Pycharm/Daily Pain/daily.txt", "r+") as fh:
#         lines = fh.read().splitlines()
#         random_choice = random.randint(0, len(lines) - 1)
#         return lines[random_choice]


def date():
    now = dt.datetime.now()
    weekday = now.weekday()
    print(weekday)

#
# def connection(subject):
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(EMAIL,PASSWORD)
#         connection.sendmail(from_addr=EMAIL,to_addrs=RECEIVER,msg= subject)
#
#
#
#
# connection(lines())

date()