import tkinter as tk
from tkinter import messagebox
from sympy import symbols, diff, sympify
import math
import re

class AdvancedCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Calculator")
        self.master.geometry("500x600")
        self.master.resizable(True, True)

        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.entry.bind("<Return>", self.process_entry)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
            'sin', 'cos', 'tan', 'log',
            'ln', '√', 'x²', 'xⁿ',
            'd/dx', '(', ')', '⌫'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, padx=20, pady=20, font=('Arial', 18),
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column, sticky="nsew")
        button.bind("<ButtonPress>", lambda e: self.animate_button(button, True))
        button.bind("<ButtonRelease>", lambda e: self.animate_button(button, False))

    def process_entry(self, event):
        self.expression = self.result_var.get()
        self.on_button_click('=')

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.result_var.set("")
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.result_var.set(self.expression)
        elif char == '=':
            try:
                expr = self.expression.replace('√', 'math.sqrt')
                expr = expr.replace('log', 'math.log10')
                expr = expr.replace('ln', 'math.log')
                expr = expr.replace('x²', '**2')
                expr = expr.replace('xⁿ', '**')
                
                # Convert sin, cos, tan to use radians properly
                expr = re.sub(r'sin\(([^)]+)\)', r'math.sin(math.radians(\1))', expr)
                expr = re.sub(r'cos\(([^)]+)\)', r'math.cos(math.radians(\1))', expr)
                expr = re.sub(r'tan\(([^)]+)\)', r'math.tan(math.radians(\1))', expr)
                
                self.expression = str(eval(expr, {"math": math}))
                self.result_var.set(self.expression)
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.result_var.set("")
        elif char == 'd/dx':
            try:
                x = symbols('x')
                sym_expr = sympify(self.expression)
                derivative = str(diff(sym_expr, x))
                self.result_var.set(derivative)
                self.expression = derivative
            except Exception:
                messagebox.showerror("Error", "Invalid Differentiation")
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

    def animate_button(self, button, pressed):
        if pressed:
            button.config(bg='lightblue')
        else:
            button.config(bg='SystemButtonFace')

if __name__ == "__main__":
    root = tk.Tk()
    calculator = AdvancedCalculator(root)
    root.mainloop()

