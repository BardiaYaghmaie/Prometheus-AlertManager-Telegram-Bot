from telegram import InlineKeyboardButton, InlineKeyboardMarkup

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Start to Resolve", callback_data='start_resolve')]
    ])

resolved_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Resolved", callback_data='resolved')]
    ])

final_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="", callback_data='resolved')]
    ])