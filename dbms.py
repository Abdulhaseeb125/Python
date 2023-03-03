import sqlite3
from tkinter import ttk

from tqdm import tk

import customtkinter as ctk


conn = sqlite3.connect('data.db')
# Create a cursor object
cur = conn.cursor()
# Execute a SQL query
cur.execute("SELECT * FROM purchased_data")
# Fetch all the results
results = cur.fetchall()
# Create a new Tkinte-r window
window = ctk.CTk()

# Create a treeview widget to display the results
tree = ttk.Treeview(window)

# Define the columns of the treeview
tree['columns'] = ('Brand_Name', 'Model_Name', 'IMEI-1', 'IMEI-2', 'Customer_Name', 'Date', 'Time')
# Format the columns
tree.column('#0', width=0, )
tree.column('Brand_Name', width=200)
tree.column('Model_Name', width=200)
tree.column('IMEI-1', width=150)
tree.column('IMEI-2', width=150)
tree.column('Customer_Name', width=150)
tree.column('Date', width=100)
tree.column('Time', width=100)
# Add column headings
tree.heading('Brand_Name', text='Brand_Name')
tree.heading('Model_Name', text='Model_Name')
tree.heading('IMEI-1', text='IMEI-1')
tree.heading('IMEI-2', text='IMEI-2')
tree.heading('Customer_Name', text='Customer_Name')
tree.heading('Date', text='Date')
tree.heading('Time', text='Time')
# Add each row of data to the treeview
for row in results:
    tree.insert('', ctk.END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
# Pack the treeview widget
tree.pack()
# Create a function to search for records with a specific IMEI-1
def search_record():
    # Get the search term from the search box
    search_term = search_box.get()

    # Connect to the database and execute the SELECT query with a WHERE clause
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM purchased_data WHERE `IMEI-1` LIKE ?", ('%' + search_term + '%',))
    results = cur.fetchall()
    conn.close()

    # Clear the existing rows from the treeview
    for row in tree.get_children():
        tree.delete(row)

    # Add each matching row of data to the treeview
    for row in results:
        tree.insert('', ctk.END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

def delete_record():
    # Get the ID of the selected record from the treeview
    selected_item = tree.selection()[0]
    record_id = tree.item(selected_item)['text']

    # Connect to the database and execute the DELETE query
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM sold_data WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Update the treeview by removing the selected row
    tree.delete(selected_item)

# Add a search box and search button
search_box = ttk.Entry(window)
search_box.pack(side=ctk.LEFT, padx=5, pady=5)
search_button = ttk.Button(window, text="Search", command=search_record)
search_button.pack(side=ctk.LEFT, padx=5, pady=5)

# Add a scrollbar to the window
scrollbar = ttk.Scrollbar(window)
scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

delete_button = ctk.CTkButton(window, text="Delete", command=delete_record)
delete_button.pack()
# Start the GUI event loop
tree = ttk.Treeview(window, yscrollcommand=scrollbar.set)

window.mainloop()
# Close the database connection
conn.close()