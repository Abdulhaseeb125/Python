import sqlite3
import time
import customtkinter as ctk
import datetime
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

import ask


class PurchaseCanvas:
    def __init__(self, master):
        self.entry = None
        self.purchase_frame = None
        self.master = master

    def frame_1(self):
        self.purchase_frame = ctk.CTkFrame(self.master, height=500, width=500)
        self.purchase_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.go_back = ctk.CTkButton(self.purchase_frame,text="<<<",width=20,fg_color='transparent',command=self.go_back)
        self.go_back.place(relx=0.1,rely=0.1,anchor=ctk.CENTER)

        self.section = ctk.CTkLabel(self.purchase_frame, text="Purchasing Details", font=("arial", 20))
        self.section.place(relx=0.35, rely=0.05)

        self.brand_entry = ctk.CTkEntry(self.purchase_frame, width=180, placeholder_text="Brand Name")
        self.brand_entry.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        self.model_entry = ctk.CTkEntry(self.purchase_frame, width=180, placeholder_text="Model Name")
        self.model_entry.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

        self.imei1_entry = ctk.CTkEntry(self.purchase_frame, width=180, placeholder_text="IMEI-1 Name")
        self.imei1_entry.configure(validate='key')
        self.imei1_entry.configure(validatecommand=(self.imei1_entry.register(lambda P: P.isdigit() or P == ""), '%P'))
        self.imei1_entry.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

        self.imei2_entry = ctk.CTkEntry(self.purchase_frame, width=180, placeholder_text="IMEI-2 Name")
        self.imei2_entry.configure(validate='key')
        self.imei2_entry.configure(validatecommand=(self.imei1_entry.register(lambda P: P.isdigit() or P == ""), '%P'))
        self.imei2_entry.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.purchasing_entry = ctk.CTkEntry(self.purchase_frame, width=180, placeholder_text="Purchased From")
        self.purchasing_entry.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        self.date = datetime.date.today().__str__()
        self.date_entry = ctk.CTkEntry(self.purchase_frame, width=100, placeholder_text=self.date)
        self.date_entry.insert(0, self.date)
        self.date_entry.place(relx=0.4, rely=0.7, anchor=ctk.CENTER)

        self.time = time.strftime("%H:%M:%S")
        self.time_entry = ctk.CTkEntry(self.purchase_frame, width=100)
        self.time_entry.insert(1, self.time)
        self.time_entry.place(relx=0.61, rely=0.7, anchor=ctk.CENTER)

        self.submit = ctk.CTkButton(self.purchase_frame, command=self.submit, text="Add", fg_color="black",
                                    border_width=1, corner_radius=30)
        self.submit.place(relx=0.35, rely=0.8)

    def submit(self):
        conn = sqlite3.connect('data.db')

        c = conn.cursor()
        self.model_name = self.model_entry.get()
        self.brand_name = self.brand_entry.get()
        self.imei1_number = self.imei1_entry.get()
        self.imei2_number = self.imei2_entry.get()
        self.purchased_from = self.purchasing_entry.get()
        self.sdate = self.date_entry.get()
        self.stime = self.time_entry.get()
        # insert data into the table
        c.execute('''INSERT INTO purchased_data(model_name,brand_name, imei1, imei2,purchased_from, date, time) 
                     VALUES (?, ?, ?, ?, ?, ?, ?)''', (
            self.model_name, self.brand_name, self.imei1_number, self.imei2_number, self.purchased_from, self.sdate,
            self.stime))
        conn.commit()
        if conn:
             messagebox.showinfo(title="Messege", message="Successfully Added")


    def go_back(self):
        self.new = ask.Ask(self.master)