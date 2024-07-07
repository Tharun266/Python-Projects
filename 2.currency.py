import tkinter as tk
from tkinter import ttk, messagebox

class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Currency Converter")
        self.geometry("500x300")

        # Predefined exchange rates
        self.exchange_rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.75,
            "INR": 73.5,
            "AUD": 1.35,
            "CAD": 1.25,
            "JPY": 110.0,
            "CNY": 6.5
        }

        self.currencies = list(self.exchange_rates.keys())

        self.create_widgets()

    def create_widgets(self):
        # Heading
        self.heading_label = tk.Label(self, text="Currency Converter", font=("Arial", 24))
        self.heading_label.pack(pady=10)

        # Frame for currency selection
        self.selection_frame = tk.Frame(self)
        self.selection_frame.pack(pady=10)

        # Source currency
        self.source_label = tk.Label(self.selection_frame, text="From:")
        self.source_label.grid(row=0, column=0, padx=10)

        self.source_currency = ttk.Combobox(self.selection_frame, values=self.currencies)
        self.source_currency.grid(row=0, column=1, padx=10)
        self.source_currency.current(0)

        # Target currency
        self.target_label = tk.Label(self.selection_frame, text="To:")
        self.target_label.grid(row=0, column=2, padx=10)

        self.target_currency = ttk.Combobox(self.selection_frame, values=self.currencies)
        self.target_currency.grid(row=0, column=3, padx=10)
        self.target_currency.current(1)

        # Frame for amount entry and result
        self.amount_frame = tk.Frame(self)
        self.amount_frame.pack(pady=10)

        # Amount label
        self.amount_label = tk.Label(self.amount_frame, text="Enter Amount:")
        self.amount_label.grid(row=0, column=0, padx=10)

        # Amount entry
        self.amount_entry = tk.Entry(self.amount_frame)
        self.amount_entry.grid(row=0, column=1, padx=10)

        # Convert button
        self.convert_button = tk.Button(self.amount_frame, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Result label
        self.result_label = tk.Label(self, text="", font=("Arial", 18))
        self.result_label.pack(pady=20)

    def convert_currency(self):
        from_currency = self.source_currency.get()
        to_currency = self.target_currency.get()
        amount = self.amount_entry.get()

        if not amount:
            messagebox.showerror("Error", "Please enter an amount")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
            return

        conversion_rate = self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
        converted_amount = amount * conversion_rate
        self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    app = CurrencyConverter()
    app.mainloop()
