from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("About Me", callback_data="about_me"),
            InlineKeyboardButton("Close", callback_data="close"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
