import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


load_dotenv()  # Loading .env file
API_KEY = os.getenv('API_KEY')  # Extracting the API_KEY from .env file


# To get INFO about the program while running
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, I'm still in development!")

if __name__ == '__main__':
    application = ApplicationBuilder().token(API_KEY).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()