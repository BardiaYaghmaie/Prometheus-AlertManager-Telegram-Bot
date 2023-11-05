## Prometheus Alertmanager Telegram Bot

This Notifier Telegram Bot is designed to receive alerts from Prometheus AlertManager through web-hooks and send them as messages to a Telegram chat. This bot also allows users to acknowledge alerts and receive updates when alerts are being resolved.


### Get Started

1- Open Telegram app, search @botfather, start the bot and from the menu select "/newbot".

2- Choose a name (e.g. Alert Notifier), a username ending in "bot" (e.g. myalertnotifier_bot).

3- Congrats, your bot has been made! Keep that HTTP API token somewhere safe you'll need it.

4- Open a chat with your bot (t.me/myalertnotifier_bot), click start and send something to the chat (e.g. Dummy Text).

5- Go to https://api.telegram.org/botYOUR_API_TOKEN/getUpdates, from the json response, keep the chat id (e.g 87242341), you'll need it.

6- From now on, you better get yourself a server which has a valid IP and domain.

7- Clone the project in server
```
git clone https://github.com/BardiaYaghmaie/Prometheus-AlertManager-Telegram-Bot.git
```
8- Modify appsetting.py and put your api token, chat_id and server url in it.

9- Run the application using
```
docker compose up --build
```
10- Setup webhook using
```
python3 setupwebhook.py
```
and wait for the success response.

**IMPORTANT!** You should be familiar with setting webhooks for telegram bots, if you are not, or your server has not a valid IP/domain or ...
Please read: https://core.telegram.org/bots/api#setwebhook

11- Modify your prometheus alertmanager configs and setup alert webhook.
##### alertmanager.yml:
```
global:
# catch-all route to receive and handle all incoming alerts
route:
  group_by: ['alertname']
  group_wait: 10s       # wait up to 10s for more alerts to group them
  receiver: 'telepush_dev'  # see below
receivers:
- name: 'telepush_dev'
  webhook_configs:
  - url: 'https://alertmanager-server-url/alert'
    http_config:
```

#### Congrats! Now everything should be working.
