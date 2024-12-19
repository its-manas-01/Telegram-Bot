from telegram.ext import Updater, CommandHandler

class Rezero:
    def __init__(self,Token):
        self.updater = Updater(Token)
        self.dispatcher = self.updater.dispatcher
        
        
    def Season1(self,update,context):
        update.message.reply_text(
        """ 
        season 1: 
            Episode 1:  https://www.udlinks.com/5vDvOtZ
            Episode 2:  https://www.udlinks.com/IILN4hFS
            Episode 3:  https://www.udlinks.com/o0wQ
            Episode 4:  https://www.udlinks.com/SXp0X6A
        """
        )
    