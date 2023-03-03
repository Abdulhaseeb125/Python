import random
import sqlite3
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
import sell
import purchase


class Ask:
    """It Is the Index class that appears first on window"""

    def __init__(self, root):
        self.root = root
        self.index_frame = ctk.CTkFrame(root, 500, 500)
        self.index_frame.place(anchor=ctk.CENTER, relx=0.5, rely=0.5)
        self.color_list = ['#5D3891', '#000000', '#393053', '#03001C']
        self.buttons()
        self.sell_button = None
        self.purchase_button = None
        self.label = None
        self.Purchase = None

    def buttons(self):
        """The Methods are for Adding Buttons on the index/Home Window"""
        # Sell_Button
        self.exit = ctk.CTkButton(self.index_frame, text="X", width=30, fg_color='transparent', border_width=1,
                                  hover_color='red', corner_radius=30, command=self.root.destroy)
        self.exit.place(relx=0.9, rely=0.05, anchor=ctk.CENTER)

        self.sell_button = ctk.CTkButton(self.index_frame, text="Sell",
                                         hover_color=random.choice(self.color_list),
                                         fg_color='transparent',
                                         border_color='white',
                                         corner_radius=30,
                                         border_width=1,
                                         command=self.sell
                                         )
        self.sell_button.place(relx=0.33, rely=0.35)
        # Purchase_button
        self.purchase_button = ctk.CTkButton(self.index_frame, text="Purchase",
                                             hover_color=random.choice(self.color_list),
                                             fg_color='transparent',
                                             border_color='white',
                                             corner_radius=30,
                                             border_width=1,
                                             command=self.purchase
                                             )
        self.purchase_button.place(relx=0.33, rely=0.45)
        # Show_Sell_Records
        self.sell_records_button = ctk.CTkButton(self.index_frame, text="Sell Records",
                                                 hover_color=random.choice(self.color_list),
                                                 fg_color='transparent',
                                                 border_color='white',
                                                 corner_radius=30,
                                                 border_width=1,
                                                 command=self.sell_records
                                                 )
        self.sell_records_button.place(relx=0.33, rely=0.55)
        # Show Purchase_Records
        self.purchase_records_button = ctk.CTkButton(self.index_frame, text="Purchase Records",
                                                     hover_color=random.choice(self.color_list),
                                                     fg_color='transparent',
                                                     border_color='white',
                                                     corner_radius=30,
                                                     border_width=1,
                                                     command=self.purchase_records

                                                     )
        self.purchase_records_button.place(relx=0.33, rely=0.65)

    def purchase(self):
        """Response for Purchase Button"""
        self.index_frame.destroy()
        self.Purchase = purchase.PurchaseCanvas(self.root)
        self.Purchase.frame_1()

    def sell(self):
        """Response for Sell Button"""
        self.index_frame.destroy()
        self.Purchase = sell.SellCanvas(self.root)
        self.Purchase.frame_1()

    def sell_records(self):
        """Response for Sold Records"""
        conn = sqlite3.connect('data.db')
        # Create a cursor object
        cur = conn.cursor()
        # Execute a SQL query
        cur.execute("SELECT * FROM sold_data")
        # Fetch all the results
        results = cur.fetchall()
        # Create a new Tkinter window
        window = ctk.CTk()
        window.title("Sold Records")

        # Create a treeview widget to display the results
        tree = ttk.Treeview(window, height=30)
        # Define the columns of the treeview
        tree['columns'] = ('Brand_Name', 'Model_Name', 'IMEI-1', 'IMEI-2', 'Customer_Name', 'Date', 'Time')
        # Format the columns
        tree.column('#0', width=50, stretch=tk.NO)
        tree.column('Brand_Name', width=200)
        tree.column('Model_Name', width=200)
        tree.column('IMEI-1', width=150)
        tree.column('IMEI-2', width=150)
        tree.column('Customer_Name', width=150)
        tree.column('Date', width=100)
        tree.column('Time', width=100)
        # Add column headings
        tree.heading('#0', text='S.No')
        tree.heading('Brand_Name', text='Brand_Name')
        tree.heading('Model_Name', text='Model_Name')
        tree.heading('IMEI-1', text='IMEI-1')
        tree.heading('IMEI-2', text='IMEI-2')
        tree.heading('Customer_Name', text='Customer_Name')
        tree.heading('Date', text='Date')
        tree.heading('Time', text='Time')
        # Add each row of data to the treeview
        for row in results:
            tree.insert('', tk.END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        # Pack the treeview widget
        tree.pack()

        def delete_record():
            # Get the ID of the selected record from the treeview
            try:
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
            except IndexError:
                messagebox.showinfo('Error', 'No item selected')

        delete_button = tk.Button(window, text="Delete", command=delete_record)
        delete_button.pack()
        # Start the GUI event loop

        window.mainloop()
        # Close the database connection
        conn.close()

    def purchase_records(self):
        """Response for Purchased Records"""
        conn = sqlite3.connect('data.db')

        # Create a cursor object
        cur = conn.cursor()

        # Execute a SQL query
        cur.execute("SELECT * FROM purchased_data")

        # Fetch all the results
        results = cur.fetchall()

        # Create a new Tkinter window
        window = tk.Tk()
        window.title("Purchase Records")

        # Create a treeview widget to display the results
        tree = ttk.Treeview(window, height=30)

        # Define the columns of the treeview
        tree['columns'] = ('Brand_Name', 'Model_Name', 'IMEI-1', 'IMEI-2', 'purchased_from', 'Date', 'Time')

        # Format the columns
        tree.column('#0', width=50, stretch=tk.NO)
        tree.column('Brand_Name', width=200)
        tree.column('Model_Name', width=200)
        tree.column('IMEI-1', width=150)
        tree.column('IMEI-2', width=150)
        tree.column('purchased_from', width=150)
        tree.column('Date', width=100)
        tree.column('Time', width=100)

        # Add column headings
        tree.heading('#0', text='S.No')
        tree.heading('Brand_Name', text='Brand_Name')
        tree.heading('Model_Name', text='Model_Name')
        tree.heading('IMEI-1', text='IMEI-1')
        tree.heading('IMEI-2', text='IMEI-2')
        tree.heading('purchased_from', text='purchased_from')
        tree.heading('Date', text='Date')
        tree.heading('Time', text='Time')

        # Add each row of data to the treeview
        for row in results:
            tree.insert('', tk.END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        # Pack the treeview widget
        tree.pack()

        def delete_record():
            try:
                # Get the ID of the selected record from the treeview
                selected_item = tree.selection()[0]
                record_id = tree.item(selected_item)['text']
                # Connect to the database and execute the DELETE query
                conn = sqlite3.connect('data.db')
                cur = conn.cursor()
                cur.execute("DELETE FROM purchased_data WHERE id=?", (record_id,))
                conn.commit()
                conn.close()

            # Update the treeview by removing the selected row
                tree.delete(selected_item)
            except IndexError:
                messagebox.showinfo("Error","No item selected")

        delete_button = tk.Button(window, text="Delete", command=delete_record)
        delete_button.pack()

        # Start the GUI event loop
        window.mainloop()
        # Close the database connection
        conn.close()
