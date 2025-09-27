from tkinter import *

def button_clicked():
    try:
        result = float(input_field.get())
        km = result * 1.609
        text_result.config(text=f"{km:.3f}")
    except ValueError:
        text_result.config(text="Error")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=150)
window.config(padx=20, pady=20)

default_font = ("Arial", 14)

input_field = Entry(width=8, font=default_font)
input_field.grid(column=1, row=0)

text_mile = Label(text="Mile(s)", font=default_font)
text_mile.grid(column=2, row=0)

text_equal = Label(text="is equal to", font=default_font)
text_equal.grid(column=0, row=1)

text_result = Label(text="0", font=("Arial", 16, "bold"))
text_result.grid(column=1, row=1)

text_km = Label(text="Km", font=default_font)
text_km.grid(column=2, row=1)

my_button = Button(text="Calculate", command=button_clicked, font=default_font)
my_button.grid(column=1, row=2)

window.bind("<Return>", lambda event: button_clicked())

window.mainloop()
