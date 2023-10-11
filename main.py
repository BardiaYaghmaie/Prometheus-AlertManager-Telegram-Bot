from fastapi import FastAPI, Request
from pydantic import BaseModel
from telegram import Bot
import appsetting  # Assuming this module contains your API token

app = FastAPI()

# Initialize your bot with the API token
bot = Bot(token=appsetting.appsetting.accl_alert_bot_API_TOKEN)

class PrometheusAlert(BaseModel):
    status: str
    externalURL: str
    commonLabels: dict
    commonAnnotations: dict

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

    await bot.send_message(chat_id=appsetting.appsetting.accl_alert_group_CHAT_ID, text=message)
    return {"message": "Alert received and sent to the group."}
