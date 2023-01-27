import tkinter as tk


class TicTacToe:

    count = 0
    button = [tk.Button for i in range(9)]

    # for k in range(9):
    #     button_text[k] = ''

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("TicTacToe")
        self.window.geometry("300x200")

        self.button_text = [tk.StringVar() for k in range(9)]

        self.button_frame = tk.Frame(self.window, padx=10, pady=10)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)

        for i in range(3):
            for j in range(3):
                self.button_text[self.count] = tk.StringVar()
                self.button_text[self.count] = str(self.count)
                self.button[self.count] = tk.Button(self.button_frame, textvariable=self.button_text[self.count], text=str(self.count), font=('Arial', 18), command=self.msg)
                self.button[self.count].grid(row=i, column=j, sticky=tk.E + tk.W)
                self.count += 1

        self.button_frame.pack(fill="both", padx=10, pady=10)

        self.window.mainloop()

    def msg(self):

        for i in range(9):
            if self.button_text[i] == str(i):
                self.button_text[i].set('x')
        #      self.


play = TicTacToe()
