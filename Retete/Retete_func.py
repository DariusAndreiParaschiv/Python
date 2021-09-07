from difflib import get_close_matches
import tkinter as tk

class RF:

    def __init__(self):
        print("Init")

    def ingrediente(self, l, data): #Modifica lista de retete astfel incat sa indice ingredientele lipsa
        c = list(data.keys())
        d = {}
        for i in c:
            if all(el in data[i] for el in l):
                d[i] = []
                for j in data[i]:
                    if j in l:
                        d[i].append(j)
                    else:
                        d[i].append(j + '*')
        for i in d:
            d[i] = d[i][0 : (len(d[i]) - 1)]
        return d

    def yes(self, W, q, t): #daca apasa da la translate
        t.pack()
        yn.pack_forget()
        y.pack_forget()
        n.pack_forget()
        t.delete('0.0', 'end')
        t.insert('end', W + "\n")
        t.insert('end', "\n" + "Ingrediente:")
        for i in range(len(q) - 1):
            t.insert('end', '\n')
            t.insert('end', q[i])
        t.insert('end', "\n"+ "\n" + "Mod de preparare:" + "\n" + q[len(q) - 1])

    def no(self, t): #daca apasa nu la translate
        t.pack()
        yn.pack_forget()
        y.pack_forget()
        n.pack_forget()
        t.delete('0.0', 'end')
        t.insert('0.0', "Reteta nu exista.")

    def translate(self, w, data, t2, f2): #verifica daca cuvantul introdus apare in lista de retete
        global yn
        global y
        global n
        w = w.lower()
        if type(data) == dict:
            if w in data:
                t2.pack()
                t2.delete('0.0', 'end')
                t2.insert('end', w + "\n")
                t2.insert('end', "\n" + "Ingrediente:")
                for i in range(len(data[w]) - 1):
                    t2.insert('end', '\n')
                    t2.insert('end', data[w][i])
                t2.insert('end', "\n" + "\n" + "Mod de preparare:" + "\n" + data[w][len(data[w]) - 1])

            elif len(get_close_matches(w, data.keys())) > 0: # aici cauta varianta cea mai apropiata de cuvantul introdus
                t2.pack_forget()
                W = get_close_matches(w, data.keys())[0]
                yn = tk.Label(f2, text = "Voiati sa scrieti %s?" %W)
                yn.pack()
                y = tk.Button(f2, text = "Da", command = lambda: self.yes(W, data[W], t2))
                y.pack()
                n = tk.Button(f2, text = "Nu", command = lambda : self.no(t2))
                n.pack()
            else:
                t2.delete('0.0', 'end')
                return "Reteta nu exista"