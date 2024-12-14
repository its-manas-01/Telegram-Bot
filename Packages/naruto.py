from telegram.ext import Updater, CommandHandler

class ognaruto:
    def __init__(self,Token):
        self.updater = Updater(Token)
        self.dispatcher = self.updater.dispatcher
        
    def Sesaon1(self,update, context):
        update.message.reply_text("Naruto : https://shrinkme.ink/UGjkA")       
        
    # def naruto1(self,update, context):
    #     update.message.reply_text(
    #         """/Sesaon1-> Sesaon1"""
    #     )
    #     self.dispatcher.add_handler(CommandHandler('Sesaon1',Sesaon1))
    #     def Sesaon1(self,update, context):
    #         update.message.reply_text("Naruto : https://shrinkme.ink/UGjkA")  
       