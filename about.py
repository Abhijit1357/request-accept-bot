from telegram import Update
from telegram.ext import ContextTypes

async def about_me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "Creator: Owner\nFounder: @abhijit_135 \nChannel: "
    await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id, text=message)
