from telegram import Bot
from fastapi import FastAPI, Request
from pydantic import BaseModel

# Initialize your bot with the API token
bot = Bot(token="YOUR_BOT_API_TOKEN")

app = FastAPI()


class PrometheusAlert(BaseModel):
    status: str
    externalURL: str
    commonLabels: dict
    commonAnnotations: dict


@app.post('/alert')
async def alert(request: Request, alert: PrometheusAlert):
    status_icon = "⌛️" if alert.status == "firing" else "✅"
    severity_icon = "❗️" if "severity" in alert.commonLabels else ""

    message = f"{status_icon} Status: {alert.status} {severity_icon}\n"
    message += f"🔗 Source: {alert.externalURL}\n"
    message += "🏷 Labels:\n"
    for key, value in alert.commonLabels.items():
        message += f"- {key} = {value}\n"
    message += "📝 Annotations:\n"
    for key, value in alert.commonAnnotations.items():
        message += f"- {key} = {value}\n"