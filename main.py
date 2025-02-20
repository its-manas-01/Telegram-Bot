from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os
from Packages.naruto import *
from Packages.towerofgod import *
from Packages.bluelock import *
from Packages.mashlemagicandmuscles import *
from Packages.dandadan import *
from Packages.Spyxfamily import *
from Packages.rezero import *
from Packages.dayofwedding import *
from Packages.blackclover import *
from Packages.thatTimeIgotReincarnatedasASlime import *
from Packages.tokyorevenge import *
from Packages.truebeauty import *
from Packages.sololeveling import *
from Packages.loghorizen import *
from Packages.thedailylifeofimmortalking import *

load_dotenv()
Token = os.getenv("Token")

updater = Updater(Token,use_context=True)
dispatcher = updater.dispatcher

naruto= ognaruto(Token)
blulock = bluelock(Token)
towerofgod = Towerofgod(Token)
mashlemagicandmuscles = Mashlemagicandmuscles(Token)
dandadan = Dandadan(Token)
spyxfamily = Spyxfamily(Token)
dayofwedding = Dayofwedding(Token)
rezero = Rezero(Token)
blackclover = BlackClover(Token)
thatTimeIgotReincarnatedasASlime = ThattimeIgotreincarnatedasAslime(Token)

truebeauty = Truebeauty(Token)
soloLeveling = Sololeveling(Token)
loghorizen = Loghorizen(Token)
thedailylifeofimmortalking = ThedailylifeofimmortalKing(Token)
tokyorevengers = TokyoRevengers(Token)


def help(update, context):
    update.message.reply_text(
        """
        /start ->welcome to anime Hub
        /help -> shows this help message
        /anime -> lists anime series
        /contactus -> For contact the owner.
        """
    )


def start(update, context):
    update.message.reply_text(
        """
        Welcome to Anime Hub.
        please type /anime for choosing your anime.
        please type /help for help.
        """
        )

def contactus(update, context):
    update.message.reply_text(
        """
        For contacting the owner:
        Telegram: @manas002
        instagram: @Anime_Jod.01
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
        /ThedailylifeofImmortalKing->The Daily Life of Immortal King
        /DrStone->Dr. Stone
        /365daysToTheWedding->365 days to  the Wedding
        /LogHorizen->Log Horizen
        /YouArMsServant->You ar Ms. Servant
        /DANDADAN->DAN DA DAN
        /soloLeveling->Solo Leveling
        /mashlemagicandmuscles->Mashle Magic and Mscles
        /rezero->Re Zero
        Anime Movies:
        /Iwanttoeatyourpancreas->I want to Eat Your Pancreas 
        /spyxfamilycodewhite-> Spy x Family: Code White
        /asilentvoice->A Silent Voice
        """
        )


def Naruto(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
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
    towerofgod.Season1(update, context)
    towerofgod.Season2(update, context)


def Tokyorevengers(update, context):
    tokyorevengers.Season1(update, context)
    tokyorevengers.Season2(update, context)
    
def BlueLock(update, context):
    blulock.Season1(update, context)
    blulock.Season2(update, context)
    
def ThatTimeIgotReincarnatedasASlime(update, context):
    thatTimeIgotReincarnatedasASlime.Season1(update, context)
    thatTimeIgotReincarnatedasASlime.Season2(update, context)
    

def DragonBallZ(update, context):
    update.message.reply_text("This anime will be avlible in next week.")

def Blackclover(update, context):
    blackclover.Season1(update, context)
    

def TrueBeauty(update, context):
    truebeauty.Season1(update, context)
    
    
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
    spyxfamily.Season1(update, context)
    spyxfamily.Season2(update, context)
    
def ThedailylifeofImmortalKing(update, context):
    thedailylifeofimmortalking.Season1(update, context)
    thedailylifeofimmortalking.Season2(update, context)
    thedailylifeofimmortalking.Season3(update, context)
    thedailylifeofimmortalking.Season4(update, context)
    
def DrStone(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
def LogHorizen(update, context):
    loghorizen.Season1(update, context)
    loghorizen.Season2(update, context)
    
def YouArMsServant(update, context):
    update.message.reply_text(
        """
        This anime will be avlible in next week.
        """
        )
    
def SoloLeveling(update, context):
    soloLeveling.Season1(update, context)
    
    
def daystotheWedding(update,context):
   dayofwedding.Season1(update,context)
    
def DANDADAN(update,context):
    dandadan.Season1(update,context)
 
def MashleMagicandMuscles(update, context):
    mashlemagicandmuscles.Season1(update, context)
    mashlemagicandmuscles.Season2(update, context)



def Iwanttoeatyourpancreas(update, context):
    update.message.reply_text(
        """
        I want to Eat Your Pancreas: https://www.udlinks.com/h24n6L
        """
        )
       
    
def spyxfamilycodewhite(update,context):
    update.message.reply_text(
        """
        SpyX Family Code White: https://www.udlinks.com/RieCpR6
        """
        )


def ReZero(update, context):
    rezero.Season1(update, context)


def Asilentvoice(update, context):
    update.message.reply_text(
        """
        A Silent Voice: https://www.udlinks.com/sWZNi6P
        """
        )


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('anime', anime))
dispatcher.add_handler(CommandHandler('contactus', contactus))
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
dispatcher.add_handler(CommandHandler('ThedailylifeofImmortalKing', ThedailylifeofImmortalKing))
dispatcher.add_handler(CommandHandler('DrStone', DrStone))
dispatcher.add_handler(CommandHandler('LogHorizen', LogHorizen))
dispatcher.add_handler(CommandHandler('YouArMsServant', YouArMsServant))
dispatcher.add_handler(CommandHandler('365daysToTheWedding', daystotheWedding))
dispatcher.add_handler(CommandHandler('SoloLeveling', SoloLeveling))
dispatcher.add_handler(CommandHandler('DANDADAN', DANDADAN))
dispatcher.add_handler(CommandHandler('mashlemagicandmuscles', MashleMagicandMuscles))
dispatcher.add_handler(CommandHandler('Iwanttoeatyourpancreas', Iwanttoeatyourpancreas))
dispatcher.add_handler(CommandHandler('spyxfamilycodewhite',spyxfamilycodewhite))
dispatcher.add_handler(CommandHandler('rezero',ReZero))
dispatcher.add_handler(CommandHandler('asilentvoice',Asilentvoice))


updater.start_polling()
updater.idle()