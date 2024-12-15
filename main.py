from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os
from Packages.naruto import *


load_dotenv()
Token = os.getenv("Token")

updater = Updater(Token,use_context=True)
dispatcher = updater.dispatcher

naruto= ognaruto(Token)

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
        /DANDADAN->DAN DA DAN
        /soloLeveling->Solo Leveling
        /mashlemagicandmuscles->Mashle Magic and Mscles
        Anime Movies:
        /Iwanttoeatyourpancreas->I want to Eat Your Pancreas 
        /spyxfamilycodewhite-> Spy x Family: Code White
        """
        )


def Naruto(update, context):
    naruto.Sesaon1(update,context)


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
        Season 1:
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
            Episode 13:
            Episode 14:
            Episode 15:
            Episode 16:
            Episode 17:
            Episode 18:
            Episode 19:
            Episode 20:
            Episode 21:
            Episode 22:
            Episode 23:
            Episode 24:
        Season 2:
            Episode 1:
            Episode 2:
            Episode 3:
            Episode 4:
            Episode 5:
            Episode 6:
            Episode 7:
            Episode 8:
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
        This anime will be avliable in next week.
        """
        )
    
def DANDADAN(update,context):
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

# Mashle Magic and Mscles completed.

def Iwanttoeatyourpancreas(update, context):
    update.message.reply_text(
        """
        I want to Eat Your Pancreas: https://www.udlinks.com/h24n6L
        """
        )
    
#  I want to Eat Your Pancreas completed.    
    
def spyxfamilycodewhite(update,context):
    update.message.reply_text(
        """
        SpyX Family Code White: https://www.udlinks.com/RieCpR6
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
dispatcher.add_handler(CommandHandler('DANDADAN', DANDADAN))
dispatcher.add_handler(CommandHandler('mashlemagicandmuscles', mashlemagicandmuscles))
dispatcher.add_handler(CommandHandler('Iwanttoeatyourpancreas', Iwanttoeatyourpancreas))
dispatcher.add_handler(CommandHandler('spyxfamilycodewhite',spyxfamilycodewhite))



updater.start_polling()
updater.idle()