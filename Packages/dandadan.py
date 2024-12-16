from telegram.ext import Updater, CommandHandler

class Dandadan:
    def __init__(self,Token):
        self.updater = Updater(Token)
        self.dispatcher = self.updater.dispatcher
        
        
    def Season1(self,update,context):
        update.message.reply_text(
        """
        DAN DA DAN:
        season 1:
            Episode 1:  https://www.udlinks.com/iLb6N4
            Episode 2:  https://www.udlinks.com/64On33
            Episode 3:  https://www.udlinks.com/jD6bjq
            Episode 4:  https://www.udlinks.com/bF2Y2t
            Episode 5:  https://en.mrproblogger.com/lUSMMRiZ
            Episode 6:  https://en.mrproblogger.com/pry5X
            Episode 7:  https://en.mrproblogger.com/SSpS
            Episode 8:  https://en.mrproblogger.com/C7EOMV
            Episode 9:  https://www.udlinks.com/BA7yX
        Next Episode will be avliable in Friday.
        If you want to watch other anime then click here 👉 /anime . 
        """
        )