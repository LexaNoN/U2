from telegram import InlineKeyboardButton
from os import walk
ikb = InlineKeyboardButton


class Keyboards:
    @staticmethod
    def start():
        text = 'Welcome to Tic Tac Toe!'
        start = [
            [
                ikb("GAME!", callback_data='game'),
                ikb("Single", callback_data="single")
            ],
            [
                ikb("⚙️", callback_data='sett')
            ]
        ]
        return text, start

    @staticmethod
    def transform(string):
        string = str(string)
        string = string.replace("[", "")
        string = string.replace("]", "")
        string = string.replace("'", "")
        string = string.replace(",", "")
        string = string.replace(" ", "")
        return string

    @staticmethod
    def keyb(trust, table):
        pos = []
        for i in table:
            x = ""
            if i == "1":
                x = "❌"
            elif i == "2":
                x = "⭕"
            elif i == "0":
                x = '◻️'
            else:
                x = i
            pos.append(x)
        table = Keyboards.transform(table)
        keyb = [
            [
                ikb(pos[0], callback_data=trust + ":" + "1" + table),
                ikb(pos[1], callback_data=trust + ":" + "2" + table),
                ikb(pos[2], callback_data=trust + ":" + "3" + table),
            ],
            [
                ikb(pos[3], callback_data=trust + ":" + "4" + table),
                ikb(pos[4], callback_data=trust + ":" + "5" + table),
                ikb(pos[5], callback_data=trust + ":" + "6" + table),
            ],
            [
                ikb(pos[6], callback_data=trust + ":" + "7" + table),
                ikb(pos[7], callback_data=trust + ":" + "8" + table),
                ikb(pos[8], callback_data=trust + ":" + "9" + table),
            ],
            [
                ikb("🏠", callback_data="main")
            ]
        ]
        return keyb


    @staticmethod
    def home():
        home = [
            [ikb("🏠", callback_data="main")],
        ]
        return home

"""elif ep_end == 1:
            keyb = [
                [ikb(pos[] + p5), callback_data=trust + ":" + p5)]
            ]
            pass

        elif ep_end == 0:
            pass
        """
