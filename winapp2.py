from __future__ import print_function
from tkinter import *
import test
import scipy.io.wavfile as wavfile
import matplotlib
matplotlib.use('TkAgg')

WORK = test
class Main(Frame) :
    def __init__(self , root):
        super().__init__(root)
        self.init_main()

    def init_main (self) :
        toolbar = Frame(bg = "black" , bd = 2)
        toolbar.pack(side=TOP, fill=X)
        name = StringVar()
        name_label = Label(text="input_file:")
        name_label.place(x=0, y=60)

        name_entry = Entry(textvariable=name)
        name_entry.place(x=0, y=80)
                ####### test #######
        btn_input = Button(toolbar, text="in file", command=WORK.wr_in_file, compound=TOP)
        btn_input.pack(side=LEFT)
       # btn_input = Button(toolbar, text="visual", command=WORK.display_plot_file(name.get()), compound=TOP)
       # btn_input.pack(side=LEFT)
        btn_input = Button(toolbar, text="mp3 -> wav", command=WORK.convertor , compound=TOP)
        btn_input.pack(side=LEFT)

                ####### test #######
if __name__ == "__main__" :
    root = Tk()
    app = Main(root)
    app.pack()
    root.title("work with fft")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()