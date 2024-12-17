from telegram.ext import Updater, CommandHandler

class Spyxfamily:
    def __init__(self,Token):
        self.updater = Updater(Token)
        self.dispatcher = self.updater.dispatcher


    def Season1(self,update,context):
       update.message.reply_text(
        """
        Season 1:
            Episode 1:   https://www.udlinks.com/mrfb
            Episode 2:   https://www.udlinks.com/Qmmu0w
            Episode 3:   https://www.udlinks.com/yvnM
            Episode 4:   
            Episode 5:   
            Episode 6:   
            Episode 7:   
            Episode 8:   
            Episode 9:   
            Episode 10:   
            Episode 11:   
            Episode 12:   
            Episode 13:   
            Episode 14:   
            Episode 15:   
            Episode 16:   
            Episode 17:   
            Episode 18:   
            Episode 19:   
            Episode 20:   
            Episode 21:   
            
        

        """
        )
       