from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def inline_keyboard():
    keyboard = [
        [InlineKeyboardButton("Add Channel", callback_data="add_channel")],
        [InlineKeyboardButton("Channel Check", callback_data="channel_check")],
    ]
    return InlineKeyboardMarkup(keyboard)
