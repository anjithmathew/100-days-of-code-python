import tkinter

window  = tkinter.Tk()
window.title("First Gui Program")
window.minsize(500,500)
#label 

my_label = tkinter.Label(text="hello Guys")
my_label.pack()
window.mainloop()