from tkinter import *

counter = 0
def counter_label(label):
	def count():
		global counter
		counter += 1
		label.config(text=str(counter))
		label.after(1000, count)
	count()

root = Tk()
root.title("Counting Seconds")
label = Tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = Tk.Button(root, text='Stop', width= 25, comand= root.destroy)
button.pack()
root.mainloop()
