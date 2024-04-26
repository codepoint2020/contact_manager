import tkinter as tk
from tkinter import ttk 


window = tk.Tk()


table = ttk.Treeview(window, columns=('name', 'contact_number'), show='headings')

table.heading('name', text='Name')
table.heading('contact_number', text='Phone Number')

table.column('name', width=200)
table.column('contact_number', width=150)


table.insert('', tk.END, values=("John Doe", "123-456-7890"))
table.insert('', tk.END, values=("Jane Smith", "987-654-3210"))
table.insert('', tk.END, values=("Alice Johnson", "555-123-4567"))


table.pack(expand=True, fill='both')


window.mainloop()