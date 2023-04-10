from tkinter import *
from tkinter import Tk

class StudentsData:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1650x800')
        title1=Label(self.root, text='Students Data',font=('Century', 30),bg='white',fg='black',bd=5,relief=GROOVE)
        title1.pack()
        
        self.rollnoVar=StringVar()
        self.fnameVar=StringVar()
        self.lnameVar=StringVar()
        self.contactVar=StringVar()
        self.emailVar=StringVar()
        self.locationVar=StringVar()
        self.courseVar=StringVar()

        # Creating Frame
        DataEntryFrame=Frame(self.root, bg='#F56040')
        DataEntryFrame.place(x=16,y=70, width=470,height=710)

        DataDisplayFrame=Frame(self.root, bg='#F56040')
        DataDisplayFrame.place(x=505,y=70,width=1015, height=710)

        # working with data entry frame
        title2=Label(DataEntryFrame,text='Data Entry',font=('Century', 15),bg='white',bd=5)
        title2.grid(row=0,columnspan=2,padx=165,pady=20)

        # Roll No.
        rollnoL=Label(DataEntryFrame, text='Roll No',font=('Gadugi',20),bg='#F56040',fg='white')
        rollnoL.grid(row=1,column=0,sticky='w',padx=10,pady=13)

        rollnoE=Entry(DataEntryFrame,textvariable=self.rollnoVar,font=('Gadugi',20),relief=RAISED)
        rollnoE.grid(row=1,column=1,sticky='e')

        # First Name
        fnameL=Label(DataEntryFrame, text='First Name',font=('Gadugi',20),bg='#F56040',fg='white')
        fnameL.grid(row=2,column=0,sticky='w',padx=10,pady=13)

        fnameE=Entry(DataEntryFrame,textvariable=self.fnameVar,font=('Gadugi',20),relief=RAISED)
        fnameE.grid(row=2,column=1,sticky='e')

        # Last Name
        lnameL=Label(DataEntryFrame, text='Last Name',font=('Gadugi',20),bg='#F56040',fg='white')
        lnameL.grid(row=3,column=0,sticky='w',padx=10,pady=13)

        lnameE=Entry(DataEntryFrame,textvariable=self.lnameVar,font=('Gadugi',20),relief=RAISED)
        lnameE.grid(row=3,column=1,sticky='e')

        # contact
        contactL=Label(DataEntryFrame, text='Contact',font=('Gadugi',20),bg='#F56040',fg='white')
        contactL.grid(row=4,column=0,sticky='w',padx=10,pady=13)

        contactE=Entry(DataEntryFrame,textvariable=self.contactVar,font=('Gadugi',20),relief=RAISED)
        contactE.grid(row=4,column=1,sticky='e')

        # Email
        emailL=Label(DataEntryFrame, text='Email ID',font=('Gadugi',20),bg='#F56040',fg='white')
        emailL.grid(row=5,column=0,sticky='w',padx=10,pady=13)

        emailE=Entry(DataEntryFrame,textvariable=self.emailVar,font=('Gadugi',20),relief=RAISED)
        emailE.grid(row=5,column=1,sticky='e')

        # locaation
        locationL=Label(DataEntryFrame, text='Location',font=('Gadugi',20),bg='#F56040',fg='white')
        locationL.grid(row=6,column=0,sticky='w',padx=10,pady=13)

        locationE=Entry(DataEntryFrame,textvariable=self.locationVar,font=('Gadugi',20),relief=RAISED)
        locationE.grid(row=6,column=1,sticky='e')

        #Course
        courseL=Label(DataEntryFrame, text='Course',font=('Gadugi',20),bg='#F56040',fg='white')
        courseL.grid(row=7,column=0,sticky='w',padx=10,pady=13)

        courseE=Entry(DataEntryFrame,textvariable=self.courseVar,font=('Gadugi',20),relief=RAISED)
        courseE.grid(row=7,column=1,sticky='e')


        # Creating Frame for Button
        btnFrame=Frame(DataEntryFrame)
        btnFrame.place(x=10,y=550,width=450,height=130)

        addBtn=Button(btnFrame, text='ADD',command=self.addingData, font=('Gadugi',18), bg='black', fg='white')
        addBtn.grid(row=0,column=0,padx=13,pady=40)

        updateBtn=Button(btnFrame, text='UPDATE',command=self.updatingData, font=('Gadugi',18), bg='black', fg='white')
        updateBtn.grid(row=0,column=1,padx=10,pady=40)

        deleteBtn=Button(btnFrame, text='DELETE',command=self.deletingData, font=('Gadugi',18), bg='black', fg='white')
        deleteBtn.grid(row=0,column=2,padx=10,pady=40)

        clearBtn=Button(btnFrame, text='CLEAR',command=self.clearingData, font=('Gadugi',18), bg='black', fg='white')
        clearBtn.grid(row=0,column=3,padx=10,pady=40)

        # working with data display frame
        title3=Label(DataDisplayFrame, text='Data Display',font=('Century', 15),bg='white',bd=5)
        title3.place(x=450,y=20)

        tblFrame=Frame(DataDisplayFrame)
        tblFrame.place(x=20,y=90,width=973,height=590)
        
        from tkinter import ttk
        self.StudentInfo=ttk.Treeview(tblFrame,columns=('rollno','fname','lname','contact','email','location','course'))
        self.StudentInfo.heading('rollno',text='Roll No.')
        self.StudentInfo.heading('fname',text='First Name')
        self.StudentInfo.heading('lname',text='Last Name')
        self.StudentInfo.heading('contact',text='Contact')
        self.StudentInfo.heading('email',text='Email ID')
        self.StudentInfo.heading('location',text='Location')
        self.StudentInfo.heading('course',text='Course')
    

        self.StudentInfo.column('rollno',width=100,anchor='center')
        self.StudentInfo.column('fname',width=130,anchor='center')
        self.StudentInfo.column('lname',width=130,anchor='center')
        self.StudentInfo.column('contact',width=180,anchor='center')
        self.StudentInfo.column('email',width=180,anchor='center')
        self.StudentInfo.column('location',width=125,anchor='center')
        self.StudentInfo.column('course',width=125,anchor='center')
        s = ttk.Style()
        s.configure('.', font=('Century', 14))
        
        self.StudentInfo['show']='headings'
        self.fetchingData()
        self.StudentInfo.pack()

    
        self.StudentInfo.bind('<ButtonRelease-1>',self.cursor_row)
    
    def addingData(self):
        import pymysql
        connection=pymysql.connect(host='localhost',user='root',password='256584130000',db='studentdb')
        c=connection.cursor()
        c.execute('insert into studentdata values(%s, %s, %s, %s, %s, %s, %s)',
                  (
                      self.rollnoVar.get(),
                      self.fnameVar.get(),
                      self.lnameVar.get(),
                      self.contactVar.get(),
                      self.emailVar.get(),
                      self.locationVar.get(),
                      self.courseVar.get()
                      ))
        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()
        
    def clearingData(self):
        self.rollnoVar.set(''),
        self.fnameVar.set(''),
        self.lnameVar.set(''),
        self.contactVar.set(''),
        self.emailVar.set(''),
        self.locationVar.set(''),
        self.courseVar.set('')
        
    def fetchingData(self):
        import pymysql
        connection=pymysql.connect(host='localhost',user='root',password='256584130000',db='studentdb')
        c=connection.cursor()
        c.execute('select * from studentdata')
        data=c.fetchall()
        self.StudentInfo.delete(*self.StudentInfo.get_children())
        for i in data:
            self.StudentInfo.insert('',END, value=i)
        connection.commit()
        connection.close()

    def cursor_row(self,a):
        cursor_row=self.StudentInfo.focus()
        content=self.StudentInfo.item(cursor_row)
        row=content['values']
        self.rollnoVar.set(row[0])
        self.fnameVar.set(row[1])
        self.lnameVar.set(row[2])
        self.contactVar.set(row[3])
        self.emailVar.set(row[4])
        self.locationVar.set(row[5])
        self.courseVar.set(row[6])
        
    def updatingData(self):
        import pymysql
        connection=pymysql.connect(host='localhost',user='root',password='256584130000',db='studentdb')
        c=connection.cursor()
        c.execute('update studentdata set fname=%s, lname=%s, contact=%s, email=%s, location=%s, course=%s where rollno=%s',
                  (
                      self.fnameVar.get(),
                      self.lnameVar.get(),
                      self.contactVar.get(),
                      self.emailVar.get(),
                      self.locationVar.get(),
                      self.courseVar.get(),
                      self.rollnoVar.get(),
                      
                       ))
        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()
        
    def deletingData(self):
        import pymysql
        connection=pymysql.connect(host='localhost',user='root',password='256584130000',db='studentdb')
        c=connection.cursor()
        c.execute('delete from studentdata where rollno=%s',self.rollnoVar.get())
        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()

   
       
root=Tk()
s=StudentsData(root)
