from tkinter import *
import csv_util
import web_util
gui = Tk()
gui.geometry('1000x600')
gui.title("Homebrew CRM:Developed by THOMAS DION")



def reset_frame():
    counter = 0
    for widget in gui.winfo_children():
        if counter > 124:
            widget.destroy()
        counter += 1

def update_all():
    pass
def qualify(client,client_number):
    csv_util.save_client_externally(client)
    csv_util.delete_client(client_number)
    load_client(client_number)
    client = csv_util.get_client(client_number)
    web_util.open_crm(client['First Name'],client['Last Name'])

def next_client(client_number):
    print(client_number)
    client_number += 1
    print(client_number)
    find_client.entry.delete(0, END)
    find_client.entry.insert(END, str(client_number))
    load_client(client_number)
def precedent_client(client_number):
    client_number -= 1
    find_client.entry.delete(0, END)
    find_client.entry.insert(END, str(client_number))
    load_client(client_number)

def load_client(client_number):
    reset_frame()
    csv_util.save_client_number(client_number)
    def delete_wrapper(client_number):
        csv_util.delete_client(client_number)
        load_client(client_number)

    button = Button(gui, text="delete prospect", command=lambda: delete_wrapper(client_number))
    button.grid(row=1,column=1)
    row = 4
    col = 0
    client = csv_util.get_client(client_number)
    for key, value in client.items():
        if key == "ID":
            pass
        else:
            field = Field(key, value)
            field.grid(col, row)
            col += 4
            if col == 8:
                col = 0
                row += 3



    inspect_button = Button(gui, text="Inspect",height=5,bg="GREEN",fg="Black",command= lambda: web_util.inspect(client))
    inspect_button.grid(row=20, column= 5)




    qualified_button = Button(gui, text="Qualify",bg="PINK",fg="BLACK",command= lambda: qualify(client,client_number))
    qualified_button.grid(row=24, column= 5)

    next_client_button = Button(gui,height=3,text="Next Client =>",
                                command = lambda:next_client(int(client_number)))
    precedent_client_button = Button(gui,height=3,text="<= Precedent Client",
                                command = lambda: precedent_client(int(client_number)))
    precedent_client_button.grid(row = 24, column=2)
    next_client_button.grid(row=24, column = 3)

def update_client(client_number,key,new_value):
    csv_util.update_client(
        client_number,
        key,
        new_value
    )
    load_client(client_number)

def open_linkedin(first_name,last_name):
    web_util.open_linkedin(first_name,last_name)


class Field:
    def __init__(self,key,value):
        self.label = Label(gui,text=key)
        self.entry = Entry(gui, width='20',font="Helvetica 12")
        self.entry.insert(END, value)

        self.button = Button(gui,text="update field",command = lambda: update_client(
            find_client.entry.get(),
            key,
            self.entry.get()
        ))



    def grid(self,col,row):
        self.label.grid(column=col,row=row)
        self.entry.grid(column=col+1,row=row)
        self.button.grid(column=col+2,row=row)
    def pack(self):
        self.label.pack()
        self.entry.pack()
        self.entry.pack()
        self.button.pack()


find_client = Field('Client NO:', ' ')
find_client.button = Button(gui, text="Load client", command= lambda: load_client(find_client.entry.get()))
find_client.grid(row=0, col=3)

load_client(csv_util.get_last_client_number())


reset_frame()

gui.mainloop()