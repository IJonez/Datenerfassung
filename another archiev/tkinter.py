from tkinter import *
root= Tk()

v = IntVar()


liste = [("python",1),
         ("perl",2),
         ("JAVA",3),
         ("C**",4),
]

def ShowChoice():
    print (v.get())



Label(root,
      text="""Coose a programming language""",
      justify = LEFT,
      padx = 20).pack()

for name, val in liste:
    Radiobutton(root,
                text=name,
                indicatoron = 0,
                width = 50,
                padx = 20,
                variable=v,
                value=val).pack(anchor=W)

mainloop()

                        
            
