from tkinter import *
import requests

def get_quote():
    data_get = requests.get('https://api.kanye.rest/')
    quotes = data_get.json()
    return quotes['quote']



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="/home/anjithmathew/Documents/1.Python/100-days-of-code-python/Day-33/2.kanye west/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=get_quote(), width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="/home/anjithmathew/Documents/1.Python/100-days-of-code-python/Day-33/2.kanye west/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=gquote)
kanye_button.grid(row=1, column=0)


window.mainloop()
