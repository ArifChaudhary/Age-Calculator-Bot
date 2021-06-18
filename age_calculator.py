from datetime import date
today = date.today()

# Exit function 
def exit():
    window.destroy()
def get_age():
    day=int(e1.get())
    month=int(e2.get())
    year=int(e3.get())
    age =today.year-year-((today.month, today.day)<(month,day))
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,age)
    t1.config(state='disabled')
 
import tkinter as tk
window = tk.Tk()
window.geometry("400x320")
window.config(bg="#454545")
window.resizable(width=False,height=False)
window.title('Age-Calculator-Bot')

# Label 
l1 = tk.Label(window,text="Calculate Your Age",font=("Arial", 20),fg="#008000",bg="#454545")
l2 = tk.Label(window,font=("Arial",12),text="Enter your birth date in this way day-month-year.",fg="white",bg="#454545")
 
l_d=tk.Label(window,text="Date: ",font=('Arial',12,"bold"),fg="white",bg="#454545")
l_m=tk.Label(window,text="Month: ",font=('Arial',12,"bold"),fg="white",bg="#454545")
l_y=tk.Label(window,text="Year: ",font=('Arial',12,"bold"),fg="white",bg="#454545")

#Entry
e1=tk.Entry(window,width=5)
e2=tk.Entry(window,width=5)
e3=tk.Entry(window,width=5)
 
b1=tk.Button(window,text="Calculate Age",font=("Arial",13), fg="green" ,command=get_age)
 
l3 = tk.Label(window,text="Your Age is: ",font=('Arial',12,"bold"),fg="white",bg="#454545")
t1=tk.Text(window,width=5,height=0,state="disabled")
 
b2=tk.Button(window,text="Exit!",font=("Arial",13),fg="red", command=exit)
 
l1.place(x=70,y=5)
l2.place(x=30,y=40)

l_d.place(x=100,y=70)
l_m.place(x=100,y=95)
l_y.place(x=100,y=120)

e1.place(x=180,y=70)
e2.place(x=180,y=95)
e3.place(x=180,y=120)

b1.place(x=100,y=150)
l3.place(x=100,y=200)
t1.place(x=240,y=203)
b2.place(x=100,y=230)
 
window.mainloop()
