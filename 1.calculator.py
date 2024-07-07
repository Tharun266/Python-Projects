import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Calculator")
        self.geometry("400x500")

        self.display_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Create display entry
        display_entry = tk.Entry(self, textvariable=self.display_var, font="Arial 20 bold", bd=10, insertwidth=2, width=14, borderwidth=4, relief="sunken", justify="right")
        display_entry.grid(row=0, column=0, columnspan=4, pady=20)

        # Button text layout
        button_texts = [
            ("C", 1, 0, 2), ("/", 1, 2), ("*", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("+", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("Back", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2, 2)
        ]

        for button_spec in button_texts:
            text, row, col = button_spec[0], button_spec[1], button_spec[2]
            colspan = button_spec[3] if len(button_spec) > 3 else 1
            button = tk.Button(self, text=text, font="Arial 18 bold", padx=20, pady=20, borderwidth=4)
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew")
            button.bind("<Button-1>", self.on_click)

        # Configure grid to be responsive
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
            if i < 4:
                self.grid_columnconfigure(i, weight=1)

    def on_click(self, event):
        text = event.widget.cget("text")
        current_text = self.display_var.get()

        if text == "=":
            try:
                result = eval(current_text)
                self.display_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.display_var.set("")
        elif text == "C":
            self.display_var.set("")
        elif text == "Back":
            self.display_var.set(current_text[:-1])
        else:
            self.display_var.set(current_text + text)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()

"""

Explanation:
Imports:

tkinter is imported for creating the GUI.
messagebox from tkinter is imported to show error messages.
on_click Function:

This function handles the button click events.
It updates the display with the button text, evaluates the expression when "=" is clicked, and clears the display when "C" is clicked.
Main Window:

root is the main application window.
The window title is set to "Simple Calculator".
Display Entry:

An Entry widget is used to display the input and results.
display_var is a StringVar that holds the current display text.
Buttons:

Buttons are created and placed in a grid layout.
Each button is bound to the on_click function.
Main Loop:

root.mainloop() starts the Tkinter event loop.
This simple calculator supports basic operations and provides a clear display. The eval function is used to evaluate the arithmetic expressions. Note that eval should be used carefully, especially with untrusted input, but it's suitable for this simple example.
"""