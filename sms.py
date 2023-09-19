import time
from tkinter import*
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pandas
import pymysql

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

def clock():
    global date,timecur
    date=time.strftime('%d/%m/%Y')
    timecur=time.strftime('%H:%M:%S')
    datetimelable.config(text=f'  Date:{date}\nTime:{timecur}')
    datetimelable.after(1000,clock)


def exit():
    result=messagebox.askyesno('Exit','Do you Want to Exit?')
    if result:
        root.destroy()
    else:
        pass

def export():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=stu_table.get_children()
    newlist=[]
    for index in indexing:
        content=stu_table.item(index)
        list=content['values']
        newlist.append(list)
    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Time','Date'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Sucess','Data exported')

def top_level(tittle,button_text,command):

    global idlablee,namelablee,phonelablee,Emaillablee,addlablee,genlablee,doblablee,screen
    screen = Toplevel()
    screen.grab_set()
    screen.title(tittle)
    screen.resizable(False, False)
    idlable = Label(screen, text='Id', font=('times new roman', 20, 'bold'))
    idlable.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idlablee = Entry(screen, font=('roman', 15, 'bold'))
    idlablee.grid(row=0, column=1, pady=15, padx=10)

    namelable = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    namelable.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    namelablee = Entry(screen, font=('roman', 15, 'bold'))
    namelablee.grid(row=1, column=1, pady=15, padx=10)

    phonelable = Label(screen, text='Phone', font=('times new roman', 20, 'bold'))
    phonelable.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phonelablee = Entry(screen, font=('roman', 15, 'bold'))
    phonelablee.grid(row=2, column=1, pady=15, padx=10)

    Emaillable = Label(screen, text='Email', font=('times new roman', 20, 'bold'))
    Emaillable.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    Emaillablee = Entry(screen, font=('roman', 15, 'bold'))
    Emaillablee.grid(row=3, column=1, pady=15, padx=10)

    addlable = Label(screen, text='Address', font=('times new roman', 20, 'bold'))
    addlable.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addlablee = Entry(screen, font=('roman', 15, 'bold'))
    addlablee.grid(row=4, column=1, pady=15, padx=10)

    genlable = Label(screen, text='Gender', font=('times new roman', 20, 'bold'))
    genlable.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genlablee = Entry(screen, font=('roman', 15, 'bold'))
    genlablee.grid(row=5, column=1, pady=15, padx=10)

    doblable = Label(screen, text='D.O.B', font=('times new roman', 20, 'bold'))
    doblable.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    doblablee = Entry(screen, font=('roman', 15, 'bold'))
    doblablee.grid(row=6, column=1, pady=15, padx=10)

    stub = ttk.Button(screen, text=button_text, command=command)
    stub.grid(row=7, column=0, columnspan=2, pady=15)

    if tittle=='Update Student':
        indexing = stu_table.focus()
        content = stu_table.item(indexing)
        list_data = content['values']
        idlablee.insert(0, list_data[0])
        namelablee.insert(0, list_data[1])
        phonelablee.insert(0, list_data[2])
        Emaillablee.insert(0, list_data[3])
        addlablee.insert(0, list_data[4])
        genlablee.insert(0, list_data[5])
        doblablee.insert(0, list_data[6])
def update_data():

    query = 'UPDATE student SET name=%s, mobile_no=%s, email=%s, address=%s, gender=%s, DOB=%s, date=%s, time=%s WHERE id=%s'

    try:
        mycursor.execute(query, (
        namelablee.get(), phonelablee.get(), Emaillablee.get(), addlablee.get(), genlablee.get(), doblablee.get(),
        date, timecur, idlablee.get()))
        con.commit()
        messagebox.showinfo('Success', f'ID {idlablee.get()} has been modified!',parent=screen)
        screen.destroy()
        show_data()
    except pymysql.Error as e:
        messagebox.showerror('Error', f'An error occurred while updating the record: {str(e)}')

