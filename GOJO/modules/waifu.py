# Created By: https://telegram.dog/Mr_nack_nack 
# Assisted By: https://telegram.dog/SastaDev from https://telegram.dog/SastaNetwork

# Imports from external libraries. (DON'T EDIT)
import requests
from telegram import ParseMode
from telegram.ext import CommandHandler

import random
# Imports dispatcher = updater.dispatcher from __init__.py (*MUST EDIT* CHANGE MODULE NAME TO THE FOLDER NAME OF MODULES IN YOUR BOT)
from GOJO import dispatcher

# Main code, Credit to https://github.com/itspro-dev for making the API. 

def waifu(update, context):
    try:
        msg = update.effective_message
        # API (DON'T EDIT)
        url = f'https://api.animeepisode.org/waifu/'
        result = requests.get(url).json()
        img = result['Character_Image']
        # Message (EDIT THIS PART AS HTML *IF YOU WANT*)
        text = f'''
<b>Name :</b> <code>{result['Character_Name']}</code>
        
<b>Anime :</b> <code>{result['Anime_name']}</code>
'''
        msg.reply_photo(photo=img, caption=text, parse_mode=ParseMode.HTML)

    except Exception as e:
        text = f'<b>Error</b>: <code>' + e + '</code>'
        msg.reply_text(text, parse_mode=ParseMode.HTML)


# Code Handler (YOU CAN CHANGE 'waifu' TO ANY 'cmd' FOR THIS TO BE WORKED AS '/cmd' *IF YOU WANT*.)
WAIFUINFO_HANDLER = CommandHandler('waifuinfo', waifu, run_async=True)
dispatcher.add_handler(WAIFUINFO_HANDLER)

#  Buttons for /help .
__mod_name__ = '🇼🇦🇮🇫🇺🇸'  # *IF YOU WANT* EDIT NAME OF BUTTON IN '/help'


# *IF YOU WANT* EDIT MESSAGE FOR HELP OF THIS MODULE.
__help__ = '''
*Get waifu images*
   ➢ `/waifu`*:* Sends limited but best Waifu image. *RECOMMENDED*
   ➢ `/waifuinfo`*:* Gives random image of waifu with info. 
   ➢ `/waifus`*:* Sends Random Waifu image.
   ➢ `/swaifu`*:* Sends Random Waifu image.
   *NSFW CONTENT*
   ➢ `/nsfwwaifu`
   ➢ `/nwaifu`  
'''

# DON'T EDIT
__handlers__ = [WAIFUINFO_HANDLER]
