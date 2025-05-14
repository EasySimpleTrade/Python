import requests

channel_id = '@mychannel'
bot_key = 'bot_key_here'
message_post = 'Message to Post'

url = f"https://api.telegram.org/bot{bot_key}/sendMessage"

payload = {
    'chat_id': channel_id,
    'text': message_post
}

response = requests.post(url, data=payload)

print(response.status_code)
print(response.json())
