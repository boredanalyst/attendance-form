## Clock In Clock Out Form

## This tool allows users to clock in and clock out of their organization using a simple interface created by Tkinter and the backend supported by Python.

## SETUP

import tkinter as tk
from tkinter import ttk
from tkinter import font
import datetime
from datetime import date


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

tr_log.insert("","end",text="",values=("123","Jane",str(date.today()),"In"))

tr_log.pack(fill=tk.BOTH,padx=12,pady=12)

l_alert = tk.Label(f_log,text="",foreground="red")
l_alert.pack(fill=tk.BOTH)

b_submit = tk.Button(f_log,text="Submit Entry",command=insertLog)
b_submit.pack(fill=tk.BOTH)

f_log.pack(fill=tk.BOTH,padx=12)
root.mainloop()

