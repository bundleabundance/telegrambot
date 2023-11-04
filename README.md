#Telegrambot
Welcome to the Telegram Bot Application! This Python-based application utilizes the Telegram Bot API to create a versatile bot with basic functionalities, including voice messaging and messaging specific users. This README will guide you through setting up the bot and understanding its capabilities.

reate a Telegram Bot:

Talk to the BotFather on Telegram to create your bot and obtain a unique API token.

Clone the Repository:
`
git clone https://github.com/yourusername/telegram-bot-application.git`

Navigate to the Project Directory:
`
cd telegram-bot-application`

Configure the Bot:
Replace 'YOUR_API_TOKEN' in bot.py with the API token obtained from the BotFather.

Run the Bot:
`python bot.py`

Your bot is now active and ready to respond to commands.

Bot Functionalities

1. Voice Messaging
Command: /voicemessage [your_message]
Description: The bot will convert the text message provided after the command into a voice message and send it as a voice file.
2. Messaging Specific Users
Command: /sendmessage [user_id] [your_message]
Description: The bot will send the specified message to the user with the provided user_id. You can find a user's ID by adding the user to a group and using a bot like @userinfobot to get their ID.

To install the dependencies run the 
"pip install -r requirements.txt" 
command on console while in the directory

Notes
Ensure that the bot has permission to send messages and voice messages in the groups or channels where you intend to use it.
Contributing
Contributions to enhance the bot's functionalities or address issues are welcome! Create a pull request with your changes, and they will be reviewed.

