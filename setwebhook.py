import requests

import appsetting

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = appsetting.appsetting.BOT_API_TOKEN
alertmanager_url = appsetting.appsetting.ALERTMANAGER_URL  # or your server's public address

url = f"https://api.telegram.org/bot{bot_token}/setWebhook"
data = {"url": f"{alertmanager_url}/webhook"}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Webhook set up successfully")
else:
    print("Failed to set up webhook")
    print(response.text)
