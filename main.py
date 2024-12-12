from telegram.ext import Updater, CommandHandler
# from Packages import ognaruto

Token = "7918358947:AAEMO-d_oEjrBkvnBBTFyK286Zdw8b0z27w"

updater = Updater("7918358947:AAEMO-d_oEjrBkvnBBTFyK286Zdw8b0z27w",use_context=True)
dispatcher = updater.dispatcher

# n= ognaruto()

def help(update, context):
    update.message.reply_text(
        """
        /start ->welcome to anime Hub
        /help -> shows this help message
    
        /anime -> lists anime series
        """
    )


def start(update, context):
    update.message.reply_text("Welcome to Anime Hub.")

def anime(update, context):
    update.message.reply_text(
        """
        Anime Series:
            /Naruto->1.Naruto
            /NarutoShippuden->2.Naruto Shippuden
            /OnePunchMan->3.  One Punch Man
            /DeathNote->4.  Death Note
            /Bleach->5.  Bleach
            /DragonBallZ->6.  Dragon Ball Z
            /TowerofGod->7.  Tower of God
            /Tokyorevengers->8.  Tokyo  Revenge
            /BlueLock->9.  Blue Lock
            /ThatTimeIgotReincarnatedasASlime->10. That Time I Got Reincarnated as a Slime
            /Blackclover->11. Black clover
            /TrueBeauty->12. True Beauty
            /NoLongerAllowedinAnotherWorld->13. No Longer Allowed in Another World
            /WDNRMITW->14. Why Does Nobody Remember Me in This World
            /SpyXFamily->15. Spy X Family
            /TheImmortalKing->16. The Immortal King
            /DrStone->17. Dr. Stone
            /365daysToTheWedding->18. 365 days to  the Wedding
            /LogHorizen->19. Log Horizen
            /YouArMsServant->20. You ar Ms. Servant
            /DADADAN->21. DA DA DAN
            /soloLeveling->22. Solo Leveling
        """
        )


def Naruto(update, context):
    update.message.reply_text("Naruto : https://shrinkme.ink/UGjkA")


def NarutoShippuden(update, context):
    update.message.reply_text(" Naruto  Shippuden : https://shrinkme.ink/a71PD")


def OnePunchMan(update, context):
    update.message.reply_text(" One Punch Man :https://en.mrproblogger.com/sF8t")


def DeathNote(update, context):
    update.message.reply_text("Death Note : https://en.mrproblogger.com/QBzRh")


def Bleach(update, context):
    update.message.reply_text(" Bleach : https://en.shrinke.me/G8zS")

def TowerofGod(update, context):
    update.message.reply_text(" Tower   of God : https://shrinkme.ink/jJJxQx")


def Tokyorevengers(update, context):
    update.message.reply_text(" Tokyo  Revenge :https://shrinkme.ink/RtbcOeAr")
    
def BlueLock(update, context):
    update.message.reply_text(" Blue  Lock : https://shrinkme.ink/w801")
    
def ThatTimeIgotReincarnatedasASlime(update, context):
    update.message.reply_text("This anime will be avlible in next week.")
    

def DragonBallZ(update, context):
    update.message.reply_text("This anime will be avlible in next week.")

def Blackclover(update, context):
    update.message.reply_text("This anime will be avlible in next week.")
    

def TrueBeauty(update, context):
    update.message.reply_text("This anime will be avlible in next week.")
    
    
def NoLongerAllowedinAnotherWorld(update, context):
    update.message.reply_text("This anime will be avlible in next week.")
    
    
def WDNRMITW(update,context):
    update.message.reply_text("This anime will be avlible in next week.")
    
    
def SpyXFamily(update, context):
    update.message.reply_text("This anime will be avlible in next week.")
    
    
def TheImmortalKing(update, context):
    update.message.reply_text("This anime will be avlible in next week.")
    
    
def DrStone(update, context):
    update.message.reply_text("This anime will be avlible in next week.")
    
    
def LogHorizen(update, context):
    update.message.reply_text("This anime will be avlible in next week.")
    
    
def YouArMsServant(update, context):
    update.message.reply_text("This anime will be avlible in next week.")
    
    
def soloLeveling(update, context):
    update.message.reply_text("This anime will be avlible in next week.")
    
    
    
def daystotheWedding(update,context):
    update.message.reply_text("This anime will be avlible in next week.")
    
    
def DADADAN(update,context):
    update.message.reply_text("This anime will be avlible in next week.")
    
    

    
    
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('anime', anime))
dispatcher.add_handler(CommandHandler('Naruto', Naruto))
dispatcher.add_handler(CommandHandler('NarutoShippuden', NarutoShippuden))
dispatcher.add_handler(CommandHandler('OnePunchMan', OnePunchMan))
dispatcher.add_handler(CommandHandler('DeathNote', DeathNote))
dispatcher.add_handler(CommandHandler('Bleach', Bleach))
dispatcher.add_handler(CommandHandler('TowerofGod', TowerofGod))
dispatcher.add_handler(CommandHandler('Tokyorevengers', Tokyorevengers))
dispatcher.add_handler(CommandHandler('BlueLock',BlueLock))
dispatcher.add_handler(CommandHandler('ThatTimeIgotReincarnatedasASlime',ThatTimeIgotReincarnatedasASlime))
dispatcher.add_handler(CommandHandler('DragonBallZ', DragonBallZ))
dispatcher.add_handler(CommandHandler('Blackclover', Blackclover))
dispatcher.add_handler(CommandHandler('TrueBeauty', TrueBeauty))
dispatcher.add_handler(CommandHandler('NoLongerAllowedinAnotherWorld', NoLongerAllowedinAnotherWorld))
dispatcher.add_handler(CommandHandler('WDNRMITW', WDNRMITW))
dispatcher.add_handler(CommandHandler('SpyXFamily', SpyXFamily))
dispatcher.add_handler(CommandHandler('TheImmortalKing', TheImmortalKing))
dispatcher.add_handler(CommandHandler('DrStone', DrStone))
dispatcher.add_handler(CommandHandler('LogHorizen', LogHorizen))
dispatcher.add_handler(CommandHandler('YouArMsServant', YouArMsServant))
dispatcher.add_handler(CommandHandler('365daysToTheWedding', daystotheWedding))
dispatcher.add_handler(CommandHandler('SoloLeveling', soloLeveling))
dispatcher.add_handler(CommandHandler('DADADAN', DADADAN))

updater.start_polling()
updater.idle()