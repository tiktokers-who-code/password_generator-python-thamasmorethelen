from tkinter import *
import random
import string


window = Tk()


def password_generator():
    password = []
    num = int(user_num.get())
    if num >= 12 and num <= 20:
        while len(password) < int(num):
            choice = random.choice(string.printable)
            if choice not in string.whitespace:
                password.append(choice)
    user_pass = ''.join(password)
    pass_wig.delete("1.0", END)
    pass_wig.insert(END, user_pass)


generator_btn = Button(window, text="Generate Password", command=password_generator)
generator_btn.grid(row=1, column=1)

user_num = StringVar()
user_input = Entry(window, textvariable=user_num, width=18)
user_input.grid(row=0, column=1)


pass_wig = Text(window, height=1, width=20)
pass_wig.grid(row=2, column=1)


def app():
    window.mainloop()

if __name__ == '__main__':
    app()
