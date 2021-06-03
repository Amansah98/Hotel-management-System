from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector


class dettail:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management system")
        root.geometry("1295x550+230+220")

        lbl_title=Label(self.root,text="AVAILABLE ROOMS ",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img2=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\logo2.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)




if __name__ == "__main__":
    root = Tk()
    abc = dettail(root)
    root.mainloop()