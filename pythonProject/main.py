from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

def mile_to_kilometer():
    miles = float(mile_entry.get())
    km = round(miles * 1.609)
    kilometer_result_lable.config(text=f"{km}")

mile_entry = Entry()
mile_entry.grid(column=1, row=0)

mile_lable = Label(text="Mile")
mile_lable.grid(column=2, row=0)

is_equal_lable = Label(text="is equal to")
is_equal_lable.grid(column=0, row=1)

kilometer_result_lable = Label(text="0")
kilometer_result_lable.grid(column=1, row=1)

kilometer_result = Label(text="KM")
kilometer_result.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=mile_to_kilometer)
calculate_button.grid(column=1, row=2)


window.mainloop()