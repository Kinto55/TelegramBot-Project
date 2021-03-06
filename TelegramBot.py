import telegram
bot = telegram.bot(token='TOKEN') #Replace TOKEN with your token string

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='TOKEN', use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')

    hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

## Start the Bot     
updater.start_polling() 