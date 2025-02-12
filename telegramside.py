import logging

from telegram import ForceReply, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Started",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("not implemented")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    sender = (message.from_user or message.sender_chat)
    firstname = sender.first_name if sender.first_name != None else ""
    lastname = sender.last_name if sender.last_name != None else ""
    try:
        await context.bot.send_message(chat_id=-1002374958503, text=f"`[{message.date.strftime('%H:%M')}] {firstname} {lastname} ({sender.username}):` {message.text}", parse_mode='MarkdownV2')
        logging.info("Message sent successfully")
    except Exception as e:
        logging.error(f"Failed to send message: {str(e)}")

# Create the Application and pass it your bot's token.
application = ApplicationBuilder().token(token=open("telegramtoken.txt").read()).build()

# on different commands - answer in Telegram
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
# on non command i.e message - echo the message on Telegram
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Run the bot until the user presses Ctrl-C
application.run_polling(allowed_updates=Update.ALL_TYPES)