from tkinter import *
from tkinter import messagebox
from PIL import ImageTk   #importing jpg image

def login():
    if usernameentry.get()=='' or passentry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameentry.get()=='Aatish' and passentry.get()=='1234':
        messagebox.showinfo('Sucess','Welcome Aatish')
        window.destroy()
        import  sms

    else:
        messagebox.showerror('Error','Enter correct credential')

window=Tk() #to display the window
window.geometry('1280x700+0+0')  #size of login window
window.title('Login Page')
window.resizable(0,0)


backgroundImage=ImageTk.PhotoImage(file='bg.jpg')   #onlyjpg
bgl=Label(window,image=backgroundImage)
bgl.place(x=0,y=0)


loginFrame=Frame(window,bg='white')   #login detail
loginFrame.place(x=400,y=150)     #position


logo=PhotoImage(file='logo.png')
logolable=Label(loginFrame,image=logo,bg='white')
logolable.grid(row=0,column=0,columnspan=2,pady=10)

#userid
user=PhotoImage(file='user.png')
usernamel=Label(loginFrame,image=user,text='User Name',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernamel.grid(row=1,column=0,pady=10,padx=5)


usernameentry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
usernameentry.grid(row=1,column=1,pady=10,padx=5)

#pass
password=PhotoImage(file='pass.png')
usernamel=Label(loginFrame,image=password,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernamel.grid(row=2,column=0,pady=10,padx=5)


passentry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,show='*')
passentry.grid(row=2,column=1,pady=10,padx=5)


#login
Button=Button(loginFrame,text='Login',font=('times new roman',15,'bold'),width=15,bg='cornflowerblue',fg='white'
              ,cursor='hand2',command=login)
Button.grid(row=3,column=0,columnspan=2)
window.mainloop()