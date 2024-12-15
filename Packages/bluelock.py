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

    def Season2(self,update,context):
        update.massage.reply_test(
         """
        Season 2:
            Episode 1:  https://www.udlinks.com/ZQuO3j
            Episode 2:  https://www.udlinks.com/ZR76JfpC
            Episode 3:  https://www.udlinks.com/VrlXDF
            Episode 4:  https://www.udlinks.com/mWDxp
            Episode 5:  https://www.udlinks.com/IM28z
            Episode 6:  https://www.udlinks.com/KOUnrSwB
            Episode 7:  https://www.udlinks.com/eYWW
            Episode 8:  https://www.udlinks.com/GG6jL
            
        """
        )