## Clock In Clock Out Form

## This tool allows users to clock in and clock out of their organization using a simple interface created by Tkinter and the backend supported by Python.

## SETUP

import tkinter as tk
from tkinter import ttk
from tkinter import font
import datetime
import csv
from datetime import date
import random


## SETTING UP FUNCTIONS

def insertLog():
    empID = e_emp.get()
    name = e_name.get()
    actiondate = date.today()
    action = d_action["text"]
    time = datetime.datetime.now().time().strftime("%H:%M")

    if (empID == "") or (name == "") or (action == "Select Option"):
        l_alert.config(text="One of the fields contain invalid responses.")
        return

    tr_log.insert("","end",text="",values=(empID,name,actiondate,time,action))
    e_emp.delete(0,tk.END)
    e_name.delete(0,tk.END)
    d_action.config(text="Select Option")
    l_alert.config(text="Entry successfully recorded")

## SETTING UP THE GUI

### creating the main window
root = tk.Tk()
root.title("Attendance Form")
root.resizable(False,False)
root.geometry("500x500")


### Setting up the header

header = tk.Frame(root)
header.pack(fill=tk.BOTH)
l_title = tk.Label(header,text="Attendance Form",font=("Calibri",18))
l_title.pack(fill=tk.BOTH)
l_subtitle = tk.Label(header,text="Powered by Tkinter and Python",font=("Noto Mono",8))
l_subtitle.pack(fill=tk.BOTH)

l_date = tk.Label(header,text="Date Today",font=("Calibri",8))
def displayDate():
    today = date.today()
    today = today.strftime("%B %d, %Y")
    l_date.config(text=f'Date Today: {today}')
    l_date.after(3_600_000,displayDate)
displayDate()
l_date.pack(fill=tk.BOTH)

l_time = tk.Label(header,text="Time Right Now",font=("Calibri",8))

def displayTime():
    now = datetime.datetime.now().time()
    now = now.strftime("%H:%M")
    l_time.config(text=f'Current Time: {now}')
    l_time.after(15000,displayTime)
displayTime()
l_time.pack(fill=tk.BOTH)


### Setting up the input fields.

f_input = tk.Frame(root,borderwidth=2,relief=tk.GROOVE)

l_emp = tk.Label(f_input,text="Employee ID: ")
l_emp.grid(row=0,column=0,pady=5,sticky="ew")
e_emp = tk.Entry(f_input,width=60)
e_emp.grid(row=0,column=1,pady=5,sticky="ew")

l_name = tk.Label(f_input,text="Full Name: ")
l_name.grid(row=1,column=0,pady=5,sticky="ew")
e_name = tk.Entry(f_input,width=30)
e_name.grid(row=1,column=1,pady=5,sticky="ew")

l_action = tk.Label(f_input,text="Action: ")
l_action.grid(row=2,column=0,sticky="ew")
active = tk.StringVar(root)
active.set("Select Option")
d_action = tk.OptionMenu(f_input,active,*["Clock In","Clock Out"])
d_action.grid(row=2,column=1,sticky="ew")

f_input.pack(fill=tk.BOTH,padx=12)

### Displaying time entries.

f_log = tk.Frame(root,borderwidth=2,relief=tk.GROOVE)

tr_log = ttk.Treeview(root)
tr_log["columns"] = ("Employee ID","Employee Name","Date","Time","Action")

tr_log.column("#0",width=0,stretch=tk.NO) ## Hides the initial column that should not be displayed.
tr_log.column("Employee ID",width=8)
tr_log.column("Employee Name",width=8)
tr_log.column("Date",width=8)
tr_log.column("Time",width=8)
tr_log.column("Action",width=8)

tr_log.heading("Employee ID",text="Employee ID")
tr_log.heading("Employee Name",text="Employee Name")
tr_log.heading("Date",text="Date")
tr_log.heading("Time",text="Time")
tr_log.heading("Action",text="Action")

tr_log.pack(fill=tk.BOTH,padx=12,pady=12)

l_alert = tk.Label(f_log,text="",foreground="red")
l_alert.pack(fill=tk.BOTH)

b_submit = tk.Button(f_log,text="Submit Entry",command=insertLog)
b_submit.pack(fill=tk.BOTH)

f_log.pack(fill=tk.BOTH,padx=12)

### ------------------------------------------ MODULE: ADDING NEW EMPLOYEES

### ------------------------------------------ MODULE: ADDING NEW EMPLOYEES : Creating functions

