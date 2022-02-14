#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://git.io/JOmFw.
"""
import logging
import requests
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from tg_keyboards import Keyboards

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

    # ------### Telegram logic ###------
class Telega:
    @staticmethod
    def start(update: Update, context: CallbackContext) -> None:
        n = update.message.from_user
        update.message.reply_text(Keyboards.start(n.id)[0], reply_markup=InlineKeyboardMarkup(Keyboards.start(n.id)[1]))

    @staticmethod
    def menu(update: Update, context: CallbackContext) -> None:
        n = update.effective_chat
        update.callback_query.message.edit_text(Keyboards.start(n.id)[0],
                                                reply_markup=InlineKeyboardMarkup(Keyboards.start(n.id)[1]))
    @staticmethod
    def button(update: Update, context: CallbackContext) -> None:
        """Parses the CallbackQuery and updates the message text."""
        query = update.callback_query
        ikb = InlineKeyboardMarkup
        qd = query.data
        qe = query.edit_message_text
        n = update.effective_chat
        # CallbackQueries need to be answered, even if no notification to the user is needed
        # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
        query.answer()
        if qd == "pc":
            qe(text="PC Menu", reply_markup=ikb(Keyboards.pc()))
        elif qd == "pc_log":
            qe(text="PC Menu", reply_markup=ikb(Keyboards.pc()))
        elif qd == "help":
            qe(text=Keyboards.help(n.id), reply_markup=ikb(Keyboards.help_but()))
        elif qd == "main":
            Telega.menu(update, context)

    @staticmethod
    def help_command(update: Update, context: CallbackContext) -> None:
        """Displays info on how to use the bot."""
        update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("922716285:AAHHR8bX97EbFRmQdxazwmjmsaHSS4X95D4")

    updater.dispatcher.add_handler(CommandHandler('start', Telega.start))
    updater.dispatcher.add_handler(CallbackQueryHandler(Telega.button))
    updater.dispatcher.add_handler(CommandHandler('notificate', Telega.notificate))
    updater.dispatcher.add_handler(CommandHandler('help', Telega.help_command))

    # Start the Bot
    updater.start_polling()
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