def delete_student():
    selected_row = stu_table.focus()
    content = stu_table.item(selected_row)
    content_id = content['values'][0]

    # Ensure content_id is not None before proceeding
    if content_id is not None:
        try:
            # Delete the record with the given ID
            query = 'DELETE FROM student WHERE id=%s'
            mycursor.execute(query, (content_id,))
            con.commit()
            messagebox.showinfo('Deleted', f'Student with ID {content_id} has been deleted.')
        except pymysql.Error as e:
            messagebox.showerror('Error', f'An error occurred while deleting: {str(e)}')
    else:
        messagebox.showerror('Error', 'Please select a row to delete.')

    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    stu_table.delete(*stu_table.get_children())
    for data in fetched_data:
        stu_table.insert('',END,values=data)



def show_data():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    stu_table.delete(*stu_table.get_children())
    for data in fetched_data:
        stu_table.insert('', END, values=data)



def search_data():
    query='select * from student where id=%s or name=%s or mobile_no=%s or email=%s or address=%s or gender=%s or DOB=%s'
    mycursor.execute(query,(idlablee.get(),namelablee.get(),phonelablee.get(),Emaillablee.get(),addlablee.get(),genlablee.get(),doblablee.get()))
    stu_table.delete(*stu_table.get_children())
    fetect_data=mycursor.fetchall()

    for data in fetect_data:
        stu_table.insert('',END,values=data)




def add_data():
    if idlablee.get()=='' or namelablee.get()=='' or phonelablee.get()=='' or Emaillablee.get()=='' or addlablee.get()=='' or genlablee.get()=='' or doblablee.get()=='':
        messagebox.showerror('error','All fields required',parent=screen)
    else:
        try:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idlablee.get(),namelablee.get(),phonelablee.get(),Emaillablee.get(),addlablee.get(),genlablee.get(),doblablee.get(),
                                    date,timecur))
            con.commit()
            result=messagebox.askyesno('data added','data added Succesfull, Do you want to clean the form?')
            if result:
                idlablee.delete(0,END)
                namelablee.delete(0, END)
                phonelablee.delete(0, END)
                Emaillablee.delete(0, END)
                addlablee.delete(0, END)
                genlablee.delete(0, END)
                doblablee.delete(0, END)

            else:
                pass
        except:
            messagebox.showerror('Erroe','Id cannot be repeated', parent=screen)
            return

        show_data()

def connect_db():
    def connect():
        try:
            global mycursor,con
            con = pymysql.connect(host=hoste.get(), user=usere.get(), passwd=Passe.get())
            mycursor = con.cursor()
            messagebox.showinfo('Success', 'Database connection is success full', parent=database)
            database.destroy()
        except:
            messagebox.showerror('Error', 'Invalid Detail', parent=database)
            database.destroy()
            return

        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query=('create table student (id int not null primary key, name varchar(30),mobile_no varchar(30),email varchar(30),address varchar(100),gender varchar(20),DOB varchar(20),date varchar(50),time varchar(50))')
            mycursor.execute(query)
        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)

        addstu_b.config(state=NORMAL)
        searchstu_b.config(state=NORMAL)
        deletestu_b.config(state=NORMAL)
        updatestu_b.config(state=NORMAL)
        showstu_b.config(state=NORMAL)
        exstu_b.config(state=NORMAL)



    database=Toplevel()
    database.grab_set()
    database.geometry('470x250+730+230')
    database.title('database connection')
    database.resizable(0,0)

    hostl=Label(database,text='Host Name',font=('areial',20,'bold'))
    hostl.grid(row=0,column=0,padx=20)

    hoste=Entry(database,font=('areial',15,'bold'),bd=2)
    hoste.grid(row=0,column=1,padx=30,pady=20)

    userl = Label(database, text='User Name', font=('areial', 20, 'bold'))
    userl.grid(row=1, column=0, padx=20)

    usere = Entry(database, font=('areial', 15, 'bold'), bd=2)
    usere.grid(row=1, column=1, padx=30, pady=20)

    Passl = Label(database, text='Password ', font=('areial', 20, 'bold'))
    Passl.grid(row=2, column=0, padx=20)

    Passe = Entry(database, font=('areial', 15, 'bold'), bd=2)
    Passe.grid(row=2, column=1, padx=30, pady=20)

    connbut=ttk.Button(database,text='Connect',command=connect)
    connbut.grid(row=3,column=1,columnspan=2)


