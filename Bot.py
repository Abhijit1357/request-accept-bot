from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, filters
from handlers import start, add_channel_callback, channel_id_handler, set_channel, set_channel_id_handler, set_time, about_me, close_message, help_command
from config import TOKEN
import asyncio
import logging

logging.basicConfig(level=logging.ERROR)

async def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(add_channel_callback, pattern='^add_channel$'))
    app.add_handler(ConversationHandler(
        entry_points=[CallbackQueryHandler(add_channel_callback, pattern='^add_channel$')],
        states={
            "CHANNEL_ID": [MessageHandler(filters.TEXT, channel_id_handler)],
        },
        fallbacks=[],
        per_message=True
    ))
    app.add_handler(ConversationHandler(
        entry_points=[CommandHandler('set_channel', set_channel)],
        states={
            "CHANNEL_ID": [MessageHandler(filters.TEXT, set_channel_id_handler)],
        },
        fallbacks=[],
        per_message=True
    ))
    app.add_handler(CommandHandler('set_time', set_time))
    app.add_handler(CallbackQueryHandler(about_me, pattern='^about_me$'))
    app.add_handler(CallbackQueryHandler(close_message, pattern='^close$'))
    app.add_handler(CommandHandler('help', help_command))
    await app.run_polling()

if __name__ == '__main__':
    main()
