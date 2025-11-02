from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def show_tariffs_categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ['🌐 Интернет', '📺 Телевидение'],
        ['📦 Комплекты', '🔙 Назад']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text('Выберите категорию тарифов:', reply_markup=reply_markup)

async def show_internet_tariffs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "🌐 Тарифы на интернет:\n\n"
        "Эконом 50\nСкорость: 50 Мбит/с\nЦена: 300 руб./мес.\nИдеально для соцсетей и просмотра видео\n\n"
        "Стандарт 100\nСкорость: 100 Мбит/с\nЦена: 500 руб./мес.\nОтлично для онлайн-игр и потокового видео"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def show_tv_tariffs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "📺 Тарифы на телевидение:\n\n"
        "Базовый\nКаналы: 150\nЦена: 250 руб./мес.\nПопулярные каналы\n\n"
        "Расширенный\nКаналы: 250\nЦена: 400 руб./мес.\nВсе каналы + HD"
    )
    await update.message.reply_text(message, parse_mode='Markdown')