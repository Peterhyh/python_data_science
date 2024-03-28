from tkinter import *
import psycopg2 as pg2


def handleLogin():
    database = database_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    connectDatabase(database=database, password=password, username=username)


def connectDatabase(database, username, password):
    conn = pg2.connect(database=database,
                       user=username, password=password)
    cur = conn.cursor()
    cur.execute('SELECT * FROM payment')
    print(cur.fetchone())
    conn.close()


window = Tk()
window.config(pady=50, padx=150)
window.title('Data Science')
window.geometry('650x250')

database_label = Label(text='Database: ')
database_label.grid(column=0, row=1)

database_entry = Entry()
database_entry.grid(column=1, row=1)

username_label = Label(text='Username: ')
username_label.grid(column=0, row=2)

username_entry = Entry()
username_entry.grid(column=1, row=2)

password_label = Label(text='Password: ')
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.grid(column=1, row=3)

submit_button = Button(text='Submit', command=handleLogin)
submit_button.grid(column=1, row=4)

window.mainloop()
