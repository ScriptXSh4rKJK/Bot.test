from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Замените на свой токен, полученный у BotFather
BOT_TOKEN = "7666865681:AAElXZNiViC6Pkjk7MPRCaflSImhNV4puVk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Добро пожаловать!\n\n"
        "Меня зовут <b>Ксюша</b> "
        "(<a href=\"https://t.me/By_sqakk\">@By_sqakk</a>) — разработчик Telegram-ботов и автоматизаций.\n\n"
        "Если вам нужен надёжный, быстрый и индивидуальный бот — вы можете связаться со мной по ссылке ниже.\n"
    )

    keyboard = [
        [InlineKeyboardButton("📨 Написать в Telegram", url="https://t.me/By_sqakk")],
        [InlineKeyboardButton("💰 Профиль на FunPay",     url="https://funpay.com/users/15460978/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
