from telegram.ext import Updater, CommandHandler

class bluelock:
    def __init__(self,Token):
        self.updater = Updater(Token)
        self.dispatcher = self.updater.dispatcher
        
        
    def season1(self,update,context):
        update.message.reply_test(
        """
        Season 1:
            Episode 1:
        """
        )