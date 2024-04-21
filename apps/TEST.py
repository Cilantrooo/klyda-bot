import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the display
        self.display = tk.Entry(master, width=25, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        row = 1
        col = 0
        for text in button_list:
            button = tk.Button(master, text=text, width=5, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Create clear button
        clear_button = tk.Button(master, text="Clear", width=11, command=self.clear_display)
        clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def button_click(self, text):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, str(current) + str(text))

    def clear_display(self):
        self.display.delete(0, tk.END)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()