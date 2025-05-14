import requests

# Telegram bot token and channel ID
bot_key = 'bot_key_here'
channel_id = '@mychannel'

# Image file path
image_path = 'path/to/your/image.jpg'

# Optional caption
caption = 'Here is an image!'

# Telegram API endpoint for sending photos
url = f'https://api.telegram.org/bot{bot_key}/sendPhoto'

# Prepare payload and file
with open(image_path, 'rb') as image_file:
    files = {'photo': image_file}
    data = {
        'chat_id': channel_id,
        'caption': caption
    }

    response = requests.post(url, data=data, files=files)

# Print the response
print(response.status_code)
print(response.json())