def addemp():
    fname = ent_addemp.get()
    lname = ent_lname.get()
    mname = ent_mname.get()
    job = ent_job.get()
    super = ent_super.get()
    emp_id = f'{fname[:2].upper()}{lname[:2].upper()}{str(random.randint(100,999))}'
    tbl_emp.insert("","end",values=(emp_id,fname,lname,mname,job,super))

    with open('employee.csv', 'a') as file:
        file.write(f'\n{emp_id},{fname},{lname},{mname},{job},{super}')

    ## clearing of values
    ent_addemp.delete(0,tk.END)
    ent_lname.delete(0,tk.END)
    ent_mname.delete(0,tk.END)
    ent_job.delete(0,tk.END)
    ent_super.delete(0,tk.END)
    emp_id = ""

def loadData():
    try:
        with open('employee.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header row if it exists
            for row in reader:
                tbl_emp.insert('', 'end', values=row)
    except:
        with open("employee.csv","w") as file:
            writer = csv.writer(file)
            writer.writerow(["Employee ID","First Name","Last Name","Middle Name","Job Title","Direct Supervisor"])


### ------------------------------------------ MODULE: ADDING NEW EMPLOYEES : Preparing variables and functions

style_label = ttk.Style()

style_label.configure(
    "Add.Employee.Label",
    ##font=("Arial",30,"bold"),
    anchor="w",
    width=12,
    background="blue"
    )

mystyle = ttk.Style()
mystyle.configure("My.TLabel",background="blue")
mystyle.theme_use("clam")


### ------------------------------------------ MODULE: ADDING NEW EMPLOYEES : Setting up the GUI

root_addemp = tk.Tk()
root_addemp.title("Add new employee")
root_addemp.geometry("700x620")

lbl_empheading = ttk.Label(root_addemp,text="Add Employees",anchor="w",font=("Arial Black",12),background="skyblue")
lbl_empheading.pack(fill=tk.BOTH,pady=(0,10))

lfrm_newemp = ttk.LabelFrame(root_addemp,text="Employee Information",padding=20,relief=tk.SUNKEN,borderwidth=5)

lbl_addemp = ttk.Label(lfrm_newemp,text="First Name",anchor="w",width=20)
lbl_addemp.grid(row=0,column=0,sticky="w",pady=10)

ent_addemp = ttk.Entry(lfrm_newemp,width=20)
ent_addemp.grid(row=0,column=1,sticky="w",pady=10)

lbl_lname = ttk.Label(lfrm_newemp,text="Last Name",width=20)
lbl_lname.grid(row=1,column=0,sticky="ew",pady=10)

ent_lname = ttk.Entry(lfrm_newemp,width=20)
ent_lname.grid(row=1,column=1,sticky="ew",pady=10)

lbl_mname = ttk.Label(lfrm_newemp,text="Middle Name",width=20)
lbl_mname.grid(row=2,column=0,sticky="ew",pady=10)

ent_mname = ttk.Entry(lfrm_newemp,width=20)
ent_mname.grid(row=2,column=1,sticky="ew",pady=10)

lbl_job = ttk.Label(lfrm_newemp,text="Job Title",width=20)
lbl_job.grid(row=3,column=0,sticky="ew",pady=10)

ent_job = ttk.Entry(lfrm_newemp,width=20)
ent_job.grid(row=3,column=1,sticky="ew",pady=10)

lbl_super = ttk.Label(lfrm_newemp,text="Direct Supervisor",width=20)
lbl_super.grid(row=4,column=0,sticky="ew",pady=10)

ent_super = ttk.Entry(lfrm_newemp,width=20)
ent_super.grid(row=4,column=1,sticky="ew",pady=10)

btn_add = ttk.Button(lfrm_newemp,text="Add Employee",command=addemp)
btn_add.grid(row=5,column=0,columnspan=2,sticky="ew",pady=10)

### ------------------------------------------ MODULE: ADDING NEW EMPLOYEES : Adding employee table

tbl_emp = ttk.Treeview(master=root_addemp)

tbl_emp["columns"] = ["Employee ID","First Name","Last Name","Middle Name","Job Title","Direct Supervisor"]

tbl_emp.column("#0",width=0,stretch=tk.NO)

for col in tbl_emp["columns"]:
    tbl_emp.column(col,width=100)
    tbl_emp.heading(col,text=col)

lfrm_newemp.pack(pady=15)

loadData()
tbl_emp.pack()

root_addemp.mainloop()
root.mainloop()

