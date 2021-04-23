import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from tkinter import filedialog
import Kalkulator_Page

x, y = [], []

class Matplotlib(Toplevel):
    def __init__(self, parent, title):
        Toplevel.__init__(self, parent)
        self.title(title)
        self.geometry("400x300")
        self.resizable(False, False)

        self.aturKomponen()
        self.transient(parent)
        self.grab_set()
        self.wait_window()


    def aturKomponen(self):
        mainFrame = Frame(self, bd=10, command=self.komponen())
        #mainFrame.pack(fill=BOTH, expand=YES)

        #Label(mainFrame, text="File-to-Graph Converter").pack(side=TOP, expand=YES)

        Label(mainFrame, text="").pack(expand=YES)
        menuBar = Menu(self)

        menuUtama = Menu(menuBar, tearoff=1)
        menuUtama.add_command(label="Matplotlib", command=self.bukaWindow)
        # menuUtama.add_command(label="Keluar", command=self.onTutup)
        menuBar.add_cascade(label="Matplotlib", menu=menuUtama)

    def komponen(self):
        #self.__window = tk.Tk()

        self.nama = Label(master=self, text="Fidela Trisaktiyani 1841720211")
        self.nama.grid(row=1, column=1)
        self.judul = Label(master=self, text="File-to-Graph Converter")
        self.judul.grid(row=2, column=1)
        self.label1 = Label(master=self, text="Pilih File: ", anchor=N, justify=CENTER)
        self.chooseFile = Button(master=self, text="Browse", command=self.choose_file)
        self.label1.grid(row=4, column=1, ipadx=25)
        self.chooseFile.grid(row=5, column=1, ipadx=20)
        self.txt = Label(master=self, text="*.txt", anchor=W, justify=CENTER)
        self.txt.grid(row=4, column=2, ipadx=25)

        self.keterangan = Label(master=self, text="Ubah ke:")
        self.keterangan.grid(row=6, column=1)

        self.lineGraph = Button(master=self, text="Line Graph", command=self.line_Graph)
        self.lineGraph.grid(row=7, column=0, ipadx=15)
        self.barGraph = Button(master=self, text="Bar Graph", command=self.bar_Graph)
        self.barGraph.grid(row=7, column=1, ipadx=15)
        self.scatterGraph = Button(master=self, text="Scatter", command=self.scatterGraph)
        self.scatterGraph.grid(row=7, column=2, ipadx=15)

        self.adaFile = Label(master=self, text="File belum ada")
        self.adaFile.grid(row=6, column=1)

    def choose_file(self):
        file_name = filedialog.askopenfilename()
        if not file_name:
            return
        for line in open(file_name, 'r'):
            values = [float(s) for s in line.split()]
            x.append(values[0])
            y.append(values[1])
            self.adaFile["text"] = "File sudah tersedia!"

    def line_Graph(self):
        plt.figure(num='Line Graph | File-to-Graph Converter')
        plt.plot(x, y, marker="o")
        plt.xlabel("Tahun")
        plt.ylabel("Jumlah")
        plt.show()

    def bar_Graph(self):
        plt.figure(num='Bar Graph | File-to-Graph Converter')
        plt.bar(x, y)
        plt.xlabel("Tahun")
        plt.ylabel("Jumlah")
        plt.show()

    def scatterGraph(self):
        plt.figure(num='Bar Graph | File-to-Graph Converter')
        plt.scatter(x, y)
        plt.xlabel("Tahun")
        plt.ylabel("Jumlah")
        plt.show()

    def bukaWindow(self, event=None):
        app = Kalkulator_Page.Kalkulator_Page(self.parent, "Kalkulator")

if __name__ == '__main__':
    root = Tk()


    def run():
        import window1
        app = window1.Window1(root, "Window 1")


    Button(root, text="Tes", command=run, width=10).pack()

    root.mainloop()