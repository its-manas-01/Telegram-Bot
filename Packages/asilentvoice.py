from telegram.ext import Updater, CommandHandler

class Dayofwedding:
    def _init_(self,Token):
        self.updater = Updater(Token)
        self.dispatcher = self.updater.dispatcher
        
        
    def Season1(self,update,context):
        update.message.reply_text(
        """ 
        season 1: 
            Episode 1:  
            Episode 2:  
            Episode 3:  
            Episode 4:  
            Episode 5:  
            Episode 6:  
            Episode 7:  
            Episode 8:  
            Episode 9:  
            Episode 10: 
            Episode 11: 
            Episode 12: 
        """)
    def Season2(self,update,context):
        update.message.reply_text(
        """
        season 2:
            Episode 1:  
            Episode 2:  
            Episode 3:  
            Episode 4:  
            Episode 5:  
            Episode 6:  
            Episode 7:  
            Episode 8:  
            Episode 9:  
            Episode 10: 
            Episode 11: 
            Episode 12:
        """
        )