from tkinter import *
import tkinter as tk
from functools import partial
import matplotlib_page

class Kalkulator_Page:
    def __init__(self, parent, title):
        self.parent = parent

        self.parent.geometry("400x300")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onTutup)
        self.parent.resizable(False, False)

        self.aturKomponen()

        #self.parent.__window = tk.Tk()
        #self.parent.__window.title('Kalkulator GUI')
        self.membuatTombol()
        self.penentu = False

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, command=self.membuatTombol())
        #mainFrame.pack(fill=BOTH, expand=YES)

        # label window Utama
        Label(mainFrame, text="").pack(expand=YES)

        # buat menu
        menuBar = Menu(self.parent)

        menuUtama = Menu(menuBar, tearoff=1)
        menuUtama.add_command(label="Matplotlib", command=self.bukaWindow)
        #menuUtama.add_command(label="Keluar", command=self.onTutup)
        menuBar.add_cascade(label="Matplotlib", menu=menuUtama)

        self.parent.config(menu=menuBar)

    def membuatTombol(self):
        self.layar = tk.Entry(master=self.parent, width=20)
        self.layar.grid(row=0, column=0, columnspan=10)

        btn_list = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', '+', '-',
            'C', '/', '*',
            '='
        ]
        baris = 1
        kolom = 0
        for penampung in btn_list:
            perintah = partial(self.hitung, penampung)
            if penampung == '=':
                tk.Button(master=self.parent, text='=', width=19, command=perintah).grid(row=baris, column=kolom, columnspan=5)
            else:
                tk.Button(master=self.parent, text=penampung, width=5, command=perintah).grid(row=baris, column=kolom)
            kolom += 1
            if kolom > 2:
                kolom = 0
                baris += 1

    def hitung(self, key):
        if key == '=':
            self.penentu = True
            try:
                result = eval(self.layar.get())
                self.layar.delete(0, tk.END)
                self.layar.insert(tk.END, str(result))
            except:
                self.layar.insert(tk.END, "-> Error!")
        elif key == 'C':
            self.layar.delete(0, tk.END)
        else:
            if self.penentu:
                self.layar.delete(0, tk.END)
                self.penentu = False
            self.layar.insert(tk.END, key)

    def bukaWindow(self, event=None):
        app = matplotlib_page.Matplotlib(self.parent, "File-to-Graph Converter")

    def onTutup(self, event=None):
        self.parent.destroy()


if __name__ == '__main__':
    root = Tk()

    app = Kalkulator_Page(root, "Kalkulator")

    root.mainloop()