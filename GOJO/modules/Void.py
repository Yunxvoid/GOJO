from GOJO import dispatcher
from GOJO.vars import NETWORK_USERNAME
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/5677587af5c20b1d91099.jpg"

network_name = NETWORK_USERNAME.lower()

if network_name == "【V๏ɪ፝֟𝔡】◈Network◈":
    def Void(update: Update, context: CallbackContext):

        TEXT = f"""
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ [【V๏ɪ፝֟𝔡】◈Network◈](https://t.me/VoidxNetwork),
【V๏ɪ፝֟𝔡】 𝙞𝙨 𝙖𝙣 𝙖𝙣𝙞𝙢𝙚 𝙗𝙖𝙨𝙚𝙙 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮 𝙬𝙞𝙩𝙝 𝙖 𝙢𝙤𝙩𝙞𝙫𝙚 𝙩𝙤 𝙨𝙥𝙧𝙚𝙖𝙙 𝙡𝙤𝙫𝙚 𝙖𝙣𝙙 𝙥𝙚𝙖𝙘𝙚 𝙖𝙧𝙤𝙪𝙣𝙙 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢. 𝙂𝙤 𝙩𝙝𝙧𝙤𝙪𝙜𝙝 𝙩𝙝𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙟𝙤𝙞𝙣 𝙩𝙝𝙚 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮, 𝙞𝙛 𝙞𝙩 𝙙𝙧𝙖𝙬𝙨 𝙮𝙤𝙪𝙧 𝙖𝙩𝙩𝙚𝙣𝙩𝙞𝙤𝙣.
"""

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】◈Network◈", url="https://t.me/VoidxNetwork")],
                    [
                    InlineKeyboardButton(text="Vᴏɪᴅ Tᴀɢ", url="https://t.me/VoidxNetwork/136"),
                    InlineKeyboardButton(text="V๏ɪ፝֟𝔡 ◈Hᴇᴀᴅ-Qᴜᴀʀᴛᴇʀs◈", url="https://t.me/Void_HeadQuarters")
                    ],
                ]
            ),
        )


    Void_handler = CommandHandler(("Void", "network", "net"), Void, run_async = True)
    dispatcher.add_handler(Void_handler)

    __help__ = """
    【V๏ɪ፝֟𝔡】◈Network◈                        
    
    ❂ /Void: Get information about our community! Using it in groups may create promotion so we don't support using it in groups."""
    
    __mod_name__ = "【V๏ɪ፝֟𝔡】"
