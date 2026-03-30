from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Falta la variable de entorno BOT_TOKEN")

BUY_WORDS = [
    "buy", "access", "pay", "join", "subscribe",
    "enter", "price", "cost", "membership", "premium", "vip",
    "get access", "full access", "how do i join", "how can i join",
    "how to join", "how can i enter", "register", "sign up",
    "comprar", "acceso", "pagar", "unirme", "unirme", "precio",
    "costo", "membresia", "membresía", "premium", "vip",
    "registrarme", "registrar", "como entrar", "cómo entrar",
    "como me uno", "cómo me uno", "como unirme", "cómo unirme",
    "quiero entrar", "quiero acceso", "quiero unirme"
]

CRYPTO_WORDS = [
    "crypto", "btc", "usdt", "binance", "bitcoin",
    "cripto", "crypto payment", "pago cripto"
]

HELP_WORDS = [
    "help", "support", "problem", "issue",
    "ayuda", "soporte", "problema", "error"
]

MEMBER_WORDS = [
    "member", "already member", "i am member",
    "miembro", "ya soy miembro", "soy miembro"
]


def contains_any(text: str, words: list[str]) -> bool:
    return any(word in text for word in words)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower().strip()

    if contains_any(text, BUY_WORDS):
        await update.message.reply_text(
            "🚀 Full Access Available\n\n"
            "💳 Price: 99.99 USDT\n\n"
            "👉 PAY HERE:\n"
            "https://s.binance.com/iXbyQcVL\n\n"
            "⚠️ IMPORTANT:\n"
            "After payment, send screenshot + details to:\n"
            "toc.services.requests@gmail.com"
        )

    elif contains_any(text, CRYPTO_WORDS):
        await update.message.reply_text(
            "💳 Crypto Payment\n\n"
            "✔ USDT\n"
            "✔ BTC\n\n"
            "👉 Payment link:\n"
            "https://s.binance.com/iXbyQcVL\n\n"
            "⚠️ After payment, send screenshot + details to:\n"
            "toc.services.requests@gmail.com"
        )

    elif contains_any(text, MEMBER_WORDS):
        await update.message.reply_text(
            "✅ Member Support\n\n"
            "If you need assistance, contact:\n"
            "toc.services.requests@gmail.com\n\n"
            "You can also type:\n"
            "help → support\n"
            "crypto → payment info"
        )

    elif contains_any(text, HELP_WORDS):
        await update.message.reply_text(
            "🛠 Need help?\n\n"
            "Contact support:\n"
            "toc.services.requests@gmail.com\n\n"
            "You can also type:\n"
            "join → access info\n"
            "crypto → payment options"
        )

    else:
        await update.message.reply_text(
            "🔥 Welcome to TOC\n\n"
            "Full access: 99.99 USDT\n\n"
            "Type any of these:\n"
            "join → access info\n"
            "buy → payment link\n"
            "crypto → payment options\n"
            "help → support"
        )


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot corriendo...")
    app.run_polling()


if __name__ == "__main__":
    main()