from tkinter import *
window=Tk()

window.title('BMI Calculator')
window.geometry("300x400")
window.configure(bg='lightcyan')

def calculate_bmi():
    weight = int(weight_entry.get())
    height = int(height_entry.get())/100
    bmi = weight/(height*height)
    bmi = round(bmi, 1)
    name = username.get()

    result_label.destroy()

    msg=""

    if bmi < 18.5:
        msg="You are Underweight"
    elif bmi >18.5 and bmi <= 24.9:
        msg="You are in the normal range"
    elif bmi >25 and bmi <= 29.9:
        msg="You are Overweight"
    elif bmi > 30:
        msg="You are obese"
    else:
        msg="Something went wrong. Try Again!"

    output_message=Label(result_frame,text=name+", your BMI is "+str(bmi)+" and "+msg, bg = "lightcyan")
    output_message.place(x=20,y=40)
    output_message.pack()

app_label=Label(window, text="BMI CALCULATOR", fg="black", bg="lightcyan")
app_label.place(x=50, y=20)

name_label=Label(window, text="Your name", fg="black", bg="lightcyan")
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

height_label=Label(window, text="Enter Height (cm)", fg="black", bg="lightcyan")
height_label.place(x=20, y=140)

height_entry=Entry(window, text="", bd=2, width=15)
height_entry.place(x=150, y=142)

weight_label=Label(window, text="Wnter Weight (kg)", fg="black", bg="lightcyan")
weight_label.place(x=20, y=185)

weight_entry=Entry(window, text="", bd=2,width=15)
weight_entry.place(x=150, y=187)

calculate_button=Button(window, text="CALCULATE", fg="black", bg="cyan", bd=4, command=calculate_bmi)
calculate_button.place(x=20, y=250)

result_frame=LabelFrame(window, text="Result", bg="lightcyan")
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

result_label=Label(result_frame, text=" ", bg="lightcyan")
result_label.place(x=20, y=20)
result_label.pack()

window.mainloop()