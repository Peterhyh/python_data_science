from tkinter import *
import psycopg2 as pg2

database = ''
username = ''
password = ''
query = ''


def setCredentials():
    global database
    global username
    global password
    global query
    database = database_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    query = query_entry.get()


def hideLogin():
    database_label.grid_forget()
    database_entry.grid_forget()
    username_label.grid_forget()
    username_entry.grid_forget()
    password_label.grid_forget()
    password_entry.grid_forget()
    login_button.grid_forget()


def showQuery():
    query_label.grid(column=0, row=1)
    query_entry.grid(column=1, row=1)
    query_button.grid(column=1, row=2)


def handleLogin():
    setCredentials()
    connectDatabase()
    hideLogin()
    showQuery()


def connectDatabase():
    conn = pg2.connect(database=database,
                       user=username, password=password)
    cur = conn.cursor()
    if query:
        runQuery(cur=cur)
    conn.close()


def runQuery(cur):
    cur.execute(query)
    query_array = cur.fetchall()
    for item in query_array:
        print(item)


def handleQuery():
    setCredentials()
    connectDatabase()


window = Tk()
window.config(pady=50, padx=150)
window.title('Data Science')
window.geometry('650x300')

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


# After login:
query_label = Label(text='Query: ')
query_label.grid_forget()

query_entry = Entry()
query_entry.grid_forget()


login_button = Button(text='Login', command=handleLogin)
login_button.grid(column=1, row=4)

query_button = Button(text='Query', command=handleQuery)
query_button.grid_forget()


window.mainloop()
