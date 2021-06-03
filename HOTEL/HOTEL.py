from tkinter import*
from PIL import Image,ImageTk

class HOTEL:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management system")

    img1=Image.open(r"C:\Users\AMAN SAH\OneDrive\Documents\python series\HOTEL\hotel2.jpg")

    
     

       


if __name__ == "__main__":
    root = Tk()
    abc = HOTEL(root)
    root.mainloop()