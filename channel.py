from telegram import Update
from telegram.ext import ContextTypes

async def channel_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    channel_list = []
    for chat in await context.bot.get_chats():
        if chat.type == 'channel':
            channel_list.append(chat)
    message = "Channel List:\n"
    for channel in channel_list:
        message += f"- {channel.title} ({channel.username})\n"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
