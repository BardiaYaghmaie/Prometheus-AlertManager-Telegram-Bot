from fastapi import FastAPI
from models import PrometheusAlert, Update
from telegram import Bot
from keyboards import *
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



    await bot.send_message(chat_id=user_chat_id, text=message, reply_markup=start_keyboard)


    return {"message": "Alert received and sent to the group."}


@app.post("/webhook")
async def telegram_webhook(update: Update):
    message = update.message
    callback_query = update.callback_query

    if callback_query:
        callback_message = callback_query.message
        c_user = callback_query.from_user
        username = c_user.username
        firstname = c_user.first_name
        if callback_query.data == 'start_resolve':
            c_user = callback_query.from_user
            username = c_user.username
            firstname = c_user.first_name

            await bot.send_message(
                    text=f"{firstname.title()} (@{username}) started resolving this issue",
                    chat_id=user_chat_id,
                    reply_to_message_id=callback_message.message_id
            )
            await bot.editMessageReplyMarkup(
                message_id=callback_message.message_id,
                chat_id=user_chat_id,
                reply_markup=resolved_keyboard
            )

        if callback_query.data == 'resolved':
            await bot.send_message(
                    text=f"{firstname.title()} (@{username}) resolved this issue.",
                    chat_id=user_chat_id,
                    reply_to_message_id=callback_message.message_id
            )
            await bot.editMessageReplyMarkup(
                message_id=callback_message.message_id,
                chat_id=user_chat_id,
                reply_markup=final_keyboard
            )

        return

    if message.text:
        t_user = message.from_user
        username = t_user.username
        firstname = t_user.first_name
        if "/start" in message.text:
            response_text = "Welcome to your Telegram bot!"
        else:
            response_text = f"{firstname} (@{username}) said: " + message.text

        # Send a response to the user
        await bot.send_message(chat_id=user_chat_id, text=response_text)
        return

    return {"message": "Received update"}