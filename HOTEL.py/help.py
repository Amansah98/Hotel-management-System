from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector


class hellp:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management system")
        root.geometry("1295x550+230+220")

        lbl_title=Label(self.root,text="FOR ANY QUERY CONTACT TO : 9131984982    or   \n\n\nEMAIL at @khandelwalaman0000@gmail.com \n\n\n THANKYOU !  VISIT AGAIN",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=500)

        img2=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\logo2.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)









if __name__ == "__main__":
    root = Tk()
    abc = hellp(root)
    root.mainloop()