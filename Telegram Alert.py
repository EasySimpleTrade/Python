import requests
import urllib.parse

# Telegram bot credentials
channel_id = '@mychannel'
bot_key = 'bot_key_here'

# Message to post
message_post = 'Message to Post'

# URL-encode the message
encoded_message = urllib.parse.quote(message_post)

# Telegram API URL
url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={channel_id}&text={encoded_message}"

# Send the request
response = requests.get(url)

# Print the response (optional)
print(response.status_code)
print(response.json())
