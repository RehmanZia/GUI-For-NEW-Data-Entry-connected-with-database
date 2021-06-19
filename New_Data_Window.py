from tkinter import *
import os
import sqlite3
from tkinter import filedialog
import cv2
from tkinter import messagebox


def home():
    registerwindow.destroy()
    os.system("HomeWindow.py")


def Insert_Image():
    f = filedialog.asksaveasfile(filetypes=(("png files", "*.png"), ("all files", "*.*")), mode='w',
                                 initialdir="C:/Users/rzia9/PycharmProjects/Final Year Project/images")
    response = messagebox.askyesno("Message", "Do You Wish To Save More Images")
    if response == 1:
        Insert_Image()
    else:
        pass


def train():
    registerwindow.destroy()
    os.system("Face_trainner.py")


def Capture_Image():
    filename = filedialog.askdirectory(initialdir="C:/Users/rzia9/PycharmProjects/Final Year Project/images")
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    Message_Resopnse = messagebox.askyesno("Message", "Do you wish to Start taking picture")
    if Message_Resopnse == 1:
        def face_extractor(img):

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)

            if faces is ():
                return None

            for (x, y, w, h) in faces:
                cropped_face = img[y:y + h, x:x + w]

            return cropped_face

        cap = cv2.VideoCapture(0)
        count = 0

        while True:
            ret, frame = cap.read()
            if face_extractor(frame) is not None:
                count += 1
                face = cv2.resize(face_extractor(frame), (350, 350))

                file_name_path = (filename + '/') + First_Name_entry.get() + str(count) + '.jpg'

                cv2.imwrite(file_name_path, face)

                cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('Face Cropper', face)
            else:
                print("Face not found")
                pass

            if cv2.waitKey(1) == 13 or count == 150:
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Message", "Images Successfully Captured")
    else:
        messagebox.showinfo("Message")


def submit():
    conn = sqlite3.connect("InviteListInfro.db")
    c = conn.cursor()
    c.execute("INSERT INTO PeoplesInfo VALUES(:ID,:First_Name,:Last_Name,:Age,:Gender,:MobileNumber,:Invited)",

              {
                  "ID": ID_entry.get(),
                  "First_Name": First_Name_entry.get(),
                  "Last_Name": Last_Name_entry.get(),
                  "Age": Age_entry.get(),
                  "Gender": Gender_entry.get(),
                  "MobileNumber": Mobile_Number_entry.get(),
                  "Invited": Invited_entry.get(),
              })
    conn.commit()
    conn.close()

    # Clear The Text Boxes
    ID_entry.delete(0, END)
    First_Name_entry.delete(0, END)
    Last_Name_entry.delete(0, END)
    Age_entry.delete(0, END)
    Gender_entry.delete(0, END)
    Mobile_Number_entry.delete(0, END)
    Invited_entry.delete(0, END)
    messagebox.showinfo("Message", "Data Successfully Saved in Database")


registerwindow = Tk()
registerwindow.title("Survillance APP")
registerwindow.geometry("600x300")
registerwindow.resizable(False, False)
registerwindow.configure(bg='#003e53')
# *****Labels*****
Reg_Label = Label(registerwindow, text="New Data Entry", fg="White", bg="#003e53", font=("bold", 18))
Reg_Label.place(x=220, y=20)
Id_Label = Label(registerwindow, text="ID", fg="White", bg="#003e53", font=(12))
Id_Label.place(x=70, y=90)
First_Name_Label = Label(registerwindow, text="First Name", fg="White", bg="#003e53", font=(12))
First_Name_Label.place(x=70, y=120)
Last_Name_Label = Label(registerwindow, text="Last Name", fg="White", bg="#003e53", font=(12))
Last_Name_Label.place(x=70, y=150)
Age_Label = Label(registerwindow, text="Age", fg="White", bg="#003e53", font=(12))
Age_Label.place(x=70, y=180)
Gender_Label = Label(registerwindow, text="Gender", fg="White", bg="#003e53", font=(12))
Gender_Label.place(x=70, y=210)
Mobile_Number_Label = Label(registerwindow, text="Mobile Number", fg="White", bg="#003e53", font=(12))
Mobile_Number_Label.place(x=300, y=90)
Invited_Label = Label(registerwindow, text="Invited", fg="White", bg="#003e53", font=(12))
Invited_Label.place(x=300, y=120)
# *****EntryField*****
ID_entry = Entry(registerwindow)
ID_entry.place(x=160, y=94)
First_Name_entry = Entry(registerwindow)
First_Name_entry.place(x=160, y=124)
Last_Name_entry = Entry(registerwindow)
Last_Name_entry.place(x=160, y=154)
Age_entry = Entry(registerwindow)
Age_entry.place(x=160, y=184)
Gender_entry = Entry(registerwindow)
Gender_entry.place(x=160, y=214)
Mobile_Number_entry = Entry(registerwindow)
Mobile_Number_entry.place(x=420, y=94)
Invited_entry = Entry(registerwindow)
Invited_entry.place(x=420, y=124)

# *****Button*****
Submit_Button = Button(registerwindow, text="Submit", fg="Black", font=(8), command=submit).place(x=405, y=250)
Back_Button = Button(registerwindow, text="Back", fg="Black", font=(8), command=home).place(x=500, y=250)
Train_Model_Button = Button(registerwindow, text="Train Model", fg="Black", font=(8), command=train).place(x=285, y=250)
Capture_Image_Button = Button(registerwindow, text="Capture Image", fg="Black", font=(8), command=Capture_Image).place(
    x=140, y=250)
Insert_Image_Button = Button(registerwindow, text="Insert Image", fg="Black", font=(8), command=Insert_Image).place(
    x=10, y=250)
registerwindow.mainloop()