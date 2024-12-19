from telegram.ext import Updater, CommandHandler

class Truebeauty:
    def _init_(self,Token):
        self.updater = Updater(Token)
        self.dispatcher = self.updater.dispatcher
        
        
    def Season1(self,update,context):
        update.message.reply_text(
        """ 
        season 1: 
            Episode 1:  https://www.udlinks.com/5ebEW
            Episode 2:  https://www.udlinks.com/oU0b59Y
            Episode 3:  https://www.udlinks.com/8ofL
            Episode 4:  https://www.udlinks.com/gqpMYF
            Episode 5:  https://www.udlinks.com/B6jn
            Episode 6:  https://www.udlinks.com/13Fkw
            Episode 7:  https://www.udlinks.com/bnnB
            Episode 8:  https://www.udlinks.com/QpFTp
            Episode 9:  https://www.udlinks.com/5bcmZr
            Episode 10: https://www.udlinks.com/cmoDM
            Episode 11: https://www.udlinks.com/CNV9
            Episode 12: https://www.udlinks.com/CjCVJ
            Episode 13: https://www.udlinks.com/eBoy
        """
        )

