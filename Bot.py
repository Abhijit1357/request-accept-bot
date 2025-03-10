from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, filters
from config import TOKEN
from inline import inline_keyboard
import re

async def start(update, context):
    await update.message.reply_text("Namaste!", reply_markup=inline_keyboard())

async def add_channel_callback(update, context):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text("Kripya channel ka ID dena hoga.")
    # Channel ID ko input ke roop mein lena
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Channel ID?")
    return "CHANNEL_ID"

def channel_id_handler(update, context):
    channel_id = update.message.text
    # Channel ko set karna
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Channel {channel_id} set kiya gaya hai.")
    return ConversationHandler.END

async def set_time(update, context):
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

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(add_channel_callback, pattern='^add_channel$'))
    application.add_handler(ConversationHandler(
        entry_points=[CallbackQueryHandler(add_channel_callback, pattern='^add_channel$')],
        states={
            "CHANNEL_ID": [MessageHandler(filters.TEXT, channel_id_handler)],
        },
        fallbacks=[]
    ))
    application.add_handler(CommandHandler('set_time', set_time))
    application.run_polling()

if __name__ == '__main__':
    main()
