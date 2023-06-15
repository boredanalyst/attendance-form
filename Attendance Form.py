## Clock In Clock Out Form

## This tool allows users to clock in and clock out of their organization using a simple interface created by Tkinter and the backend supported by Python.

## SETUP

import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import datetime
import csv
from datetime import date
import random


## SETTING UP FUNCTIONS AND VARIABLES
record_no = 0

def openAddEmployee():
    def addemp():
        newrow = []
        fname = ent_addemp.get()
        lname = ent_lname.get()
        mname = ent_mname.get()
        job = ent_job.get()
        super = ent_super.get()

        if (newrow =="") | (fname == "") | (lname =="") | (mname == "") | (job == "") | (super == ""):
            messagebox.showerror("Empty fields","One of the required fields is empty.")
            return

        emp_id = f'{fname[:2].upper()}{lname[:2].upper()}{str(random.randint(100,999))}'
        newrow = [emp_id,fname,lname,mname,job,super]
        tbl_emp.insert("","end",values=newrow)

        with open('employee.csv', 'a',newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(newrow)

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

def updateEmployee():
    ### ------------------------------------------ MODULE: UPDATING AND DELETING RECORDS
    ### ------------------------------------------ MODULE: UPDATING AND DELETING RECORDS -- Functions
    
    def load_emp():
        try:
            with open("employee.csv","r") as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    tbl_emp.insert("","end",values=row)
        except:
            with open("employee.csv","w") as file:
                writer = csv.writer(file)
                writer.writerow(["Employee ID","First Name","Last Name","Middle Name","Job Title","Direct Supervisor"])

    def int_emp():
        global record_no
        try:
            with open("employee.csv","r") as file:
                reader = csv.reader(file)
                header = next(reader)
                reader = list(reader)
                ent_empid.insert(0,reader[record_no][0])
                ent_fname.insert(0,reader[record_no][1])
                ent_lname.insert(0,reader[record_no][2])
                ent_mname.insert(0,reader[record_no][3])
                ent_job.insert(0,reader[record_no][4])
                ent_super.insert(0,reader[record_no][5])
        except:
            with open("employee.csv","w") as file:
                writer = csv.writer(file)
                writer.writerow(["Employee ID","First Name","Last Name","Middle Name","Job Title","Direct Supervisor"])

    def next_record():
        global record_no
        try:
            with open("employee.csv","r") as file:
                reader = csv.reader(file)
                header = next(reader)
                reader = list(reader)
                ##delete previous record
                ent_empid.delete(0,tk.END)
                ent_fname.delete(0,tk.END)
                ent_lname.delete(0,tk.END)
                ent_mname.delete(0,tk.END)
                ent_job.delete(0,tk.END)
                ent_super.delete(0,tk.END)

                ##adding previous record
                ent_empid.insert(0,reader[record_no+1][0])
                ent_fname.insert(0,reader[record_no+1][1])
                ent_lname.insert(0,reader[record_no+1][2])
                ent_mname.insert(0,reader[record_no+1][3])
                ent_job.insert(0,reader[record_no+1][4])
                ent_super.insert(0,reader[record_no+1][5])
                record_no += 1

                if record_no >= len(reader) - 1:
                    btn_next.config(state="disabled")
                    return
                else:
                    btn_previous.config(state="enabled")
        except:
            with open("employee.csv","w") as file:
                writer = csv.writer(file)
                writer.writerow(["Employee ID","First Name","Last Name","Middle Name","Job Title","Direct Supervisor"])

    def prev_record():
        global record_no
        try:
            with open("employee.csv","r") as file:
                reader = csv.reader(file)
                header = next(reader)
                reader = list(reader)
                ##delete previous record
                ent_empid.delete(0,tk.END)
                ent_fname.delete(0,tk.END)
                ent_lname.delete(0,tk.END)
                ent_mname.delete(0,tk.END)
                ent_job.delete(0,tk.END)
                ent_super.delete(0,tk.END)
                ## add the new details
                ent_empid.insert(0,reader[record_no-1][0])
                ent_fname.insert(0,reader[record_no-1][1])
                ent_lname.insert(0,reader[record_no-1][2])
                ent_mname.insert(0,reader[record_no-1][3])
                ent_job.insert(0,reader[record_no-1][4])
                ent_super.insert(0,reader[record_no-1][5])
                record_no -= 1

                if record_no == 0:
                    btn_previous.config(state="disabled")
                    record_no = 0
                    return
                else:
                    btn_next.config(state="enabled")
        except:
            with open("employee.csv","w") as file:
                writer = csv.writer(file)
                writer.writerow(["Employee ID","First Name","Last Name","Middle Name","Job Title","Direct Supervisor"])        

    def deleteEmp():
        global record_no
        print(record_no)
        
        try: 
            with open("employee.csv", "r") as file:
                reader = csv.reader(file)
                header = next(reader)
                rows = list(reader)
                print(rows[record_no])
            
            ##if record_no < len(rows):
            del rows[record_no]
                
            with open("employee.csv", "w",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)  # Write the header row
                writer.writerows(rows)  # Write the updated rows
            
            # Reset record_no if it exceeds the new number of rows
            if record_no >= len(rows):
                record_no = len(rows) - 1
        except:
            with open("employee.csv","w") as file:
                writer = csv.writer(file)
                writer.writerow(["Employee ID","First Name","Last Name","Middle Name","Job Title","Direct Supervisor"])
        tbl_emp.delete(*tbl_emp.get_children())
        
        ent_empid.delete(0,tk.END)
        ent_fname.delete(0,tk.END)
        ent_lname.delete(0,tk.END)
        ent_mname.delete(0,tk.END)
        ent_job.delete(0,tk.END)
        ent_super.delete(0,tk.END)
        int_emp()
        load_emp()

    ### ------------------------------------------ MODULE: UPDATING AND DELETING RECORDS -- GUI

    root_delemp = tk.Tk()
    root_delemp.geometry("800x600")

    lbl_delhead = ttk.Label(root_delemp,text="Employee Records",anchor="w",font=("Arial Black",20))
    lbl_delhead.pack(fill=tk.BOTH)

    lbl_delsub = ttk.Label(root_delemp,text="View, update, and delete records.",anchor="w",font=("Arial",8,"italic"))
    lbl_delsub.pack(fill=tk.BOTH)

    frm_view = ttk.Frame(root_delemp,width=300)

    frm_viewrecord = ttk.Frame(root_delemp,width=300,borderwidth=5,relief=tk.SUNKEN,padding=5)

    lbl_empid = ttk.Label(frm_viewrecord,text="Employee ID",anchor="w",width=40)
    lbl_empid.grid(row=0,column=0,sticky="ew",pady=5)

    ent_empid = ttk.Entry(frm_viewrecord,width=65)
    ent_empid.grid(row=0,column=1,sticky="ew",pady=5)

    lbl_fname = ttk.Label(frm_viewrecord,text="First Name",anchor="w",width=40)
    lbl_fname.grid(row=1,column=0,sticky="ew",pady=5)

    ent_fname = ttk.Entry(frm_viewrecord,width=65)
    ent_fname.grid(row=1,column=1,sticky="ew",pady=5)

    lbl_lname = ttk.Label(frm_viewrecord,text="Last Name",anchor="w", width=40)
    lbl_lname.grid(row=2,column=0,sticky="ew",pady=5)

    ent_lname = ttk.Entry(frm_viewrecord,width=50)
    ent_lname.grid(row=2,column=1,sticky="ew",pady=5)

    lbl_mname = ttk.Label(frm_viewrecord,text="Middle Name",anchor="w", width=40)
    lbl_mname.grid(row=3,column=0,sticky="ew",pady=5)

    ent_mname = ttk.Entry(frm_viewrecord,width=50)
    ent_mname.grid(row=3,column=1,sticky="ew",pady=5)

    lbl_job = ttk.Label(frm_viewrecord,text="Job Title",anchor="w", width=40)
    lbl_job.grid(row=4,column=0,sticky="ew",pady=5)

    ent_job = ttk.Entry(frm_viewrecord,width=50)
    ent_job.grid(row=4,column=1,sticky="ew",pady=5)

    lbl_super = ttk.Label(frm_viewrecord,text="Description",anchor="w", width=40)
    lbl_super.grid(row=5,column=0,sticky="ew",pady=5)

    ent_super = ttk.Entry(frm_viewrecord,width=50)
    ent_super.grid(row=5,column=1,sticky="ew",pady=5)

    btn_previous = ttk.Button(frm_viewrecord,width=50,text="Previous Record",command=prev_record)
    btn_previous.grid(row=6,column=0,sticky="ew",pady=6,padx=10)

    btn_next = ttk.Button(frm_viewrecord,width=50,text="Next Record",command=next_record)
    btn_next.grid(row=6,column=1,sticky="ew",pady=6,padx=10)
                  
    btn_delete = ttk.Button(frm_viewrecord,width=50,text="Delete Record",command=deleteEmp)
    btn_delete.grid(row=7,column=0,sticky="ew",pady=6,padx=10)

    frm_viewrecord.pack(fill=tk.BOTH)


    ### ------------------------------------------ MODULE: UPDATING AND DELETING RECORDS -- Table records

    tbl_emp = ttk.Treeview(master=frm_view)

    tbl_emp["columns"] = ["Employee ID","First Name","Last Name","Middle Name","Job Title","Direct Supervisor"]

    tbl_emp.column("#0",width=0,stretch=tk.NO)

    for col in tbl_emp["columns"]:
        tbl_emp.column(col,width=100)
        tbl_emp.heading(col,text=col)

    load_emp()

    tbl_emp.pack()

    int_emp()


    frm_view.pack()

    root_delemp.mainloop()

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
root.geometry("500x800")


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
b_submit.pack(fill=tk.BOTH,pady=12)

btn_addemp = tk.Button(f_log,text="Add Employee",command=openAddEmployee)
btn_addemp.pack(fill=tk.BOTH,pady=12)

btn_addemp = tk.Button(f_log,text="Update Records",command=updateEmployee)
btn_addemp.pack(fill=tk.BOTH,pady=12)

f_log.pack(fill=tk.BOTH,padx=12)


## ----------------------------------------------------------------------- MODULE: UPDATE RECORDS



root.mainloop()