from chatbot import cb as me
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from chatbot.utils.errors import capture_err


@me.on_message(~filters.me & filters.command('start', prefixes='/'), group=8)
@capture_err
async def start(_, message):
   if message.chat.type == "private":
     if len(message.text.split()) >= 2:
       low = message.text.split()[1]
       if low == "help":
          buttons = [
                     [
                        InlineKeyboardButton('Support', url='t.me/naotosu'),
                     ]
                  ]
          await message.reply_text('Hey there! I am naoto a chatbot using brainshop.ai, feel free add me to your group!', reply_markup=InlineKeyboardMarkup(buttons))
     else:
       photo = "https://telegra.ph/file/8c611c1dcbc687f30f387.jpg"
       buttons = [
            [
            InlineKeyboardButton('Add me to your Group', url='t.me/?startgroup=true'),
            InlineKeyboardButton('Help', url='help')
            ]
                  ]
       await message.reply_photo(photo,
         caption='Hi, iam a chatbot lets talk with me!',
         reply_markup=InlineKeyboardMarkup(buttons))
   else:
       await message.reply_text("Hi there, wanna talk?.")
