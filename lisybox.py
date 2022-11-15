import tkinter as tk
from tkinter import ttk
import db

def show():
        db.connection.autocommit = True
            # Creating a cursor object using the cursor() method
        cursor = db.connection.cursor()
        cursor.execute("SELECT amount,category FROM public.expenseaddtable WHERE email = 'am'")
        records = cursor.fetchall()
        print(records)

        for i, (amount,category) in enumerate(records, start=1):
             listBox.insert("", "end", values=(amount, category))



root = tk.Tk()
root.geometry('1280x720')
root.title("Student Records")
label = tk.Label(root, text="Student Records", font=("Arial",30)).grid(row=0, columnspan=3)

cols = ('amount','category')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
     listBox.heading(col, text=col)    
     listBox.grid(row=1, column=0, columnspan=2)
closeButton = tk.Button(root, text="Close", width=15, command=exit).grid(row=4, column=1)
show()
root.mainloop()