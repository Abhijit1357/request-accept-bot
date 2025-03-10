from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, filters
from telegram import Update
from telegram.ext import ContextTypes
from inline import inline_keyboard
import re

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! Welcome to our bot. Type /help to know more about our bot.", reply_markup=inline_keyboard())

async def add_channel_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await update.callback_query.answer()
    await update.callback_query.edit_message_text("Please enter the channel ID.")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Channel ID?")
    return "CHANNEL_ID"

async def channel_id_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    channel_id = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Channel {channel_id} set successfully.")
    return ConversationHandler.END

async def set_channel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await update.message.reply_text("Please enter the channel ID.")
    return "CHANNEL_ID"

async def set_channel_id_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    channel_id = update.message.text
    try:
        channel = await context.bot.get_chat(channel_id)
        if not channel:
            await update.message.reply_text("Channel not found. Please check the ID.")
            return
        admin_status = await context.bot.get_chat_member(channel_id, context.bot.id)
        if admin_status.status != "administrator":
            await update.message.reply_text("Please make the bot an administrator in the channel.")
            return
        channel_name = channel.title
        channel_link = f"https://t.me/{channel.username}" if channel.username else f"https://t.me/c/{channel.id}"
        await update.message.reply_text(f"Channel '{channel_name}' ({channel_link}) added successfully.")
        return ConversationHandler.END
    except Exception as e:
        await update.message.reply_text("Error: " + str(e))
        return

async def set_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
    else:
        await update.message.reply_text("Invalid time format. Please use 1m, 2h, or 1d.")

async def about_me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "Creator: Owner\nFounder: \nChannel: Ana"
    await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id, text=message)

async def close_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "Hello! This bot can help you to set channel and time. Here are the commands:\n/start - Start the bot\n/set_channel - Set the channel\n/set_time - Set the time\n/help - Show this help message"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

async def channel_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    channel_list = context.bot.get_my_chats()
    message = "Channel List:\n"
    for channel in channel_list:
        message += f"- {channel.title} ({channel.username})\n"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
