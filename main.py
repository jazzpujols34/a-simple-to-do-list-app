import tkinter
from tkinter import *

# Initialize the root window
root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

# Initialize the task list
task_list = []

# Function to add a task
def addTask():
    # Get the task from the entry field
    task = task_entry.get()
    # Clear the entry field
    task_entry.delete(0, END)

    # If the task is not empty
    if task:
        # Append the task to the task file
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        # Append the task to the task list
        task_list.append(task)
        # Add the task to the listbox
        listbox.insert( END, task)

# Function to delete a task
def deleteTask():
    global task_list
    # Get the selected task from the listbox
    task = str(listbox.get(ANCHOR))
    # If the task is in the task list
    if task in task_list:
        # Remove the task from the task list
        task_list.remove(task)
        # Rewrite the task file without the deleted task
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        # Delete the task from the listbox
        listbox.delete(ANCHOR)

# Function to open the task file and load the tasks
def openTaskFile():
    try:
        global task_list
        # Open the task file and read the tasks
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        
        # For each task in the tasks
        for task in tasks:
            # If the task is not empty
            if task !='\n':
                # Append the task to the task list
                task_list.append(task)
                # Add the task to the listbox
                listbox.insert(END, task)
                
    # If the task file does not exist
    except:
        # Create the task file
        file=open('tasklist.txt', 'w')
        file.close()



# Set the application icon
Image_icon = PhotoImage(file="Image/task.png")
root.iconphoto(False,Image_icon)

# Set the top bar image
TopImage=PhotoImage(file="Image/topbar.png")
Label(root,image=TopImage).pack()

# Set the dock image
dockImage = PhotoImage(file="Image/dock.png")
Label(root,image=dockImage, bg="#32405b").place(x=30,y=25)

# Set the note image
noteImage=PhotoImage(file="Image/task.png")
Label(root,image=noteImage,bg="#32405b").place(x=340,y=25)

# Set the heading
heading=Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)

# Set the main frame
frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)


# Set the task entry field
task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

# Set the add button
# This creates a button labeled "ADD" which calls the addTask function when clicked
button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0, command=addTask)
button.place(x=300,y=0)

#listbox# Create a frame for the listbox
frame1= Frame(root,bd=3, width=700,height=280, bg="#32405b")
frame1.pack(pady=(160,0))

# Create the listbox which will display the tasks
# The listbox is placed inside frame1 and has a scrollbar
listbox = Listbox(frame1, font=('arial',12),width=40,height=16,bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side= RIGHT, fill= BOTH)

# Configure the listbox and scrollbar to work together
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Open the task file and load the tasks into the listbox
openTaskFile()

# Set the delete button
# This creates a button with a delete icon which calls the deleteTask function when clicked
Delete_icon=PhotoImage(file="Image/delete.png")
Button(root,image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM,pady=13)

# Start the Tkinter event loop
# This line should be at the end of your script and it tells Tkinter to start running the GUI
root.mainloop()