from fastapi import FastAPI
from models import PrometheusAlert, Update
from telegram import Bot
import appsetting  # Assuming this module contains your API token

app = FastAPI()
user_chat_id = appsetting.appsetting.USER_CHAT_ID
bot_api_token = appsetting.appsetting.BOT_API_TOKEN

# Initialize your bot with the API token
bot = Bot(token=bot_api_token)

@app.post('/alert')
async def alert(alert: PrometheusAlert):
    status_icon = "❗️" if alert.status == "firing" else "✅"

    message = f"{status_icon} Status: {alert.status} \n\n"
    message += "\n🏷 Labels:\n"
    for key, value in alert.commonLabels.items():
        message += f"- {key} = {value}\n"
    message += "\n📝 Annotations:\n"
    for key, value in alert.commonAnnotations.items():
        message += f"- {key} = {value}\n"

    await bot.send_message(chat_id=user_chat_id, text=message)
    return {"message": "Alert received and sent to the group."}


@app.post("/webhook")
async def telegram_webhook(update: Update):
    message = update.message
    text = message.text
    if text:
        if "/start" in text:
            response_text = "Welcome to your Telegram bot!"
        else:
            response_text = "You said: " + text

        # Send a response to the user
        await bot.send_message(chat_id=user_chat_id, text=response_text)

    return {"message": "Received update"}