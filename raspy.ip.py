import telebot
import requests

# Replace with your bot token and chat ID
BOT_TOKEN = "INSERIRE.IL.TOKEN"
CHAT_ID = "@INSERIRE.IL.TUO.CANALE"

# Create a Telegram bot object
bot = telebot.TeleBot(BOT_TOKEN)

# Get the public IP address
ip_api_url = "https://api.ipify.org?format=text"
response = requests.get(ip_api_url)
public_ip = response.text

# Format the message
message = f"**Raspberry is online IP Address:**\n\n* Public IP: {public_ip}"

# Send the message to Telegram chat
bot.send_message(chat_id=CHAT_ID, text=message)
