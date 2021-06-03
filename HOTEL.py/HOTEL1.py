from tkinter import*
from PIL import Image,ImageTk
from help import hellp
from detail import dettail
from room_won import available
from cust_win import custem



import mysql.connector

class HOTEL:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management system")

        img1=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\hotel2.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=140)

        img2=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\logo.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=230,height=140)

        lbl_title=Label(self.root,text="GREAT GRAND HOTEL ",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)



        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cut_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width="18",font=("times new roman",16,"bold"),bg="black",fg="gold", bd=0,cursor="hand1")
        cut_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="BOOKING",width="18",command=self.cust2_details,font=("times new roman",16,"bold"),bg="black",fg="gold", bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.cust4_details,width="18",font=("times new roman",16,"bold"),bg="black",fg="gold", bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        contact_btn=Button(btn_frame,text="HELP",command=self.cust3_details,width="18",font=("times new roman",16,"bold"),bg="black",fg="gold", bd=0,cursor="hand1")
        contact_btn.grid(row=3,column=0,pady=1)

       

        
        img3=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\reception2.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling1.place(x=225,y=0,width=1310,height=590)

          
        img4=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\bed.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbling2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbling2.place(x=0,y=225,width=230,height=210)

          
        img5=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\food1.jpg")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lbling3=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lbling3.place(x=0,y=420,width=230,height=190)





    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=custem(self.new_window)

    def cust2_details(self):
        self.new_window=Toplevel(self.root)
        self.app=available(self.new_window)

    def cust3_details(self):
        self.new_window=Toplevel(self.root)
        self.app=hellp(self.new_window)

    def cust4_details(self):
        self.new_window=Toplevel(self.root)
        self.app=dettail(self.new_window)





        

    
     

       

#Constructor
if __name__ == "__main__":
    root = Tk()
    abc = HOTEL(root)
    root.mainloop()