from telegram import InlineKeyboardButton
ikb = InlineKeyboardButton


def user(id):
    admins = [666147669]
    friends = []
    if admins.count(id):
        return "admin"
    elif friends.count(id):
        return "friend"
    else:
        return None



def serv_mrwn_power():
    return


class Keyboards:
    @staticmethod
    def help_but():
        help_but = [
            [
                ikb('🔙', callback_data='main')
            ],
            [
                ikb("Password's", callback_data='passwords')
            ]
        ]
        return help_but

    @staticmethod
    def start(id):
        if user(id) == "admin":
            text = 'Speedrun for tic-tac-toe:'
            start = [
                [
                    ikb("Enter to the game!", callback_data='game')
                ],
                [
                    ikb("Help", callback_data='help')
                ]
            ]
        else:
            text = "Who are you?"
            start = [
                [
                    ikb("If u think, uoy need permission - text to me (in direct)", callback_data='none')
                ]
            ]
        return text, start

    @staticmethod
    def home():
        home = [
            [ikb("🏠", callback_data="main")],
        ]
        return home

    @staticmethod
    def serv():
        serv = [
            [
                ikb('MRWN', callback_data="serv_mrwn"),
                ikb('Statistic', callback_data="serv_statistic")
            ],
            [
                ikb('🔙', callback_data='main')
            ]
        ]
        return serv