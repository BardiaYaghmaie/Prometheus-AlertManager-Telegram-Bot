## Prometheus Alertmanager Telegram Bot

This Notifier Telegram Bot is designed to receive alerts from Prometheus AlertManager through web-hooks and send them as messages to a Telegram chat. This bot also allows users to acknowledge alerts and receive updates when alerts are being resolved.


### Get Started

1- Open Telegram app, search @botfather, start the bot and from the menu select "/newbot".
2- Choose a name (e.g. Alert Notifier), a username ending in "bot" (e.g. myalertnotifier_bot).
3- Congrats, your bot has been made! Keep that HTTP API token somewhere safe you'll need it.
4- Open a chat with your bot (t.me/myalertnotifier_bot), click start and send something to the chat (e.g. Dummy Text).
5- Go to https://api.telegram.org/botYOUR_API_TOKEN/getUpdates, from the json response, keep the chat id (e.g 87242341), you'll need it.