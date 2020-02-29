from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()
 
def implementDB():
    connect = psycopg2.connect( host="localhost",password="artuiup1", user="postgres",port="5427",dbname = "postgres")
    curr = connect.cursor()
    curr.execute(''' CREATE TABLE studentdetail(ID SERIAL, name text , age  text , adress text ) ; ''')
    print("data base created")
    connect.commit()
    connect.close()
    
#implementDB()

def displayAll():
    connect = psycopg2.connect(host="localhost",password="artuiup1", user="postgres",port="5424",dbname = "postgres")
    curr = connect.cursor()
    query = ''' select * from studentdetail '''
    curr.execute( query )
    entry = curr.fetchall()
    listbox = Listbox(frame , width= 20 , height = 5  )
    listbox.grid( row = 9 , column = 1 )
    for x in entry:
        listbox.insert(END , x )
    connect.commit()
    connect.close()

def fetchData(id):
    connect = psycopg2.connect(host="localhost",password="artuiup1", user="postgres",port="5422",dbname = "postgres")
    curr = connect.cursor()
    query = ''' select * from studentdetail where id = %s ''' 
    curr.execute( query ,(id) )
    entry = curr.fetchone()
    displayAll()
    connect.commit()
    connect.close()
    
def insert_Data( name , age , adress):
   
    connect = psycopg2.connect( host="localhost",password="avoogardo1", user="postgres",port="5422",dbname = "postgres")
    curr = connect.cursor()
    query = ''' INSERT INTO studentdetail(name , age , adress) VALUES( %s ,%s , %s ) ; ''' 
    curr.execute( query , (name , age, adress ))
    print("Inserted")
    connect.commit()
    connect.close()
    displayAll()

    

canvas = Canvas(root, height = 300 , width = 600 )
canvas.pack()

frame = Frame( root )
frame.place(relx = 0.3 , rely = 0.1 , relwidth = 0.8 , relheight = 0.8 )

label = Label( frame , text = "Add Information ")
label.grid(row = 0, column = 1 )

label = Label( frame , text = "NAME: ")
label.grid(row= 1 , column = 0 ,sticky = W)

name_entry = Entry( frame )
name_entry.grid( row = 1 , column = 1 , sticky = E )

label = Label( frame , text = "AGE: ")
label.grid(row= 2 , column = 0 ,sticky = W)

name_age = Entry( frame )
name_age.grid( row = 2 , column = 1 , sticky = E)

label = Label( frame , text = "ADRESS: ")
label.grid(row= 3 , column = 0 , sticky = W)

name_adress = Entry( frame )
name_adress.grid( row = 3 , column = 1 , sticky = E)

button = Button( frame , text = "REGISTER" , command = lambda : insert_Data( name_entry.get() , name_age.get(), name_adress.get()))
button.grid(row = 4 , column = 1 )

label = Label( frame , text = "Search Data: ")
label.grid(row= 6 , column = 1 )

label = Label( frame , text = "Search By Name: ")
label.grid(row= 7 , column = 0 )


search_ID = Entry( frame )
search_ID.grid( row = 7 , column = 1 , sticky = E)

button = Button( frame , text = "Fetch: " ,command = lambda : fetchData( search_ID.get() ) )
button.grid(row = 7 , column = 2 )

displayAll()
   
root.mainloop()
