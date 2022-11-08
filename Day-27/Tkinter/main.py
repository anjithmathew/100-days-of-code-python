import tkinter

window  = tkinter.Tk()
window.title("First Gui Program")
window.minsize(500,500)
#label 

my_label = tkinter.Label(text="hello Guys",font = ("Arial",24,"bold"))
my_label.pack()



window.mainloop()