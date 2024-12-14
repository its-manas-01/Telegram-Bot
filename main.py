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
    update.message.reply_text(
        """
        Welcome to Anime Hub.
        please type /anime for choosing your anime.
        """
        )

def anime(update, context):
    update.message.reply_text(
        """
        Anime Series:
        /Naruto->Naruto
        /NarutoShippuden->Naruto Shippuden
        /OnePunchMan->One Punch Man
        /DeathNote->Death Note
        /Bleach->Bleach
        /DragonBallZ->Dragon Ball Z
        /TowerofGod->Tower of God
        /Tokyorevengers->Tokyo  Revenge
        /BlueLock->Blue Lock
        /ThatTimeIgotReincarnatedasASlime->That Time I Got Reincarnated as a Slime
        /Blackclover->Black clover
        /TrueBeauty->True Beauty
        /NoLongerAllowedinAnotherWorld->No Longer Allowed in Another World
        /WDNRMITW->Why Does Nobody Remember Me in This World
        /SpyXFamily->Spy X Family
        /TheImmortalKing->The Immortal King
        /DrStone->Dr. Stone
        /365daysToTheWedding->365 days to  the Wedding
        /LogHorizen->Log Horizen
        /YouArMsServant->You ar Ms. Servant
        /DADADAN->DA DA DAN
        /soloLeveling->Solo Leveling
        /mashlemagicandmuscles->Mashle Magic and Mscles
        Anime Movies:
        /Iwanttoeatyourpancreas->I want to Eat Your Pancreas 
        """
        )


def Naruto(update, context):
    update.message.reply_text(
        """
        Naruto :
        """
        )


def NarutoShippuden(update, context):
    update.message.reply_text(
        """
        Naruto  Shippuden : 
        """
        )


def OnePunchMan(update, context):
    update.message.reply_text(
        """
        One Punch Man :
        """
        )


def DeathNote(update, context):
    update.message.reply_text(
        """
        Death Note :
        """
        )


def Bleach(update, context):
    update.message.reply_text(
        """
        Bleach :
        """
        )

def TowerofGod(update, context):
    update.message.reply_text(
        """ 
        Tower of God :
        """
        )


def Tokyorevengers(update, context):
    update.message.reply_text(
        """
        Tokyo  Revenge :
        """
        )
    
def BlueLock(update, context):
    update.message.reply_text(
        """ 
        Blue  Lock :
        """
        )
    
def ThatTimeIgotReincarnatedasASlime(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    

def DragonBallZ(update, context):
    update.message.reply_text("This anime will be avlible in next week.")

def Blackclover(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    

def TrueBeauty(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
    
def NoLongerAllowedinAnotherWorld(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
    
def WDNRMITW(update,context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
def SpyXFamily(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
def TheImmortalKing(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
def DrStone(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
def LogHorizen(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
def YouArMsServant(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
def soloLeveling(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
    
def daystotheWedding(update,context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
def DADADAN(update,context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
 
def mashlemagicandmuscles(update, context):
    update.message.reply_text(
        """
        Mashle Magic and Mscles : 
        season 1: 
            Episode 1:  https://en.shrinke.me/qv8RfvXT
            Episode 2:  https://www.udlinks.com/Z85IAVT
            Episode 3:  https://en.shrinke.me/DCMzB
            Episode 4:  https://en.shrinke.me/blR3e
            Episode 5:  https://www.udlinks.com/08St6y
            Episode 6:  https://www.udlinks.com/iJOGuo
            Episode 7:  https://www.udlinks.com/S6raAJLm
            Episode 8:  https://www.udlinks.com/AWqcyX0
            Episode 9:  https://www.udlinks.com/mFtD2IE
            Episode 10: https://en.mrproblogger.com/grolTV
            Episode 11: https://www.udlinks.com/ntyx
            Episode 12: https://en.mrproblogger.com/UA9RcSy
        season 2:
            Episode 1:  https://www.udlinks.com/VgYk
            Episode 2:  https://en.mrproblogger.com/OZn7
            Episode 3:  https://www.udlinks.com/wKldtJV
            Episode 4:  https://en.mrproblogger.com/Bxcc4Rbi
            Episode 5:  https://www.udlinks.com/hQ6BN
            Episode 6:  https://en.mrproblogger.com/9baR
            Episode 7:  https://www.udlinks.com/58vZzs
            Episode 8:  https://www.udlinks.com/xiG0F
            Episode 9:  https://www.udlinks.com/Lauta4
            Episode 10: https://en.mrproblogger.com/VI39eO
            Episode 11: https://en.mrproblogger.com/AsW3t2k
            Episode 12: https://www.udlinks.com/5Y2qys
        Mashle Magic and Mscles has been completed.
        Please wait for next season.
        If you want to watch other anime then click here 👉 /anime . 
        """
        )   


def Iwanttoeatyourpancreas(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
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
dispatcher.add_handler(CommandHandler('mashlemagicandmuscles', mashlemagicandmuscles))
dispatcher.add_handler(CommandHandler('Iwanttoeatyourpancreas', Iwanttoeatyourpancreas))



updater.start_polling()
updater.idle()