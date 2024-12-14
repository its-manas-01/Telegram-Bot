from telegram.ext import Updater, CommandHandler

class ognaruto:
    def __init__(self,Token):
        self.updater = Updater(Token)
        self.dispatcher = self.updater.dispatcher
        
    # def Sesaon1(self,update, context):
    #     update.message.reply_text("Naruto : https://shrinkme.ink/UGjkA")       
        
    def naruto1(self,update, context):
        update.message.reply_text(
            """/sesaon1-> sesaon1"""
        )
        def Sesaon1(self,update, context):
            update.message.reply_text("Naruto : https://shrinkme.ink/UGjkA")  
        self.dispatcher.add_handler(CommandHandler('sesaon1',Sesaon1))