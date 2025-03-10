from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, filters
from telegram import Update, InlineKeyboardMarkup
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
