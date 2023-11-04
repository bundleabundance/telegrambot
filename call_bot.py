from pyrogram import Client, filters
import config

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API credentials.
api_id = config.api_id
api_hash = config.api_hash

app = Client("my_bot", api_id=api_id, api_hash=api_hash)


@app.on_chat_voice_chat_ended()
async def handle_voice_chat_ended(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    print(f'Voice chat ended in chat {chat_id} by user {user_id}')


@app.on_voice_chat_scheduled()
async def on_voice_chat_scheduled(client, message):
    # Handle the event when a voice call is scheduled
    print("Voice call scheduled:", message.chat.id)


@app.on_message(filters.voice)
async def handle_voice_message(client, message):
    # Handle incoming voice messages (VoIP calls)
    chat_id = message.chat.id

    # Send an MP3 file as a response to the call
    # Replace 'YOUR_MP3_FILE_URL' with the URL of your MP3 file.
    await client.send_voice(chat_id, voice='YOUR_MP3_FILE_URL')


if __name__ == "__main__":
    app.run()