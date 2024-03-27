from tkinter import *


def handleSubmit():
    result = num_entry.get()
    print(result)


window = Tk()
window.title('Data Science')
window.geometry('650x250')

num_label = Label(text='Number: ')
num_label.grid(column=0, row=0)

num_entry = Entry()
num_entry.grid(column=1, row=0)

num_button = Button(text='Submit', command=handleSubmit)
num_button.grid(column=1, row=1)

window.mainloop()


# import psycopg2 as pg2
# import classified
# conn = pg2.connect(database=classified.psql_database,
#                    user=classified.psql_username, password=classified.psql_password)
# cur = conn.cursor()
# cur.execute(classified.psql_query)
# print(cur.fetchone())
# conn.close()
