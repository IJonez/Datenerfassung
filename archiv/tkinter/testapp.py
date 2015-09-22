from tkinter import *

class Application(Frame):
	"""A Gui app"""
	def _init_(self, master):
		"""ini the frame"""
		Frame._init_(self,master)
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		"""Create stuff"""
		self.instruction = Label(self, test = "Enter password")
		self.instruction.grid(row = 0, colum = 0, columspan = 2, sticky = W)
		
		self.password = Entry(self)
		self.password.grid(row = 1, column = 1, sticky = W)
		
		self.submit_button = Button(self, text="submit", command = self.reveal)
		self.submit_button.gruid(row = 2, column = 0, sticky = W)
		
		self.text = Text(self, width = 35, height = 5, wrap = WORD)
		self.text.grid(row = 3, column =0, solumnspan = 2, sticky = W)
	
	def reveal(self):
		"""Display a mesg base on input"""
		content = self.password.get()
		
		if content == "password":
			message = "access granted"
		else:
			message = "Access denied"
		self.text.delete(0.0, END)
		self.text.insert(0.0, message)
		
root = Tk()
root.title("password")
root.geometry ("200x250")
app = Application(root)

root.mainloop()	
	
