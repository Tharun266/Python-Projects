import tkinter as tk
from tkinter import ttk, messagebox

class TemperatureConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Converter")
        self.geometry("350x200")

        self.create_widgets()

    def create_widgets(self):
        self.temp_label = tk.Label(self, text="Enter temperature:", font=("Arial", 12))
        self.temp_label.grid(row=0, column=0, padx=10, pady=10)

        self.temp_entry = tk.Entry(self, font=("Arial", 12), width=10)
        self.temp_entry.grid(row=0, column=1, padx=10, pady=10)

        self.from_label = tk.Label(self, text="From:", font=("Arial", 12))
        self.from_label.grid(row=1, column=0, padx=10, pady=10)

        self.from_unit = ttk.Combobox(self, values=["Fahrenheit", "Celsius"], font=("Arial", 12), width=10)
        self.from_unit.grid(row=1, column=1, padx=10, pady=10)
        self.from_unit.current(0)  # Default selection

        self.to_label = tk.Label(self, text="To:", font=("Arial", 12))
        self.to_label.grid(row=2, column=0, padx=10, pady=10)

        self.to_unit = ttk.Combobox(self, values=["Celsius", "Fahrenheit"], font=("Arial", 12), width=10)
        self.to_unit.grid(row=2, column=1, padx=10, pady=10)
        self.to_unit.current(0)  # Default selection

        self.convert_button = tk.Button(self, text="Convert", font=("Arial", 12), command=self.convert_temperature)
        self.convert_button.grid(row=3, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 12))
        self.result_label.grid(row=4, columnspan=2, padx=10, pady=10)

    def convert_temperature(self):
        temperature = self.temp_entry.get()

        if not temperature:
            messagebox.showerror("Error", "Please enter a temperature")
            return

        try:
            temperature = float(temperature)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            return

        from_unit = self.from_unit.get()
        to_unit = self.to_unit.get()

        if from_unit == "Fahrenheit" and to_unit == "Celsius":
            converted_temp = (temperature - 32) * 5/9
            self.result_label.config(text=f"{temperature:.2f} Fahrenheit = {converted_temp:.2f} Celsius")
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            converted_temp = (temperature * 9/5) + 32
            self.result_label.config(text=f"{temperature:.2f} Celsius = {converted_temp:.2f} Fahrenheit")
        else:
            self.result_label.config(text="Conversion not supported")

if __name__ == "__main__":
    app = TemperatureConverter()
    app.mainloop()
todolist.py
