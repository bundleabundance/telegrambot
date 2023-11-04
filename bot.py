from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from handlers import handle_message, handle_voice_message
from utils import send_message
import config 
import time

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram Bot API token
BOT_TOKEN = config.API_TOKEN

def start(update, context):
    """Handle the /start command."""
    # Extract relevant information from the update
    chat_id = update.message.chat.id

    # Generate a response for the /start command
    response_text = 'Hello! I am your bot. Send me a message or voice recording.'

    # Send the response back to the chat
    send_message(chat_id, response_text)

def unsupported_command(update, context):
    """Handle unsupported commands."""
    # Extract relevant information from the update
    chat_id = update.message.chat.id

    # Generate a response for unsupported commands
    response_text = 'Sorry, I don\'t recognize that command. Send me a message or voice recording.'

    # Send the response back to the chat
    send_message(chat_id, response_text)

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

     # Handlers
    start_handler = CommandHandler('start', start)
    unsupported_command_handler = MessageHandler(Filters.command, unsupported_command)
    message_handler = MessageHandler(Filters.text, handle_message)
    voice_handler = MessageHandler(Filters.voice, handle_voice_message)
    


    # Add handlers to the dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(unsupported_command_handler)
    dispatcher.add_handler(message_handler)
    dispatcher.add_handler(voice_handler)
    

    # Start the Bot
    updater.start_polling()
    updater.idle()

     # Keep the bot running in a loop
    while True:
        try:
            time.sleep(3)  # Adjust the sleep time as needed
        except KeyboardInterrupt:
            updater.stop()
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            continue


if __name__ == '__main__':
    main()