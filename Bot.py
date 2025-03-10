import asyncio
from telegram.ext import Updater, CommandHandler, MessageHandler, Application
from config import TOKEN

channels = {}

async def start(update, context):
    await update.message.reply_text("Namaste! Main aapka bot hoon. Mujhe apne channel ka admin banaein aur `/set_channel` command ke saath forward message ID dena hoga.")

async def set_channel(update, context):
    channel_id = update.effective_chat.id
    if channel_id not in channels:
        if len(context.args) > 0:
            forward_message_id = int(context.args[0])
            channels[channel_id] = {'time': 4 * 60 * 60, 'forward_message': forward_message_id}  # 4 ghante ke liye default time set
            await update.message.reply_text(f"Channel set kiya gaya hai {channel_id} ke liye.")
        else:
            await update.message.reply_text(f"Channel set karne ke liye forward message ID dena hoga.")
    else:
        await update.message.reply_text(f"Channel {channel_id} pehle se hi set hai.")

async def set_time(update, context):
    channel_id = update.effective_chat.id
    if channel_id in channels:
        try:
            time_set = int(context.args[0]) * 60 * 60  # ghante mein time set karein
            channels[channel_id]['time'] = time_set
            await update.message.reply_text(f"Time set kiya gaya hai {context.args[0]} ghante ke liye channel {channel_id} ke liye.")
        except (IndexError, ValueError):
            await update.message.reply_text("Invalid time. Kripya ghante mein time set karein.")
    else:
        await update.message.reply_text("Channel nahi set kiya gaya hai.")

async def accept_join_request(update, context):
    channel_id = update.effective_chat.id
    if channel_id in channels:
        await update.message.reply_text("Join request accept hone ke liye kuch der wait karein...")
        await asyncio.sleep(channels[channel_id]['time'])
        context.bot.accept_join_request(update.effective_chat.id)
        await update.message.reply_text("Join request accept ho gaya hai!")
    else:
        await update.message.reply_text("Channel nahi set kiya gaya hai.")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('set_channel', set_channel))
    application.add_handler(CommandHandler('set_time', set_time))
    application.add_handler(CommandHandler('accept_join_request', accept_join_request))
    application.run_polling()

if __name__ == '__main__':
    main()
