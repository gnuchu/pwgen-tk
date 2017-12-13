from tkinter import *
from tkinter.ttk import *
import string
import random
import numpy as np

# window = tkinter.Tk()
# window.title('Password Generator')
# window.geometry('600x400')
# window.mainloop()

class Application(ttk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.set_length(20)
    self.set_variables()
    self.create_widgets()
    self.pack()

  def set_length(self, l):
    self.length = l

  def create_widgets(self):
    self.passwordLabel = tk.Label(self, borderwidth=3, relief='ridge')
    self.passwordLabel['text'] = self.generatePassword()
    self.passwordLabel.pack()

    self.quit = tk.Button(self, text="Quit", command=root.destroy)
    self.quit.pack(side="bottom")

    self.generate = tk.Button(self, text="generate", command=self.setPassword)
    self.generate.pack(side="bottom")

  def set_variables(self):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    numbers = list(range(10))
    special = list("|!£$%^&*()_+-=][{}#~@;:.></?")
    a = np.asarray(lower + upper + numbers + special)
    random.shuffle(a)
    self.chars = a

  def setPassword(self):
    password = self.generatePassword()
    self.passwordLabel['text'] = password
  
  def generatePassword(self):
    password = ""
    
    for x in range(1, self.length):
      i = random.randint(0, len(self.chars))
      password += self.chars[i-1]

    return password


root = tkinter.Ttk()
root.title('Password Generator')
root.geometry('600x600')

app = Application(master=root)
app.mainloop()
