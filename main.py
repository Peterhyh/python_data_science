from tkinter import *
import psycopg2 as pg2

database = ''
username = ''
password = ''
column = ''
table = ''
user_purpose = 0


def setCredentials():
    global database
    global username
    global password
    global column
    global table
    database = database_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    column = column_entry.get()
    table = table_entry.get()


def hideLogin():
    database_label.grid_forget()
    database_entry.grid_forget()
    username_label.grid_forget()
    username_entry.grid_forget()
    password_label.grid_forget()
    password_entry.grid_forget()
    login_button.grid_forget()


def showQuery():
    column_label.grid(column=0, row=5)
    column_entry.grid(column=1, row=5)
    table_label.grid(column=0, row=6)
    table_entry.grid(column=1, row=6)
    query_button.grid(column=1, row=10)
    purpose_label.grid(column=0, row=2)
    purpose_search.grid(column=1, row=2)
    purpose_create.grid(column=2, row=2)


def handleLogin():
    setCredentials()
    connectDatabase()


def connectDatabase():
    try:
        conn = pg2.connect(database=database, user=username, password=password)
    except:
        print('Access Denied')
    else:
        print('Successfully connected to database')
        hideLogin()
        showQuery()
        cur = conn.cursor()
        if column and table and user_purpose != 0:
            runQuery(cur=cur)
        conn.close()
        print('Database closed out')


def runQuery(cur):
    global column
    global table
    if user_purpose == '1':
        cur.execute("SELECT " + column + " FROM " + table)
        query_array = cur.fetchall()
        print(query_array[0])
    elif user_purpose == '2':
        cur.execute("CREATE TABLE " + column + " FROM " + table)
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
window.config(pady=20, padx=20)
window.title('Data Science')
window.geometry('600x300')

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


purpose_label = Label(text="What would you like to perform?")
purpose_label.grid_forget()

var = StringVar()
purpose_search = Radiobutton(
    window, text='Search', variable=var, value=1, command=handlePSearch)
purpose_search.grid_forget()
purpose_create = Radiobutton(
    window, text='Create table', variable=var, value=2, command=handlePCreate)
purpose_create.grid_forget()

column_label = Label(text='Column(s): ')
column_label.grid_forget()

column_entry = Entry()
column_entry.grid_forget()

table_label = Label(text='Table: ')
table_label.grid_forget()

table_entry = Entry()
table_entry.grid_forget()

query_button = Button(text='Query', command=handleQuery)
query_button.grid_forget()


window.mainloop()
