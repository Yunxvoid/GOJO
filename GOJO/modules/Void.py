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
【V๏ɪ፝֟𝔡】 ɪs ᴀɴ ᴀɴɪᴍᴇ ʙᴀsᴇᴅ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴡɪᴛʜ ᴍᴏᴛɪᴠᴇ ᴛᴏ sᴘʀᴇᴀᴅ ʟᴏᴠᴇ ᴀɴᴅ ᴘᴇᴀᴄᴇ ᴀʀᴏᴜɴᴅ ᴛᴇʟᴇɢʀᴀᴍ. ɢᴏ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴊᴏɪɴ ᴛʜᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ, ɪғ ɪᴛ ᴅʀᴀᴡs ʏᴏᴜʀ ᴀᴛᴛᴇɴᴛɪᴏɴ.
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
