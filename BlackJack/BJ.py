import tkinter as tk
from PIL import ImageTk, Image
import random
import os
import re
import json

class BJ:
    __deck = {}
    __restore = {}
    __P = {}
    __p_val = 0
    __D = {}
    __d_val = 0
    __pas = 0
    __pah = 0
    __pad = 0
    __pac = 0
    __das = 0
    __dah = 0
    __dad = 0
    __dac = 0

    def __init__(self):
        BJ.__create_deck(self)
        try:
            with open('deck.json') as json_file:
                BJ.__deck = json.load(json_file)
        except:
            print("ups")
        BJ.__restore = BJ.__deck.copy()

    def start(self):
        for _ in range(0, 2):
            c = random.choice(list(BJ.__deck.keys()))
            BJ.__P[c] = BJ.__deck[c]
            BJ.__p_val += BJ.__P[c][1]
            BJ.__deck.pop(c)

        c = random.choice(list(BJ.__deck.keys()))
        BJ.__D[c] = BJ.__deck[c]
        BJ.__d_val += BJ.__D[c][1]
        BJ.__deck.pop(c)

        if BJ.__p_val > 21:
            BJ.__check_ace_player(self)

        if BJ.__d_val > 21:
            BJ.__check_ace_dealer(self)

        print(BJ.__P)
        print(BJ.__p_val)
        print(BJ.__D)
        print(BJ.__d_val)
        print(BJ.__deck)
        return [BJ.__P, BJ.__p_val, BJ.__D, BJ.__d_val, BJ.__deck]

    def hit(self, deck):
        c = random.choice(list(deck.keys()))
        BJ.__P[c] = BJ.__deck[c]
        BJ.__p_val += BJ.__P[c][1]
        deck.pop(c)
        # if BJ.__p_val > 21:
        #     if BJ.__ace_check_player(self) == 1:
        #         BJ.__pb = 1
        #         return [BJ.__P, 0, deck, c]
        # return [BJ.__P, BJ.__p_val, deck, c]
        while BJ.__p_val > 21:
            if BJ.__ace_check_player(self) == 1:
                BJ.__pb = 1
                return [BJ.__P, 0, deck, c]
        print(BJ.__p_val)
        return [BJ.__P, BJ.__p_val, deck, c]

    def stay(self, deck):
        db = 0
        D_temp = {}
        while BJ.__d_val <= 17:
            print(BJ.__d_val)
            c = random.choice(list(deck.keys()))
            print(c)
            D_temp[c] = BJ.__deck[c]
            BJ.__d_val += D_temp[c][1]
            BJ.__deck.pop(c)
            print(BJ.__d_val)
            # if BJ.__d_val > 21:
            #     if BJ.__ace_check_dealer(self) == 1:
            #         db = 1
            #         print("Bust")
            #         break
            while BJ.__d_val > 21:
                if BJ.__ace_check_dealer(self) == 1:
                    db = 1
                    print("Bust")
                    break
        return [D_temp, BJ.__d_val, db]

    def __create_deck(self):
        directory = r'PNG'
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            card = re.split(".p|G.", f)[1]
            number = '0'
            for i in list(card):
                if i.isdigit():
                    number += i
                elif i == 'A' or i == 'K' or i == 'Q' or i == 'J':
                    number += i
                    break
            if number.isdigit():
                number = int(number)
            elif number == '0K' or number == '0Q' or number == '0J':
                number = 10
            elif number == '0A':
                number = 11
            # print(__number)
            # print(__card)
            # print(__f)
            # print(__number)
            if os.path.isfile(f):
                BJ.__deck[card] = [f, number]
        try:
            with open('deck.json', 'w') as f:
                json.dump(BJ.__deck, f)
        except:
            pass
        BJ.__deck.clear()

    def img(self, img, type):
        if type == 0:
            img = Image.open(img)
            img = img.resize((500, 300))  # (500, 300)
            img = ImageTk.PhotoImage(img)
        else:
            img = Image.open(img)
            img = img.resize((200, 270))  # (500, 300)
            img = ImageTk.PhotoImage(img)
        return img

    def restart(self):
        BJ.__deck.clear()
        BJ.__deck = BJ.__restore.copy()
        BJ.__P.clear()
        BJ.__p_val = 0
        BJ.__pb = 0
        BJ.__D.clear()
        BJ.__d_val = 0
        BJ.__db = 0
        BJ.__pas = 0
        BJ.__pah = 0
        BJ.__pad = 0
        BJ.__pac = 0
        BJ.__das = 0
        BJ.__dah = 0
        BJ.__dad = 0
        BJ.__dac = 0

    def __ace_check_player(self):
        print(list(BJ.__P.keys()))
        print(BJ.__pas, BJ.__pah, BJ.__pad, BJ.__pac)
        if 'AS' in list(BJ.__P.keys()) and BJ.__pas == 0:
            BJ.__p_val -= 10
            BJ.__pas = 1
            return 0
        if 'AH' in list(BJ.__P.keys()) and BJ.__pah == 0:
            BJ.__p_val -= 10
            BJ.__pah = 1
            return 0
        if 'AD' in list(BJ.__P.keys()) and BJ.__pad == 0:
            BJ.__p_val -= 10
            BJ.__pad = 1
            return 0
        if 'AC' in list(BJ.__P.keys()) and BJ.__pac == 0:
            BJ.__p_val -= 10
            BJ.__pac = 1
            return 0

        return 1

    def __ace_check_dealer(self):
        print(list(BJ.__D.keys()))
        print(BJ.__das, BJ.__dah, BJ.__dad, BJ.__dac)
        if 'AS' in list(BJ.__D.keys()) and BJ.__das == 0:
            BJ.__d_val -= 10
            BJ.__das = 1
            return 0
        if 'AH' in list(BJ.__D.keys()) and BJ.__dah == 0:
            BJ.__d_val -= 10
            BJ.__dah = 1
            return 0
        if 'AD' in list(BJ.__D.keys()) and BJ.__dad == 0:
            BJ.__d_val -= 10
            BJ.__dad = 1
            return 0
        if 'AC' in list(BJ.__D.keys()) and BJ.__dac == 0:
            BJ.__d_val -= 10
            BJ.__dac = 1
            return 0
        
        return 1

bj = BJ()
