from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if "buy" in text or "access" in text or "pay" in text:
        await update.message.reply_text(
            "🚀 Get Full Access Now\n\n"
            "💳 Price: 99.99 USDT\n\n"
            "👉 PAY HERE:\n"
            "https://s.binance.com/iXbyQcVL\n\n"
            "⚠️ After payment send screenshot to support"
        )
    else:
        await update.message.reply_text(
            "🔥 Welcome to TOC\n\n"
            "Type: buy → access"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot corriendo...")
app.run_polling()