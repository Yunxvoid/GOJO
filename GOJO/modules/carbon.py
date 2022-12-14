from pyrogram import filters

from GOJO import pbot
from GOJO.core.decorators.errors import capture_err
from GOJO.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Reply to a text message to make carbon."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "Reply to a text message to make carbon."
        )
    m = await message.reply_text("Preparing Carbon")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()
