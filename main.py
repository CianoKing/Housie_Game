from tkinter import *
from number_checker import NumberChecker

window = Tk()
window.minsize(width=500, height=500)

window.config(pady=30, padx=100, bg="black")
label = Label(text="HOUSIE", font=("BREMEN BD BT", 40, "bold"), bg="black", highlightthickness=0, fg="blue")
label.grid(column=0, row=0, columnspan=2)
canvas = Canvas(bg="light blue", width=300, height=300)
canvas.create_text(150, 150, text="Let's\nPlay", justify="center", font=("Charter BT", 50, "bold"))
canvas.grid(row=1, column=0, columnspan=2)
number_obj = NumberChecker()


def hold():
    global loop0, loop1, loop2, loop3
    if loop1 != "":
        window.after_cancel(loop1)
    if loop2 != "":
        window.after_cancel(loop2)
    if loop3 != "":
        window.after_cancel(loop3)
    number_obj.board()


hold_button = Button(text="HOLD", width=15, pady=7, font=("Charter BT", 10, "bold"), command=hold)
hold_button.grid(row=2, column=0, pady=5)

check_num = 0
dot = "."
loop0 = ""
loop1 = ""
loop2 = ""
loop3 = ""


def play():
    global loop0
    canvas.delete("all")
    canvas.create_text(150, 150, text="Ready..", font=("Charter BT", 50, "bold"))
    loop0 = window.after(2000, game_on)


play_button = Button(text="PLAY", width=15, pady=7, font=("Charter BT", 10, "bold"), command=play)
play_button.grid(row=2, column=1, pady=5)


def game_on():
    print("started")
    global dot, check_num, loop1
    dot = "."
    check_num = 0
    label.config(text="Next Number is.....", font=("BREMEN BD BT", 20, "bold"))
    canvas.delete("all")
    num = number_obj.fetch_number()
    canvas.create_text(150, 150, text=num, font=("Charter BT", 90, "bold"))
    loop1 = window.after(4000, pause)


def pause():
    global dot, check_num, loop2, loop3
    canvas.delete("all")
    if check_num < 3:
        canvas.create_text(150, 150, text=dot, font=("Charter BT", 70, "bold"))
        dot += " ."
        check_num += 1
        loop2 = window.after(1000, pause)
    else:
        loop3 = window.after(250, game_on)


window.mainloop()
