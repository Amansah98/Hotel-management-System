class library:
    def __init__(self,listbooks):
        self.books= listbooks

    def displaybooks(self):
        print("List of books available in the library :")
        for books in self.books:
            print(" * " + books) 

    def borrowbooks(self,bookName):
        print("Which books you want to take for reading")
      


    def returnbooks(self):
        pass



class student:



        def requestbooks(self):
                self.books=input("Enter the book that you want : " )
                print(f"you have been issued {self.books} .please keep it safe and return within 30 days..")

                

            
               
            


        def returnbooks(self):
            self.books=input("Enter the name of the book that you want to return: ")

            print("Thankyou ! Hope you have enjoyed")

    
            
        


    

centrallibrary = library(["data_structure","Algorithms","TOC","Mathematical","artificial intelligence","data mining"])
student1=student()
centrallibrary.displaybooks()
welcomemsg='''======WELCOME TO THE CENTRAL LIBRARY=====
    please choose an option given below:

    1.List of all available books:
    2.Request the books:
    3.return the books:
    4.Exit the library:
'''
print(welcomemsg)
a=int(input("Enter the choice: "))
if(a==1):
    centrallibrary.displaybooks()
elif(a==2):
        student1.requestbooks()
elif(a==3):
        student1.returnbooks()
elif(a==4):
    print("Thanks for using central library ! Have a great day")
    exit()
else:
    print("Invalid choice\n Please choose the right option")



