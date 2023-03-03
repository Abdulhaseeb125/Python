
import customtkinter as ctk
import ask
import sqlite3


conn = sqlite3.connect('data.db')
c = conn.cursor()

# create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS sold_data
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             model_name TEXT,
             brand_name TEXT,
             imei1 INTEGER,
             imei2 INTEGER,
             customer_name TEXT,
             date TEXT,
             time TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS purchased_data
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             model_name TEXT,
             brand_name TEXT,
             imei1 INTEGER,
             imei2 INTEGER,
             purchased_from TEXT,
             date TEXT,
             time TEXT)''')
conn.commit()

# Main
if __name__ == "__main__":
    main_window = ctk.CTk()
    main_window.title("Mian Computers")
    main_window.geometry('600x600')
    main_window.maxsize(width=600, height=600)
    # Index/Ask Frame
    index = ask.Ask(main_window)
    main_window.mainloop()

