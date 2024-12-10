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
        /naruto -> lists anime series
        /naruto shippuden -> lists anime series
        /solo leveling -> lists anime series
        """
    )


def start(update, context):
    update.message.reply_text("Welcome to Anime Hub.")

def anime(update, context):
    update.message.reply_text("Anime Series:")
    update.message.reply_text("1. Naruto")
    update.message.reply_text("2. Naruto Shippuden")
    update.message.reply_text("2. One Punch Man")
    update.message.reply_text("3. Death Note")
    update.message.reply_text("4. Bleach")
    update.message.reply_text("5. Dragon Ball Z")


def naruto(update, context):
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
    
    
    
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('naruto', naruto))
dispatcher.add_handler(CommandHandler('anime', anime))
dispatcher.add_handler(CommandHandler('NarutoShippuden', NarutoShippuden))
dispatcher.add_handler(CommandHandler('OnePunchMan', OnePunchMan))
dispatcher.add_handler(CommandHandler('DeathNote', DeathNote))
dispatcher.add_handler(CommandHandler('Bleach', Bleach))
dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
updater.idle()