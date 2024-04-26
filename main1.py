import tkinter as tk
from tkinter import ttk, messagebox
import json


window = tk.Tk()

ttk.Label(window, text='Contact List', font=('Arial', 16, 'bold')).pack()

# list variable to hold entered contact temporarily
#contact_list = []
def read_data():
    global contact_list
    try:
        with open("data.json","r") as temp_list:
            contact_list = json.load(temp_list)
    except FileNotFoundError:
        print("something went wrong")


def table_refresh():
    # Remove all items from the treeview
    for item in table.get_children():
        table.delete(item)
    # Re-insert items into the treeview
    for contact in contact_list:
        table.insert('', tk.END, values=(contact['name'], contact['number']))


read_data()

# read the data.json and print it on console
#read the data.json and preview it on treeview


#function to add contact
def add_contact():
    contact_name = name_entry.get()
    contact_number = number_entry.get()

    new_entry = {
        "name": contact_name,
        "number": contact_number
    }

    contact_list.append(new_entry)

    try:
        with open("data.json", "w") as temp_var:
            json.dump(contact_list, temp_var, indent=4)
            table_refresh()
            messagebox.showinfo("Confirmation Box", f"{contact_name} \n {contact_number} \n has been added" )
            
    except FileNotFoundError:
        print("")



frm_frame = ttk.LabelFrame(window, text="Add New Info")
frm_frame.pack(padx=10, pady=10)

ttk.Label(frm_frame, text="Enter a name:").grid()
name_entry = ttk.Entry(frm_frame)
name_entry.grid()

ttk.Label(frm_frame, text="Enter a number:").grid()
number_entry = ttk.Entry(frm_frame)
number_entry.grid()

add_btn = ttk.Button(frm_frame, text="Add", command=add_contact)
add_btn.grid()


tbl_frame = ttk.LabelFrame(window, text="Contacts")
tbl_frame.pack(padx=10, pady=10)


table = ttk.Treeview(tbl_frame, columns=('name', 'contact_number'), show='headings')

table.heading('name', text='Name')
table.heading('contact_number', text='Phone Number')

table.column('name', width=200)
table.column('contact_number', width=150)


for contact in contact_list:
    table.insert('', tk.END, values=(contact["name"], contact["number"]))


# table.insert('', tk.END, values=("Jane Smith", "987-654-3210"))
# table.insert('', tk.END, values=("Alice Johnson", "555-123-4567"))


table.pack()


window.mainloop()