from telegram.ext import Updater, CommandHandler

class Sololeveling:
    def __init__(self,Token):
        self.updater = Updater(Token)
        self.dispatcher = self.updater.dispatcher
        
        
    def Season1(self,update,context):
        update.message.reply_text(
        """ 
        season 1: 
            Episode 1:  https://www.udlinks.com/ad34KQBY
            Episode 2:  https://www.udlinks.com/LZQll
            Episode 3:  https://www.udlinks.com/BNWvp406
            Episode 4:  https://www.udlinks.com/YvmSc0
            Episode 5:  https://www.udlinks.com/OHNPF
            Episode 6:  https://www.udlinks.com/RV90WL
            Episode 7:  https://www.udlinks.com/KyCXuvq
            Episode 8:  https://www.udlinks.com/S1jcpS6B
            Episode 9:  https://www.udlinks.com/OC37
            Episode 10: https://www.udlinks.com/bWsr
            Episode 11: https://www.udlinks.com/2u6v11
            Episode 12: https://www.udlinks.com/zBjJ
        """)
    