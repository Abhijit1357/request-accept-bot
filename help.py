from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "Hello! This bot can help you to set channel and time. Here are the commands:\n/start - Start the bot\n/set_channel - Set the channel\n/set_time - Set the time\n/help - Show this help message"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
