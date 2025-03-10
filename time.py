from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import re

async def set_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Please select a channel.")
    channels = []
    keyboard = []
    for channel in channels:
        keyboard.append([InlineKeyboardButton(channel, callback_data=channel)])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select a channel:", reply_markup=reply_markup)
    return "SELECT_CHANNEL"

async def set_time_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    channel_id = query.data
    await query.edit_message_text(f"Channel {channel_id} selected.")
    await update.message.reply_text("Please enter the time (e.g. 1m, 2h, 1d).")
    return "TIME"

async def time_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    time_set = update.message.text
    match = re.match(r"(\d+)(m|h|d)", time_set)
    if match:
        value = int(match.group(1))
        unit = match.group(2)
        if unit == "m":
            time_set = value * 60
        elif unit == "h":
            time_set = value * 60 * 60
        elif unit == "d":
            time_set = value * 60 * 60 * 24
        await update.message.reply_text(f"Time set successfully for {time_set} seconds.")
        return ConversationHandler.END
    else:
        await update.message.reply_text("Invalid time format. Please use 1m, 2h, or 1d.")
        return
