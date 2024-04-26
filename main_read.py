import tkinter as tk
from tkinter import ttk 
import json


window = tk.Tk()


#contact_list = []


def read_data():
    global contact_list
    try:
        with open("data.json","r") as temp_list:
            contact_list = json.load(temp_list)
    except FileNotFoundError:
        print("something went wrong")

read_data()


table = ttk.Treeview(window, columns=('name', 'contact_number'), show='headings')

table.heading('name', text='Name')
table.heading('contact_number', text='Phone Number')

table.column('name', width=200)
table.column('contact_number', width=150)

# Inserting data from the list of dictionaries
for contact in contact_list:
    table.insert('', tk.END, values=(contact['name'], contact['number']))



# table.insert('', tk.END, values=("John Doe", "123-456-7890"))
# table.insert('', tk.END, values=("Jane Smith", "987-654-3210"))
# table.insert('', tk.END, values=("Alice Johnson", "555-123-4567"))

print(contact_list)


table.pack(expand=True, fill='both')


window.mainloop()