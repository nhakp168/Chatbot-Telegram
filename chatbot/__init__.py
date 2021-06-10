from pyrogram import Client, errors


API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
BOT_ID = Config.BOT_ID

cb = Client("Chatbot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
