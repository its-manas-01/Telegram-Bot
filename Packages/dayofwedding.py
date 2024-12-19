from telegram.ext import Updater, CommandHandler

class Dayofwedding:
    def __init__(self,Token):
        self.updater = Updater(Token)
        self.dispatcher = self.updater.dispatcher
        
        
    def Season1(self,update,context):
        update.message.reply_text(
        """ 
        season 1: 
            Episode 1:  https://www.udlinks.com/D1t1el
            Episode 2:  https://www.udlinks.com/dUiF
            Episode 3:  https://www.udlinks.com/95Th
            Episode 4:  https://www.udlinks.com/mdOHo
            Episode 5:  https://www.udlinks.com/2x5M
            Episode 6:  https://www.udlinks.com/kXEgc
            Episode 7:  https://www.udlinks.com/CHV3Phi7
            Episode 8:  https://www.udlinks.com/mpr3Qg 
        """
        )