import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

app = Flask(__name__)
telegram_app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot webhook mode me chal raha hai ✅")

telegram_app.add_handler(CommandHandler("start", start))

@app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return "ok"

@app.route("/")
def home():
    return "Bot is alive 🚀"

if __name__ == "__main__":
    telegram_app.bot.set_webhook(
        url="https://bot-y412.onrender.com/webhook"
    )
    app.run(host="0.0.0.0", port=10000)

