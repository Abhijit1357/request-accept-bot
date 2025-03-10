from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, filters
from telegram import Update, ContextTypes
from keyboard import inline_keyboard
import re

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! Welcome to our bot. Type /help to know more about our bot.", reply_markup=inline_keyboard())

async def add_channel_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await update.callback_query.answer()
    await update.callback_query.edit_message_text("Kripya channel ka ID dena hoga.")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Channel ID?")
    return "CHANNEL_ID"

def channel_id_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    channel_id = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Channel {channel_id} set kiya gaya hai.")
    return ConversationHandler.END

async def set_channel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await update.message.reply_text("Kripya channel ka ID dena hoga.")
    return "CHANNEL_ID"

def set_channel_id_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    channel_id = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Channel {channel_id} set kiya gaya hai.")
    return ConversationHandler.END

async def set_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) > 0:
        time_set = context.args[0]
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
            await update.message.reply_text(f"Time set kiya gaya hai {time_set} seconds ke liye.")
        else:
            await update.message.reply_text("Invalid time format. Please use 1m, 2h, or 1d.")
    else:
        await update.message.reply_text("Please provide time value.")

async def about_me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "◈ ᴄʀᴇᴀᴛᴏʀ: Owner\n◈ ꜰᴏᴜɴᴅᴇʀ: \n◈ ᴄʜᴀɴɴᴇʟ: Ana"
    await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id, text=message)

async def close_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)

def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "Hello! This bot can help you to set channel and time. Here are the commands:\n/start - Start the bot\n/set_channel - Set the channel\n/set_time - Set the time\n/help - Show this help message"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
