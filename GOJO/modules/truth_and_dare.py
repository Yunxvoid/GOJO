import random
import GOJO.strings.truth_and_dare_string as truth_and_dare_string
from GOJO import dispatcher
from telegram import Update
from GOJO.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext

def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))

def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))

def wyr(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(truth_and_dare_string.WYR))


def tord(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TORD))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)
TORD_HANDLER = DisableAbleCommandHandler("tord", tord, run_async=True)
WYR_HANDLER = DisableAbleCommandHandler(("rather", "wyr"), wyr, run_async=True)


dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(TORD_HANDLER)
dispatcher.add_handler(WYR_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__mod_name__ = "ᴛʀᴜᴛʜ ᴏʀ ᴅᴀʀᴇ"
__help__ = """
*Truth or Dare*
 ❍ `/truth` : Asks a question
 ❍ `/dare` : Tells a task to do
 ❍ `/tord` : Can either be a truth or dare
 ❍ `/rather` or `/wyr`: Would you rather?
"""
