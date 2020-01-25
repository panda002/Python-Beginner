from tkinter import *


def onclick():
    print(Day1)
    print(Day2)
    print(Day3)


cal = Tk()
cal.title("ToDo List")
text_input = StringVar()
text_input1 = StringVar()
text_input2 = StringVar()


btn1 = Button(cal, padx=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="Submit", command=onclick).grid(row=0, column=5)
btn2 = Button(cal, padx=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="Submit", command=onclick).grid(row=1, column=5)
btn3 = Button(cal, padx=10, bd=4, fg='black', font=('arial', 20, 'bold'),
              text="Submit", command=onclick).grid(row=2, column=5)

Day1 = Entry(cal, text="1. ", font=('arial', 20, 'bold'), textvariable=text_input, bd=5, insertwidth=10,
             bg="light blue", justify='left').grid(columnspan=4)

Day2 = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input1, bd=5, insertwidth=10,
             bg="light blue", justify='left').grid(columnspan=4)

Day3 = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input2, bd=5, insertwidth=10,
             bg="light blue", justify='left').grid(columnspan=4)

var1 = IntVar()
Checkbutton(cal, text=Day1, variable=var1).grid(row=4, sticky=W)
var2 = IntVar()
Checkbutton(cal, text=Day2, variable=var2).grid(row=5, sticky=W)
var3 = IntVar()
Checkbutton(cal, text=Day3, variable=var3).grid(row=4, sticky=W)

cal.mainloop()
