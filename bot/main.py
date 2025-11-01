import os
import logging
import asyncio
import contextlib

import datetime as dtm  # import timezone, date, datetime, time, timedelta
from dotenv import load_dotenv

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


load_dotenv()  # Loading .env file
API_KEY = os.getenv('API_KEY')  # Extracting the API_KEY from .env file


# To get INFO about the program while running
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi! How can I help you {update.message.chat.first_name}?")
    keyboard = [
        [
            InlineKeyboardButton("Get a GF", callback_data="1"),
            InlineKeyboardButton("Get a Life", callback_data="2"),
        ],
        [InlineKeyboardButton("Quit Life", callback_data="3")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)

async def echo_time():
    ...


def main() -> None:
    application = ApplicationBuilder().token(API_KEY).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()


if __name__ == "__main__":
    main()
