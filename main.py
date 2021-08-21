from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def print(what):
	console["text"] = console["text"] + "\n" + str(what)
def openFile():
    tf = filedialog.askopenfilename( 
        title="Open Python file", 
        filetypes=(("Python Files", "*.py; *.py3"),)
        )
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

ws = Tk()
ws.title("Python")
ws.geometry("1500x1500")
tab_control = ttk.Notebook(ws)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab_control.add(tab1, text='Console')  
tab_control.add(tab2, text='Code') 
txtarea = Text(tab2, width=110, height=30, font="Times 12", fg="white", bg="black")
txtarea.pack(pady=20)
def Start():
    try:

        result=txtarea.get(1.0, END+"-1c")
        r = exec(result)
    except Exception as e:
        print(e)    
def Save():
    file_name = filedialog.asksaveasfilename(filetypes=(("Python Files", "*.py; *.py3")), defaultextension="*.py ") 
    f = open(file_name, 'a')
    f.write(console["text"])
    f.close()
console = Label(tab1, bg="black", fg="white")
console.pack()
console["text"] = "                                                                                                                "
Button(
    tab2, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)
Button(tab2, text="Compile File", command=Start).pack(side=RIGHT, expand=True, fill=X, padx=20)
Button(
    tab2,
    text="Save File",
    command=Save).pack(side=RIGHT, expand=True, fill=X, padx=20)
tab_control.pack(expand=1, fill='both') 
ws.mainloop()
