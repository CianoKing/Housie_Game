import random
from tkinter import Canvas, PhotoImage, Button


class NumberChecker:
    def __init__(self):
        self.continue_button = None
        self.board_canvas = None
        self.num_list = [a for a in range(1, 91)]
        self.gone_nums = []
        self.circle = PhotoImage(file="green_circle.png")

    def fetch_number(self):
        num = random.choice(self.num_list)
        self.num_list.remove(num)
        self.gone_nums.append(num)
        return num

    def continue_game(self):
        self.board_canvas.destroy()
        self.continue_button.destroy()

    def board(self):
        x_cord = 0.5
        y_cord = 40
        self.board_canvas = Canvas(width=500, height=500)
        self.board_canvas.grid(row=0, column=0, rowspan=3, columnspan=2)
        for i in range(1, 91):
            if x_cord >= 10:
                x_cord = 0.5
                y_cord += 50

            if i in self.gone_nums:
                self.board_canvas.create_image(x_cord * 50, y_cord, image=self.circle)
            self.board_canvas.create_text(x_cord*50, y_cord, text=i, font=("Charter BT", 20, "bold"))
            x_cord += 1
        self.continue_button = Button(text="CONTINUE", width=40, pady=5, font=("Charter BT", 10, "bold"),
                                      command=self.continue_game)
        self.continue_button.grid(row=3, column=0, pady=5, columnspan=2)
