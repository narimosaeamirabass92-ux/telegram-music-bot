from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! ربات تشخیص آهنگ آماده است.\n"
        "لینک اینستاگرام یا ویدیو را بفرست."
    )

async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "لینک اینستاگرام یا فایل ویدیو را بفرست تا بررسی کنم."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        await update.message.reply_text(
            f"لینک دریافت شد: {update.message.text}"
        )

    elif update.message.video:
        await update.message.reply_text(
            "ویدیو دریافت شد. در حال بررسی آهنگ..."
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("music", music))
app.add_handler(MessageHandler(filters.TEXT | filters.VIDEO, handle_message))

app.run_polling()
