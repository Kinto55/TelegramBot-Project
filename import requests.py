import requests
import json
def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200): #Everything went okay, we have the data
        data = response.json()
        print(data['Global'])
        context.bot.send_message(chat_id=update.effective_chat.id, text=data['Global'])
    else: #something went wrong
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")
        
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a bot that can give you the latest COVID-19 data.")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Use /summary to get the latest data.")

def main():
    updater = Updater('TOKEN', use_context=True) #Replace TOKEN with your token string
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    summary_handler = CommandHandler('summary', summary)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(summary_handler)
    updater.start_polling()
    

corona_summary_handler = CommandHandler('summary', summary)
dispatcher.add_handler(corona_summary_handler)