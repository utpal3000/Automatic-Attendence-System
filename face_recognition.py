import codeop
from email.mime import image
from itertools import Predicate
from pyexpat import features
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root. geometry ( "1530x790+0+0")
        self.root.title("face Recogniton System")

        title_lbl = Label(self.root, text="FACE RECOGNITION ",font=("helvetica", 25,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
# img 1
        img_top=Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-RECOG\Images\faceRecogL.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS) 
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=5,y=55,width=650,height=700)
# img 2
        img_bottom=Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-RECOG\Images\face_recogR.jpg")
        img_bottom=img_bottom.resize((950,325),Image.ANTIALIAS) 
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb1=Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=650,y=55,width=950,height=700)

        b1_1=Button(f_lb1,text="START FACE RECOGNITION" ,cursor="hand2",font=("helvetica", 18,"bold"),bg="black",fg="white")
        b1_1.place(x=365,y=620,width=400,height=40)

    # face recognition funciton 

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord =[]

            for(x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                con=mysql.connector.connect(host="localhost",username="root",password="")

                if confidence>77:
                    pass 






        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()

