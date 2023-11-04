from utils import send_message, make_voip_call, send_audio

def handle_message(update, context):
    """Handle incoming text messages."""
    # Extract relevant information from the update
    chat_id = update.message.chat_id
    text = update.message.text

    # Process the text and generate a response
    response_text = f'You said: {text}'

    # Send the response back to the chat
    send_message(chat_id, response_text)

def handle_voice_message(update, context):
    """Handle incoming voice messages (calls)."""
    # Extract relevant information from the update
    chat_id = update.message.chat.id

    # Generate a response for the call
    response_text = 'Thank you for the call!'

    # Send the response back to the chat
    send_message(chat_id, response_text)

    # Check if the message contains a voice recording
    if update.message.voice:
        # Replace 'https://example.com/your_voice_file.ogg' with the actual voice URL
        voice_url = 'https://example.com/your_voice_file.ogg'
        make_voip_call(chat_id, voice_url)
    else:
        # Replace 'https://example.com/your_audio_file.ogg' with the actual audio URL
        audio_url = 'https://example.com/your_audio_file.ogg'
        send_audio(chat_id, audio_url)

