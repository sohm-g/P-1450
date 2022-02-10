from tkinter import *

root = Tk()
root.title("drivers license")
root.geometry("300x400")
root.configure(bg="white")

canvas = Canvas(root,width=300,height=400)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0,0,300,55,fill="red")
canvas.create_rectangle(0,345,300,400,fill="red")

label_heading = canvas.create_text(150,90,font=('times','24','bold italic'),text="Driving License")
label_name_tag = canvas.create_text(40,165,font=('times','16','bold'),text="Name :")
label_date_of_birth_tag = canvas.create_text(40,205,font=('times','16','bold'),text="Date of birth :")
label_pin_no_tag = canvas.create_text(50,250,font=('times','16','bold'),text="Pin no :")
label_ID_tag = canvas.create_text(50,265,font=('times','16','bold'),text="ID :")

label_name = Label(root)
label_date_of_birth = Label(root)
label_pin_no = Label(root)
label_ID = Label(root)

def myCardDetails():
    name = "Sohm Soumitra Satish Bal Krishana vishanoo Gokhale"
    print(type(name))
    
    grade = 10
    print(type(grade))
    
    subjects = ["Math","P.E.","Science"]
    print(type(subjects))
    
    label_name['text'] = name
    
button1 = Button(root,text="Show my ID card",command=myCardDetails)
button1.configure(width=20,activebackground="red",relief=FLAT)
button1_window = canvas.create_window(150,330,anchor=CENTER,window=button1)

label_name_window = canvas.create_window(120,165,anchor=CENTER,window=label_name)
label_grade_window = canvas.create_window(90,205,anchor=CENTER,window=label_grade)
label_subjects_window = canvas.create_window(155,252,anchor=CENTER,window=label_subjects)

canvas.pack()
root.mainloop()