root.geometry('1174x680+0+0')
root.title('Student Management system')
#root.resizable(0,0)


datetimelable=Label(root,text="hello",font=('time new roman',18,'bold'))
datetimelable.place(x=0,y=0)
clock()

s='Student Management System'
Slider=Label(text=s,font=('time new roman',25,'bold'),width=30)
Slider.place(x=200,y=0)

button=ttk.Button(root,text='Connect database',command=connect_db)
button.place(x=980,y=0)


leftframe=Frame(root)
leftframe.place(x=50,y=80,width=300,height=600)

logoimg=PhotoImage(file='inside.png')
Logolable=Label(leftframe,image=logoimg)
Logolable.grid(row=0,column=0)

addstu_b=ttk.Button(leftframe,text='Add Student',width=25,state=DISABLED,command=lambda :top_level('Add Student','Add Student',add_data))
addstu_b.grid(row=1,column=0,pady=15)

searchstu_b=ttk.Button(leftframe,text='Search Student',width=25,state=DISABLED,command=lambda :top_level('Search Student','Search',search_data))
searchstu_b.grid(row=2,column=0,pady=15)

deletestu_b=ttk.Button(leftframe,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestu_b.grid(row=3,column=0,pady=15)

updatestu_b=ttk.Button(leftframe,text='Update Student',width=25,state=DISABLED,command=lambda :top_level('Update Student','Update',update_data))
updatestu_b.grid(row=4,column=0,pady=15)

showstu_b=ttk.Button(leftframe,text='Show Student',width=25,state=DISABLED,command=show_data)
showstu_b.grid(row=5,column=0,pady=15)

exstu_b=ttk.Button(leftframe,text='Export Data',width=25,state=DISABLED,command=export)
exstu_b.grid(row=6,column=0,pady=15)

Exitstu_b=ttk.Button(leftframe,text='Exit',width=25,command=exit)
Exitstu_b.grid(row=7,column=0,pady=15)

rightframe=Frame(root)
rightframe.place(x=350,y=80,width=820,height=550)

scrollx=Scrollbar(rightframe,orient=HORIZONTAL)
scrolly=Scrollbar(rightframe,orient=VERTICAL)

scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
stu_table=ttk.Treeview(rightframe,column=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added date','Added Time')
                       ,xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

scrollx.config(command=stu_table.xview)
scrolly.config(command=stu_table.yview)
stu_table.pack(fill=BOTH,expand=1)

stu_table.heading('Id',text='Id')
stu_table.heading('Name',text='Name')
stu_table.heading('Mobile No',text='Mobile No')
stu_table.heading('Email',text='Email')
stu_table.heading('Address',text='Address')
stu_table.heading('Gender',text='Gender')
stu_table.heading('D.O.B',text='D.O.B')
stu_table.heading('Added date',text='Added date')
stu_table.heading('Added Time',text='Added Time')


stu_table.column('Id',width=100,anchor=CENTER)
stu_table.column('Name',width=300,anchor=CENTER)
stu_table.column('Email',width=300,anchor=CENTER)
stu_table.column('Mobile No',width=200,anchor=CENTER)
stu_table.column('Address',width=300,anchor=CENTER)
stu_table.column('Gender',width=100,anchor=CENTER)
stu_table.column('D.O.B',width=100,anchor=CENTER)
stu_table.column('Added date',width=150,anchor=CENTER)
stu_table.column('Added Time',width=150,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview',rowheight=40,font=('arial',14,'bold'),background='white',fieldbackground='white')
style.configure('Treeview.heading',font=('arial',15,'bold'))


stu_table.config(show='headings')

root.mainloop()



