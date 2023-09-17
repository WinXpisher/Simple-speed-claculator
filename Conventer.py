from tkinter import *

class Main():
    #Setting interface
    def __init__(self):
        self.window = Tk()
        self.window.title("Converter")
        self.window.geometry('200x100+800+300')
        self.window.resizable(False, False)
        self.widget(self.window)
    #KTS calculating
    def KTS(self):
        a = float(self.ent.get()) / 1.852
        self.lab.config(text = str(format(a, '.2f')))
    #MPH calculating
    def MPH(self):
        a = float(self.ent.get()) / 1.609
        self.lab.config(text = str(format(a, '.2f')))
    #Feet/S calculating
    def feet_s(self):
        a = float(self.ent.get()) / 1.097
        self.lab.config(text = str(format(a, '.2f')))
    #Setting buttons
    def widget(self, root):
        W = 4
        self.lab_m = Label(root, text = 'Convert kph to:')
        self.ent = Entry(root, text = '0')
        self.lab = Label(root, text = '0')
        self.btn = Button(root, text = 'kts', command = self.KTS, width = W)
        self.btn_1 = Button(root, text = 'mph', command = self.MPH, width = W)
        self.btn_2 = Button(root, text = 'feet/s', command = self.feet_s, width = W)
        self.lab_m.pack()
        self.ent.pack()
        self.btn.place(x = 38, y = 42 )
        self.btn_1.place(x = 82, y = 42)
        self.btn_2.place(x = 125, y= 42)
        self.lab.place(x = 85, y = 65)
    # func with start loop 
    def start(self):
        self.window.mainloop()
#run program
if __name__ == '__main__':
    Main().start()
