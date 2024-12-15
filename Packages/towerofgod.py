from telegram.ext import Updater, CommandHandler

class towerofgod:
    def __init__(self,Token):
        self.updater = Updater(Token)
        self.dispatcher = self.updater.dispatcher