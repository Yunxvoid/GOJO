import time
from GOJO.modules.helper_funcs.readable_time import get_readable_time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.utils.helpers import escape_markdown
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler
from GOJO.vars import ANIME_NAME, BOT_USERNAME, NETWORK, NETWORK_USERNAME, PM_START_TEXT, START_MEDIA, SUPPORT_CHAT, UPDATE_CHANNEL
from GOJO import StartTime, dispatcher
import GOJO.modules.sql.users_sql as sql

bot_name = f"{dispatcher.bot.first_name}"

IMG_START = START_MEDIA.split(".")
start_id = IMG_START[-1]

buttons = [
    [
        InlineKeyboardButton(
            text=f"۞‌ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢƦᴏᴜᴘ ۞‌‌", url=f"t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="Uᴘᴅᴀᴛᴇ", url=f"https://t.me/{UPDATE_CHANNEL}"),   
    ], 
]

network_name = NETWORK_USERNAME.lower()

try:
    if network_name == "【V๏ɪ፝֟𝔡】◈Network◈":
        HMMM = InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】◈Network◈", callback_data="sern_")
    elif NETWORK:
        HMMM = InlineKeyboardButton(text=f"{NETWORK}", url=f"https://t.me/VoidxNetwork")
    else:
        HMMM = None
except:
    HMMM = None

def GOJO_about_callback(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        text=f"๏ I'm *{bot_name}*, a powerful group management bot built to help you manage your group easily."
        "\n• I can restrict users."
        "\n• I can greet users with customizable welcome messages and even set a group's rules."
        "\n• I have an advanced anti-flood system."
        "\n• I can warn users until they reach max warns, with each predefined actions such as ban, mute, kick, etc."
        "\n• I have a note keeping system, blacklists, and even predetermined replies on certain keywords."
        "\n• I check for admins' permissions before executing any command and more stuffs",
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(text="Github", callback_data="github_"),
                InlineKeyboardButton(text="License", callback_data="license_"),
                ],
                [
                HMMM,
                InlineKeyboardButton(text="Documentation", url="https://github.com/Yunxvoid/GOJO/"),
                ],
                [
                InlineKeyboardButton(text="Back", callback_data="home_"),
                ],
            ]
        ),
    )

def git_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "github_":
        query.message.edit_text(
            text=f"Orginal Repositiory created by [Yᴜɴ윤](https://github.com/yunxvoid) on [github](https://github.com/Yunxvoid/GOJO) for [GOJO神 Bot](https://t.me/Gojoa_satoru_bot)",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="Repo", url="https://github.com/Yunxvoid/GOJO"),
                    InlineKeyboardButton(text="Creator", url="https://github.com/Yunxvoid"),
                    ],
                ]
            ),
        )
def home_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "home_":
        first_name = update.effective_user.first_name
        users = f"{sql.num_users()}"
        uptime = get_readable_time((time.time() - StartTime))
        chats = f"{sql.num_chats()}"
        first_name = update.effective_user.first_name
        start_text = PM_START_TEXT.format(escape_markdown(first_name), bot_name, ANIME_NAME, users, chats, uptime)
        query.message.delete()
        try:
            if start_id in ("jpeg", "jpg", "png"):
                query.edit_photo(
                    START_MEDIA, caption = start_text, reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
            )
            elif start_id in ("mp4", "mkv"):
                update.effective_message.reply_video(
                START_MEDIA, caption = start_text, reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
            )
            elif start_id in ("gif", "webp"):
                update.effective_message.reply_animation(
                START_MEDIA, caption = start_text, reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
            )
            else:
                update.effective_message.reply_text(start_text, reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,)

        except:
            update.effective_message.reply_text(start_text, reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,)
    

def sern_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "sern_":
        query.message.edit_text(
            text=f"""
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ [【V๏ɪ፝֟𝔡】◈Network◈](https://t.me/VoidxNetwork),
【V๏ɪ፝֟𝔡】 ɪs ᴀɴ ᴀɴɪᴍᴇ ʙᴀsᴇᴅ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴡɪᴛʜ ᴍᴏᴛɪᴠᴇ ᴛᴏ sᴘʀᴇᴀᴅ ʟᴏᴠᴇ ᴀɴᴅ ᴘᴇᴀᴄᴇ ᴀʀᴏᴜɴᴅ ᴛᴇʟᴇɢʀᴀᴍ. ɢᴏ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴊᴏɪɴ ᴛʜᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ, ɪғ ɪᴛ ᴅʀᴀᴡs ʏᴏᴜʀ ᴀᴛᴛᴇɴᴛɪᴏɴ.""", parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=False,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】◈Network◈", url="https://t.me/VoidxNetwork")],
                    [
                    InlineKeyboardButton(text="Vᴏɪᴅ Tᴀɢ ", url="https://t.me/VoidxNetwork/136"),
                    InlineKeyboardButton(text="V๏ɪ፝֟𝔡 ◈Hᴇᴀᴅ-Qᴜᴀʀᴛᴇʀs◈", url="https://t.me/Void_HeadQuarters")
                    ],
                ]
            ),
        )

def license_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "license_":
        query.message.edit_text(
            text=f"\n\n_{bot_name}'s licensed under the GNU General Public License v3.0_",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="License", url="https://github.com/Yunxvoid/GOJO/blob/main/LICENSE"),
                    ],
                ]
            ),
        )

about_callback_handler = CommandHandler(
        "about", GOJO_about_callback, run_async=True
    )
license_call_back_handler = CallbackQueryHandler(
    license_call_back, pattern=r"license_", run_async=True
)
git_call_back_handler = CallbackQueryHandler(
    git_call_back, pattern=r"github_", run_async=True
)
sern_call_back_handler = CallbackQueryHandler(
    sern_call_back, pattern=r"sern_", run_async=True
)
home_handler = CallbackQueryHandler(
    home_back, pattern=r"home_", run_async=True
)

dispatcher.add_handler(sern_call_back_handler)
dispatcher.add_handler(home_handler)
dispatcher.add_handler(git_call_back_handler)
dispatcher.add_handler(about_callback_handler)
dispatcher.add_handler(license_call_back_handler)
