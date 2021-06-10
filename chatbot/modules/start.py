from chatbot import cb as me
import asyncio
from pyrogram import filters

@me.on_message(filters.command(["help", "start"]))
async def hello(client, message):
    await message.reply_text(f"Hello {message.from_user.mention} my name is tachibana naoto! from tokyo revengers anime, if you want to talk with me just say Naoto or reply my message, powered by brainshop.ai !")