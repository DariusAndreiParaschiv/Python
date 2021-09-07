import tkinter as tk
import json
from Retete_func import RF

rf = RF()

class interf:

    def __init__(self, root):
        #Frame-ul 1 + componente
        self.f0 = tk.LabelFrame(root, text = "Menu")
        self.f0.pack()

        self.b_ing = tk.Button(self.f0, text = "Cauta dupa ingrediente", command = self.ingrediente)
        self.b_ing.pack()

        self.b_m = tk.Button(self.f0, text = "Cauta dupa mancaruri", command = self.mancare)
        self.b_m.pack()

        self.b_quit = tk.Button(self.f0, text = "Iesire", command = root.quit)
        self.b_quit.pack()

        #Frame-ul 2 + componente
        self.f1 = tk.LabelFrame(root, text = "Ingrediente")

        #Variantele de ingrediente
        self.i1 = tk.StringVar()
        self.I1 = tk.Checkbutton(self.f1, text = "mere", variable = self.i1, onvalue = "mere", offvalue = '0')
        self.I1.deselect()
        self.I1.pack()
        self.i2 = tk.StringVar()
        self.I2 = tk.Checkbutton(self.f1, text = "faina", variable = self.i2, onvalue = "faina", offvalue = '0')
        self.I2.deselect()
        self.I2.pack()
        self.i3 = tk.StringVar()
        self.I3 = tk.Checkbutton(self.f1, text = "oua", variable = self.i3, onvalue = "oua", offvalue = '0')
        self.I3.deselect()
        self.I3.pack()
        self.i4 = tk.StringVar()
        self.I4 = tk.Checkbutton(self.f1, text = "salam", variable = self.i4, onvalue = "salam", offvalue = '0')
        self.I4.deselect()
        self.I4.pack()
        self.i5 = tk.StringVar()
        self.I5 = tk.Checkbutton(self.f1, text = "cascaval", variable = self.i5, onvalue = "cascaval", offvalue = '0')
        self.I5.deselect()
        self.I5.pack()

        self.caut = tk.Button(self.f1, text = "Cauta", command = self.lipeste)
        self.caut.pack()

        self.Retur = tk.Button(self.f1, text = "Inapoi", command = self.retur)
        self.Retur.pack()

        self.t0 = tk.Text(self.f1, height = 30, width = 50)

        self.list1 = tk.Listbox(self.f1, height=6, width=35)
        self.list1.pack(side = 'left')

        sb1 = tk.Scrollbar(self.f1)
        sb1.pack(side='right', fill=tk.Y)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        #self.list1.bind('<<ListboxSelect>>', self.selected)

        #Frame-ul 3 + componente
        self.f2 = tk.LabelFrame(root, text = "Mancaruri")

        self.l2 = tk.Label(self.f2, text = "Introdu numele mancarii")
        self.l2.pack()

        self.e2 = tk.Entry(self.f2)
        self.e2.pack()

        self.Caut0 = tk.Button(self.f2, text = "Cauta", command = self.caut0)
        self.Caut0.pack()

        self.t2 = tk.Text(self.f2, height = 10, width = 100)

        self.Retur0 = tk.Button(self.f2, text = "Inapoi", command = self.retur0)
        self.Retur0.pack()

    def afis(self, D): #Afiseaza retetele in functie de lista intoarsa de lipeste
        '''text = ''
        for i in D:
            text += i + '\n' + '\n' + "Ingrediente:"
            text += '\n'
            for j in D[i]:
                text += j + '\n'
            text += '\n' + '\n'
        self.list1.delete(0, 'end')
        self.list1.insert('end', text)'''

        self.list1.delete(0, 'end')
        for i in D:
            self.list1.insert('end', i)
            self.list1.insert('end', 'Ingrediente:')
            for j in D[i]:
                self.list1.insert('end', j)
            self.list1.insert('end', '')
        #self.t0.pack()

    def lipeste(self): #Intoarce lista de ingrediente selectate
        L = [self.i1.get(), self.i2.get(), self.i3.get(), self.i4.get(), self.i5.get()]
        l = []
        for i in L:
            if i != '0':
                l.append(i)
        D = rf.ingrediente(l, ret)
        self.afis(D)

    def mancare(self): #Afiseaza Frame-ul 3
        self.f0.pack_forget()
        self.f2.pack()

    def ingrediente(self): #Afiseaza Frame-ul 2
        self.f0.pack_forget()
        self.f1.pack()

    def caut0(self): #Cauta reteta introdusa
        m = self.e2.get()
        w = rf.translate(m, ret, self.t2, self.f2)
        if w:
            self.t2.insert('0.0', w)

    def retur0(self): #Intoarce de la Frame-ul 3 la Frame-ul 1
        self.t2.pack_forget()
        self.f2.pack_forget()
        self.f0.pack()

    def retur(self): #Intoarce de la Frame-ul 2 la Frame-ul 1
        #self.t0.pack_forget()
        self.f1.pack_forget()
        self.list1.pack_forget()
        self.f0.pack()

    def reteta(self, n):
        for i in ret.keys():
            if i == n:
                self.t0.insert('end', ret[i])

ing = list(json.load(open(r"ingrediente.json"))) #lista de ingrediente
ret = json.load(open(r"retete.json")) #lista de retete

#Fereastra de baza
root = tk.Tk()
root.title("Retete")
R = interf(root)
root.mainloop()
