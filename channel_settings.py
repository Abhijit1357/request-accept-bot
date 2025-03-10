from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, filters
from telegram import Update
from telegram.ext import ContextTypes

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

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('set_channel', set_channel)],
    states={
        "CHANNEL_ID": [MessageHandler(filters.TEXT, set_channel_id_handler)],
    },
    fallbacks=[]
)

def get_conv_handler():
    return conv_handler
