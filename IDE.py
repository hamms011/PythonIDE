from tkinter import *
import tkinter.messagebox
from io import StringIO

main = Tk()
main.title("Python IDE")
main.geometry('800x500')
main.resizable(height=FALSE, width=FALSE)
main.configure(bg='gray')


def clear_text():
    code.delete(1.0, END)

def runCode():
    stdoutNew = sys.stdout
    output = sys.stdout = StringIO()
    exec(code.get(1.0, END))
    sys.stdout = stdoutNew
    tkinter.messagebox.showinfo('Result', output.getvalue())


sidebar = Frame(main, width=80, height=500, bg='#212121')
sidebar.pack(side=RIGHT)

rightbar = Frame(main, width=720, height=500, bg='#424242')
rightbar.pack(side=LEFT)


btnClear = Button(sidebar, text="Clear", command=lambda : clear_text())
btnClear.place(x=22, y=5)
btnClear.configure(bg='gray')

btnRun = Button(sidebar, text="Run", command=lambda : runCode())
btnRun.place(x=24, y=35)
btnRun.configure(bg='gray')

code = Text(rightbar, font=('arial', 11), fg='white', bg='#424242')
code.configure(width=720, height=500)
code.pack(side=RIGHT)

main.mainloop()