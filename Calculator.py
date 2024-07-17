import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Smart Calc")
root.configure(bg='#E0FFFF')

# Create the display widget
display = tk.Entry(root, font=('Arial', 20), borderwidth=2, relief='solid', justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)


# Define the button click function
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)


# Define the clear display function
def clear_display():
    display.delete(0, tk.END)


# Define the delete function
def delete():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


# Define the calculate function
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Define the button style
button_style = {
    'font': ('Arial', 18),
    'bg': '#00FFFF',
    'fg': '#000000',
    'borderwidth': 2,
    'relief': 'solid',
    'width': 4,
    'height': 2
}

# Create the buttons
buttons = [
    ('AC', 1, 0, clear_display), ('DEL', 1, 1, delete), ('.', 1, 2, lambda: button_click('.')), ('/', 1, 3, lambda: button_click('/')),
    ('7', 2, 0, lambda: button_click('7')), ('8', 2, 1, lambda: button_click('8')), ('9', 2, 2, lambda: button_click('9')), ('*', 2, 3, lambda: button_click('*')),
    ('4', 3, 0, lambda: button_click('4')), ('5', 3, 1, lambda: button_click('5')), ('6', 3, 2, lambda: button_click('6')), ('-', 3, 3, lambda: button_click('-')),
    ('1', 4, 0, lambda: button_click('1')), ('2', 4, 1, lambda: button_click('2')), ('3', 4, 2, lambda: button_click('3')), ('+', 4, 3, lambda: button_click('+')),
    ('00', 5, 0, lambda: button_click('00')), ('0', 5, 1, lambda: button_click('0')), ('=', 5, 2, calculate, 2)
]

for (text, row, col, command, *span) in buttons:
    button = tk.Button(root, text=text, command=command, **button_style)
    button.grid(row=row, column=col, columnspan=span[0] if span else 1, sticky="nsew", padx=5, pady=5)

# Run the main loop
root.mainloop()
