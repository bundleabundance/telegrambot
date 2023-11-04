import requests
import config


BOT_TOKEN = config.API_TOKEN

def send_message(chat_id, text):
    """Send a text message to a chat."""
    try:
        api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        data = {'chat_id': chat_id, 'text': text}
        response = requests.post(api_url, data=data)
        response_json = response.json()
        if not response_json.get('ok'):
            raise Exception(response_json.get('description'))
    except Exception as e:
        print(f"Error while sending message: {e}")

def make_voip_call(chat_id, voice_url):
    """Initiate a VoIP call to a chat."""
    try:
        api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendVoice'
        data = {'chat_id': chat_id, 'voice': voice_url}
        response = requests.post(api_url, data=data)
        response_json = response.json()
        if not response_json.get('ok'):
            raise Exception(response_json.get('description'))
    except Exception as e:
        print(f"Error while making VoIP call: {e}")

def send_audio(chat_id, audio_url):
    """Send an audio message to a chat."""
    try:
        api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendAudio'
        data = {'chat_id': chat_id, 'audio': audio_url}
        response = requests.post(api_url, data=data)
        response_json = response.json()
        if not response_json.get('ok'):
            raise Exception(response_json.get('description'))
    except Exception as e:
        print(f"Error while sending audio: {e}")