from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector



class custem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management system")
        root.geometry("1295x550+230+220")

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS ",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img2=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\logo2.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

        labelframeleft=LabelFrame(self.root,bd=2,text="Customer Details",font=("times new roman",25,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #custname
        lablname=Label(labelframeleft,text="customer Name: ",padx=2,pady=6,font=("times new roman",20,"bold"))
        lablname.grid(row=0,column=0,sticky=W)

        txtname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=25)
        txtname.grid(row=0,column=1)

        #father name
        lablfname=Label(labelframeleft,text="Father Name: ",padx=2,pady=6,font=("times new roman",20,"bold"))
        lablfname.grid(row=1,column=0,sticky=W)

        txtfname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=25)
        txtfname.grid(row=1,column=1)

        #AGE
        lablage=Label(labelframeleft,text="Age: ",padx=2,pady=6,font=("times new roman",20,"bold"))
        lablage.grid(row=2,column=0,sticky=W)

        txtage=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=25)
        txtage.grid(row=2,column=1)
        
        #phonenumber
        lablnumber=Label(labelframeleft,text=" ph_Number: ",padx=2,pady=6,font=("times new roman",20,"bold"))
        lablnumber.grid(row=3,column=0,sticky=W)

        txtname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=25)
        txtname.grid(row=3,column=1)
        #address

        labladd=Label(labelframeleft,text="Address: ",padx=2,pady=6,font=("times new roman",20,"bold"))
        labladd.grid(row=4,column=0,sticky=W)

        txtadd=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=25)
        txtadd.grid(row=4,column=1)

        #idproof

        lablno=Label(labelframeleft,text="Adhar_number: ",padx=2,pady=6,font=("times new roman",20,"bold"))
        lablno.grid(row=5,column=0,sticky=W)

        txtno=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=25)
        txtno.grid(row=5,column=1)

        #gender
        labl_gender=Label(labelframeleft,text="Gender: ",padx=2,pady=6,font=("times new roman",20,"bold"))
        labl_gender.grid(row=6,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("MALE","FEMALE","OTHERS")
        combo_gender.current(0)
        combo_gender.grid(row=6,column=1)

        labl_nationality=Label(labelframeleft,text="Nationality: ",padx=2,pady=6,font=("times new roman",20,"bold"))
        labl_nationality.grid(row=7,column=0,sticky=W)
        combo_nationality=ttk.Combobox(labelframeleft,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_nationality["value"]=("INDIAN","AMERICAN","JAPANESE","RUSSIAN")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=45)

        btnadd=Button(btn_frame,text="ADD",font=("times new roman",20,"bold"),bg="black",fg="gold",width=8)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="UPDATE",font=("times new roman",20,"bold"),bg="black",fg="gold",width=8)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="RESET",font=("times new roman",20,"bold"),bg="black",fg="gold",width=8)
        btndelete.grid(row=0,column=2,padx=1)

        '''btnreset=Button(btn_frame,text="SET",font=("times new roman",20,"bold"),bg="black",fg="gold",width=6)
        btnreset.grid(row=0,column=3,padx=1)'''

        

        img3=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\customer1.jpg")
        img3=img3.resize((300,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lbling.place(x=760,y=55,width=720,height=300)

        img4=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\customer2.jpg")
        img4=img4.resize((300,300),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbling=Label(self.root,image=self.photoimg4,bd=0,relief=RIDGE)
        lbling.place(x=660,y=55,width=320,height=300)

        
        img5=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\customer3.jpg")
        img5=img5.resize((300,300),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lbling=Label(self.root,image=self.photoimg5,bd=0,relief=RIDGE)
        lbling.place(x=460,y=55,width=200,height=300)



        def add_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="db")

    

        
        
        
        
        




       


if __name__ == "__main__":
    root = Tk()
    abc = custem(root)
    root.mainloop()