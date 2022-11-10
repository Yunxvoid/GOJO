from GOJO import dispatcher
from GOJO.vars import APOD_API_KEY
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import (
    CallbackContext,
    CommandHandler,
)
import requests

def apod(update: Update, context: CallbackContext):
    url = 'https://apod.nasa.gov/apod/'
    result = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + APOD_API_KEY).json()
    img = result['hdurl']
    title = result['title']
    if result['copyright']:       
        copyright = result['copyright']
        text = f'<b>Title: <u>{title}</u></b>\n\n<i>Credits: {copyright}</i>'
    else:
        text = f'<b>Title: <u>{title}</u></b>'
    
    update.effective_message.reply_photo(img, caption=text, reply_markup=InlineKeyboardMarkup(
        [    
            [InlineKeyboardButton("More Info" , url=url)]

        ]),
        parse_mode=ParseMode.HTML)

apod_handler = CommandHandler("apod", apod, run_async = True)
dispatcher.add_handler(apod_handler)

__mod_name__ = "ɴᴀsᴀ"

__help__ = """
Use `/apod` to get Picture of the Day by NASA.
"""
