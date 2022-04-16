from cProfile import label
from cgitb import handler, text
from tkinter import*
from tkinter import ttk
from tkinter import font
import os 
from turtle import title 
from PIL import Image,ImageTk
from student import Student
from train import Train
#commenting it coz it has indentation issues
#from face_recognition import Face_Recognition 



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Img1
        img = Image.open(r"Images\StudentInfo.png")
        img = img.resize((500,130))
        self.photoimg = ImageTk.PhotoImage(img)


        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        # Img 2
        img1 = Image.open(r"Images\FaceRecog.jpg")
        img1 = img1.resize((500,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)


        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        # img 3
        img2 = Image.open(r"Images\database.png")
        img2 = img2.resize((500,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)


        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        # img bg
        img3 = Image.open(r"Images\project.png")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)


        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img, text="Attendance System !",font=("helvetica", 25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Student Button
        img4 = Image.open(r"Images\student.jpg")
        img4 = img4.resize((220,220))
        self.photoimg4= ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("helvetica", 15,"bold"),bg="cyan",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # Detect Face
        img5 = Image.open(r"Images\detectFace.png")
        img5 = img5.resize((220,220))
        self.photoimg5= ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("helvetica", 15,"bold"),bg="cyan",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        # Take Attendance !
        img6 = Image.open(r"Images\Attendance.png")
        img6 = img6.resize((220,220))
        self.photoimg6= ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance Button",cursor="hand2",font=("helvetica", 15,"bold"),bg="cyan",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


        # Help Attendance !
        img7 = Image.open(r"Images\help.jpg")
        img7 = img7.resize((220,220))
        self.photoimg7= ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Button ",cursor="hand2",font=("helvetica", 15,"bold"),bg="cyan",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        # Train the Image
        img8 = Image.open(r"Images\Tr.jpg")
        img8 = img8.resize((220,220))
        self.photoimg8= ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Image ",cursor="hand2",command=self.train_data,font=("helvetica", 15,"bold"),bg="cyan",fg="white")
        b1_1.place(x=200,y=570,width=220,height=40)


 # Images Data Set...
        img9 = Image.open(r"Images\Dataset.jpg")
        img9 = img9.resize((220,220))
        self.photoimg9= ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Data Set",cursor="hand2",font=("helvetica", 15,"bold"),bg="cyan",fg="white")
        b1_1.place(x=500,y=570,width=220,height=40)


 # Exit
        img10 = Image.open(r"Images\Exit.jpg")
        img10 = img10.resize((220,220))
        self.photoimg10= ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit ",cursor="hand2",font=("helvetica", 15,"bold"),bg="cyan",fg="white")
        b1_1.place(x=800,y=570,width=220,height=40)
        
# Function buttons 
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

       
                #  self.app=Train(self.new_window)
               














if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()