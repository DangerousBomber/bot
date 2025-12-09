from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# -------------------- START --------------------
async def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton("🎯 Demo", callback_data="demo"),
            InlineKeyboardButton("💰 Paid", callback_data="paid")
        ]
    ]
    await update.message.reply_text(
        "🔥 Welcome Bro!\nChoose your experience below 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# -------------------- BUTTON HANDLER --------------------
async def button_handler(update, context):
    query = update.callback_query
    await query.answer()
    data = query.data

    # ---------------- DEMO ----------------
    if data == "demo":
        keyboard = [
            [InlineKeyboardButton("📩 Send Number", url="https://t.me/Dangerous_Bomber")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]
        await query.edit_message_text(
            "🎯 **Demo Access :**\n\nSend Number 👇👇",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    # ---------------- PAID MENU ----------------
    elif data == "paid":
        keyboard = [
            [InlineKeyboardButton("179 - Normal Paid (1 Month)", callback_data="plan_179")],
            [InlineKeyboardButton("299 - Paid Max (2 Months)", callback_data="plan_299")],
            [InlineKeyboardButton("499 - Paid Ultra Max (3 Months)", callback_data="plan_499")],
            [InlineKeyboardButton("799 - Max + Ultra Max (6 Months)", callback_data="plan_799")],
            [InlineKeyboardButton("1499 - Powerful Ultra Max (1 Year)", callback_data="plan_1499")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]

        await query.edit_message_text(
            "💰 **Choose Plan:**\n\nNote: Jitna High Price, Utna Hard Bomber 💣",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    # ---------------- PLANS: QR + ADMIN BUTTON ----------------
    elif data.startswith("plan_"):
        amount = data.split("_")[1]

        keyboard = [
            [InlineKeyboardButton("📩 Send Screenshot to Admin", url="https://t.me/Dangerous_Bomber")],
            [InlineKeyboardButton("🔙 Back", callback_data="paid")]
        ]

        try:
            with open("qr.jpg", "rb") as qr:
                await query.message.reply_photo(
                    photo=qr,
                    caption=f"💸 Scan & Pay ₹{amount}\n\n📩 Send Your Screenshot 👇👇",
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )
        except:
            await query.message.reply_text("⚠️ qr.jpg file missing!")

    # ---------------- PAYMENT DONE (NO LONGER USED) ----------------
    # Removed "done_" system since screenshot flow used now.

    # ---------------- BACK ----------------
    elif data == "back":
        keyboard = [
            [
                InlineKeyboardButton("🎯 Demo", callback_data="demo"),
                InlineKeyboardButton("💰 Paid", callback_data="paid")
            ]
        ]
        await query.edit_message_text(
            "🔥 Welcome Bro!\nChoose your experience below 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

# -------------------- TEXT HANDLER --------------------
async def echo(update, context):
    await update.message.reply_text("Use /start bro 😄")

# -------------------- MAIN APP --------------------
def main():
    if not TOKEN:
        print("Bot Token Missing! Add TELEGRAM_BOT_TOKEN in .env file.")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is live bro 🔥")
    app.run_polling()

if __name__ == "__main__":
    main()



