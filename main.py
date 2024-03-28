from tkinter import *
import psycopg2 as pg2

database = ''
username = ''
password = ''
query = ''
user_purpose = 0


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
    query_label.grid(column=0, row=5)
    query_entry.grid(column=1, row=5)
    query_button.grid(column=0, row=7)
    purpose_label.grid(column=0, row=2)
    purpose_search.grid(column=1, row=2)
    purpose_create.grid(column=2, row=2)


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
    if user_purpose == '1':
        cur.execute("SELECT " + query)
        query_array = cur.fetchall()
        print(query_array[0])
    elif user_purpose == '2':
        cur.execute("CREATE TABLE " + query)
        query_array = cur.fetchall()
        print(query_array[0])


def handleQuery():
    setCredentials()
    connectDatabase()


def handlePSearch():
    global var
    global user_purpose
    user_purpose = var.get()


def handlePCreate():
    global var
    global user_purpose
    user_purpose = var.get()


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

login_button = Button(text='Login', command=handleLogin)
login_button.grid(column=1, row=4)


# After login:
query_label = Label(text='Query: ')
query_label.grid_forget()

query_entry = Entry()
query_entry.grid_forget()

purpose_label = Label(text="What would you like to perform?")
purpose_label.grid_forget()

var = StringVar()
purpose_search = Radiobutton(
    window, text='Search', variable=var, value=1, command=handlePSearch)
purpose_search.grid_forget()
purpose_create = Radiobutton(
    window, text='Create', variable=var, value=2, command=handlePCreate)
purpose_create.grid_forget()


query_button = Button(text='Query', command=handleQuery)
query_button.grid_forget()


window.mainloop()
