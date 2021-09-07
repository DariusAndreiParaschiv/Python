#pylint: disable = import-error
import tkinter as tk
import random
import os
from BJ import BJ
import json
  
class Game:
    __menu = None
    __game = None
    __bj = BJ()
    __deck = None
    __P = {}
    __PI = []
    __p_hand = None
    __p_val = 0
    __D = {}
    __DI = []
    __d_hand = None
    __d_val = 0
    __optiuni = None
    __scor = None
    __rezultat = None
    __valoare = None
    __back_nou = None
    __again = None
    __hit = None
    __stay = None
    
    def __init__(self, root):
        s = Game.__bj.img(r'ALT_PNG\aces.png', 0)
        Game.__menu = tk.Frame(root)
        Game.__menu.pack(side='top')
        title = tk.Label(Game.__menu, text = 'BlackJack', font = 'Helvetica 70')
        title.pack(side = 'top')
        logo = tk.Label(Game.__menu, image=s)
        logo.image = s
        logo.pack(side = 'top')
        play = tk.Button(Game.__menu, text="Play", font='Helvetica 30', padx=50, pady=20, command=lambda: Game.__Game(self, root))
        play.pack(side = 'top')
        quit = tk.Button(Game.__menu, text="Quit", font='Helvetica 30', padx=50, pady=20, command=root.destroy)
        quit.pack(side='top')

    def hit(self, root):
        print('hit pressed')
        temp = Game.__bj.hit(Game.__deck)
        Game.__P = temp[0].copy()
        Game.__p_val = temp[1]
        Game.__valoare.set(str(Game.__p_val))
        card = temp[3]
        print(card)
        Game.__deck = temp[2].copy()
        img = Game.__bj.img(Game.__P[card][0], 1)
        img_nou = tk.Label(Game.__p_hand, image=img)
        img_nou.image = img
        img_nou.pack(side='left')
        Game.__valoare.set("Your hand is %s" % Game.__p_val)
        if Game.__p_val == 0:
            Game.__valoare.set("Busted")
            Game.stay(self, root, 1)
    
    def stay(self, root, pb):
        Game.__hit["state"] = "disabled"
        Game.__stay["state"] = "disabled"
        Game.__back_nou.pack_forget()
        temp = Game.__bj.stay(Game.__deck)
        Game.__D = temp[0].copy()
        Game.__d_val = temp[1]
        for card in Game.__D:
            img = Game.__bj.img(Game.__D[card][0], 1)
            img_nou = tk.Label(Game.__d_hand, image=img)
            img_nou.image = img
            img_nou.pack(side='left')
        db = temp[2]
        if pb == 1:
            print("D")
            Game.__valoare.set("Dealer wins!")
            Game.__rezultat.pack()
        if db == 1 and pb == 0:
            print("P")
            Game.__valoare.set("Player wins!")
            Game.__rezultat.pack()
        if pb == 0 and db == 0 and Game.__d_val > Game.__p_val:
            print("D")
            Game.__valoare.set("Dealer wins!")
            Game.__rezultat.pack()
        if pb == 0 and db == 0 and Game.__p_val > Game.__d_val:
            print("P")
            Game.__valoare.set("Player wins!")
            Game.__rezultat.pack()
        if pb == 0 and db == 0 and Game.__p_val == Game.__d_val:
            print("Tie")
            Game.__valoare.set("Draw")
            Game.__rezultat.pack()
        Game.__again.pack(side='right')
        
    def __restart(self, root):
        for card in Game.__PI:
            print(card)
            card.pack_forget()
        for card in Game.__DI:
            card.pack_forget()
        Game.__PI.clear()
        Game.__DI.clear()
        Game.__game.pack_forget()
        Game.__d_hand.pack_forget()
        Game.__p_hand.pack_forget()
        Game.__P.clear()
        Game.__D.clear()
        Game.__p_val = 0
        Game.__d_val = 0
        print("circ")
        print(Game.__PI, Game.__P)
        Game.__bj.restart()
        Game.__Game(self, root)

    def __Game(self, root):
        Game.__menu.pack_forget()
        Game.__game = tk.Frame(root)
        Game.__game.pack(side='top')
        dealer = tk.Label(Game.__game, text='Dealer', font='Helvetica 30')
        dealer.pack(side='top')
        Game.__d_hand = tk.Frame(Game.__game)
        Game.__d_hand.pack(side='top')
        temp = Game.__bj.start()
        Game.__P = temp[0].copy()
        Game.__p_val = temp[1]
        Game.__D = temp[2].copy()
        Game.__d_val = temp[3]
        Game.__deck = temp[4]
        print('')
        print('')
        print('')
        print('Main')
        print(Game.__P)
        print(Game.__p_val)
        print(Game.__D)
        print(Game.__d_val)
        print(Game.__deck)
        Game.__valoare = tk.StringVar()
        Game.__valoare.set("Your hand is %s" %Game.__p_val)
        Game.__scor = tk.Label(
            Game.__game, textvariable=Game.__valoare)
        Game.__scor.pack(side='top')
        Game.__rez = tk.StringVar()
        Game.__rezultat = tk.Label(
            Game.__game, textvariable=Game.__rez)
        Game.__optiuni = tk.Frame(Game.__game)
        Game.__optiuni.pack(side='top')
        Game.__p_hand = tk.Frame(Game.__game)
        Game.__p_hand.pack(side='bottom')
        player = tk.Label(Game.__game, text='Player', font='Helvetica 30')
        player.pack(side='bottom')
        for card in Game.__P:
            img = Game.__bj.img(Game.__P[card][0], 1)
            img_nou = tk.Label(Game.__p_hand, image=img)
            img_nou.image = img
            img_nou.pack(side='left')
            Game.__PI.append(img_nou)
            print('p card', card)
        print(Game.__PI)
        for card in Game.__D:
            img = Game.__bj.img(Game.__D[card][0], 1)
            img_nou = tk.Label(Game.__d_hand, image=img)
            img_nou.image = img
            img_nou.pack(side='left')
            Game.__DI.append(img_nou)
            print('d card', card)
        back = Game.__bj.img("ALT_PNG\\blue_back.png", 1)
        Game.__back_nou = tk.Label(Game.__d_hand, image=back)
        Game.__back_nou.image = back
        Game.__back_nou.pack(side='left')
        print('ok afis')
        Game.__hit = tk.Button(Game.__optiuni, text="Hit", font='Helvetica 15',
                        padx=30, pady=5, command=lambda: Game.hit(self, root))
        Game.__hit.pack(side = 'left')
        Game.__stay = tk.Button(Game.__optiuni, text="Stay", font='Helvetica 15',
                         padx=30, pady=5, command=lambda: Game.stay(self, root, 0))
        Game.__stay.pack(side='right')
        Game.__again = tk.Button(Game.__optiuni, text="Play again!", font='Helvetica 15',
                         padx=30, pady=5, command=lambda: Game.__restart(self, root))



root = tk.Tk()
root.title("BlackJack")
root.geometry('1500x900')
page = Game(root)
root.mainloop()
